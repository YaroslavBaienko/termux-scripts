#!/bin/bash

# Change to the directory of your Git repository
cd /data/data/com.termux/files/home/storage/dcim/obsidian || { echo "Failed to navigate to the repository"; exit 1; }

# Start the SSH agent in the background
eval "$(ssh-agent -s)"

# Add the SSH private key, assuming it starts with 'id' and does not end with '.pub'
SSH_KEY=$(find ~/.ssh -type f -name "id*" ! -name "*.pub" -print -quit)
if [[ -n "$SSH_KEY" ]]; then
    ssh-add $SSH_KEY
else
    echo "No suitable SSH key found in ~/.ssh"
    exit 1
fi

# List added SSH keys to verify
ssh-add -l

# Test connection to GitHub (or the relevant Git server if using a private one)
ssh -T git@github.com

# Define the branch name (you can modify this if you're not using the main branch)
BRANCH="main"

# Switch to the target branch
git checkout $BRANCH

# Fetch the latest changes from the remote repository and rebase local changes on top
git pull origin $BRANCH --rebase

# Add all local changes to the staging area
git add .

# Check if there are any changes to commit
if ! git diff-index --quiet HEAD --; then
    # Commit the changes with a specific message
    git commit -m "Automatic sync by script"

    # Push local changes back to the remote repository
    git push origin $BRANCH
else
    echo "No changes to commit."
fi
