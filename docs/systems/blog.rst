.. index::
   single: Systems; Blog

====
Blog
====

Purpose
=======

This system hosts the blog, blog.cacert.org. The blog meets the needs of public
relations and the CAcert community to publish CAcert's activities.

Application Links
-----------------

Blog URL
   https://blog.cacert.org/

Adding a category
   https://blog.cacert.org/wp-admin/categories.php

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_dirk`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+-----------------------+-------------------------------------------------+
| Role                  | Users                                           |
+=======================+=================================================+
| Wordpress Admin       | :ref:`people_dirk`,                             |
|                       | :ref:`people_mario`,                            |
+-----------------------+-------------------------------------------------+
| Wordpress Editor      | PR Team,                                        |
|                       | `Support`_                                      |
+-----------------------+-------------------------------------------------+
| Wordpress Author      | Anyone with a certificate                       |
+-----------------------+-------------------------------------------------+
| Wordpress Contributor | Anyone with contributor privileges              |
+-----------------------+-------------------------------------------------+
| Wordpress Subscriber  | Any Spammer or person who has not posted or has |
|                       | not logged in                                   |
+-----------------------+-------------------------------------------------+

.. _Support: support@cacert.org

Contact
-------

* blog-admin@cacert.org

Additional People
-----------------

:ref:`Jan Dittberner <people_jandd>`, :ref:`Mario Lipinski <people_mario>` and
:ref:`Dirk Astrath <people_dirk>` have :program:`sudo` access on that machine
too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.234`
:IP Intranet: :ip:v4:`172.16.2.13`
:IP Internal: :ip:v4:`10.0.0.13`
:MAC address: :mac:`00:ff:fa:af:b2:9b` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Blog

====================== ======== ============================================
Name                   Type     Content
====================== ======== ============================================
blog.cacert.org.       IN A     213.154.225.234
blog.cacert.org.       IN SSHFP 1 1 32CA6E4BA3275AAB0D65F0F46969B11A4C4B36E8
blog.cacert.org.       IN SSHFP 2 1 AAFBA94EBE5C5C45CDF5EF10D0BC31BEA4D9ECEC
blog.intra.cacert.org. IN A     172.16.2.13
====================== ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.10

* Debian GNU/Linux 8.10

Applicable Documentation
------------------------

A small (work in progress) guide can be found in the :wiki:`BlogDoc`.

Services
========

Listening services
------------------

+----------+---------+---------+----------------------------+
| Port     | Service | Origin  | Purpose                    |
+==========+=========+=========+============================+
| 22/tcp   | ssh     | ANY     | admin console access       |
+----------+---------+---------+----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA |
+----------+---------+---------+----------------------------+
| 80/tcp   | http    | ANY     | application                |
+----------+---------+---------+----------------------------+
| 443/tcp  | https   | ANY     | application                |
+----------+---------+---------+----------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+
| 3306/tcp | mysql   | local   | MySQL database for blog    |
+----------+---------+---------+----------------------------+
| 9000/tcp | php-fpm | local   | PHP FPM executor           |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: PHP FPM
   single: Postfix
   single: cron
   single: nrpe
   single: openssh

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for blog | init script                            |
|                    |                    | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| MySQL              | MySQL database     | init script                            |
|                    | server for blog    | :file:`/etc/init.d/mysql`              |
+--------------------+--------------------+----------------------------------------+
| PHP FPM            | PHP FPM executor   | init script                            |
|                    | for blog           | :file:`/etc/init.d/php5-fpm`           |
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

