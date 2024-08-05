# Jira Assign Action

This action assigns a Jira ticket to a specified user.

## Inputs

* `jira-base-url`: The base URL of your Jira instance
* `jira-user-email`: The email of the Jira user making the API call
* `jira-api-token`: The API token for the Jira user
* `jira-ticket`: The Jira ticket key to be assigned
* `jira-assignee`: The username of the Jira user to assign the ticket to

## Example usage

```yaml
- name: Assign Jira ticket using composite action
  uses: Adesam97/jira-assignee-action@v2
  with:
    jira_base_url: ${{ secrets.JIRA_BASE_URL }}
    jira_user_email: ${{ secrets.JIRA_USER_EMAIL }}
    jira_api_token: ${{ secrets.JIRA_API_TOKEN }}
    jira_assignee: ${{ secrets.JIRA_ASSIGNEE }}
    jira_issue_key: 'RAV-44' # you can use a dynamic approach if you like
