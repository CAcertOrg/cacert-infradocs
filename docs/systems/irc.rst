.. index::
   single: Systems; Irc

===
IRC
===

Purpose
=======

This system provides the CAcert IRC service for private communications,
allowing usage of CAcert-secured SSL-Encrypted IRC traffic for our everyday
chat, meetings, and general support.

Application Links
-----------------

https://irc.cacert.org/
   HTTPS secured Web based IRC access

http://irc.cacert.org/
   HTTP fallback for Web based IRC access

Administration
==============

System Administration
---------------------

* Primary: None
* Secondary: :ref:`people_mario`, :ref:`people_jandd`

Application Administration
--------------------------

+--------------+------------------+
| Application  | Administrator(s) |
+==============+==================+
| IRC server   | None             |
+--------------+------------------+
| IRC services | None             |
+--------------+------------------+
| IRC webchat  | None             |
+--------------+------------------+

.. todo::
   find an administrator willing to properly setup/maintain IRC applications
   and push the migration to :doc:`ircserver`.

Contact
-------

* irc-admin@cacert.org

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.233`
:IP Intranet: :ip:v4:`172.16.2.14`
:IP Internal: :ip:v4:`10.0.0.14`
:MAC address: :mac:`00:ff:8d:45:01:a4` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Irc

======================= ======== ==========================================
Name                    Type     Content
======================= ======== ==========================================
irc.cacert.org.         IN A     213.154.225.233
irc.cacert.org.         IN SSHFP 1 1 C123F73001682277DE5346923518D17CC94E298E
irc.cacert.org.         IN SSHFP 2 1 B85941C077732F78BE290B8F0B44B0A5E8A0E51D
irc.intra.cacert.org.   IN A     172.16.2.14
======================= ======== ==========================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.11

* Debian GNU/Linux 7.11

Applicable Documentation
------------------------

:wiki:`Technology/TechnicalSupport/EndUserSupport/IRC`

Services
========

Listening services
------------------

+----------+---------+---------+--------------------------------------+
| Port     | Service | Origin  | Purpose                              |
+==========+=========+=========+======================================+
| 22/tcp   | ssh     | ANY     | admin console access                 |
+----------+---------+---------+--------------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA           |
+----------+---------+---------+--------------------------------------+
| 80/tcp   | http    | ANY     | IRC webchat                          |
+----------+---------+---------+--------------------------------------+
| 443/tcp  | https   | ANY     | IRC webchat                          |
+----------+---------+---------+--------------------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service            |
+----------+---------+---------+--------------------------------------+
| 5432/tcp | pgsql   | local   | PostgreSQL database for IRC services |
+----------+---------+---------+--------------------------------------+
| 6667/tcp | ircd    | ANY     | IRC                                  |
+----------+---------+---------+--------------------------------------+
| 6668/tcp | ircd    | ANY     | IRC [#f1]_                           |
+----------+---------+---------+--------------------------------------+
| 7000/tcp | ircd    | ANY     | IRC                                  |
+----------+---------+---------+--------------------------------------+

ircd opens a random UDP port for some reason.

.. [#f1] Not forwarded from :doc:`infra02` to container

.. todo:: find out what the UDP port is used for

Running services
----------------

.. index::
   single: Postfix
   single: PostgreSQL
   single: cron
   single: lighttpd
   single: nrpe
   single: openssh
   single: oftc-hybrid-ircd

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| lighttpd           | Webserver for      | init script                            |
|                    | IRC webchat        | :file:`/etc/init.d/lighttpd`           |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for IRC services   |                                        |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| OFTC Hybrid IRCD   | IRC server         | start script                           |
|                    |                    | :file:`/home/ircserver/ircd/bin/ircd`  |
|                    |                    | started manually                       |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+------------+-------------+--------------+
| RDBMS      | Name        | Used for     |
+============+=============+==============+
| PostgreSQL | ircservices | IRC services |
+------------+-------------+--------------+

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
   :RSA:   6e:7c:14:4b:a3:fe:8c:88:1b:d0:e8:3c:93:9c:33:2f
   :DSA:   e7:92:a5:80:49:a9:fe:d3:57:11:1d:ca:b8:0f:c0:44
   :ECDSA: c5:6a:f5:cc:be:a5:94:03:b8:32:d0:97:ef:26:ac:35

Dedicated user roles
--------------------

+-----------+--------------+
| Group     | Purpose      |
+===========+==============+
| ircserver | IRC daemon   |
+-----------+--------------+
| services  | IRC services |
+-----------+--------------+

Non-distribution packages and modifications
-------------------------------------------

.. index::
   pair: non-distribution; oftc-ircd

OFTC Hybrid IRC daemon
......................

* The IRC server runs as a self compiled `OFTC Hybrid
  <http://www.oftc.net/CodingProjects/#ircd>`_ from upstream's `GitHub
  repository <https://github.com/oftc/oftc-hybrid>`_ at revision
  1435aa49a8b20d6ed816f53518ae5f22d0579cc4 (tag: oftc-hybrid-1.6.15).
* The configured source code is available in
  :file:`/home/ircserver/oftc-hybrid/`
* The installed ircd is in :file:`/home/ircserver/ircd/`
* The used configure options are contained in
  :file:`/home/ircserver/configline`

