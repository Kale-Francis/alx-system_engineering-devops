class user_limit {
  exec { 'change-os-configuration-for-holberton-user':
    command => "/bin/echo 'holberton soft nofile 65535' >> /etc/security/limits.conf &&
                /bin/echo 'holberton hard nofile 131072' >> /etc/security/limits.conf &&
                /bin/echo 'session required pam_limits.so' >> /etc/pam.d/common-session &&
                /bin/echo 'session required pam_limits.so' >> /etc/pam.d/common-session-noninteractive",
    path    => ['/bin', '/usr/bin'],
    onlyif  => "grep -qv 'holberton' /etc/security/limits.conf",
  }
}

include user_limit
