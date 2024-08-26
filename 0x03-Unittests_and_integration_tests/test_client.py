#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google",
                    "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc",
                 "repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')  # Mock 'get_json' in the context of 'client'
    def test_org(self, org_name, expected_org_data, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        # Setup the mock to return the expected_org_data
        mock_get_json.return_value = expected_org_data

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org property
        org_data = client.org

        # Assert get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert the returned data is as expected
        self.assertEqual(org_data, expected_org_data)


if __name__ == "__main__":
    unittest.main()
