#!/usr/bin/env bash
# Puppet manifest to configure Nginx with a custom HTTP header
class custom_http_header {
    # Install Nginx
    package { 'nginx':
        ensure => installed,
    }

    # Ensure Nginx is running
    service { 'nginx':
        ensure     => running,
        enable     => true,
        require    => Package['nginx'],
    }

    # Configure Nginx to add the X-Served-By header
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        add_header X-Served-By \$hostname;
        try_files \$uri \$uri/ =404;
    }
}",
        require => Package['nginx'],
        notify  => Service['nginx'],
    }
}

# Apply the class
include custom_http_header

