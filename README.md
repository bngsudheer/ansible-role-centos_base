Role Name
=========

After the CentOS operating system is installed, perform some basic software installation and tweak a few things.

    - Updates packages
    - Installs a few packages such as 'Development Tools', mercurial, git, gcc, firewalld
    - Install and configure fail2ban and protect against ssh brute force attacks
    - Secure SSH config file
    - Install SELinux packages

Requirements
------------

Not much.

Role Variables
--------------

    - centos_base_secure_sshd: yes
    - centos_base_basic_vim_tweaks: yes
    - centos_base_htop_configuration: yes
    - centos_base_fail2ban_configuration: yes
    - centos_base_install_selinux_packages: yes

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
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
