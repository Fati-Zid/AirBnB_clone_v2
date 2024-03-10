#!/usr/bin/python3
""" Script to compress site files """

from fabric.api import local
from datetime import datetime

def do_pack():
    """ Function to compress site files """
    
    try:
        # Create versions folder if it doesn't exist
        local("mkdir -p versions")

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create archive file name
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress web_static folder into the archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the archive path if the archive has been correctly generated
        return "versions/{}".format(archive_name)
    except Exception as e:
        # Print error message if any exception occurs
        print("Error:", e)
        return None
