Role Description
=========
Name: *bngsudheer.centos_base*

After the CentOS operating system is installed, perform some basic software installation and tweak a few things.

  - Install a few packages such as 'Development Tools', *mercurial*, *git*, *firewalld*
  - Install and configure *fail2ban* and protect against SSH brute force attacks
  - Secure SSH config file to allow only key based login
  - Install SELinux packages

Requirements
------------

None.

Role Variables
--------------
The following role variables are available:

| Variable | Default Value | Description | Required? |
|----------|---------------|-----------|
| centos_base_secure_sshd |  false | Secure ssd configuration | No  |
| centos_base_basic_vim_tweaks | false | Install Basic VIM tweaks | No |
| centos_base_htop_configuration | false | Basic htoprc configuration | No |
| centos_base_fail2ban_configuration | false |Basic fail2ban configuration |  No |
| centos_base_install_selinux_packages |  true | Install SELinux packages | No |
| centos_base_firewalld_services| [] | List of services to enable in firewalld | No |
| centos_base_install_nagios_packages | false | Install Nagios and related packages | No |
| centos_base_utility_packages | false | Install utility packages | No |


Dependencies
------------

None.

Example Playbook
----------------

```yml
    - hosts: servers
      remote_user: root
      vars:
        - centos_base_secure_sshd: yes
        - centos_base_basic_vim_tweaks: yes
        - centos_base_htop_configuration: yes
        - centos_base_fail2ban_configuration: yes
        - centos_base_install_selinux_packages: yes
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
