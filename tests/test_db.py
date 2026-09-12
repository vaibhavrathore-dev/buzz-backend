from app.integrations.agc.client import AGCClient

agc = AGCClient()

token = agc.get_login_token()

print("Token found:", bool(token))
print("Token length:", len(token))