import os
import json
import requests
import ctypes
from dataclasses import dataclass


@dataclass
class GitHubIssueConfig:
    repo_owner: str
    repo_name: str
    access_token: str
    issue_title: str
    issue_body: str
    how_many: int

class GitHubIssueCreator:
    def __init__(self, config: GitHubIssueConfig):
        self.config = config

    def create_github_issue(self):
        url = f'https://api.github.com/repos/{self.config.repo_owner}/{self.config.repo_name}/issues'
        issue_data = {
            'title': self.config.issue_title,
            'body': self.config.issue_body
        }
        headers = {
            'Authorization': f'token {self.config.access_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        status_code = self.github_issue_creator(url, issue_data, headers)
        if status_code == 201:
            print(f"Created Issue ~ {self.config.repo_owner}/{self.config.repo_name}")

    @staticmethod
    def github_issue_creator(url, issue_data, headers):
        response = requests.post(url, data=json.dumps(issue_data), headers=headers)
        return response.status_code

    def run(self):
        ctypes.windll.kernel32.SetConsoleTitleW('[GitHub Issue Creator] created by H4cK3dR4Du | updated by cxstles (reciprocated)')
        for _ in range(self.config.how_many):
            self.create_github_issue()

    def __str__(self):
        return f"GitHub Issue Creator for {self.config.repo_owner}/{self.config.repo_name}"

if __name__ == "__main__":
    config = GitHubIssueCreator.load_config('config.json')
    issue_creator = GitHubIssueCreator(config)
    issue_creator.run()
