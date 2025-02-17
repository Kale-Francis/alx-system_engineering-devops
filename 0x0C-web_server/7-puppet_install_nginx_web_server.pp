#!/usr/bin/env bash
# Install and configure Nginx with Puppet

class nginx_setup {
    # Ensure Nginx is installed
    package { 'nginx':
        ensure => installed,
    }

    # Ensure Nginx service is running and enabled
    service { 'nginx':
        ensure => running,
        enable => true,
        require => Package['nginx'],
    }

    # Configure Nginx to listen on port 80
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # 301 Redirection for /redirect_me
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
",
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    # Create a test HTML file
    file { '/var/www/html/index.html':
        ensure  => file,
        content => 'Hello World!',
        require => Package['nginx'],
    }
}

# Apply the class
include nginx_setup
