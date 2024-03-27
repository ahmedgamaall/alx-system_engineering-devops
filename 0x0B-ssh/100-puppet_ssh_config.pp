#!/usr/bin/env bash
file { '/etc/ssh/ssh_config':
        ensure => present,
}
file_line { 'Turn off password auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'passwordAuthentication no',
  match   => '^#passwordAuthentication',
}
