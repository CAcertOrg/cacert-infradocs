.. index::
   single: Systems; Bugs

====
Bugs
====

Purpose
=======

This system provides the public bug tracker for the CAcert community.

.. note:: There currently seems to be a problem for users signing up themselves
   for new accounts. Unless this is fixed by Debian, new accounts must be
   created by administrators. For more details ask the `support mailing list
   <cacert-support@lists.cacert.org>`_.

Application Links
-----------------

Bugtracker
   https://bugs.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_neo`
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

+----------------------+--------------------------------------------+
| Application          | Administrator(s)                           |
+======================+============================================+
| Mantis Administrator | :ref:`people_benbe`, :ref:`people_neo`,    |
|                      | :ref:`people_dirk`, :ref:`people_jandd`,   |
|                      | :ref:`people_ted`, :ref:`people_mario`,    |
|                      | :ref:`people_philipp`                      |
+----------------------+--------------------------------------------+
| Mantis Manager       | :ref:`people_marcus`, :ref:`people_ulrich` |
+----------------------+--------------------------------------------+

Contact
-------

* bugs-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` and :ref:`people_dirk` have :program:`sudo` access on that
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
:MAC address: :mac:`00:ff:fe:13:14:7a` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Bugs

======================== ======== ============================================
Name                     Type     Content
======================== ======== ============================================
bugs.cacert.org.         IN A     213.154.225.232
bugs.cacert.org.         IN SSHFP 1 1 4B4BC32C4E655559B43A370B77CAD4983E8C24F8
bugs.cacert.org.         IN SSHFP 2 1 7916E317983D8BC85D719BB793E5E46A6B4976B2
bugs.intra.cacert.org.   IN A     172.16.2.16
======================== ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.8

* Debian GNU/Linux 8.8

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+---------+---------+--------------------------------+
| Port     | Service | Origin  | Purpose                        |
+==========+=========+=========+================================+
| 22/tcp   | ssh     | ANY     | admin console access           |
+----------+---------+---------+--------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA     |
+----------+---------+---------+--------------------------------+
| 80/tcp   | http    | ANY     | web server for bug tracker     |
+----------+---------+---------+--------------------------------+
| 443/tcp  | https   | ANY     | web server for bug tracker     |
+----------+---------+---------+--------------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service      |
+----------+---------+---------+--------------------------------+
| 3306/tcp | mysql   | local   | MySQL database for bug tracker |
+----------+---------+---------+--------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: cron
   single: nrpe
   single: openssh
   single: rsyslog

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for bug  | init script                            |
|                    | tracker            | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| MySQL              | MySQL database     | init script                            |
|                    | server for bug     | :file:`/etc/init.d/mysql`              |
|                    | tracker            |                                        |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

.. index::
   pair: MySQL database; mantis

+-------+--------+--------------------+
| RDBMS | Name   | Used for           |
+=======+========+====================+
| MySQL | mantis | Mantis bug tracker |
+-------+--------+--------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates
* crl.cacert.org (rsync) for getting CRLs
* HTTP (80/tcp) to :doc:`git`

Security
========

.. sshkeys::
   :RSA:   59:41:a6:da:9f:64:87:85:76:6f:ad:d5:5f:a8:50:45
   :DSA:   17:ef:36:49:60:6e:bb:36:fd:ef:d9:77:90:59:00:a9
   :ECDSA: a2:ee:46:14:c0:31:53:2a:b3:d1:34:82:02:df:ab:bc

Non-distribution packages and modifications
-------------------------------------------

.. index::
   pair: non-distribution package; Mantis

* custom built `mantis`_ package by :ref:`people_benbe`

.. _mantis: https://www.mantisbt.org/

Risk assessments on critical packages
-------------------------------------

Mantis as a PHP application is vulnerable to common PHP problems. The system
has to be kept up-to-date with OS patches. The custom built mantis package has
to be updated when new releases are provided upstream.

Administrators for this system should subscribe to the
mantisbt-announce@lists.sourceforge.net list to get notified when updates are
released.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: bugs.cacert.org
   :certfile:   /etc/ssl/public/bugs.c.o.20160314.crt
   :keyfile:    /etc/ssl/private/bugs.c.o.20160314.key
   :serial:     028A72
   :expiration: Mar 14 13:12:13 2018 GMT
   :sha1fp:     4D:1F:14:B2:BB:C8:59:68:D0:CF:86:36:DA:2F:B2:58:A7:90:E5:85
   :issuer:     CAcert.org Class 3 Root

* :file:`/etc/ssl/public/bugs.c.o.20160314.crt.chain` contains the server
  certificate and the Class 3 CA certificate

* :file:`/etc/mantis/config_inc.php` contains the database settings for Mantis

.. index::
   pair: Mantis; configuration

Mantis configuration
--------------------

The Mantis bug tracker configuration is stored in the directory
:file:`/etc/mantis/`.

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

Rsyslog has been configured to disable draining the kernel log:

.. code-block:: diff

   --- orig/etc/rsyslog.conf      2015-12-14 13:34:27.000000000 +0100
   +++ bugs/etc/rsyslog.conf  2015-03-03 22:22:44.385835152 +0100
   @@ -9,7 +9,7 @@
    #################

    $ModLoad imuxsock # provides support for local system logging
   -$ModLoad imklog   # provides kernel logging support
   +#$ModLoad imklog   # provides kernel logging support
    #$ModLoad immark  # provides --MARK-- message capability

    # provides UDP syslog reception

The :program:`postfix` package installed :file:`/etc/rsyslog.d/postfix.conf` to
add an additional logging socket in the Postfix chroot.


Tasks
=====

Planned
-------

.. todo:: provide the custom mantis package from a infrastructure Debian
   package repository
.. todo:: setup IPv6
.. todo:: setup X.509 authentication if possible :bug:`678`

Changes
=======

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
