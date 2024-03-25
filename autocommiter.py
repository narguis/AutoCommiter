import os
import random
import subprocess
import requests
from datetime import datetime
from git import Repo

# Paths to the files that will be gradually uploaded
path_commits = "../LeetCode"
username = "narguis"
token = ""
today = datetime.now().strftime("%Y-%m-%d")

# If False, you will only commit the difference between your desired commits and your commits today
# If True, the code will always commit your desired amount of commits
always_commit = False
desired_commits = 1


def commit(path, message = ''):
    pass


def find_files(path):
    uncommited = []
    repo = Repo(path)
    files = os.listdir(path)
    
    for file in files:
        if not(repo.git.status('--porcelain', file).startswith('D')):
            uncommited.append(file)
            
    print(uncommited)
    
    # for root, directories, files in os.walk(root_directory):
    # for file in files:
    #     file_path = os.path.join(root, file)
    #     if not(repo.git.status('--porcelain', file_path).startswith('D')):
    #         uncommited.append(file_path)

    # print(uncommited)

def commits_today():
    api_url = f"https://api.github.com/search/commits?q=author:{username}+committer-date:{today}"
    
    # Remove this line if you don't want the code to access your private commits
    headers = {"Authorization": f"token {token}"}
    # Remove the headers paramater if you don't want the code to access your private commits
    response = requests.get(api_url, headers=headers).json()
    
    return response['total_count']

if not always_commit:
    remaining = desired_commits - commits_today()
    if remaining > 0:
        commit(remaining)

else:
    commit(desired_commits)


find_files(path_commits)