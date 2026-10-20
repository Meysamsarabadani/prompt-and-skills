# Google Workspace Skill CLI Reference

All helper scripts reside in `scripts/` and use the stored OAuth credentials from `~/.gemini/gdrive_token.json`.

---

## 1. Google Drive (`gdrive.py`)
- **List Files:**
  ```bash
  python3 scripts/gdrive.py list "name contains 'SnappPay'" 20
  ```
- **Read / Export Document as Text:**
  ```bash
  python3 scripts/gdrive.py read <file_id>
  ```
- **Post Review Comment:**
  ```bash
  python3 scripts/gdrive.py comment <file_id> "Recommendation: Adopt Continuous Flow instead of 2-week sprints."
  ```

---

## 2. Google Docs (`gdocs.py`)
- **Create Document:**
  ```bash
  python3 scripts/gdocs.py create "Problem Brief: Subscription Pay+" "Problem Statement:\n..."
  ```
- **Append Text:**
  ```bash
  python3 scripts/gdocs.py append <doc_id> "\n## Architecture Non-Functional Requirements\n..."
  ```

---

## 3. Google Slides (`gslides.py`)
- **Create Deck:**
  ```bash
  python3 scripts/gslides.py create "SnappPay Operating Model Review"
  ```
- **Add Slide:**
  ```bash
  python3 scripts/gslides.py add-slide <presentation_id> "Pod Triad Architecture" "EM: People|TL: Architecture|TDM: Milestones"
  ```

---

## 4. Google Sheets (`gsheets.py`)
- **Create Spreadsheet:**
  ```bash
  python3 scripts/gsheets.py create "1405 Q3 Pod OKR Tracker" '[["Pod", "Objective", "Status"], ["Wallet", "Zero Stalls", "On Track"]]'
  ```
- **Read Values:**
  ```bash
  python3 scripts/gsheets.py read <spreadsheet_id> "Sheet1!A1:D10"
  ```
- **Append Rows:**
  ```bash
  python3 scripts/gsheets.py append <spreadsheet_id> "Sheet1!A1" '[["Checkout", "Sunsetting Scrum", "In Progress"]]'
  ```

---

## 5. Google Calendar (`gcalendar.py`)
- **List Upcoming Events:**
  ```bash
  python3 scripts/gcalendar.py list 10
  ```
- **Schedule Event:**
  ```bash
  python3 scripts/gcalendar.py create "Triad Alignment Sync" "2026-10-22T10:00:00Z" "2026-10-22T11:00:00Z" "Agenda: Review RFC for Continuous Flow"
  ```

---

## 6. Gmail (`gmail.py`)
- **Search Emails:**
  ```bash
  python3 scripts/gmail.py list "from:bahar newer_than:7d" 10
  ```
- **Create Draft:**
  ```bash
  python3 scripts/gmail.py draft "bahar@snapppay.ir" "Advisory Feedback: Pod Triad Alignment" "Hi Bahar,\n\n..."
  ```
- **Send Email:**
  ```bash
  python3 scripts/gmail.py send "bahar@snapppay.ir" "Advisory Feedback: Pod Triad Alignment" "Hi Bahar,\n\n..."
  ```
