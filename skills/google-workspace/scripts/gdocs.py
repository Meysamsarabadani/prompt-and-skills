#!/usr/bin/env python3
import sys
import json
from auth import get_service

def create_doc(title, initial_text=None):
    service = get_service('docs', 'v1')
    doc = service.documents().create(body={'title': title}).execute()
    doc_id = doc.get('documentId')
    
    if initial_text:
        requests = [{
            'insertText': {
                'location': {'index': 1},
                'text': initial_text
            }
        }]
        service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()
    return {'id': doc_id, 'url': f'https://docs.google.com/document/d/{doc_id}/edit'}

def append_to_doc(doc_id, text_to_append):
    service = get_service('docs', 'v1')
    doc = service.documents().get(documentId=doc_id).execute()
    content = doc.get('body', {}).get('content', [])
    end_index = content[-1]['endIndex'] - 1
    
    requests = [{
        'insertText': {
            'location': {'index': end_index},
            'text': '\n' + text_to_append
        }
    }]
    service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()
    return {'status': 'success', 'id': doc_id}

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'create':
        title = sys.argv[2]
        content = sys.argv[3] if len(sys.argv) > 3 else None
        print(json.dumps(create_doc(title, content), indent=2))
    elif len(sys.argv) > 3 and sys.argv[1] == 'append':
        doc_id = sys.argv[2]
        text = sys.argv[3]
        print(json.dumps(append_to_doc(doc_id, text), indent=2))
    else:
        print("Usage: gdocs.py [create <title> <content> | append <doc_id> <content>]")