+-------+------------+------------------------------+
| RDBMS | Name       | Used for                     |
+=======+============+==============================+
| MySQL | blog       | Wordpress blog               |
+-------+------------+------------------------------+
| MySQL | phpmyadmin | PHPMyAdmin settings database |
+-------+------------+------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* HTTP (80/tcp) and HTTPS (443/tcp) `Ping-o-matic`_ blog update service [#f1]_
* HTTP (80/tcp) and HTTPS (443/tcp) to Akismet anti spam service [#f2]_
* HTTP (80/tcp) and HTTPS (443/tcp) to wordpress.org
* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* crl.cacert.org (rsync) for getting CRLs

.. _Ping-o-matic: http://rpc.pingomatic.com/
.. [#f1] http://blog.cacert.org/wp-admin/options-writing.php
.. [#f2] http://blog.cacert.org/wp-admin/plugins.php?page=akismet-key-config

.. - check network status

Security
========

.. sshkeys::
   :RSA:     MD5:ec:cb:b5:13:7c:17:c4:c3:23:3d:ee:01:58:75:b5:8d
   :DSA:     MD5:c6:a7:52:f6:63:ce:73:95:41:35:90:45:9e:e0:06:a5
   :ECDSA:   MD5:00:d7:4b:3c:da:1b:24:76:74:1c:dd:2c:64:50:5f:81
   :ED25519: MD5:0c:fe:c7:a1:bd:e6:43:e6:70:5a:be:5a:15:4d:08:9d

Dedicated user roles
--------------------

+-------+--------------------------------------------------------------------+
| Group | Purpose                                                            |
+=======+====================================================================+
| blog  | group owning the blog file content and temporary files. This group |
|       | is used to execute the Wordpress PHP code.                         |
+-------+--------------------------------------------------------------------+

Non-distribution packages and modifications
-------------------------------------------

* **Wordpress Plugins**

  * `client-certificate-authentication
    <http://wordpress.org/plugins/client-certificate-authentication/>`_
  * akismet

Risk assessments on critical packages
-------------------------------------

+-------------+-------------+---------------------------------------------+
| Software    | Risk rating | Mitigation                                  |
+=============+=============+=============================================+
| *Wordpress* | high        | Regular updates, avoid unnecessary plugins, |
|             |             | Consider `Wordpress hardening`_             |
+-------------+-------------+---------------------------------------------+

.. todo:: `Wordpress hardening`_

.. _Wordpress hardening: http://codex.wordpress.org/Hardening_WordPress

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: blog.cacert.org
   :certfile:   /etc/ssl/public/blog.cacert.org.crt
   :keyfile:    /etc/ssl/private/blog.cacert.org.key
   :serial:     11e837
   :expiration: Mar 31 16:34:28 2018 GMT
   :sha1fp:     69:A5:5F:3E:1B:D8:2E:CB:B3:AB:0B:E9:81:A6:CF:31:DF:C8:A4:5F
   :issuer:     CAcert.org Class 1 Root CA

* :file:`/etc/ssl/certs/cacert.org/` directory containing CAcert.org Class 1
  and Class 3 certificates (allowed CA certificates for client certificates)
  and symlinks with hashed names as expected by OpenSSL
* :file:`/etc/ssl/certs/cacert.org.pem` CAcert.org Class 1 certificate
  (certificate chain for server certificate)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: Apache httpd; configuration

Apache httpd configuration
--------------------------

* :file:`/etc/apache2/cacert/blog.inc.conf`

  Defines settings that are shared by the HTTP and the HTTPS VirtualHost
  definitions. This file takes care of the PHP FCGI setup.

* :file:`/etc/apache2/cacert/headers.inc.conf`

  Defines HTTP headers that are shared by the HTTP and the HTTPS VirtualHost
  definitions. The file is included by
  :file:`/etc/apache2/cacert/blog.inc.conf`.

* :file:`/etc/apache2/sites-available/blog-ssl.conf`

  This file contains the HTTPS VirtualHost definition and defines client
  certificate authentication for ``/wp-admin`` and ``/wp-login.php``.

* :file:`/etc/apache2/sites-available/blog-nossl.conf`

  This file defines the HTTP VirtualHost definition and takes care of
  redirecting ``/wp-admin`` and ``/wp-login.php`` to the HTTPS VirtualHost.

The following RewriteRule is used to redirect old blog URLs::

  RewriteRule ^/[0-9]{4}/[0-9]{2}/([0-9]+)\.html$ ?p=$1 [R=302,L]

.. index::
   pair: Wordpress; configuration

Wordpress configuration
-----------------------

* :file:`/srv/www/blog/wp-config.php` contains the Wordpress database
  configuration. The rest of the Wordpress configuration is stored in the
  database (assumption).

Tasks
=====

Planned
-------

.. todo:: setup IPv6

.. todo::
   setup CRL checks (can be borrowed from :doc:`svn`) for client certificates

Changes
=======

System Future
-------------

.. todo:: system should be upgraded to Debian 9

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Wordpress website
   https://wordpress.org/
