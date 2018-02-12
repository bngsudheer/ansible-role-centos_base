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

| Variable | Default Value | Required? |
|----------|---------------|-----------|
| centos_base_secure_sshd |  false | No  |
| centos_base_basic_vim_tweaks | false | No |
| centos_base_htop_configuration|  false | No |
| centos_base_fail2ban_configuration | false | No |
| centos_base_install_selinux_packages |  true | No |
| centos_base_firewalld_services| [] | No |
| centos_base_install_packages | false | No|

It is recommended to set them all bolean variables to _yes_.

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
