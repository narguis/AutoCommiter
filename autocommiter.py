import os
import random
import subprocess
import requests
from datetime import datetime

username = 'narguis'
today = datetime.now().strftime("%Y-%m-%d")

# Path to the files that will be gradually uploaded
files_to_upload = ""

def commited_today():
    api_url = "https://api.github.com/search/commits?q=author:narguis+committer-date:2024-03-22"
    response = requests.get(api_url).json()
    print(response)
    if response['total_count'] == 0:
        return False
    else:
        return True

print(commited_today())
