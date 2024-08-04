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
uses: your-github-username/jira-assign-action@v1
with:
  jira-base-url: ${{ secrets.JIRA_BASE_URL }}
  jira-user-email: ${{ secrets.JIRA_USER_EMAIL }}
  jira-api-token: ${{ secrets.JIRA_API_TOKEN }}
  jira-ticket: PROJ-123
  jira-assignee: johndoe
