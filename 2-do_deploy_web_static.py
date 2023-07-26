#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy """


from fabric.api import env, put, run
from os import path

# Enviroment variables
env.hosts = ['100.26.138.246', '52.91.135.137']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Function to deploy """
    if path.exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split('/')[-1]
        new_folder = ("/data/web_static/releases/" + file_name.split('.')[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, new_folder))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except Exception:
        return False
