=====================================================
Setup of a new CAcert LXC container with Puppet agent
=====================================================

.. todo::

   Update the LXC setup documentation. lxc-setup might not work with LXC 3.0
   that is used on :doc:`systems/infra02` since 2019-07-13.

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

- define puppet configuration for the new container in Hiera / sitemodules in
  the :cacertgit:`cacert-puppet` on :doc:`systems/git`
- see `Puppet agent installation`_ for agent setup (install the agent from
  official Puppet repositories)
- make sure that DNS resolution is performed by :doc:`systems/infra02`. The
  :file:`/etc/resolv.conf` should contain the following lines:

  .. code-block:: text

     search infra.cacert.org intra.cacert.org
     nameserver 10.0.0.1

- set the certname in :file:`/etc/puppetlabs/puppet/puppet.conf` to match
  the name of the file in :file:`hieradata/nodes/` for the system:

  .. code-block:: ini

     [main]
     certname = <system>

- run:

  .. code-block:: sh

     root@system:  puppet agent --test --noop

  to create a new certificate for the system and send a signing request to the
  :doc:`puppet master <systems/puppet>`
- sign the system certificate on the :doc:`puppet master <systems/puppet>`
  using:

  .. code-block:: sh

     root@puppet:  puppet cert sign <system>

- run:

  .. code-block:: sh

     root@system:  puppet agent --test --noop

  on the system to see whether the catalog for the machine compiles and what it
  would change
- apply the catalog with:

  .. code-block:: sh

     root@system:  puppet agent --test

- start the puppet agent using:

  .. code-block:: sh

     root@system:  /etc/init.d/puppet start

.. _Puppet agent installation: https://puppet.com/docs/puppet/5.4/install_linux.html

Post-Setup task
===============

- Document the new container in a file of the :file:`docs/systems` directory of
  the :cacertgit:`Infrastructure documentation repository <cacert-infradocs>`
- Setup machine-admin alias on :doc:`systems/email`.
