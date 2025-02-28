import requests

def get_user_repos_commits(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data from GitHub API")
        return []

    repos = response.json()
    repos_commits = []

    for repo in repos:
        if isinstance(repo, dict):
            repo_name = repo['name']
            commits_url = repo['commits_url'].split('{')[0]
            commits_response = requests.get(commits_url)
            
            if commits_response.status_code == 200:
                commits = commits_response.json()
                commits_count = len(commits)
                repos_commits.append((repo_name, commits_count))

    return repos_commits

if __name__ == "__main__":
    user_id = input("Enter GitHub user ID: ")
    repos_commits = get_user_repos_commits(user_id)

    if repos_commits:
        for repo_name, commit_count in repos_commits:
            print(f"Repository: {repo_name}, Commits: {commit_count}")
    else:
        print("No repositories found or error fetching data.")
