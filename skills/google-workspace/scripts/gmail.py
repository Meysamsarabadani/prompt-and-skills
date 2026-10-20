#!/usr/bin/env python3
import sys
import json
import base64
from email.mime.text import MIMEText
from auth import get_service

def list_messages(query=None, max_results=10):
    service = get_service('gmail', 'v1')
    res = service.users().messages().list(userId='me', q=query, maxResults=max_results).execute()
    messages = res.get('messages', [])
    details = []
    for msg in messages:
        m = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='metadata',
            metadataHeaders=['Subject', 'From', 'Date']
        ).execute()
        headers = {h['name']: h['value'] for h in m.get('payload', {}).get('headers', [])}
        details.append({
            'id': msg['id'],
            'snippet': m.get('snippet', ''),
            'subject': headers.get('Subject', '(No Subject)'),
            'from': headers.get('From', ''),
            'date': headers.get('Date', '')
        })
    return details

def create_draft(to, subject, body_text):
    service = get_service('gmail', 'v1')
    message = MIMEText(body_text, _charset='utf-8')
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return service.users().drafts().create(userId='me', body={'message': {'raw': raw}}).execute()

def send_email(to, subject, body_text):
    service = get_service('gmail', 'v1')
    message = MIMEText(body_text, _charset='utf-8')
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return service.users().messages().send(userId='me', body={'raw': raw}).execute()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        q = sys.argv[2] if len(sys.argv) > 2 else None
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        print(json.dumps(list_messages(q, limit), indent=2))
    elif len(sys.argv) > 4 and sys.argv[1] == 'draft':
        print(json.dumps(create_draft(sys.argv[2], sys.argv[3], sys.argv[4]), indent=2))
    elif len(sys.argv) > 4 and sys.argv[1] == 'send':
        print(json.dumps(send_email(sys.argv[2], sys.argv[3], sys.argv[4]), indent=2))
    else:
        print("Usage: gmail.py [list <query> <limit> | draft <to> <subject> <body> | send <to> <subject> <body>]")
