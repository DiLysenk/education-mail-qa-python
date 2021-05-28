class nginx($ensure='stopped', $port='8080') {

    class { "nginx::repo": } ->

    class { "nginx::config":
        port => $port
    }

    pkg { "nginx":
      require => Class["nginx::config"]
    }

    service { "nginx":
      ensure => $ensure,
      start => '/usr/sbin/nginx -c /tmp/nginx.conf',
      stop  => '/usr/sbin/nginx -s stop',
      require => Package["nginx"],
      subscribe => File["/tmp/nginx.conf"]
    }

}
