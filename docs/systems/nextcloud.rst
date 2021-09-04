.. index::
   single: Systems; nextcloud

=========
Nextcloud
=========

Purpose
=======

This system serves a `Nextcloud <https://nextcloud.com/>`_ instance.

Application Links
-----------------

CAcert Nextcloud
    https://nextcloud.cacert.org

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_sat`
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

+-------------+-------------------+
| Application | Administrator(s)  |
+=============+===================+
| nextcloud   | :ref:`people_sat` |
+-------------+-------------------+

Contact
-------

* nextcloud-admin@cacert.org

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra03`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.249`
:IP Intranet: :ip:v4:`172.16.2.9`
:IP Internal: :ip:v4:`10.0.3.12`
:IPv6:        :ip:v6:`2001:7b8:616:162:3::12`
:MAC address: :mac:`00:ff:8f:af:3d:18` (eth0@if15)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; nextcloud

Monitoring
----------

:internal checks: :monitor:`nextcloud.infra.cacert.org`
:external checks: :monitor:`nextcloud.cacert.org`

DNS
---

.. index::
   single: DNS records; nextcloud

+-----------------------------+----------+----------------------------------------------------------------------+
| Name                        | Type     | Content                                                              |
+=============================+==========+======================================================================+
| nextcloud.cacert.org.       | IN A     | 213.154.225.249                                                      |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN AAAA  | 2001:7b8:616:162:3::12                                               |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.infra.cacert.org. | IN A     | 10.0.3.12                                                            |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.infra.cacert.org. | IN AAAA  | 2001:7b8:616:162:3::12                                               |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN SSHFP | 1 1 5F7F6B6FBB86C469CA52B4705BB034AAE6EA0DC9                         |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org        | IN SSHFP | 1 2 14B734AE965BF216749019B727084D70952DBBC83BD93D049F6567BD571E09B2 |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN SSHFP | 3 1 ABD6257BFC4E47909E4D41B06914A196B8B2B4F1                         |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN SSHFP | 3 2 C6F857E69CF509443FF011505B3A774BFA3A149926A7818CD37167C211BEC55B |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN SSHFP | 4 1 DC1C48FD2E62A98672EA70126B2209D604CBC758                         |
+-----------------------------+----------+----------------------------------------------------------------------+
| nextcloud.cacert.org.       | IN SSHFP | 4 2 5563549548D8BE620AAB5B609F2B48A15BE0D80986F79E3A5B28C1F4A974617B |
+-----------------------------+----------+----------------------------------------------------------------------+

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.10

* Debian GNU/Linux 10.10

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
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: openssh
   single: php-fpm
   single: puppet
   single: rsyslog

+----------------+---------------------------------------+-------------------------------------+
| Service        | Usage                                 | Start mechanism                     |
+================+=======================================+=====================================+
| Apache httpd   | Webserver for Nextcloud               | systemd unit ``apache2.service``    |
+----------------+---------------------------------------+-------------------------------------+
| cron           | job scheduler                         | systemd unit ``cron.service``       |
+----------------+---------------------------------------+-------------------------------------+
| dbus-daemon    | System message bus                    | systemd unit ``dbus.service``       |
+----------------+---------------------------------------+-------------------------------------+
| Exim           | SMTP server for local mail submission | systemd unit ``exim4.service``      |
+----------------+---------------------------------------+-------------------------------------+
| icinga2        | Icinga2 monitoring agent              | systemd unit ``icinga2.service``    |
+----------------+---------------------------------------+-------------------------------------+
| openssh server | ssh daemon for remote administration  | systemd unit ``ssh.service``        |
+----------------+---------------------------------------+-------------------------------------+
| PHP-FPM        | PHP for Nextcloud                     | systemd unit ``php7.3-fpm.service`` |
+----------------+---------------------------------------+-------------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``     |
+----------------+---------------------------------------+-------------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service``    |
+----------------+---------------------------------------+-------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`ingress03` as incoming SNI proxy for IPv4

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`mariadb` as database server
* crl.cacert.org (rsync) for getting CRLs

Security
========

.. sshkeys::
   :RSA:     SHA256:FLc0rpZb8hZ0kBm3JwhNcJUtu8g72T0En2VnvVceCbI MD5:c9:29:d7:82:f1:65:47:57:48:44:e1:1f:45:af:25:7c
   :ECDSA:   SHA256:xvhX5pz1CUQ/8BFQWzp3S/o6FJkmp4GM03FnwhG+xVs MD5:5d:62:29:ef:1f:33:7d:7a:c7:63:79:cd:de:1f:4d:9d
   :ED25519: SHA256:VWNUlUjYvmIKq1tgnytIoVvg2AmG9546WyjB9Kl0YXs MD5:64:ae:e0:b3:b0:e3:9a:a7:9e:67:07:f2:a0:e8:a1:87

Non-distribution packages and modifications
-------------------------------------------

Nextcloud has been installed from the Upstream installation archives in
:file:`/var/www/nextcloud` and is actively maintained by :ref:`people_sat`.

Risk assessments on critical packages
-------------------------------------

Apache httpd and PHP-FPM are installed from Debian distribution packages and
are security supported.

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: nextcloud.cacert.org
   :altnames:   DNS:nextcloud.cacert.org
   :certfile:   /etc/ssl/nextcloud.cacert.org.crt
   :keyfile:    /etc/ssl/nextcloud.cacert.org.key
   :serial:     02F2DB
   :expiration: Aug 28 15:31:30 2023 GMT
   :sha1fp:     15:FD:55:B9:EC:B3:F0:1F:1B:39:35:5F:E7:B3:AC:8D:A6:EA:E1:E1
   :issuer:     CAcert Class 3 Root

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Tasks
=====

Adding nextcloud users
----------------------

Nextcloud user administration is done by :ref:`people_sat`.

Changes
=======

Planned
-------

.. todo::

   implement OpenID Connect authentication when the CAcert OIDC IDP has been
   setupIt is planned to add OpenID Connect

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
