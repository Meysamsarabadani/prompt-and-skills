#!/usr/bin/env python3
import sys
import json
from auth import get_service

def create_presentation(title):
    service = get_service('slides', 'v1')
    p = service.presentations().create(body={'title': title}).execute()
    pid = p.get('presentationId')
    return {'id': pid, 'url': f'https://docs.google.com/presentation/d/{pid}/edit'}

def add_slide(presentation_id, title_text, bullets=None):
    service = get_service('slides', 'v1')
    slide_id = f"slide_{abs(hash(title_text)) % 1000000}"
    body_id = f"body_{abs(hash(title_text)) % 1000000}"
    
    requests = [
        {
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': 'TITLE_AND_BODY'}
            }
        }
    ]
    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={'requests': requests}
    ).execute()
    return {'status': 'success', 'slide_id': slide_id}

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'create':
        print(json.dumps(create_presentation(sys.argv[2]), indent=2))
    elif len(sys.argv) > 3 and sys.argv[1] == 'add-slide':
        bullets = sys.argv[4].split('|') if len(sys.argv) > 4 else []
        print(json.dumps(add_slide(sys.argv[2], sys.argv[3], bullets), indent=2))
    else:
        print("Usage: gslides.py [create <title> | add-slide <presentation_id> <title> <bullets_separated_by_pipe>]")
