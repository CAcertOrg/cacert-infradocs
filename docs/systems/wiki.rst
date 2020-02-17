.. index::
   single: Systems; Wiki

====
Wiki
====

Purpose
=======

The purpose of the wiki server is to serve the wiki, implemented with MoinMoin.

Application Links
-----------------

Wiki URL
     https://wiki.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_dirk`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

.. todo:: document wiki admins

Contact
-------

* wiki-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd` and :ref:`people_mario` have :program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.235`
:IP Intranet: :ip:v4:`172.16.2.12`
:IP Internal: :ip:v4:`10.0.0.12`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::12`
:MAC address: :mac:`00:ff:32:e3:13:66` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Wiki

Monitoring
----------

:internal checks: :monitor:`wiki.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Wiki

+------------------------+----------+----------------------------------------------+
| Name                   | Type     | Content                                      |
+========================+==========+==============================================+
| wiki.cacert.org.       | IN SSHFP | 2 1 04F7AB767579F004CC3AB2CC42A4CCAA24E51154 |
| wiki.cacert.org.       | IN SSHFP | 1 1 5C3E0D3265782405E0141C47BF0E16EC14B12E08 |
| wiki.cacert.org.       | IN A     | 213.154.225.235                              |
| wiki.intra.cacert.org. | IN A     | 172.16.2.12                                  |
| wiki.infra.cacert.org. | IN AAAA  | 2001:7b8:616:162:2::12                       |
| wiki.infra.cacert.org. | IN MX    | 1 emailout.infra.cacert.org.                 |
+------------------------+----------+----------------------------------------------+

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.11

* Debian GNU/Linux 7.11

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

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: exim4
   single: nginx
   single: nrpe
   single: openssh
   single: postfix
   single: syslog-ng

+--------------------+-----------------------------------------------------+----------------------------------------------------+
| Service            | Usage                                               | Start mechanism                                    |
+====================+=====================================================+====================================================+
| Apache httpd       | Webserver for the Wiki                              | init script :file:`/etc/init.d/apache2`            |
+--------------------+-----------------------------------------------------+----------------------------------------------------+
| cron               | job scheduler                                       | init script :file:`/etc/init.d/cron`               |
+--------------------+-----------------------------------------------------+----------------------------------------------------+
| Nagios NRPE server | remote monitoring service queried by :doc:`monitor` | init script :file:`/etc/init.d/nagios-nrpe-server` |
+--------------------+-----------------------------------------------------+----------------------------------------------------+
| openssh server     | ssh daemon for remote administration                | init script :file:`/etc/init.d/ssh`                |
+--------------------+-----------------------------------------------------+----------------------------------------------------+
| Postfix            | SMTP server for local mail submission               | init script :file:`/etc/init.d/postfix`            |
+--------------------+-----------------------------------------------------+----------------------------------------------------+
| syslog-ng          | syslog daemon                                       | init script :file:`/etc/init.d/syslog-ng`          |
+--------------------+-----------------------------------------------------+----------------------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA:   SHA256:aRAYcstinjCnjKSqx4FyDhIXw3M/a7jWWQNOnCPIkN8 MD5:f8:16:e5:40:91:42:10:a6:ba:aa:e3:f9:1a:71:d7:09
   :DSA:   SHA256:cgJn47gOMu4RSqz9DUvWvnHh0v3pFNfD9hrBmOYQ9ZI MD5:d5:36:2d:0c:bb:73:da:43:0c:23:61:df:b6:b9:8c:c9
   :ECDSA: SHA256:iNc8go1W08zKxTBVi/ChsmeMI48oXD72th+gXqeC/WA MD5:09:ea:70:41:1b:bb:a4:6a:fa:fd:37:c2:29:05:35:0e

Non-distribution packages and modifications
-------------------------------------------

MoinMoin in :file:`/srv/www/wiki/`.

.. todo:: properly document the Wiki setup or replace it with a packaged version

Risk assessments on critical packages
-------------------------------------

The whole system is outdated an end of life and must be updated.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: wiki.cacert.org
   :altnames:   DNS:wiki.cacert.org
   :certfile:   /etc/ssl/public/wiki.cacert.org.crt
   :keyfile:    /etc/ssl/private/wiki.cacert.org.key
   :serial:     138206
   :expiration: Mar 16 12:04:29 2020 GMT
   :sha1fp:     F8:2F:5A:31:5D:73:CD:62:F0:59:EE:6E:D6:F8:9E:95:EA:23:FE:A9
   :issuer:     CA Cert Signing Authority

:file:`/etc/ssl/certs/cacert.org.pem` CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for client certificates)
:file:`/etc/ssl/certs/cacert.org/` CAcert.org Class 1 certificate (certificate chain for server certificate)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache configuration
--------------------

Apache is configured using files in :file:`/etc/apache2` integrating the MoinMoin wiki using `mod_wsgi`.

.. todo:: more comprehensive Apache configuration documentation for :doc:`wiki`

Changes
=======

System Future
-------------

.. todo:: update the OS of :doc:`wiki`

.. todo:: introduce Puppet management for :doc:`wiki`

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

* http://moinmo.in/
