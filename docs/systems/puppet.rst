.. index::
   single: Systems; Puppet

======
Puppet
======

Purpose
=======

This system acts as `Puppet`_ master for infrastructure systems.

.. _Puppet: https://docs.puppet.com/puppet/

Application Links
-----------------

This system has no publicly visible URLs.


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+---------------+---------------------+
| Application   | Administrator(s)    |
+===============+=====================+
| Puppet server | :ref:`people_jandd` |
+---------------+---------------------+
| PuppetDB      | :ref:`people_jandd` |
+---------------+---------------------+

Contact
-------

* puppet-admin@cacert.org

Additional People
-----------------

* None

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: None
:IP Intranet: None
:IP Internal: :ip:v4:`10.0.0.200`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::200`
:MAC address: :mac:`00:ff:f9:32:9d:2a` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Puppet

Monitoring
----------

:internal checks: :monitor:`puppet.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Puppet

+--------------------------+------+------------+
| Name                     | Type | Content    |
+==========================+======+============+
| puppet.infra.cacert.org. | IN A | 10.0.0.200 |
+--------------------------+------+------------+

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.3

* Debian GNU/Linux 10.3

Services
========

Listening services
------------------

+----------+----------+----------+------------------------------------------+
| Port     | Service  | Origin   | Purpose                                  |
+==========+==========+==========+==========================================+
| 22/tcp   | ssh      | ANY      | admin console access                     |
+----------+----------+----------+------------------------------------------+
| 25/tcp   | smtp     | local    | mail delivery to local MTA               |
+----------+----------+----------+------------------------------------------+
| 5432/tcp | pgsql    | local    | PostgreSQL database for PuppetDB         |
+----------+----------+----------+------------------------------------------+
| 5665/tcp | icinga2  | monitor  | remote monitoring service                |
+----------+----------+----------+------------------------------------------+
| 8000/tcp | git-hook | internal | HTTP endpoint for git-pull-hook          |
+----------+----------+----------+------------------------------------------+
| 8080/tcp | puppetdb | local    | HTTP endpoint for local PuppetDB queries |
+----------+----------+----------+------------------------------------------+
| 8081/tcp | puppetdb | internal | HTTPS endpoint for PuppetDB              |
+----------+----------+----------+------------------------------------------+
| 8140/tcp | puppet   | internal | Puppet master                            |
+----------+----------+----------+------------------------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim
   single: git-pull-hook
   single: icinga2
   single: openssh
   single: postgresql
   single: puppet agent
   single: puppetdb
   single: puppetserver
   single: rsyslog

+----------------+--------------------------+----------------------------------------+
| Service        | Usage                    | Start mechanism                        |
+================+==========================+========================================+
| cron           | job scheduler            | systemd unit ``cron.service``          |
+----------------+--------------------------+----------------------------------------+
| dbus           | system message bus       | systemd unit ``dbus.service``          |
+----------------+--------------------------+----------------------------------------+
| Exim           | SMTP server for          | systemd unit ``exim4.service``         |
|                | local mail submission    |                                        |
+----------------+--------------------------+----------------------------------------+
| git-pull-hook  | Custom Python3 hook      | systemd unit ``git-pull-hook.service`` |
|                | to pull git changes      |                                        |
|                | from the cacert-puppet   |                                        |
|                | repository               |                                        |
+----------------+--------------------------+----------------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service``       |
+----------------+--------------------------+----------------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``           |
|                | remote administration    |                                        |
+----------------+--------------------------+----------------------------------------+
| PostgreSQL     | PostgreSQL database      | systemd unit ``postgresql.service``    |
|                | server for PuppetDB      |                                        |
+----------------+--------------------------+----------------------------------------+
| Puppet agent   | local Puppet agent       | systemd unit ``puppet.service``        |
+----------------+--------------------------+----------------------------------------+
| PuppetDB       | PuppetDB for querying    | systemd unit ``puppetdb.service``      |
|                | Puppet facts, nodes      |                                        |
|                | and resources            |                                        |
+----------------+--------------------------+----------------------------------------+
| Puppet server  | Puppet master for        | systemd unit ``puppetserver.service``  |
|                | infrastructure systems   |                                        |
+----------------+--------------------------+----------------------------------------+
| rsyslog        | syslog daemon            | init script                            |
|                |                          | :file:`/etc/init.d/syslog`             |
+----------------+--------------------------+----------------------------------------+

