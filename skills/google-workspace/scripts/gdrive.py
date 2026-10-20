#!/usr/bin/env python3
import sys
import io
import json
from auth import get_service
from googleapiclient.http import MediaIoBaseDownload

def list_files(query=None, limit=20):
    service = get_service('drive', 'v3')
    q = query if query else "trashed = false"
    res = service.files().list(
        q=q,
        pageSize=limit,
        fields="files(id, name, mimeType, modifiedTime)"
    ).execute()
    return res.get('files', [])

def export_file(file_id, mime_type='text/plain'):
    service = get_service('drive', 'v3')
    req = service.files().export_media(fileId=file_id, mimeType=mime_type)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, req)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    fh.seek(0)
    return fh.read().decode('utf-8')

def add_comment(file_id, comment_text):
    service = get_service('drive', 'v3')
    comment = service.comments().create(
        fileId=file_id,
        fields='id, content, createdTime, author',
        body={'content': comment_text}
    ).execute()
    return comment

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        q = sys.argv[2] if len(sys.argv) > 2 else None
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        print(json.dumps(list_files(q, limit), indent=2))
    elif len(sys.argv) > 2 and sys.argv[1] == 'read':
        print(export_file(sys.argv[2]))
    elif len(sys.argv) > 3 and sys.argv[1] == 'comment':
        print(json.dumps(add_comment(sys.argv[2], sys.argv[3]), indent=2))
    else:
        print("Usage: gdrive.py [list <query> <limit> | read <file_id> | comment <file_id> <text>]")
