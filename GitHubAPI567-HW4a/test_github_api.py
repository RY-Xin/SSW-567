import unittest
from unittest.mock import patch
from github_api import get_user_repos_commits

class TestGitHubAPI(unittest.TestCase):
    @patch('github_api.requests.get')
    def test_user_repos_commits(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: [
                {"name": "Repo1", "commits_url": "https://api.github.com/repos/user/Repo1/commits{/sha}"},
                {"name": "Repo2", "commits_url": "https://api.github.com/repos/user/Repo2/commits{/sha}"}
            ]),
            unittest.mock.Mock(status_code=200, json=lambda: [{}, {}, {}]),  
            unittest.mock.Mock(status_code=200, json=lambda: [{}, {}])  
        ]

        result = get_user_repos_commits("test_user")
        self.assertEqual(result, [("Repo1", 3), ("Repo2", 2)])

if __name__ == '__main__':
    unittest.main()
