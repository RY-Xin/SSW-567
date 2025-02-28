## Project Description
This project is a Python program that interacts with GitHub's REST API to retrieve a list of repositories for a specified user and the number of commits in each repository. The program demonstrates how to make HTTP requests, parse JSON responses, and handle API data effectively.
## Functionality
- Takes a GitHub user ID as input.
- Retrieves the list of repositories for the user.
- Fetches the number of commits for each repository.
- Outputs the repository names along with their commit counts.
## Code Structure
- `github_api.py`: The main program file containing the function to interact with the GitHub API.
- `test_github_api.py`: The unit test file to verify the functionality of the main program.
## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/RY-Xin/SSW-567.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SSW-567/GitHubApi567-hw4a
   ```
3. Install the required dependencies:
   ```bash
   pip install requests
   ```
4. Run the main program:
   ```bash
   python github_api.py
   ```
   Enter a GitHub user ID when prompted, and the program will output the repository names and their commit counts.
5. Run the unit tests:
   ```bash
   python -m unittest test_github_api.py
   ```
