# web stack debugging task: amount of file

exec { 'fix-nginx':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

# web stack debugging task: restart nginx

exec { 'nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix-nginx'],
}
