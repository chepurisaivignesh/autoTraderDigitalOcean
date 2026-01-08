from fyers_apiv3 import fyersModel
import json, os
from config import APP_ID, SECRET_KEY, REDIRECT_URI

TOKEN_FILE = "fyers_token.json"

def authenticate():
    if os.path.exists(TOKEN_FILE):
        return json.load(open(TOKEN_FILE))["access_token"]

    session = fyersModel.SessionModel(
        client_id=APP_ID,
        secret_key=SECRET_KEY,
        redirect_uri=REDIRECT_URI,
        response_type="code",
        grant_type="authorization_code"
    )

    print("LOGIN URL:\n", session.generate_authcode())
    auth_code = input("Paste auth code: ")
    session.set_token(auth_code)

    token = session.generate_token()["access_token"]
    json.dump({"access_token": token}, open(TOKEN_FILE, "w"))
    return token
