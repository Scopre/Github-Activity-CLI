import sys
import json
import urllib.request

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # Open URL and read response
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        if not data:
            print(f"No recent activity found for user: {username}")
            return
        
        print(f"Recent GitHub Activity for {username}:\n")

        for event in data[:5]:  # Display only the last 5 activities
            event_type = event["type"]
            repo_name = event["repo"]["name"]

            if event_type == "PushEvent":
                print(f"- Pushed code to {repo_name}")
            elif event_type == "IssuesEvent":
                print(f"- Opened an issue in {repo_name}")
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
            elif event_type == "ForkEvent":
                print(f"- Forked {repo_name}")
            elif event_type == "CreateEvent":
                print(f"- Created a new repository: {repo_name}")
            else:
                print(f"- {event_type} in {repo_name}")

    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}. Possible invalid username or API limit exceeded.")
    except urllib.error.URLError:
        print("Network error. Please check your connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <github_username>")
    else:
        username = sys.argv[1]
        fetch_github_activity(username)
