# 🏏 IPL Live Tracker

A Python-based terminal tool that fetches and displays **live IPL match scores** using the [CricAPI](https://cricapi.com) service. It lets you search for a match by entering team names and instantly see the live scorecard in your terminal.

---

## 📋 Features

- Fetches live cricket match data from the CricAPI
- Search matches by team name (case-insensitive)
- Displays live scorecard with runs, wickets, and overs per innings
- Graceful fallback to a local JSON backup if the API is unavailable or the network is blocked

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install dependencies with:

```bash
pip install requests
```

---

## ⚙️ Setup

1. Clone or download this repository.
2. Open the script and replace the `API_KEY` with your own key from [CricAPI](https://cricapi.com):

```python
API_KEY = "your_api_key_here"
```

3. Run the script:

```bash
python ipl_tracker.py
```

---

## 🚀 Usage

When prompted, enter the names (or partial names) of the two teams you want to track:

```
TEAM 1: Mumbai
TEAM 2: Chennai
```

The tracker will search for any live match containing either team name and display the current scorecard:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                       IPL LIVE TRACKER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[T20] Mumbai Indians vs Chennai Super Kings
Status: Match in progress
Live Scorecard:
  * Mumbai Indians Inning 1: 186/4 (20.0 ov)
  * Chennai Super Kings Inning 1: 142/6 (17.2 ov)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

## 📁 Backup / Offline Mode

If the API call fails (network issue, blocked endpoint, expired key), the tool automatically loads data from a local `cricket_data.json` file in the same directory. This allows the tracker to work in restricted environments.

---

## 📌 Notes

- The API endpoint used is `https://cricapi.com`. Ensure your API key is valid and active.
- Only matches currently live or recently active will appear in results.
- If a match hasn't started yet, the scorecard section will indicate that innings data is pending.

---

## 📂 File Structure

```
ipl_tracker.py          # Main script
cricket_data.json       # Auto-generated API cache / offline backup
README.md               # This file
```

---

---

# 🔧 What I Would Improve

## 1. Security — Remove Hardcoded API Key
The API key is exposed directly in the source code, which is a security risk (especially if this is pushed to GitHub).

**Fix:** Use environment variables or a `.env` file:
```python
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")
```
And add `.env` to `.gitignore`.

---

## 2. Fix the API URL
The base URL `https://cricapi.com` is incomplete — it's missing the actual endpoint path. A correct URL should look something like:
```python
BASE_URL = "https://api.cricapi.com/v1/currentMatches"
```
The current URL likely results in failed or malformed requests, which is why the backup JSON is always being hit.

---

## 3. Use a Config File or argparse
Hardcoding team names via `input()` is fine for personal use, but accepting them as command-line arguments makes the tool more scriptable and automation-friendly:
```bash
python ipl_tracker.py --team1 "Mumbai" --team2 "Chennai"
```

---

## 4. Add Proper Logging Instead of print()
Using `print()` for errors and warnings makes it hard to control verbosity or redirect output. Python's `logging` module is the right tool:
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.warning("Network blocked. Loading from backup...")
```

---

## 5. Split Into Functions
The entire script runs as one flat block of code. Refactoring it into functions makes it testable, reusable, and readable:
```python
def fetch_data(url, api_key): ...
def load_backup(path): ...
def display_match(match): ...
def main(): ...
```

---

## 6. Better Error Messages
The `except Exception` blocks swallow all errors silently. You should log the actual exception so debugging is possible:
```python
except Exception as e:
    print(f"⚠️ API error: {e}. Falling back to local data...")
```

---

## 7. Filter for IPL Matches Specifically
The search currently matches on any match name containing the team name. Adding an IPL-specific filter (e.g., checking `matchType == "T20"` and `name` contains `"IPL"`) would reduce false positives from other tournaments.

---

## 8. Add a `requirements.txt`
For anyone cloning this project, a `requirements.txt` makes setup straightforward:
```
requests==2.31.0
python-dotenv==1.0.0
```

---

## 9. Auto-Refresh / Polling Mode (Optional Enhancement)
For a live tracker, it would be useful to add a loop that refreshes scores every 30–60 seconds, rather than requiring the user to manually re-run the script:
```python
import time
while True:
    fetch_and_display()
    time.sleep(60)
```