# This Puppet manifest installs missing PHP modules and restarts Apache
exec { 'install-php-mysql':
  command => '/usr/bin/sudo /usr/bin/apt-get update && /usr/bin/sudo /usr/bin/apt-get install -y php-mysql',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/dpkg -l | grep php-mysql',
  user    => 'root',
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Exec['install-php-mysql'],
}
