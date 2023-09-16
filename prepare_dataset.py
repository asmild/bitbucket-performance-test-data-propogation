import sys
sys.path.append('../app')

import yaml
import os
from pathlib import Path
from bitbucket_client_extended import BitbucketRestClientExtended
# from util.api.bitbucket_clients import BitbucketRestClient
from util.conf import BitbucketSettings
from util.project_paths import BITBUCKET_YML

PROJECT_NAME = 'PROJECT_1'

def main():
    BITBUCKET_SETTINGS = BitbucketSettings(config_yml=BITBUCKET_YML)
    print("Started preparing data")

    url = BITBUCKET_SETTINGS.server_url
    client = BitbucketRestClientExtended(url, BITBUCKET_SETTINGS.admin_login, BITBUCKET_SETTINGS.admin_password,
                                 verify=BITBUCKET_SETTINGS.secure)

    local_repo_path = 'dataset'
    branchname = 'testbranch'
    main_branch = 'master'
    os.system(f'git config --global init.defaultBranch {main_branch}')

    for repo_num in range(20):
        repo_name = f'repo_{repo_num+1}'
        client.create_repo(
            PROJECT_NAME,
            repo_name,
            user=BITBUCKET_SETTINGS.admin_login,
            password=BITBUCKET_SETTINGS.admin_password
        )
        repo_url = f'{url}/scm/{PROJECT_NAME}/{repo_name}.git'


        os.system(f'cd {local_repo_path} && \
            rm -rf .git && \
            git init -b {main_branch} && \
            git add --all && \
            git commit -m "Initial Commit" && \
            git remote add origin http://{BITBUCKET_SETTINGS.admin_login}:{BITBUCKET_SETTINGS.admin_password}@localhost:7990/bitbucket/scm/{PROJECT_NAME}/{repo_name}.git && \
            git push -u origin HEAD:{main_branch} && \
            echo "Creating test branch" && \
            git checkout -b {branchname} && \
            echo "newtestline" >> testfile && \
            git add --all && \
            git commit -m "Some changes" && \
            git push --set-upstream origin {branchname} && \
            git switch {main_branch} && rm -rf .git')

        client.create_pull_request(
            project_key=PROJECT_NAME,
            repo_name=repo_name,
            source_branch=branchname,
            target_branch=main_branch,
            user=BITBUCKET_SETTINGS.admin_login,
            password=BITBUCKET_SETTINGS.admin_password)

if __name__ == "__main__":
    main()
