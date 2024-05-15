# web stack debugging task: Change the OS configuration

exec { 'holberton hard limit':
    command => '/bin/sed -i "s/5/4096/g" /etc/security/limits.conf',
}

exec { 'holberton soft limit':
    command => '/bin/sed -i "s/4/4096/g" /etc/security/limits.conf',
}
