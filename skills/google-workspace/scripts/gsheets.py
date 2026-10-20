#!/usr/bin/env python3
import sys
import json
from auth import get_service

def create_sheet(title, rows=None):
    service = get_service('sheets', 'v4')
    sheet = service.spreadsheets().create(
        body={'properties': {'title': title}}
    ).execute()
    sid = sheet.get('spreadsheetId')
    
    if rows:
        service.spreadsheets().values().update(
            spreadsheetId=sid,
            range='Sheet1!A1',
            valueInputOption='USER_ENTERED',
            body={'values': rows}
        ).execute()
    return {'id': sid, 'url': f'https://docs.google.com/spreadsheets/d/{sid}/edit'}

def read_sheet(spreadsheet_id, range_name='Sheet1!A1:Z100'):
    service = get_service('sheets', 'v4')
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    return result.get('values', [])

def append_rows(spreadsheet_id, range_name, rows):
    service = get_service('sheets', 'v4')
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='USER_ENTERED',
        body={'values': rows}
    ).execute()
    return result

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'create':
        rows = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
        print(json.dumps(create_sheet(sys.argv[2], rows), indent=2))
    elif len(sys.argv) > 2 and sys.argv[1] == 'read':
        r = sys.argv[3] if len(sys.argv) > 3 else 'Sheet1!A1:Z50'
        print(json.dumps(read_sheet(sys.argv[2], r), indent=2))
    elif len(sys.argv) > 4 and sys.argv[1] == 'append':
        rows = json.loads(sys.argv[4])
        print(json.dumps(append_rows(sys.argv[2], sys.argv[3], rows), indent=2))
    else:
        print("Usage: gsheets.py [create <title> <json_rows> | read <id> <range> | append <id> <range> <json_rows>]")
