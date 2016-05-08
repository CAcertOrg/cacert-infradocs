.. index::
   single: Systems; Arbitration

===========
Arbitration
===========

Purpose
=======

This system is planned to host a future collaboration platform for arbitrators.

Application Links
-----------------

Arbitration nginx welcome page
   http://arbitration.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_martin`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

There is no application yet.

.. todo:: setup application(s) and document admins

Contact
-------

* arbitration-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd` and :ref:`people_mario` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.241`
:IP Intranet: :ip:v4:`172.16.2.241`
:IP Internal: :ip:v4:`10.0.0.241`
:MAC address: :mac:`00:ff:5b:e0:cd:8a` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Arbitration

============================= ======== ============================================
Name                          Type     Content
============================= ======== ============================================
arbitration.cacert.org.       IN A     213.154.225.241
arbitration.cacert.org.       IN SSHFP 1 1 40D9C8EBCF8D41A04B990FBC5308675D029BF4EF
arbitration.cacert.org.       IN SSHFP 2 1 7474BFB01AF775511805BF15C45BB9D7591D0CE6
arbitration.intra.cacert.org. IN A     172.16.2.241
============================= ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.4

* Debian GNU/Linux 8.4

Applicable Documentation
------------------------

This is it :-) There is nothing usable on this system yet.

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 80/tcp   | http      | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+
| 3306/tcp | mysql     | local     | MySQL database for ...                  |
+----------+-----------+-----------+-----------------------------------------+
| 5432/tcp | pgsql     | local     | PostgreSQL database for ...             |
+----------+-----------+-----------+-----------------------------------------+

.. todo:: add TLS/SSL to nginx and add HTTPS port
.. todo:: clarify whether both MySQL and PostgreSQL are used

Running services
----------------

.. index::
   single: openssh
   single: nginx
   single: cron
   single: PostgreSQL
   single: MySQL
   single: Exim
   single: nrpe

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| nginx              | Webserver for ...  | init script                            |
|                    |                    | :file:`/etc/init.d/nginx`              |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for ...            |                                        |
+--------------------+--------------------+----------------------------------------+
| MySQL              | MySQL database     | init script                            |
|                    | server for ...     | :file:`/etc/init.d/mysql`              |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission, ...    |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+-------------+----------+------------------------------+
| RDBMS       | Name     | Used for                     |
+=============+==========+==============================+
| MySQL       | etherpad | future etherpad installation |
+-------------+----------+------------------------------+

.. todo:: setup databases

.. note::
   There is a PostgreSQL server setup in this container but it contains
   no database yet.

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates

Security
========

.. sshkeys::
   :RSA:   a3:6c:f1:f8:8c:81:7c:f7:3b:4e:e4:0e:a3:02:8e:18
   :DSA:   eb:66:0e:0d:d1:f3:d8:02:3a:ed:71:7a:b2:04:db:75
   :ECDSA: 54:a3:76:46:66:fc:3f:2d:9b:e4:bd:49:ba:fe:98:09

.. todo:: setup ED25519 host key

Dedicated user roles
--------------------

.. If the system has some dedicated user groups besides the sudo group used for administration it should be documented here
   Regular operating system groups should not be documented

.. '''Group''' || '''Purpose''' ||
   goodguys || Shell access for the good guys ||

Non-distribution packages and modifications
-------------------------------------------

* some experimental nmp/nodejs/etherpad things in :file:`/home/magu` not
  running yet

Risk assessments on critical packages
-------------------------------------

* No exposed services yet.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

* No keys or certificates setup yet

..
   * :file:`/etc/apache2/ssl/<path to certificate>` server certificate (valid
     until <datetime>)
   * :file:`/etc/apache2/ssl/<path to server key>` server key
   * `/etc/apache2/ssl/cacert-certs.pem` CAcert.org Class 1 and Class 3 CA
     certificates (allowed CA certificates for client certificates)
   * `/etc/apache2/ssl/cacert-chain.pem` CAcert.org Class 1 certificate
     (certificate chain for server certificate)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: Nginx; configuration

Nginx configuration
-------------------

* :file:`/etc/nginx/sites/available/default` default nginx configuration

Tasks
=====

Planned
-------

.. todo:: Evaluate and setup a collaboration system for arbitrators.
.. todo:: setup IPv6

Changes
=======

System Future
-------------

The system should be setup properly or should be removed it is not required
anymore.

Additional documentation
========================

.. add inline documentation

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

nginx Documentation
   http://nginx.org/en/docs/
