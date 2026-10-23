# GitHub Profile Viewer

A simple Python CLI tool that fetches and displays a GitHub user's profile info using the GitHub REST API.

## Features

- Profile details: name, email, location, bio, account creation date
- Lists followers and following
- Lists starred repositories
- Lists public repositories

## Requirements

- Python 3.8+
- A GitHub personal access token

## Setup

1. Clone the repo:

```bash
git clone https://github.com/not-rajharsh/github-profile-inspector
.git
cd github-profile-inspector

```

2. Install dependencies:

```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root:

```
KEY=your_github_token_here
```

4. Make sure `.env` is in your `.gitignore`.

## Usage

```bash
python main.py
```

Enter a GitHub username when prompted.

## Example Output

```
=====================================================
Name: Octocat
Email: None
Location: San Francisco
Bio: ...
Account Created: 2011-01-25T18:44:36Z
=====================================================
Followers:
...
```

## Known Limitations

- Only the first 30 items of each list are shown (GitHub's default page size).
- No error handling for invalid usernames or rate limits.

## Roadmap

- [ ] Pagination
- [ ] Error handling
- [ ] Refactor into classes

## License

MIT
