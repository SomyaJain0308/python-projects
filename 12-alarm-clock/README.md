# 12 — Alarm Clock

A terminal countdown timer that takes hours, minutes, and seconds as input, counts down to zero, and plays an alarm sound when time's up.

## How to Run

```bash
pip install playsound
python alarm.py
```

Make sure `alarm.mp3` is in the same folder as `alarm.py`.

## Example

```
Hours: 0
Minutes: 0
Seconds: 10
#After 10 seconds
00:00:00
Time's up!
```

## What I Learned

- Converting hours/minutes/seconds into total seconds for clean countdown logic
- `from time import sleep` for time-based loops
- Integrating an external `.mp3` file with `playsound`

## Sound Compatibility

| Environment | Does it work? |
|---|---|
| Local Windows/Mac (Python 3.10–3.12) | ✅ Yes |
| GitHub Codespaces | ❌ No — no audio output in browser-based environments |
| Local Linux | ⚠️ Sometimes — may need `sudo apt install python3-gst-1.0` |

If sound doesn't work in your environment, replace `playsound('alarm.mp3')` with `print("\a")` for a terminal bell, or just rely on the "Time's up!" print.

## What I'd Improve

- Add live display with `end="\r"` so the timer visibly counts down instead of a blank terminal
- Fix the `while True / if secs != 0` logic — entering 0 seconds causes an infinite loop