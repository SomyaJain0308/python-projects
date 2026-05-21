"""
The NBA Stats & Current Scores project is an excellent way to learn about working with APIs and processing external data in Python.
Understanding the API: The project utilizes the free data.nba.net API. You begin by sending a request to the main endpoint to get a list of 
available data links.
Fetching Data: You will learn to use the requests library to send GET requests to specific endpoints and process the returned data, which is 
in JSON format.
Displaying Live Scores: You will navigate the JSON structure to extract information like home/away teams, game scores, clock status, and periods.
Processing Statistics: The project shows how to fetch team leaders and league statistics.
Filtering and Sorting: You will learn how to filter out unnecessary data, sort teams based on specific criteria like Points Per Game (PPG) using 
a lambda function, and format the output for readability.
"""
import json
import requests

