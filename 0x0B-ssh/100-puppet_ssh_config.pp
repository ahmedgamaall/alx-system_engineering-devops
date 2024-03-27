r/bin/env bash
file { '/etc/ssh/ssh_config':
        ensure => present,
content => "
Include /etc/ssh/ssh_config.d/*.conf
Host *
    IdentityFile ~/.ssh/school
    passwordAuthentication no
",
  mode    => '0644',
}
