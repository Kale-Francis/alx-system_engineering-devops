# THis manifest installs flask package 'requests' via  pip3 at version 2.1.0

package {'Flask':
  ensure => '2.1.0',
  provider=> 'pip3',
  install_options => ['--break-system-packages'],
}
