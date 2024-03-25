import os
import random
import subprocess
import requests
from datetime import datetime
from git import Repo
import tkinter as tk

# Paths to the files that will be gradually uploaded
path_commits = "./"
username = "narguis"
token = ""
today = datetime.now().strftime("%Y-%m-%d")

# If False, you will only commit the difference between your desired commits and your commits today
# If True, the code will always commit your desired amount of commits
always_commit = False
desired_commits = 1
    

def find_files(path):
    uncommited = []
    repo = Repo(path)
    files = os.listdir(path)
    
    for file in files:
        file_status = repo.git.status('--porcelain', file)

        if file_status and not file_status.startswith('D'):
            # Split the multiline string into separate lines
            file_status_lines = file_status.splitlines()
            # Append each line individually to the uncommitted list
            for line in file_status_lines:
                uncommited.append(line[3:])
            
    return uncommited

def commits_today():
    api_url = f"https://api.github.com/search/commits?q=author:{username}+committer-date:{today}"
    
    # Remove this line if you don't want the code to access your private commits
    headers = {"Authorization": f"token {token}"}
    # Remove the headers paramater if you don't want the code to access your private commits
    response = requests.get(api_url, headers=headers).json()
    
    return response['total_count']


def push_commit(amount, files):

    for i in range(amount):
        repo = Repo(path)

        repo.git.add(path)
        repo.index.commit(f"Changes made to {file}")
        repo.remotes.origin.push()

    for file in files:
        message = f"Changes made to {file}"

    if not always_commit:
        remaining = desired_commits - commits_today()
    else:
        remaining = desired_commits

    if remaining > 0:
        commit(remaining)

    else:
        commit(desired_commits)


    find_files(path_commits)
    
    for i in range(remaining):
        repo = Repo(path)
        repo.git.add(path)
        repo.index.commit(message)
        repo.remotes.origin.push()

def popup():
    popup = tk.Tk()
    popup.title("Choose your repository")

def commit():
    find_files(path_commits)


commit()

if not always_commit:
    remaining = desired_commits - commits_today()
else:
    commit(desired_commits, find_files(path_commits))




print(find_files(path_commits))

