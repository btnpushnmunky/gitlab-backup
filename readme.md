A simple utility to clone all of your Gitlab repositories so you have a backup.

Start with `pipenv install`.

You'll need to add a `.config` file with the following structure in the same directory as `glbackup.py`:
```
[global]
default = default
ssl_verify = true
timeout = 50

[default]
url = https://gitlab.com
private_token = PrivateTokenHere
api_version = 4
```

The script will create a `repos` directory in the same location as the `glbackup.py` file. All of your Gitlab repositories will be cloned into `repos`.

It's worth noting that there is currently no handling for updating already cloned repos.