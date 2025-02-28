# SSW-567
1. What challenges did you encounter with this assignment, if any?
One of the main challenges I faced was correctly identifying right triangles. Specifically, when the input sides met the conditions for a right triangle, my code didn't return the correct result. Initially, I didn't check for right triangles first; I checked last, which caused the incorrect result. After reviewing the logic and adjusting the order of checks, I was able to resolve the issue.
2. What did you think about the requirements specification for this assignment?
Overall, the assignment requirements were very clear, covering a variety of triangle classification conditions, including right triangles, equilateral triangles, isosceles triangles, and scalene triangles. Each condition was clearly defined, which guided me in implementing the program systematically and ensuring that the classifications and validations were correct.
3. What challenges did you encounter with the tools?
I encountered some challenges with GitHub because I was unfamiliar with how to upload code and resolve conflicts. Initially, I had difficulty understanding how to push code to the remote repository and how to manage branch conflicts. After researching and debugging, I was able to resolve these issues.
4. Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?
I made sure my test cases covered all the required triangle types, including equilateral, isosceles, scalene, and right triangles. I also included test cases for invalid triangle configurations, such as negative or zero side lengths, to ensure the program could handle invalid inputs properly. All the test cases passed successfully, confirming that the program was thoroughly tested.
https://github.com/RY-Xin/SSW-567.git

GitHubAPI
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
   # GitHub API Assignment

![Build Status](https://circleci.com/gh/RY-Xin/SSW-567/tree/main.svg?style=shield)

## Features
- Input GitHub user ID to get the number of commits for all repositories.
- Implemented using GitHub API.

## How to Run
```bash
python3 github_api.py

