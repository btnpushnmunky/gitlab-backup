import gitlab
import git
from pathlib import Path
import os


g = git.Git()

gl = gitlab.Gitlab.from_config("default", [".config"])

my_projects = gl.projects.list(owned=True, all=True)

if Path("repos").exists():
    print("Moving to repos directory")
    os.chdir("repos")    
else:
    print("Making repos directory")
    Path("repos").mkdir()
    print("Moving to repos directory")
    os.chdir("repos")

for project in my_projects:
    repo = gl.projects.get(project.id)
    print(repo.name)
    g.clone(repo.ssh_url_to_repo)
