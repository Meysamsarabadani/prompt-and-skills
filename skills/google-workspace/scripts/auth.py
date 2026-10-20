import os
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKEN_PATH = os.path.expanduser('~/.gemini/gdrive_token.json')

def get_credentials():
    if not os.path.exists(TOKEN_PATH):
        sys.stderr.write(f"Error: Token not found at {TOKEN_PATH}\n")
        sys.exit(1)
    return Credentials.from_authorized_user_file(TOKEN_PATH)

def get_service(api_name, version):
    creds = get_credentials()
    return build(api_name, version, credentials=creds)
