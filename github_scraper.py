import requests
from bs4 import BeautifulSoup

response = requests.get("https://github.com/Analog-Devices-MSDK/msdk")
soup = BeautifulSoup(response.text, 'html.parser')
num_commits = soup.find_all('span', class_="d-none d-sm-inline")[1].find('strong').text
#print(f"msdk repo contains {num_commits} commits")

last_commit_user = soup.find("a", class_="commit-author user-mention").text
#print(last_commit_user)

commit_message = soup.find("a",class_="Link--primary markdown-title")['title'].replace("\n"," ")
#print(commit_message)

commit_time = soup.find("relative-time",class_="no-wrap")['datetime'][:-1]

commit_date = soup.find("relative-time",class_="no-wrap").text

#print(f"{commit_date} {commit_time}")

issues_count = soup.find("span", id="issues-repo-tab-count").text
#print(f"Issues Count: {issues_count}")

pr_count = soup.find("span", id="pull-requests-repo-tab-count").text
#print(f"Pull Requests: {pr_count}")

fork_count = soup.find("span", id="repo-network-counter").text
#print(f"Fork Count: {fork_count}")

star_count = soup.find("span", id="repo-stars-counter-star").text
#print(f"Star Count: {star_count}")


# PUTTING IT ALL TOGETHER

#DICTIONARY
repo_info = {
    "last_user":last_commit_user,
    "date": commit_date,
    "time": commit_time,
    "message": commit_message,
    "commits": num_commits,
    "issues": issues_count,
    "pull_requests": pr_count,
    "forks": fork_count,
    "stars": star_count,
    
}

# PRINTING OUT EACH KEY AND VALUE FROM DICTIONARY
for key, value in repo_info.items():
    print(f"{key:<20}{value}")