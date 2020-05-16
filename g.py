import git

repo = git.Repo('deploying_pythonanywhere')

# List all branches
for branch in repo.branches:
    print(branch)

# Create a new branch
repo.git.branch('my_new_branch')

# List all branches
for branch in repo.branches:
    print(branch)


