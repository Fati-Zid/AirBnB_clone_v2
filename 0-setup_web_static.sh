#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing Nginx configuration
echo "<html><head><title>Test Page</title></head><body>Hello, this is a test page!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static {\n    alias /data/web_static/current/;\n}"
if grep -q "location /hbnb_static" "$nginx_config"; then
    sudo sed -i "/location \/hbnb_static/,$ d" "$nginx_config"
fi
sudo sed -i "/server_name _;/a $nginx_alias" "$nginx_config"

# Restart Nginx
sudo service nginx restart

exit 0
