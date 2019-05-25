import gitlab


gl = gitlab.Gitlab.from_config("default", [".config"])

projects = gl.projects.list(owned=True, all=True)

for project in projects:
    print(project.name)