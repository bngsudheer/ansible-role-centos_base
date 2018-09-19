Role Description
=========
Name: *bngsudheer.centos_base*

A role to install some common packages and tweak a few things.

By default, the role does not change the state of the target server. You have to
enable the boolean variables to change the default behaviour of this role.

After the CentOS operating system is installed, perform some basic software
installation and tweak a few things.

  - Install a few packages such as *Development Tools*, *mercurial*, *git*, *firewalld*
  - Install and configure *fail2ban* and protect against SSH brute force attacks
  - Secure SSH daemon configuration file to allow only key based login
  - Install SELinux packages

Requirements
------------

None.

Role Variables
--------------
The following role variables are available:

| Variable | Default Value | Description | Required? |
|----------|---------------|-----------|-------------|
| centos_base_enable_epel | false | Enable EPEL Repository | No |
| centos_base_secure_sshd |  false | Secure ssd configuration | No  |
| centos_base_basic_packages | false | Basic packages | No |
| centos_base_basic_vim_tweaks | false | Install Basic VIM tweaks | No |
| centos_base_htop_configuration | false | Basic htoprc configuration | No |
| centos_base_fail2ban_configuration | false |Basic fail2ban configuration |  No |
| centos_base_selinux_packages |  true | Install SELinux packages | No |
| centos_base_firewalld_services| [] | List of services to enable in firewalld | No |
| centos_base_utility_packages | false | Install utility packages such as screen, htop, wget | No |
| centos_base_debug_packages | false | Install debugging packages | No |
| centos_base_lockprg | false | Export LOCKPRG in .bashrc | No
| centos_base_security_packages | false | Installs firewalld | No |
| centos_base_firewalld | true | Whether to install and enable firewalld | No |

Dependencies
------------

None.

Example Playbook
----------------

```yml
    - hosts: servers
      remote_user: root
      vars:
        - centos_base_enable_epel: true
        - centos_base_basic_packages: true
        - centos_base_secure_sshd: true
        - centos_base_basic_vim_tweaks: true
        - centos_base_htop_configuration: true
        - centos_base_fail2ban_configuration: true
        - centos_base_selinux_packages: true
        - centos_base_firewalld_services: ['http', 'https']
      roles:
         - bngsudheer.centos_base
```
License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana.
* [Twitter](https://twitter.com/bngsudheer)
* [GitHub](https://github.com/bngsudheer)
* [Work](https://www.gavika.com/)
