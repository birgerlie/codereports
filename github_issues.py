from github import Github
from settings import *


class GithubIssues:
    def __init__(self):
        self.gspot = Github(GITHUB_ACCESS_TOKEN)
        self.issues = []
        for repo_name in REPOS:
            for issue in self.get_issues(repo_name):
                self.issues.append(issue)

    def get_issues(self, repo):
        repo = self.gspot.get_repo(repo)
        issues = repo.get_issues(state="open")
        return issues


if __name__ == '__main__':
    issues = GithubIssues()
