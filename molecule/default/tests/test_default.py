import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_is_installed(host):
    package = host.package("epel-release")
    assert package.is_installed


def test_epel_packages(host):
    packages = ['screen', 'htop']
    for package_name in packages:
        package = host.package(package_name)
        assert package.is_installed


def test_firewalld_80_open(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
