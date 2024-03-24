import os
import random
import subprocess
import requests
from datetime import datetime

# Path to the files that will be gradually uploaded
files_to_upload = ""
username = "narguis"
token = ""
today = datetime.now().strftime("%Y-%m-%d")

# If False, you will only commit the difference between your desired commits and your commits today
# If True, the code will always commit your desired amount of commits
always_commit = False
desired_commits = 1

def commits_today():
    api_url = f"https://api.github.com/search/commits?q=author:{username}+committer-date:{today}"
    
    # Remove this line if you want the code to access only your public commits
    headers = {"Authorization": f"token {token}"}
    # Remove the headers paramater if you want the code to access only your public commits
    response = requests.get(api_url, headers=headers).json()

    print(response)
    return response['total_count']

def commit(amount):
    pass

if not always_commit:
    remaining = desired_commits - commits_today()
    if remaining > 0:
        commit(remaining)

else:
    commit(desired_commits)
