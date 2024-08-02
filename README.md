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
