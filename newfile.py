import os
import subprocess

# GitHub repository details
REPO_URL = "https://github.com/binahmad362/Test.git"  # Replace with your repository URL
BRANCH = "main"  # Replace with your branch name if different
FILE_NAME = "test.txt"
CONTENT = "hello"

# Hardcoded GitHub Personal Access Token (PAT)
GITHUB_PAT = "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"

# Git user details
GIT_USER_NAME = "binahmad362"  # Replace with your GitHub username
GIT_USER_EMAIL = "tajuttech360@gmail.com"  # Replace with your GitHub email

# Write the file
def write_file():
    print(f"Creating file '{FILE_NAME}'...")
    try:
        # Create and write to the file
        with open(FILE_NAME, "w") as file:
            file.write(CONTENT)
        print(f"File '{FILE_NAME}' created with content: '{CONTENT}'")
    except Exception as e:
        print(f"Error writing file: {e}")
        exit(1)

# Initialize Git repository and push to GitHub
def push_to_github():
    print("Pushing changes to GitHub...")
    try:
        # Initialize a new Git repository
        subprocess.run(["git", "init"], check=True)

        # Set Git user name and email
        subprocess.run(["git", "config", "user.name", GIT_USER_NAME], check=True)
        subprocess.run(["git", "config", "user.email", GIT_USER_EMAIL], check=True)

        # Add all files to the staging area
        subprocess.run(["git", "add", "--all"], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", f"Added {FILE_NAME} with content '{CONTENT}'"], check=True)

        # Add the remote repository
        if not GITHUB_PAT:
            print("Error: GitHub PAT not found. Set it in your environment.")
            exit(1)
        repo_url_with_token = REPO_URL.replace("https://", f"https://{GITHUB_PAT}@")
        subprocess.run(["git", "remote", "add", "origin", repo_url_with_token], check=True)

        # Push to GitHub
        subprocess.run(["git", "push", "-u", "origin", BRANCH], check=True)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes: {e}")
        exit(1)

# Main function
def main():
    # Ensure we're in the correct directory
    os.chdir("/storage/emulated/0/Git/")  # Adjust to your directory
    write_file()
    push_to_github()

if __name__ == "__main__":
    main()
