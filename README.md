Role Description
=========
Name: *bngsudheer.centos_base*

After the CentOS operating system is installed, perform some basic software installation and tweak a few things.

  - Update packages
  - Install a few packages such as 'Development Tools', mercurial, git, firewalld
  - Install and configure fail2ban and protect against SSH brute force attacks
  - Secure SSH config file to allow only key based login
  - Install SELinux packages

Requirements
------------

None.

Role Variables
--------------
The following role variables are available:

|Variable | Default Value | Required? |
|-------------------------------------|
| centos_base_secure_sshd |  no | No  | 
| centos_base_basic_vim_tweaks | no | No |
| centos_base_htop_configuration|  no | No |
| centos_base_fail2ban_configuration | no | No |
| centos_base_install_selinux_packages |  yes | No |

It is recommended to set them all to _yes_.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      remote_user: root
      vars:
        - centos_base_secure_sshd: yes
        - centos_base_basic_vim_tweaks: yes
        - centos_base_htop_configuration: yes
        - centos_base_fail2ban_configuration: yes
        - centos_base_install_selinux_packages: yes
      roles:
         - bngsudheer.centos_base

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana.
* [Twitter](https://twitter.com/bngsudheer)
* [GitHub](https://github.com/bngsudheer)
* [Work](https://www.gavika.com/)
