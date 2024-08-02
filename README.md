# GitHub Repository Content Fetcher

This script fetches the contents of all files in a given GitHub repository URL and organizes them into a structured format.
If you find this script useful, please consider giving it a star ⭐. Your support is greatly appreciated!

## Requirements

- Python 3.x
- `requests` library

## How to Use

1. **Install the `requests` library**:
    ```bash
    pip install requests
    ```

2. **Run the script**:
    ```bash
    python fetcher.py
    ```

3. **Enter the required inputs**:
    - GitHub repository URL (e.g., `https://github.com/user/repo`)
    - Personal access token (optional, for higher rate limits, needed for large repositories, leave empty if you don't have one)

## API Rate Limits

Accessing the contents of a public GitHub repository using the GitHub REST API is free. However, GitHub imposes rate limits on API requests:

- **Unauthenticated requests**: 60 requests per hour.
- **Authenticated requests**: 5,000 requests per hour.

If you exceed these limits, you will receive a rate limit exceeded error.

### Authentication

To make authenticated requests and benefit from higher rate limits, use a personal access token:

1. **Generate a personal access token**:
    - Go to [GitHub Settings](https://github.com/settings/tokens).
    - Click on "Generate new token".
    - Select the scopes you need and generate the token.

## Output

The script will print:
- **File Structure**: A nested dictionary representing the directory structure.
- **File Contents**: A dictionary with file paths as keys and file contents as values.

## Notes

- Ensure the provided GitHub repository URL is valid.
- The script handles both files and directories within the repository.

## Difference

**Output using GitHub API**:
 ```
 [{'name': 'LICENSE', 'path': 'LICENSE', 'sha': 'd0fb36f09eb1ed25a5cbbb873d9523e33c9dc49f', 'size': 1069, 'url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/LICENSE?ref=main', 'html_url': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/LICENSE', 'git_url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/d0fb36f09eb1ed25a5cbbb873d9523e33c9dc49f', 'download_url': 'https://raw.githubusercontent.com/basith-ahmed/github-repo-fetcher/main/LICENSE', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/LICENSE?ref=main', 'git': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/d0fb36f09eb1ed25a5cbbb873d9523e33c9dc49f', 'html': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/LICENSE'}},
{'name': 'README.md', 'path': 'README.md', 'sha': '600d67d6e4c2fd993e1f045b65ec2f219b8f2f4c', 'size': 1734, 'url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/README.md?ref=main', 'html_url': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/README.md', 'git_url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/600d67d6e4c2fd993e1f045b65ec2f219b8f2f4c', 'download_url': 'https://raw.githubusercontent.com/basith-ahmed/github-repo-fetcher/main/README.md', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/README.md?ref=main', 'git': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/600d67d6e4c2fd993e1f045b65ec2f219b8f2f4c', 'html': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/README.md'}},
{'name': 'fetcher.py', 'path': 'fetcher.py', 'sha': 'ee3614273fa23e9f8860604108d8cac83e5f9921', 'size': 2601, 'url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/fetcher.py?ref=main', 'html_url': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/fetcher.py', 'git_url': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/ee3614273fa23e9f8860604108d8cac83e5f9921', 'download_url': 'https://raw.githubusercontent.com/basith-ahmed/github-repo-fetcher/main/fetcher.py', 'type': 'file', '_links': {'self': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/contents/fetcher.py?ref=main', 'git': 'https://api.github.com/repos/basith-ahmed/github-repo-fetcher/git/blobs/ee3614273fa23e9f8860604108d8cac83e5f9921', 'html': 'https://github.com/basith-ahmed/github-repo-fetcher/blob/main/fetcher.py'}}]
 ```
**Output using fetcher.py**:
```
File Structure:
{'LICENSE': None, 'README.md': None, 'fetcher.py': None}

File Contents:
Path: LICENSE
Content:
MIT License

Copyright (c) 2024 Basith Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Path: README.md
Content:
# GitHub Repository Content Fetcher

This script fetches the contents of all files in a given GitHub repository URL and organizes them into a structured format.

## Requirements

- Python 3.x
- `requests` library

## How to Use

1. **Install the `requests` library**:
    ```bash
    pip install requests
    ```

2. **Run the script**:
    ```bash
    python fetcher.py
    ```

3. **Enter the required inputs**:
    - GitHub repository URL (e.g., `https://github.com/user/repo`)
    - Personal access token (optional, for higher rate limits, needed for large repositories, leave empty if you don't have one)

## API Rate Limits

Accessing the contents of a public GitHub repository using the GitHub REST API is free. However, GitHub imposes rate limits on API requests:

- **Unauthenticated requests**: 60 requests per hour.
- **Authenticated requests**: 5,000 requests per hour.

If you exceed these limits, you will receive a rate limit exceeded error.

### Authentication

To make authenticated requests and benefit from higher rate limits, use a personal access token:

1. **Generate a personal access token**:
    - Go to [GitHub Settings](https://github.com/settings/tokens).
    - Click on "Generate new token".
    - Select the scopes you need and generate the token.

## Output

The script will print:
- **File Structure**: A nested dictionary representing the directory structure.
- **File Contents**: A dictionary with file paths as keys and file contents as values.

## Notes

- Ensure the provided GitHub repository URL is valid.
- The script handles both files and directories within the repository.

If you find this script useful, please consider giving it a star ⭐ on GitHub. Your support is greatly appreciated!


Path: fetcher.py
Content:
#Fetch contents of a GitHub repository directory
def get_github_repo_contents(owner, repo, path='', token=''):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

#Recursively fetch all the files in the repository
def fetch_all_files(owner, repo, path='', token=''):
    all_files = []
    contents = get_github_repo_contents(owner, repo, path, token)
    for item in contents:
        if item['type'] == 'file':
            file_content = requests.get(item['download_url']).text
            all_files.append({'path': item['path'], 'content': file_content})
        elif item['type'] == 'dir':
            all_files.extend(fetch_all_files(owner, repo, item['path'], token))
    return all_files

#Extract owner and repo name from the URL
def extract_owner_repo(url):
    pattern = r'https://github.com/([^/]+)/([^/]+)'
    match = re.match(pattern, url)
    if match:
        return match.group(1), match.group(2)
    else:
        print("Invalid URL format.")
        return None, None

#Build file structure from file paths
def build_file_structure(files):
    file_structure = {}
    for file in files:
        parts = file['path'].split('/')
        current_level = file_structure
        for part in parts[:-1]:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
        current_level[parts[-1]] = None
    return file_structure

#Get user input
repo_url = input("Enter the GitHub repository URL: ")
token = input("Enter your personal access token (or leave blank for unauthenticated requests): ")

owner, repo = extract_owner_repo(repo_url)
if owner and repo:
    all_files_contents = fetch_all_files(owner, repo, '', token)

    #Build file structure
    file_structure = build_file_structure(all_files_contents)

    #Dictionary of file structure and file contents
    files_dict = {
        'file_structure': file_structure,
        'file_contents': {file['path']: file['content'] for file in all_files_contents}
    }

    print("\nFile Structure:")
    print(files_dict['file_structure'])

    print("\nFile Contents:")
    for path, content in files_dict['file_contents'].items():
        print(f"Path: {path}\nContent:\n{content}\n")

else:
    print("Could not process the repository URL.")
```
