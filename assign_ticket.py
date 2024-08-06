import os
import requests
import json

def get_account_id(base_url, email, token, assignee):
    url = f'{base_url}/rest/api/3/user/search?query={assignee}'
    auth = (email, token)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        users = response.json()
        if users:
            return users[0]['accountId']
        else:
            print('No users found.')
            exit(1)
    else:
        print(f'Failed to retrieve users: {response.status_code} - {response.text}')
        exit(1)

def assign_ticket(base_url, email, token, ticket, account_id):
    url = f'{base_url}/rest/api/3/issue/{ticket}/assignee'
    auth = (email, token)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = json.dumps({'accountId': account_id})

    response = requests.put(url, headers=headers, auth=auth, data=data)

    if response.status_code == 204:
        print('Issue successfully assigned.')
    else:
        print(f'Failed to assign issue: {response.status_code} - {response.text}')
        exit(1)

if __name__ == '__main__':
    base_url = os.getenv('JIRA_BASE_URL')
    email = os.getenv('JIRA_USER_EMAIL')
    token = os.getenv('JIRA_API_TOKEN')
    ticket = os.getenv('JIRA_TICKET')
    assignee = os.getenv('JIRA_ASSIGNEE')

    account_id = get_account_id(base_url, email, token, assignee)
    assign_ticket(base_url, email, token, ticket, account_id)