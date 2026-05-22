# Daily Automated Directory Backup

A lightweight Python script that automatically clones a source directory into a date-stamped backup folder every day at a specified time.

## 🚀 Features
* **Immediate Test Run**: Executes a backup immediately upon launch to verify configurations.
* **Automated Scheduling**: Runs seamlessly every day at 12:30 PM using the `schedule` library.
* **Chronological Sorting**: Organizes backups by date using the `YYYY-MM-DD` naming convention.
* **Collision Safety**: Prevents accidental overwrites by checking if today's backup folder already exists.
* **Low CPU Overhead**: Sleeps for 3-second intervals to minimize processor usage.

## 🛠️ Prerequisites
You need Python 3.x installed along with the `schedule` library. Install the dependency via pip:

```bash
pip install schedule
```

## ⚙️ Configuration
Open the script and update the paths inside the `main()` function to match your environment:
* `base_dir`: The path to the folder you want to back up (e.g., `/home/batman/clg`).
* `backup_dir`: The destination root folder where backups will accumulate (e.g., `/home/batman/clg_backup`).

## 💻 Usage
Run the script directly from your terminal:

```bash
python backup_script.py
```
*Leave this terminal window open to keep the script running in the background.*

---

## 🛠️ Future Improvements & Code Enhancements

While the current script works perfectly for basic daily tasks, implementing the following upgrades will make it production-ready, robust, and storage-efficient:

### 1. Storage Optimization (Zipping Backups)
* **Problem**: `shutil.copytree` duplicates raw folders, which quickly drains hard drive space.
* **Fix**: Use `shutil.make_archive` to compress the backup folder into a `.zip` or `.tar.gz` file instead.

### 2. Auto-Cleanup / Retention Policy
* **Problem**: Backups will pile up infinitely until the drive is completely full.
* **Fix**: Add a function that scans the `backup_dir`, calculates the folder ages, and automatically deletes backups older than a set threshold (e.g., older than 30 days).

### 3. Professional Logging
* **Problem**: `print()` statements disappear the moment the terminal is closed, leaving no historical record of failures.
* **Fix**: Replace `print()` with Python's built-in `logging` module to output success and error status codes directly to a persistent `backup.log` file.

### 4. Robust Error Handling (`try-except` blocks)
* **Problem**: If a file in the source directory is locked, corrupted, or permission is denied, the script will crash entirely and stop scheduling future backups.
* **Fix**: Wrap `shutil.copytree` in a `try...except Exception as e:` block so the script logs the error but remains alive to try again the next day.

### 5. Environment Variables & CLI Arguments
* **Problem**: Hardcoding absolute file paths like `/home/batman/clg` makes the script difficult to share or use on different machines.
* **Fix**: Use `argparse` or `os.environ` to pass the folder paths dynamically when launching the script.
