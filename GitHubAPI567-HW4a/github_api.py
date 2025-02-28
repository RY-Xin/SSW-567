import requests

def get_user_repos_commits(user_id):
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)
    repos = repos_response.json()

    result = []
    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        commits = commits_response.json()
        result.append(f"Repo: {repo_name} Number of commits: {len(commits)}")
    return result

if __name__ == "__main__":
    user_id = input("Enter GitHub user ID: ")
    repos_commits = get_user_repos_commits(user_id)
    for line in repos_commits:
        print(line)