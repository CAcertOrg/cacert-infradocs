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

DNS
---

.. index::
   single: DNS records; Puppet

.. todo:: setup DNS records (in infra.cacert.org zone)

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.7

* Debian GNU/Linux 8.7

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+-----------+-----------+------------------------------------------+
| Port     | Service   | Origin    | Purpose                                  |
+==========+===========+===========+==========================================+
| 22/tcp   | ssh       | ANY       | admin console access                     |
+----------+-----------+-----------+------------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA               |
+----------+-----------+-----------+------------------------------------------+
| 5432/tcp | pgsql     | local     | PostgreSQL database for PuppetDB         |
+----------+-----------+-----------+------------------------------------------+
| 8140/tcp | puppet    | internal  | Puppet master                            |
+----------+-----------+-----------+------------------------------------------+
| 8080/tcp | puppetdb  | local     | HTTP endpoint for local PuppetDB queries |
+----------+-----------+-----------+------------------------------------------+
| 8081/tcp | puppetdb  | internal  | HTTPS endpoint for PuppetDB              |
+----------+-----------+-----------+------------------------------------------+

Running services
----------------

.. index::
   single: Exim
   single: PostgreSQL
   single: Puppet agent
   single: Puppet server
   single: Puppetdb
   single: cron
   single: openssh
   single: rsyslogd

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for PuppetDB       |                                        |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Puppet server      | Puppet master for  | init script                            |
|                    | infrastructure     | :file:`/etc/init.d/puppetserver`       |
|                    | systems            |                                        |
+--------------------+--------------------+----------------------------------------+
| Puppet agent       | local Puppet agent | init script                            |
|                    |                    | :file:`/etc/init.d/puppet`             |
+--------------------+--------------------+----------------------------------------+
| Puppet DB          | PuppetDB for       | init script                            |
|                    | querying Puppet    | :file:`/etc/init.d/puppetdb`           |
|                    | facts and nodes    |                                        |
|                    | and resources      |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+-------------+----------+-------------------+
| RDBMS       | Name     | Used for          |
+=============+==========+===================+
| PostgreSQL  | puppetdb | PuppetDB database |
+-------------+----------+-------------------+

Connected Systems
-----------------

* :doc:`svn`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates
* apt.puppetlabs.com as Debian repository for puppet packages
* forgeapi.puppet.com for Puppet forge access
* rubygems.org for Puppet specific Ruby gems

Security
========

.. sshkeys::
   :RSA:     5b:50:09:cf:e8:46:a4:a7:d8:00:85:3d:ec:85:b0:9d
   :DSA:     fb:6f:e4:96:62:09:8c:08:a8:d6:9b:d5:08:d2:e9:ad
   :ECDSA:   71:44:f9:39:ef:0c:f8:1c:ae:05:8d:a1:07:05:69:f7
   :ED25519: c5:84:7a:dd:40:a9:2d:67:57:a0:0b:dc:60:3d:cc:22


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


Tasks
=====

Planned
-------

* migrate as many systems as possible to use Puppet for a more
  reproducible/auditable system setup
* automate updates of the Puppet code from Git

.. todo:: implement Webhook on the puppet machine that triggers git pull and r10k run

Changes
=======

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
