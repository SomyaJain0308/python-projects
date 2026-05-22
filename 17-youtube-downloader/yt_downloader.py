"""
Purpose: This tool is designed to programmatically download YouTube videos.
Automation Focus: It falls under the category of "Beginner Automation Projects," demonstrating how Python can interact with external web resources 
to automate repetitive tasks.
Implementation: The walkthrough covers how to write a script that can take a URL and download the corresponding video content.
Skills Applied:
Working with external libraries for video processing.
Handling HTTP requests or specific automation modules within Python.
Structuring scripts for file management and automation.
"""
import yt_dlp
video_url=input("URL: ").lower()
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([video_url])