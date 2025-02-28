import unittest
from unittest.mock import patch
from github_api import get_user_repos_commits

class TestGitHubAPI(unittest.TestCase):
    @patch('github_api.requests.get')
    def test_user_repos_commits(self, mock_get):
        mock_repos_data = [
            {'name': 'repo1', 'commits_url': 'https://api.github.com/repos/test_user/repo1/commits{/sha}'},
            {'name': 'repo2', 'commits_url': 'https://api.github.com/repos/test_user/repo2/commits{/sha}'}
        ]
        mock_get.return_value.json.return_value = mock_repos_data
        mock_get.return_value.status_code = 200
        
        mock_commits_data = [{'sha': 'commit1'}, {'sha': 'commit2'}]
        def side_effect(url):
            if 'commits' in url:
                mock_get.return_value.json.return_value = mock_commits_data
            return mock_get

        mock_get.side_effect = side_effect

        user_id = "test_user"
        result = get_user_repos_commits(user_id)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [('repo1', 2), ('repo2', 2)])

if __name__ == '__main__':
    unittest.main()
