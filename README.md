# Github-Activity-CLI
In this project, we build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. 
# GitHub Activity CLI

## Overview
This project is a simple command-line interface (CLI) tool that fetches and displays the recent activity of a GitHub user. It is designed to help you practice working with APIs, handling JSON data, and building a CLI application from scratch.

## Features
- Run the application from the command line.
- Accept a GitHub username as an argument.
- Fetch the user’s recent activity from the GitHub API.
- Display the fetched activity in the terminal.
- Handle errors gracefully, such as invalid usernames or API failures.
- Built without using any external libraries or frameworks.

## Requirements
- A programming language of your choice (Python, JavaScript, etc.).
- Internet connection to interact with the GitHub API.

## Usage
Run the CLI tool with the GitHub username as an argument:
```sh
github-activity <username>
```

### Example:
```sh
github-activity kamranahmedse
```

### Expected Output:
```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## API Endpoint
The CLI fetches activity data using the GitHub API:
```
https://api.github.com/users/<username>/events
```
Example:
```
https://api.github.com/users/kamranahmedse/events
```

## Error Handling
- Handles invalid GitHub usernames.
- Handles API request failures.
- Displays appropriate error messages.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is open-source and available under the MIT License.
https://roadmap.sh/projects/github-user-activity

---

Happy coding! 🚀

