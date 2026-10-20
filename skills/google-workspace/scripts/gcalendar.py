#!/usr/bin/env python3
import sys
import json
from datetime import datetime, timezone
from auth import get_service

def list_events(max_results=10):
    service = get_service('calendar', 'v3')
    now = datetime.now(timezone.utc).isoformat()
    res = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=max_results,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = res.get('items', [])
    return [{
        'id': e.get('id'),
        'summary': e.get('summary'),
        'start': e.get('start', {}).get('dateTime', e.get('start', {}).get('date')),
        'end': e.get('end', {}).get('dateTime', e.get('end', {}).get('date')),
        'htmlLink': e.get('htmlLink')
    } for e in events]

def create_event(summary, start_iso, end_iso, description=None):
    service = get_service('calendar', 'v3')
    body = {
        'summary': summary,
        'description': description or '',
        'start': {'dateTime': start_iso},
        'end': {'dateTime': end_iso}
    }
    event = service.events().insert(calendarId='primary', body=body).execute()
    return event

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        print(json.dumps(list_events(limit), indent=2))
    elif len(sys.argv) > 4 and sys.argv[1] == 'create':
        desc = sys.argv[5] if len(sys.argv) > 5 else ''
        print(json.dumps(create_event(sys.argv[2], sys.argv[3], sys.argv[4], desc), indent=2))
    else:
        print("Usage: gcalendar.py [list <limit> | create <summary> <start_iso> <end_iso> <description>]")
