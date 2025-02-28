import unittest
from github_api import get_user_repos_commits

class TestGitHubAPI(unittest.TestCase):
    def test_user_repos_commits(self):
        user_id = "richkempinski"
        result = get_user_repos_commits(user_id)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()