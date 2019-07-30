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

:ref:`Jan Dittberner <people_jandd>` and :ref:`Mario Lipinski <people_mario>`
have :program:`sudo` access on that machine too.

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

.. index::
   single: Monitoring; Blog

Monitoring
----------

:internal checks: :monitor:`blog.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Blog

====================== ======== ====================================================================
Name                   Type     Content
====================== ======== ====================================================================
blog.cacert.org.       IN A     213.154.225.234
blog.cacert.org.       IN SSHFP 1 1 32CA6E4BA3275AAB0D65F0F46969B11A4C4B36E8
blog.cacert.org.       IN SSHFP 1 2 3afb452ac3690cf7cd9a3332813bf7b13dbd288c7a4efbd9ab9dd4b4649ff2b6
blog.cacert.org.       IN SSHFP 2 1 AAFBA94EBE5C5C45CDF5EF10D0BC31BEA4D9ECEC
blog.cacert.org.       IN SSHFP 2 2 4d4384ebd1906125ae26d2fa976596af914b4b3587f2204a0e01368a3640f680
blog.cacert.org.       IN SSHFP 3 1 8fa85a31215f10ea78fd0126d1c705c9a3662c86
blog.cacert.org.       IN SSHFP 3 2 86d330b900db9bf0a8bc9ec34b126aa8261fec9e02b123ab61c2aee0b56ae047
blog.cacert.org.       IN SSHFP 4 1 90903e8f4b35457bf41235f070adf592d7f724dd
blog.cacert.org.       IN SSHFP 4 2 f24b770c16dcb91afc9461e62e6fe63a63d413efa4794751c039ed6d5213127b
blog.intra.cacert.org. IN A     172.16.2.13
====================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.11

* Debian GNU/Linux 8.11

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
   single: apache httpd
   single: cron
   single: dbus
   single: mysql
   single: nrpe
   single: openssh
   single: postfix

+--------------------+--------------------+-------------------------------------------------+
| Service            | Usage              | Start mechanism                                 |
+====================+====================+=================================================+
| Apache httpd       | Webserver for blog | systemd unit ``apache2.service``                |
+--------------------+--------------------+-------------------------------------------------+
| cron               | job scheduler      | systemd unit ``cron.service``                   |
+--------------------+--------------------+-------------------------------------------------+
| dbus-daemon        | System message bus | systemd unit ``dbus.service``                   |
|                    | daemon             |                                                 |
+--------------------+--------------------+-------------------------------------------------+
| MySQL              | MySQL database     | systemd unit ``mysql.service``                  |
|                    | server for blog    |                                                 |
+--------------------+--------------------+-------------------------------------------------+
| openssh server     | ssh daemon for     | systemd unit ``ssh.service``                    |
|                    | remote             |                                                 |
|                    | administration     |                                                 |
+--------------------+--------------------+-------------------------------------------------+
| Postfix            | SMTP server for    | systemd unit ``postfix.service``                |
|                    | local mail         |                                                 |
|                    | submission         |                                                 |
+--------------------+--------------------+-------------------------------------------------+
| Nagios NRPE server | remote monitoring  | systemd unit ``/etc/init.d/nagios-nrpe-server`` |
|                    | service queried by |                                                 |
|                    | :doc:`monitor`     |                                                 |
+--------------------+--------------------+-------------------------------------------------+

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
   :RSA:     SHA256:OvtFKsNpDPfNmjMygTv3sT29KIx6TvvZq53UtGSf8rY MD5:ec:cb:b5:13:7c:17:c4:c3:23:3d:ee:01:58:75:b5:8d
   :DSA:     SHA256:TUOE69GQYSWuJtL6l2WWr5FLSzWH8iBKDgE2ijZA9oA MD5:c6:a7:52:f6:63:ce:73:95:41:35:90:45:9e:e0:06:a5
   :ECDSA:   SHA256:htMwuQDbm/CovJ7DSxJqqCYf7J4CsSOrYcKu4LVq4Ec MD5:00:d7:4b:3c:da:1b:24:76:74:1c:dd:2c:64:50:5f:81
   :ED25519: SHA256:8kt3DBbcuRr8lGHmLm/mOmPUE++keUdRwDntbVITEns MD5:0c:fe:c7:a1:bd:e6:43:e6:70:5a:be:5a:15:4d:08:9d

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
   :altnames:   DNS:blog.cacert.org
   :certfile:   /etc/ssl/public/blog.cacert.org.crt
   :keyfile:    /etc/ssl/private/blog.cacert.org.key
   :serial:     1381E6
   :expiration: Mar 16 09:17:48 2020 GMT
   :sha1fp:     E9:92:97:26:01:C1:00:3C:D7:BC:A2:2D:F4:F7:24:1C:47:C0:01:51
   :issuer:     CA Cert Signing Authority

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

.. todo:: add a section documenting wordpress and plugin updates
.. todo:: add a section documenting wordpress user management

Changes
=======

Planned
-------

.. todo:: switch to Puppet management
.. todo:: replace nrpe with icinga2 agent
.. todo:: update wordpress to 5.x
.. todo:: update to Debian 9/10
.. todo:: setup IPv6

.. todo::
   setup CRL checks (can be borrowed from :doc:`svn`) for client certificates

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Wordpress website
   https://wordpress.org/
