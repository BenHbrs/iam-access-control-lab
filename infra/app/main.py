from fastapi import FastAPI, Header, HTTPException
from jose import jwt
import requests

app = FastAPI()

KEYCLOAK_REALM = "demo"
KEYCLOAK_URL = "http://keycloak:8080"
JWKS_URL = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/certs"

def get_public_key(token: str):
    jwks = requests.get(JWKS_URL, timeout=5).json()
    header = jwt.get_unverified_header(token)
    for k in jwks["keys"]:
        if k["kid"] == header["kid"]:
            return k
    raise HTTPException(status_code=401, detail="Invalid token key id")

def decode_token(token: str):
    key = get_public_key(token)
    try:
        payload = jwt.decode(token, key, algorithms=["RS256"], options={"verify_aud": False})
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_role(payload, role: str):
    roles = payload.get("realm_access", {}).get("roles", [])
    if role not in roles:
        raise HTTPException(status_code=403, detail=f"Missing role: {role}")

@app.get("/public")
def public():
    return {"ok": True, "scope": "public"}

@app.get("/user")
def user(authorization: str = Header(default="")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.split(" ", 1)[1]
    payload = decode_token(token)
    return {"ok": True, "user": payload.get("preferred_username")}

@app.get("/admin")
def admin(authorization: str = Header(default="")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.split(" ", 1)[1]
    payload = decode_token(token)
    require_role(payload, "admin")
    return {"ok": True, "scope": "admin", "user": payload.get("preferred_username")}
