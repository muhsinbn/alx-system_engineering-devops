# Create file in /tmp

file { '/tmp/school' :
    path    => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    }