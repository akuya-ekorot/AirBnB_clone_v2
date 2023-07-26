#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""


from fabric.api import local


def do_pack():
    """Function to compress files in an archive"""
    local("mkdir -p versions")
    file = local("tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        web_static")
    if file.succeeded:
        return file
    else:
        return None
