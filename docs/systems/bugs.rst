.. index::
   single: Systems; Bugs

====
Bugs
====

Purpose
=======

This system provides the public bug tracker for the CAcert community.

Application Links
-----------------

Bugtracker
   https://bugs.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: :ref:`people_dirk`

Application Administration
--------------------------

+----------------------+--------------------------------------------+
| Application          | Administrator(s)                           |
+======================+============================================+
| Mantis Administrator | :ref:`people_neo`, :ref:`people_mario`,    |
|                      | :ref:`people_dirk`, :ref:`people_jandd`,   |
|                      | :ref:`people_ted`, :ref:`people_philipp`   |
+----------------------+--------------------------------------------+
| Mantis Manager       |                                            |
+----------------------+--------------------------------------------+

Contact
-------

* bugs-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` and :ref:`people_wytze` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.232`
:IP Intranet: :ip:v4:`172.16.2.16`
:IP Internal: :ip:v4:`10.0.0.16`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::16`
:MAC address: :mac:`00:ff:fe:13:14:7a` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Bugs

Monitoring
----------

:internal checks: :monitor:`bugs.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Bugs

======================== ======== ====================================================================
Name                     Type     Content
======================== ======== ====================================================================
bugs.cacert.org.         IN A     213.154.225.232
bugs.cacert.org.         IN AAAA  2001:7b8:616:162:2::16
bugs.cacert.org.         IN SSHFP 1 1 4B4BC32C4E655559B43A370B77CAD4983E8C24F8
bugs.cacert.org          IN SSHFP 1 2 51f10258849d1194f282deb0da97009016423d5f0b28a0056a551c4f38c2870a
bugs.cacert.org.         IN SSHFP 2 1 7916E317983D8BC85D719BB793E5E46A6B4976B2
bugs.cacert.org          IN SSHFP 2 2 7632a8a40f1534a3afa3c630d062062dd23c7b1fd24fc518334d82cfa4977892
bugs.cacert.org          IN SSHFP 3 1 72737bd1240b446c2b8e0aad0acff889e3b72ec7
bugs.cacert.org          IN SSHFP 3 2 152fc9f8d7d72979846757db7fa433bd3f6340cd0dcebcce5d681e60dc46ca44
bugs.cacert.org          IN SSHFP 4 1 bb6b5f8599c3a93383392b80cc029a0d65ffc7f1
bugs.cacert.org          IN SSHFP 4 2 caa52e4c5ddecc5ee144aa2b6965101961ff7e7518063b43908d133f1cdf6e15
bugs.intra.cacert.org.   IN A     172.16.2.16
======================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.9

* Debian GNU/Linux 10.9

Services
========

Listening services
------------------

+----------+---------+---------+----------------------------------+
| Port     | Service | Origin  | Purpose                          |
+==========+=========+=========+==================================+
| 22/tcp   | ssh     | ANY     | admin console access             |
+----------+---------+---------+----------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA       |
+----------+---------+---------+----------------------------------+
| 80/tcp   | http    | ANY     | web server for bug tracker       |
+----------+---------+---------+----------------------------------+
| 443/tcp  | https   | ANY     | web server for bug tracker       |
+----------+---------+---------+----------------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service        |
+----------+---------+---------+----------------------------------+
| 3306/tcp | mariadb | local   | MariaDB database for bug tracker |
+----------+---------+---------+----------------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: dbus
   single: icinga2
   single: mariadb
   single: openssh
   single: postfix
   single: puppet agent
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| Apache httpd   | Webserver for bug        | systemd unit ``apache2.service`` |
|                | tracker                  |                                  |
+----------------+--------------------------+----------------------------------+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``    |
|                | daemon                   |                                  |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| MariaDB        | MariaDB database         | systemd unit ``mariadb.service`` |
|                | server for bug           |                                  |
|                | tracker                  |                                  |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``     |
|                | remote                   |                                  |
|                | administration           |                                  |
+----------------+--------------------------+----------------------------------+
| Postfix        | SMTP server for          | systemd unit ``postfix.service`` |
|                | local mail               |                                  |
|                | submission               |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
|                |                          |                                  |
+----------------+--------------------------+----------------------------------+

Databases
---------

.. index::
   pair: MySQL database; mantis
   pair: MariaDB database; mantis

+---------+--------+--------------------+
| RDBMS   | Name   | Used for           |
+=========+========+====================+
| MariaDB | mantis | Mantis bug tracker |
+---------+--------+--------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT
* crl.cacert.org (rsync) for getting CRLs
* HTTP (80/tcp) to :doc:`git`

Security
========

