import os
import subprocess

def delete_git_folders(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            git_dir = os.path.join(root, '.git')
            print(f"Deleting {git_dir}")
            subprocess.run(["rd", "/s", "/q", git_dir], shell=True)

root_directory = r"C:\tmp\projects"

delete_git_folders(root_directory)
