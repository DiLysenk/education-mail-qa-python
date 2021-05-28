class jenkins_slave($node, $secret) {

    pkg { "wget": } ->

    exec { "get agent.jar":
        command => "/usr/bin/wget -q http://jenkins:8080/jnlpJars/agent.jar -O /opt/agent.jar",
        creates => "/opt/agent.jar",
    } ->

    file { "/data":
        ensure => directory,
        mode => '0777'
    } ->

    service { "jenkins_slave":
      ensure => "running",
      start => "/usr/bin/java -jar /opt/agent.jar -jnlpUrl http://jenkins:8080/computer/$node/slave-agent.jnlp -secret $secret -workDir \"/data\" &",
    } ->

    pkg { "python3": }
}
