---
name: google-workspace
description: >-
  Complete Google Workspace suite integration for Google Drive, Google Docs,
  Google Slides, Google Sheets, Google Calendar, and Gmail. Use this skill
  whenever the user wants to read, create, edit, or comment on Google Docs,
  Slides, or Sheets; search or download files from Google Drive; list, check, or
  schedule Google Calendar meetings; or search, read, draft, or send Gmail emails.
---

# Google Workspace Skill

This skill provides full-lifecycle programmatic integration with Google Workspace (Google Drive, Docs, Sheets, Slides, Calendar, and Gmail) using the authenticated credentials at `~/.gemini/gdrive_token.json`.

---

## Quick Reference Workflows

### 1. Google Drive & Docs
- **Search Drive:** Run `python3 scripts/gdrive.py list "<query>" <limit>`.
- **Read / Export Document:** Run `python3 scripts/gdrive.py read <file_id>`.
- **Create Google Doc:** Run `python3 scripts/gdocs.py create "<title>" "<initial_text>"`.
- **Append to Google Doc:** Run `python3 scripts/gdocs.py append <doc_id> "<text>"`.
- **Add Drive Comment:** Run `python3 scripts/gdrive.py comment <file_id> "<comment_text>"`.

### 2. Google Slides & Sheets
- **Create Presentation:** Run `python3 scripts/gslides.py create "<title>"`.
- **Add Slide:** Run `python3 scripts/gslides.py add-slide <presentation_id> "<title>" "<bullet1|bullet2>"`.
- **Create Spreadsheet:** Run `python3 scripts/gsheets.py create "<title>" '<json_rows>'`.
- **Read Spreadsheet Range:** Run `python3 scripts/gsheets.py read <spreadsheet_id> "<range>"`.

### 3. Google Calendar & Gmail
- **List Upcoming Events:** Run `python3 scripts/gcalendar.py list <limit>`.
- **Create Calendar Event:** Run `python3 scripts/gcalendar.py create "<summary>" "<start_iso>" "<end_iso>" "<description>"`.
- **Search Emails:** Run `python3 scripts/gmail.py list "<query>" <limit>`.
- **Create Gmail Draft:** Run `python3 scripts/gmail.py draft "<to>" "<subject>" "<body>"`.
- **Send Email:** Run `python3 scripts/gmail.py send "<to>" "<subject>" "<body>"`.

---

## Detailed Specifications
See [API Reference](./references/api_reference.md) for full argument details and command options.