Databases
---------

+------------+----------+-------------------+
| RDBMS      | Name     | Used for          |
+============+==========+===================+
| PostgreSQL | puppetdb | PuppetDB database |
+------------+----------+-------------------+

Connected Systems
-----------------

* :doc:`blog`
* :doc:`bugs`
* :doc:`emailout`
* :doc:`ircserver`
* :doc:`issue`
* :doc:`jenkins`
* :doc:`monitor`
* :doc:`motion`
* :doc:`proxyin`
* :doc:`proxyout`
* :doc:`svn`
* :doc:`translations`
* :doc:`web`
* :doc:`webstatic`
* :doc:`wiki`
* :doc:`git` for triggering the git-pull-hook on newly pushed commits to the
  cacert-puppet repository

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`git` to fetch new commits from the cacert-puppet repository
* :doc:`proxyout` as HTTP proxy for APT
* forgeapi.puppet.com for Puppet forge access
* rubygems.org for Puppet specific Ruby gems

Security
========

.. sshkeys::
   :RSA:     SHA256:PPEZkD7ezGStENYmE9/RftHqJyy6cC9IN6zw63OvJTM MD5:54:57:b0:09:46:ba:56:95:5e:e3:35:df:28:27:ed:c5
   :ECDSA:   SHA256:3U1CVC9YAKmF9W5SDLibwP1A9MVSb5ltVN7nYNOE15o MD5:29:06:f1:71:8d:65:3e:39:7c:49:69:16:8d:99:97:15
   :ED25519: SHA256:AkqMLLEtMbAEuxniRRDgd7TItD+pb9hsbpn5Ab81+IM MD5:53:dc:e7:4d:25:89:a8:d5:5a:24:0b:06:3f:41:cd:4d

Non-distribution packages and modifications
-------------------------------------------

The Puppet server, Puppet agent and PuppetDB packages and a few dependencies
are installed from the official Puppet APT repository because the versions
in Debian are too old to use modern Puppet features.

Some rubygems are installed via the puppet specific ruby gem binary to support
advanced Puppet functionality like hiera-eyaml.

All puppet related code is installed in the Puppet specific /opt/puppetlabs
tree.

Risk assessments on critical packages
-------------------------------------

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

Puppet comes with its own inbuilt special purpose CA that is used to sign the
Puppet server and Puppet DB certificates as well as the certificates of all
trusted Puppet agents.

The CA data is stored in :file:`/etc/puppetlabs/puppet/ssl` and managed by
puppet itself.

Eyaml private key
-----------------

All sensitive data like passwords in Hiera data is encrypted using the public
key in :file:`keys/public_key.pkcs7.pem` in the `CAcert puppet Git repository
<ssh://git.cacert.org/var/cache/git/cacert-puppet.git>`_. The corresponding
private key is stored in
:file:`/etc/puppetlabs/code/environments/production/keys/private_key.pkcs7.pem`.

hiera configuration
-------------------

Puppet uses Hiera for hierarchical information retrieval. The global hiera
configuration is stored in :file:`/etc/puppetlabs/puppet/hiera.yaml` and
defines the hierarchy lookup as well as the eyaml key locations.

puppet configuration
--------------------

All puppet configuration is stored in :file:`/etc/puppetlabs/`. The CAcert
specific puppet code is taken from the `CAcert puppet Git repository
<ssh://git.cacert.org/var/cache/git/cacert-puppet.git>`_ and cloned to
:file:`/etc/puppetlabs/code/environments/production/` directory. Required
Puppet modules are installed by :program:`/opt/puppetlabs/puppet/bin/r10k`.

The puppet code should follow best practices like the Roles and profiles
pattern (see references below) and code/data separation via Hiera.

Updates to the cacert-puppet repository trigger a web hook listening on tcp
port 8000 that automatically updates the production environment directory.

Tasks
=====

.. todo:: add a section to describe how to add a system for puppet management

Changes
=======

Planned
-------

* migrate as many systems as possible to use Puppet for a more
  reproducible/auditable system setup

System Future
-------------

* Improve setup, use more widely

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* https://docs.puppet.com/puppet/
* https://puppet.com/blog/encrypt-your-data-using-hiera-eyaml
* https://docs.puppet.com/pe/2016.5/r_n_p_full_example.html
