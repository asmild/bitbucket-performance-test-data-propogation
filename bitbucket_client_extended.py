import sys, time, requests

sys.path.append('../app')

from util.api.bitbucket_clients import BitbucketRestClient


class BitbucketRestClientExtended(BitbucketRestClient):

    def create_repo(self, project_key, repo_name, user = '', password = ''):
        start_time = time.time()
        params = {
            'name': repo_name,
            'scmId': 'git',
            'forkable': 'true',
            'description': 'This is test repo',
        }
        api_url = f'{self.host}/rest/api/1.0/projects/{project_key}/repos'

        # this gets 400 response: No content to map to Object due to end of input","exceptionName":"java.io.EOFException"
        # response = self.post(api_url, "Could not create repository", params=params)

        response = requests.post(
            api_url,
            json=params,
            headers={'Content-Type': 'application/json'},
            auth=(user, password)
        )

        if response.ok:
            print(f'Successfully created repository [{repo_name}] in {project_key} project, in [{(time.time() - start_time)}]')
        else:
            print(response.text)
        return response

    def create_pull_request(self, project_key, repo_name, source_branch, target_branch, user = '', password = ''):
        start_time = time.time()
        params = {
            'title': 'Test PR',
            'description': 'This is test PR',
            'state': 'OPEN',
            'open': True,
            'fromRef': {
                'id': f'refs/heads/{source_branch}',
                'repository': {
                    'slug': repo_name,
                    'project': {
                        'key': project_key
                    }
                }
            },
            'toRef': {
                'id': f'refs/heads/{target_branch}',
                'repository': {
                    'slug': repo_name,
                    'project': {
                        'key': project_key
                    }
                }
            },
        }

        api_url = f'{self.host}/rest/api/1.0/projects/{project_key}/repos/{repo_name}/pull-requests'

        # this gets 400 response: No content to map to Object due to end of input","exceptionName":"java.io.EOFException"
        # response = self.post(api_url, "Could not create PR", params=params)

        response = requests.post(
            api_url,
            json=params,
            headers={'Content-Type': 'application/json'},
            auth=(user, password)
        )

        if response.ok:
            print(f'Successfully created repository [{repo_name}] in {project_key} project, in [{(time.time() - start_time)}]')
        else:
            print(response.text)
        return response