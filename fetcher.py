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
