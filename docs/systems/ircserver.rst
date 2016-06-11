.. index::
   single: Systems; Ircserver

=========
Ircserver
=========

Purpose
=======

This system is the planned replacement for :doc:`irc`

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_martin`
* Secondary: None

Application Administration
--------------------------

+--------------+----------------------+
| Application  | Administrator(s)     |
+==============+======================+
| IRC server   | :ref:`people_martin` |
+--------------+----------------------+
| IRC services | :ref:`people_martin` |
+--------------+----------------------+
| Votebot      | :ref:`people_martin` |
+--------------+----------------------+

Contact
-------

* ircserver-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd` has :program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.233`
:IP Intranet: :ip:v4:`172.16.2.24`
:IP Internal: :ip:v4:`10.0.0.130`
:MAC address: :mac:`00:ff:9a:79:ca:b1` (eth0)

.. todo:: setup IPv6

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Ircserver

Ircserver has no DNS records assigned yet.

.. todo:: setup DNS records

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.5

* Debian GNU/Linux 8.5

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+---------------+--------------+---------+----------------------------+
| Port          | Service      | Origin  | Purpose                    |
+===============+==============+=========+============================+
| 22/tcp        | ssh          | ANY     | admin console access       |
+---------------+--------------+---------+----------------------------+
| 25/tcp        | smtp         | local   | mail delivery to local MTA |
+---------------+--------------+---------+----------------------------+
| 5666/tcp      | nrpe         | monitor | remote monitoring service  |
+---------------+--------------+---------+----------------------------+
| 6660-6669/tcp | ircd         | ANY     | IRC                        |
+---------------+--------------+---------+----------------------------+
| 6697/tcp      | ircd         | ANY     | IRC (SSL)                  |
+---------------+--------------+---------+----------------------------+
| 7000/tcp      | ircd         | ANY     | IRC (SSL)                  |
+---------------+--------------+---------+----------------------------+
| 7001/tcp      | ircd         | local   | IRC (servers)              |
+---------------+--------------+---------+----------------------------+
| 8080/tcp      | irc-services | ANY     | IRC services               |
+---------------+--------------+---------+----------------------------+

irc opens a random UDP port.

The following port forwarding is setup on :doc:`infra02`

+-------------+-------+-----------------+
| Intranet IP | Port  | Target          |
+=============+=======+=================+
| 172.16.2.14 | 13022 | 10.0.0.130:22   |
+-------------+-------+-----------------+
| 172.16.2.14 | 13080 | 10.0.0.130:80   |
+-------------+-------+-----------------+
| 172.16.2.14 | 13443 | 10.0.0.130:443  |
+-------------+-------+-----------------+
| 172.16.2.14 | 13667 | 10.0.0.130:6667 |
+-------------+-------+-----------------+
| 172.16.2.14 | 13700 | 10.0.0.130:7000 |
+-------------+-------+-----------------+

Ports 80 and 443 are not used yet but are planned for an IRC web chat system.

.. todo:: implement final forwarding to required ports from :doc:`infra02`

Running services
----------------

.. index::
   single: cron
   single: exim
   single: nrpe
   single: openssh
   single: inspircd
   single: atheme-services
   single: votebot

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+
| inspircd           | IRC daemon         | init script                            |
|                    |                    | :file:`/etc/init.d/inspircd`           |
+--------------------+--------------------+----------------------------------------+
| atheme-services    | IRC services       | init script                            |
|                    |                    | :file:`/etc/init.d/atheme-services`    |
+--------------------+--------------------+----------------------------------------+
| votebot            | CAcert vote bot    | started from a screen session via      |
|                    |                    | java command line                      |
+--------------------+--------------------+----------------------------------------+

.. _votebot:

.. topic:: Votebot

   The vote bot is a Java based IRC bot developed at
   https://github.com/CAcertOrg/cacert-votebot. The bot is started manually by
   running

   .. code-block:: bash

      java -DvoteBot.meetingChn=SGM -cp VoteBot.jar \
        de.dogcraft.irc.CAcertVoteBot -u -h 10.0.0.14 -p 6667 --nick VoteBot

.. todo:: use a CAcert git repository for votebot

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

Security
========

.. sshkeys::
   :RSA:   dc:8f:c3:d7:38:72:39:13:6f:97:db:3d:06:c6:83:db
   :DSA:   52:73:d9:76:38:df:bd:18:37:4a:e3:9d:65:14:ac:39
   :ECDSA: 61:9f:ca:c7:05:0e:46:a1:8f:6d:7f:3a:68:ce:5a:21

Dedicated user roles
--------------------

+---------+-------------------------+
| User    | Purpose                 |
+=========+=========================+
| votebot | used to run the votebot |
+---------+-------------------------+

Non-distribution packages and modifications
-------------------------------------------

The :ref:`Votebot <votebot>` is a custom developed IRC daemon that is packaged
as a self contained Java jar archive. The bot is started manually as described
above. For improved maintainability it should be packaged and provide a start
mechanism that is better integrated with the system.

.. todo:: package votebot for Debian

.. todo:: provide a proper init script/and or systemd unit for votebot

Risk assessments on critical packages
-------------------------------------

Votebot is a Java based application and therefore Java security patches should
be applied as soon as they become available.


Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: irc.cacert.org
   :altnames:   DNS:irc.cacert.org, DNS:ircserver.cacert.org
   :certfile:   /etc/ssl/public/irc.cacert.org.crt
   :keyfile:    /etc/ssl/private/irc.cacert.org.key
   :serial:     0FBBE0
   :expiration: Oct 22 15:27:04 16 GMT
   :sha1fp:     82:F7:B8:08:FB:FD:C3:FA:21:6C:89:B7:07:69:3D:66:F8:BC:5F:AA
   :issuer:     CA Cert Signing Authority


.. index::
   pair: inspircd; configuration

inspircd configuration
----------------------

Inspircd is installed from a Debian package. It is configured via files in
:file:`/etc/inspircd/`. The main configuration file is :file:`inspircd.conf`.

.. index::
   pair: atheme-services; configuration

atheme-services configuration
-----------------------------

Atheme-services is installed from a Debian package. It is configured via
:file:`/etc/atheme/atheme.conf`.

Tasks
=====

Planned
-------

.. todo:: finish setup of inspircd and atheme-services (at least nickserv and chanserv).

.. todo:: setup replacement for CGI::IRC that is available on :doc:`irc`

- setup IPv6
- setup DNS records

Changes
=======

System Future
-------------

- replace :doc:`irc` by this system

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
   * :wiki:`Technology/TechnicalSupport/EndUserSupport/IRC`

References
----------

Atheme services website
   https://atheme.github.io/atheme.html

Inspircd wiki
   https://wiki.inspircd.org/
