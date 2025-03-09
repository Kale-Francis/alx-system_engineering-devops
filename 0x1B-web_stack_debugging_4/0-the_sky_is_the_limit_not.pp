# This Puppet manifest configures Nginx for high-performance handling of concurrent requests

class nginx_optimization {

  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure => running,
    enable => true,
  }

  # Optimize Nginx configuration
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx/nginx.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Create an exec command to reload Nginx
  exec { 'reload-nginx':
    command     => '/etc/init.d/nginx reload',
    refreshonly => true,
    subscribe   => File['/etc/nginx/nginx.conf'],
  }
}

include nginx_optimization
