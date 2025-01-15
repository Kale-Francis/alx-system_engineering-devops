# This manifest creates a file at /tmp/school with specific attributes.

file { '/tmp/school':
  content =>'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