The IRC server is linked against system shared libraries and may not work
anymore if these are updated to ABI incompatible versions.

This is the listed of linked libraries as of 2014-10-24::

   $ ldd ircd/bin/ircd
           linux-gate.so.1 =>  (0xf7714000)
           libdl.so.2 => /lib/i386-linux-gnu/i686/cmov/libdl.so.2 (0xf7709000)
           libcrypt.so.1 => /lib/i386-linux-gnu/i686/cmov/libcrypt.so.1 (0xf76d7000)
           libssl.so.1.0.0 => /usr/lib/i386-linux-gnu/i686/cmov/libssl.so.1.0.0 (0xf767d000)
           libcrypto.so.1.0.0 => /usr/lib/i386-linux-gnu/i686/cmov/libcrypto.so.1.0.0 (0xf74bf000)
           libc.so.6 => /lib/i386-linux-gnu/i686/cmov/libc.so.6 (0xf735a000)
           /lib/ld-linux.so.2 (0xf7715000)
           libz.so.1 => /lib/i386-linux-gnu/libz.so.1 (0xf7341000) 

OFTC IRC services
.................

* The IRC services where self compiled `OFTC Services
  <http://www.oftc.net/CodingProjects/#services>`_ from upstreams `release
  tarballs <http://www.oftc.net/releases/oftc-ircservices/>`_ unfortunatelly
  recompilation on the current Debian system does not produce a working binary.
* The configured source code is available at
  :file:`/home/services/oftc-services-1.5.8/`
* The installed disfunctional IRC services are installed in
  :file:`/home/services/services`
* The used configure options are contained in :file:`/home/services/configline`

.. warning::
   There are no services running currently because loading the PostgreSQL
   driver leads to a segmentation fault in the compiled binaries.

IRC Webchat
...........

* The used Web based IRC software is a self compiled `CGI:IRC
  <http://cgiirc.sourceforge.net/>`_ version 0.5.9
* The Web based IRC software is contained in :file:`/var/cgi/`

Risk assessments on critical packages
-------------------------------------

The self compiled binaries of OFTC Hybrid ircd, OFTC Services and IRC webchat
are not updated regularly. There is no administrator with good enough knowledge
for these applications to properly maintain these.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: irc.cacert.org
   :altnames:   DNS:cert.irc.cacert.org, DNS:irc.cacert.org, DNS:nocert.irc.cacert.org
   :certfile:   /home/ircserver/ssl/cert.pem
   :keyfile:    /home/ircserver/ssl/rsa.key
   :serial:     11E863
   :expiration: Mar 31 20:31:00 18 GMT
   :sha1fp:     04:EF:FE:61:44:9F:74:AB:C0:D3:5E:F4:D9:48:59:B5:B0:23:27:B2
   :issuer:     CA Cert Signing Authority

.. sslcert:: irc.cacert.org
   :certfile:   /etc/lighttpd/ssl/server.pem
   :keyfile:    /etc/lighttpd/ssl/server.pem
   :serial:     11E863
   :secondary:

The :file:`/etc/lighttpd/ssl/server.pem` is a combined key and certificate file
for lighttpd.

.. index::
   pair: lighttpd; configuration

lighttpd configuration
----------------------

* :file:`/etc/lighttpd/conf-enabled/10-cgi.conf` CGI path configuration
* :file:`/etc/lighttpd/conf-enabled/10-ssl.conf` TLS configuration

.. todo:: add more details

.. index::
   pair: oftc-hybrid-ircd; configuration
   pair: ircd; configuration

oftc-hybrid-ircd configuration
------------------------------

* :file:`/home/ircserver/ircd/etc/ircd.conf` main IRC server configuration,
  defining settings, ports and TLS settings

.. todo:: add more details
.. todo::
   there are a lot of ops users defined in :file:`ircd.conf` check whether
   these are still valid

.. index::
   pair: IRC webchat; configuration

IRC webchat configuration
-------------------------

* :file:`/var/cgi/cgiirc.config`

.. todo:: add more details

Potentially obsolete configuration
----------------------------------

There are some directories in :file:`/etc/` that contain seemingly unused
configuration files:

* :file:`/etc/irc/`
* :file:`/etc/oftc-hybrid/`

There is also a half-uninstalled package :program:`ircd-hybrid` whose config
files are partially still available (:file:`/etc/default/ircd-hybrid` and
:file:`/etc/logrotate.d/ircd-hybrid`)

Changes
=======

System Future
-------------

This system should be retired and replaced with the new :doc:`ircserver` that
should be running packaged and properly supported software.

.. note::

   Current Debian releases contain packaged versions of some ircd/irc services
   combinations:

      * `ircd-hybrid <https://packages.debian.org/jessie/ircd-hybrid>`_ similar
        to the current software
      * `charybdis <https://packages.debian.org/jessie/charybdis>`_ with
        `atheme-services <https://packages.debian.org/jessie/atheme-services>`_
        (compatible with ircd-hybrid too)
      * `ircd-ratbox <https://packages.debian.org/jessie/ircd-ratbox>`_ with
        `ratbox-services
        <https://packages.debian.org/jessie/ratbox-services-pgsql>`_ used by
        EFNet

   CGI:IRC has been removed from Debian because it had no active maintainer.
