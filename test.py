import os

def delete_git_folders(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            git_dir = os.path.join(root, '.git')
            print(f"Deleting {git_dir}")
            # Uncomment the line below to actually delete the .git folder
            # shutil.rmtree(git_dir)

root_directory = r"C:\tmp\projects"

delete_git_folders(root_directory)