.. sshkeys::
   :RSA:     SHA256:UfECWISdEZTygt6w2pcAkBZCPV8LKKAFalUcTzjChwo MD5:59:41:a6:da:9f:64:87:85:76:6f:ad:d5:5f:a8:50:45
   :DSA:     SHA256:djKopA8VNKOvo8Yw0GIGLdI8ex/ST8UYM02Cz6SXeJI MD5:17:ef:36:49:60:6e:bb:36:fd:ef:d9:77:90:59:00:a9
   :ECDSA:   SHA256:FS/J+NfXKXmEZ1fbf6QzvT9jQM0NzrzOXWgeYNxGykQ MD5:a2:ee:46:14:c0:31:53:2a:b3:d1:34:82:02:df:ab:bc
   :ED25519: SHA256:yqUuTF3ezF7hRKoraWUQGWH/fnUYBjtDkI0TPxzfbhU MD5:54:67:22:bf:2d:ae:35:1f:fd:13:98:ee:af:3a:f3:07

Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

.. index::
   pair: non-distribution package; Mantis

* Mantis installed in /srv/mantis (linked to /srv/mantisbt-2.4.2)
* custom built `certificate authentication`-plugin by :ref:`people_dirk`
  https://github.com/dastrath/CertificateAuthentication_Mantis
* For client certificate authentication a Class-3 client certificate issued by
  CAcert is needed, 1st email-adress in certificate has to match email-adress in
  account

.. _mantis: https://www.mantisbt.org/

Risk assessments on critical packages
-------------------------------------

Mantis as a PHP application is vulnerable to common PHP problems. The system
has to be kept up-to-date with OS patches. The custom built mantis package has
to be updated when new releases are provided upstream.

Administrators for this system should subscribe to the
mantisbt-announce@lists.sourceforge.net list to get notified when updates are
released.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

.. todo:: move all configuration of bugs to Puppet code

Keys and X.509 certificates
---------------------------

All keys and certificates are managed in the file
:file:`hieradata/nodes/bugs.yaml` in the :cacertgit:`cacert-puppet`.

.. sslcert:: bugs.cacert.org
   :altnames:   DNS:bugs.cacert.org
   :certfile:   /etc/ssl/public/bugs.cacert.org.chain.pem
   :keyfile:    /etc/ssl/private/bugs.cacert.org.key.pem
   :serial:     02F624
   :expiration: Jan 8 12:10:46 2024 GMT
   :sha1fp:     7E:24:94:73:A5:A1:01:B5:D7:D2:73:C1:E2:F6:52:6F:43:A8:86:FA
   :issuer:     CAcert Class 3 Root

* :file:`/etc/ssl/public/bugs.cacert.org_client_cas.pem` CAcert.org Class 1 and
  Class 3 CA certificates (allowed CA certificates for client certificates)

.. index::
   pair: Mantis; configuration

Mantis configuration
--------------------

The Mantis bug tracker configuration is stored in the directory
:file:`/etc/mantis/`.

* :file:`config_inc.php` contains the database settings for Mantis
* :file:`config_local.php` the main configuration file, including custom bug states
* :file:`custom_constants_inc.php` defines custom constants. Required for the
  non-default bug states
* :file:`custom_strings_inc.php` defines custom string definitions. Required
  for the non-default bug states

.. note::

   Localisation for these could go here but currently I would avoid that so all
   developers have the same vocabulary.

   -- :ref:`people_neo` 2011-07-04 02:44:45

.. index::
   pair: Apache httpd; configuration

Apache httpd configuration
--------------------------

The Apache httpd configuration in the directory :file:`/etc/apache2/` has been
changed to add some additional headers to improve client security:

.. literalinclude:: ../configdiff/bugs/apache/bugs-apache-config.diff
   :language: diff

The :index:`Mantis VirtualHost <pair: bugs.cacert.org; VirtualHost>` is
configured in :file:`/etc/apache2/sites-available/mantis` (shared
configuration) that includes configuration from the mantis package provided
:file:`/etc/apache2/conf.d/mantis` file,
:file:`/etc/apache2/sites-available/mantis-nossl.conf` (HTTP VirtualHost) and
:file:`/etc/apache2/sites-available/mantis-ssl.conf` (HTTPS VirtualHost).

.. index::
   pair: MySQL; configuration

MySQL configuration
-------------------

MySQL configuration is stored in the :file:`/etc/mysql/` directory.

.. index::
   pair: rsyslog; configuration

Rsyslog configuration
---------------------

Rsyslog is configured by Puppet.

Tasks
=====

.. todo:: add a section documenting how to manage mantis projects
.. todo:: add a section documenting how to manage mantis users

Changes
=======

Planned
-------

.. todo::

   Switch ingest traffic for webmail to proxyin and drop http redirector
   configuration from Apache httpd

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Mantis Bugtracker documentation
   https://www.mantisbt.org/documentation.php
Apache httpd documentation
   https://httpd.apache.org/docs/2.4/
