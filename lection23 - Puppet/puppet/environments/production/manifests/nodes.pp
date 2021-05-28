node "node1" {
    file { "/test1" :
        ensure => absent
    }

    file { "/test3" :
        ensure => file
    }

    class { "nginx":
        ensure => 'running',
        port => '8082'
    }
    class { "jenkins_slave":
        node => "node1",
        secret => "a18f6aa9c64f9ad09abf5de94c6a004a08e76ae2f430ad644e0276a9676e2013"
    }
}

node "node2" {
    file { "/test2" :
        ensure => absent
    }

    file { "/test4" :
        ensure => file
    }

    class { "nginx":
        ensure => 'running',
        port => '8083'
    }

    class { "jenkins_slave":
        node => "node2",
        secret => "6fef665eec3eebda9de619b4a69370bdb638f013736af100b7217c09f61d5fe1"
    }
}
