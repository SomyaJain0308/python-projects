import json
import requests
BASE_URL = "https://cricapi.com"
API_KEY = "3ad669ea-4a8e-4c9e-a2e3-f83475c38e59"
try:
    response = requests.get(BASE_URL + "?apikey=" + API_KEY + "&offset=0", timeout=10)
    api_data = response.json()
    with open("cricket_data.json", "w") as file:
        json.dump(api_data, file, indent=4)
except Exception:
    print("⚠️ Network blocked or JSON empty. Loading from local 'cricket_data.json' backup...")
    try:
        with open("cricket_data.json", "r") as file:
            api_data = json.load(file)
    except Exception:
        print("❌ Error: Backup file is empty or corrupted.")
        exit()
print("~" * 63)
print("                       IPL LIVE TRACKER                        ")
print("~" * 63)
if "data" in api_data:
    ipl_match_found = False
    team_1 = input("TEAM 1: ").strip().lower()
    team_2 = input("TEAM 2: ").strip().lower()
    for match in api_data["data"]:
        name = match.get("name", "Unknown Match")
        name_lower = name.lower()
        if team_1 in name_lower or team_2 in name_lower:
            ipl_match_found = True
            status = match.get("status", "No status available")
            match_type = match.get("matchType", "N/A").upper()
            print(f"[{match_type}] {name}")
            print(f"Status: {status}")
            score_data = match.get("score", [])
            if score_data:
                print("Live Scorecard:")
                for innings in score_data:
                    inning_name = innings.get("inning")
                    runs = innings.get("r")
                    wickets = innings.get("w")
                    overs = innings.get("o")
                    print(f"  * {inning_name}: {runs}/{wickets} ({overs} ov)")
            else:
                print("Live Scorecard: Match has not started or innings data pending.")
            print("~" * 63)
    if not ipl_match_found:
        print(f"Match containing '{team_1}' or '{team_2}' not found in the live active stream yet.")
        print("~" * 63)
else:
    print("No active live matches found in the API response.")
    print("~" * 63)
