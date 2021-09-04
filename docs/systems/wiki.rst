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
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

.. todo:: document wiki admins

Contact
-------

* wiki-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` has :program:`sudo` access on that machine too.

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

+------------------------+----------+----------------------------------------------------------------------+
| Name                   | Type     | Content                                                              |
+========================+==========+======================================================================+
| wiki.cacert.org.       | IN A     | 213.154.225.235                                                      |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN AAAA  | 2001:7b8:616:162:2::12                                               |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 1 1 5C3E0D3265782405E0141C47BF0E16EC14B12E08                         |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 1 2 69101872cb629e30a78ca4aac781720e1217c3733f6bb8d659034e9c23c890df |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 3 1 73113627b9e77be383e4da3a8c4b4a0ae07df5ba                         |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 3 2 88d73c828d56d3cccac530558bf0a1b2678c238f285c3ef6b61fa05ea782fd60 |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 4 1 c1d79ceb8986b02b6b477f8c9e50b2623a15cfe8                         |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.cacert.org.       | IN SSHFP | 4 2 6cfa531e0eebbb01b226444d33c238b83c96cc134d23662f95a36c095c4dfbdf |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.infra.cacert.org. | IN AAAA  | 2001:7b8:616:162:2::12                                               |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.infra.cacert.org. | IN MX    | 1 emailout.infra.cacert.org.                                         |
+------------------------+----------+----------------------------------------------------------------------+
| wiki.intra.cacert.org. | IN A     | 172.16.2.12                                                          |
+------------------------+----------+----------------------------------------------------------------------+

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

+----------+---------+----------+----------------------------+
| Port     | Service | Origin   | Purpose                    |
+==========+=========+==========+============================+
| 22/tcp   | ssh     | ANY      | admin console access       |
+----------+---------+----------+----------------------------+
| 25/tcp   | smtp    | local    | mail delivery to local MTA |
+----------+---------+----------+----------------------------+
| 80/tcp   | http    | ANY      | application                |
+----------+---------+----------+----------------------------+
| 443/tcp  | https   | ANY      | application                |
+----------+---------+----------+----------------------------+
| 5665/tcp | icinga2 | monitor  | remote monitoring service  |
+----------+---------+----------+----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: dbus
   single: icinga2
   single: openssh
   single: postfix
   single: puppet agent
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| Apache httpd   | Webserver for the Wiki   | systemd unit ``apache2.service`` |
+----------------+--------------------------+----------------------------------+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``    |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``     |
|                | remote administration    |                                  |
+----------------+--------------------------+----------------------------------+
| Postfix        | SMTP server for          | systemd unit ``postfix.service`` |
|                | local mail               |                                  |
|                | submission               |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`puppet` (tcp/8140) as Puppet master

Security
========

.. sshkeys::
   :RSA:   SHA256:aRAYcstinjCnjKSqx4FyDhIXw3M/a7jWWQNOnCPIkN8 MD5:f8:16:e5:40:91:42:10:a6:ba:aa:e3:f9:1a:71:d7:09
   :ECDSA: SHA256:iNc8go1W08zKxTBVi/ChsmeMI48oXD72th+gXqeC/WA MD5:09:ea:70:41:1b:bb:a4:6a:fa:fd:37:c2:29:05:35:0e
   :ED25519: SHA256:bPpTHg7ruwGyJkRNM8I4uDyWzBNNI2YvlaNsCVxN+98 MD5:1e:4f:70:ff:65:c2:d5:8a:e2:24:09:04:77:94:9b:a0

Non-distribution packages and modifications
-------------------------------------------

MoinMoin in :file:`/srv/www/wiki/`.

.. todo:: properly document the Wiki setup or replace it with a packaged version

Risk assessments on critical packages
-------------------------------------

The MoinMoin 1.x wiki software is based on Python 2 which is EOL. The software
should be replaced when MoinMoin 2.x comes out with support for Python 3.

.. todo:: upgrade to MoinMoin 2.x when it is available

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

.. todo:: move configuration of wiki to Puppet code

Keys and X.509 certificates
---------------------------

.. sslcert:: wiki.cacert.org
   :altnames:   DNS:wiki.cacert.org
   :certfile:   /etc/ssl/public/wiki.cacert.org.crt
   :keyfile:    /etc/ssl/private/wiki.cacert.org.key
   :serial:     147C63
   :expiration: Feb 16 21:17:06 2022 GMT
   :sha1fp:     BC:42:64:D7:DB:1C:CB:C6:5B:FB:3D:60:43:10:11:2F:89:98:2E:F1
   :issuer:     CA Cert Signing Authority

:file:`/etc/ssl/certs/cacert.org.pem` CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for client certificates)
:file:`/etc/ssl/certs/cacert.org/` CAcert.org Class 1 certificate (certificate chain for server certificate)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache configuration
--------------------

Apache is configured using files in :file:`/etc/apache2` integrating the MoinMoin wiki using `mod_wsgi`.

.. todo:: more comprehensive Apache configuration documentation for wiki

Changes
=======

.. todo:: manage the blog system using Puppet

System Future
-------------

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

* No plans

References
----------

* http://moinmo.in/
* https://modwsgi.readthedocs.io/en/master/index.html
* http://httpd.apache.org/docs/2.4/
