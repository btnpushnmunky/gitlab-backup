import gitlab
import git
import os


g = git.Git()

gl = gitlab.Gitlab.from_config("default", [".config"])

my_projects = gl.projects.list(owned=True, all=True)

os.chdir("exports")

for project in my_projects:
    repo = gl.projects.get(project.id)
    print(repo.name)
    g.clone(repo.ssh_url_to_repo)
