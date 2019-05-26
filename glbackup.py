import gitlab
import git
import os


gl = gitlab.Gitlab.from_config("default", [".config"])

projects = gl.projects.list(owned=True, all=True)

p = gl.projects.get(projects[0].id)

g = git.Git()
os.chdir("exports")
g.clone(p.ssh_url_to_repo)
# g.pull()
# p.ssh_url_to_repo
# export = p.exports.create({})


# # Wait for the 'finished' status
# export.refresh()
# while export.export_status != 'finished':
#     time.sleep(1)
#     export.refresh()

# # Download the result
# with open(f'{projects[0].name}-export.tgz', 'wb') as f:
#     export.download(streamed=True, action=f.write)
# # for project in projects:
#     # p = gl.projects.get(project.id)
