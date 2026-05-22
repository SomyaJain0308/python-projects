"""
Task Scheduling: The project utilizes the schedule module to run the backup process automatically at specific, user-defined times.
Automated Copying: It uses the shutil library, specifically the copy tree function, to recursively copy all contents from a source directory to 
a designated destination.
Dynamic Naming: The datetime module is used to ensure each backup is stored in a folder labeled with the current date, which helps in maintaining
an organized history of files.
File System Operations: The os module is employed to handle interactions with the operating system, allowing the script to verify paths and manage 
directory structures effectively.
"""
import schedule, shutil, datetime, os, time

def cop(base_dir, backup_dir):
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    final_backup_path = os.path.join(backup_dir, today_str)
    if not os.path.exists(final_backup_path):
        shutil.copytree(base_dir, final_backup_path)
        print("Backup Created!")
    else:
        print("Backup not created. This may happen because backup was already created for today or the code is just wrong!")

def main():
    base_dir="/home/batman/clg"
    backup_dir="/home/batman/clg_backup"
    schedule.every().day.at("12:30").do(
    cop, base_dir=base_dir, backup_dir=backup_dir
    )
    cop(base_dir, backup_dir)
    print("Scheduler running... Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__=="__main__":
    main()