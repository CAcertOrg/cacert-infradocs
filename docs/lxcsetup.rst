=====================================================
Setup of a new CAcert LXC container with Puppet agent
=====================================================

Preparation
===========

Network considerations
----------------------

- Decide on a hostname for the container. The hostname should be short and
  correspond to the functionality provided by the container.
- Define an IPv4 address from the :ip:v4range:`213.154.225.224/27` subnet if
  the container should be reachable from the outside via IPv4. If the services
  provide HTTP or HTTPS services you will not need a dedicated IP address
  because virtual hosting and SNI can be used via :doc:`systems/proxyin`
- Define an IPv6 address in the :ip:v6range:`2001:7b8:616:162:2::/80` subnet.
  There is no reason not to use IPv6 for new services.
- Define an IPv4 address in the :ip:v4range:`172.16.2.0/24` subnet if the
  container should be reachable from other CAcert machines than
  :doc:`systems/infra02` or other :doc:`systems`.
- Define an IPv4 address in the :ip:v4range:`10.0.0.0/24` subnet. Containers
  that are only used by other containers do not need any other IP addresses
  than this one.

.. note::

   Please use the same last octet for all IP addresses of a container if
   possible

Storage considerations
----------------------

- Define the size of the LVM volume for the root filesystem. Be conservative,
  volume size can be increased on demand.

OS considerations
-----------------

- Define the OS userland version for the container. Use the latest Debian
  stable release if there are no good reasons not to.

Setup
=====

- Define machine parameters for in lxc-setup.ini
- Run :command:`lxc-setup` (uses lxc-create/debootstrap and makes sure that
  systemd-sysv is not setup in the containers)
- Define firewall rules in a separate file in :file:`/etc/ferm/ferm.d/` on
  :doc:`systems/infra02`.

Setup puppet-agent
------------------

.. todo:: describe puppet setup

- Define puppet configuration for the new container in Hiera.

Post-Setup task
===============

- Document the new container in a file of the :file:`docs/systems` directory of
  the `Infrastructure documentation
  <https://git.cacert.org/gitweb/?p=cacert-infradocs.git;a=tree;f=docs/systems>`_.
