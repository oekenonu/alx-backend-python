#!/usr/bin/env python3
"""Module to test GithubOrgClient"""
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

        mock_get_json.return_value = expected_org_data
        client = GithubOrgClient(org_name)
        org_data = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert the returned data is as expected
        self.assertEqual(org_data, expected_org_data)


if __name__ == "__main__":
    unittest.main()
