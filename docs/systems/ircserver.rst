.. index::
   single: Systems; Ircserver

=========
Ircserver
=========

Purpose
=======

This system is the planned replacement for :doc:`irc`.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+--------------+---------------------+
| Application  | Administrator(s)    |
+==============+=====================+
| IRC server   | :ref:`people_jandd` |
+--------------+---------------------+
| IRC services | :ref:`people_jandd` |
+--------------+---------------------+
| Votebot      | :ref:`people_jandd` |
+--------------+---------------------+

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
   single: DNS records; Irc

======================= ======== ==========================================
Name                    Type     Content
======================= ======== ==========================================
irc.cacert.org.         IN A     213.154.225.233
irc.cacert.org.         IN SSHFP 1 1 C123F73001682277DE5346923518D17CC94E298E
irc.cacert.org.         IN SSHFP 2 1 B85941C077732F78BE290B8F0B44B0A5E8A0E51D
irc.intra.cacert.org.   IN A     172.16.2.14
======================= ======== ==========================================

.. todo:: setup new SSHFP records

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.4

* Debian GNU/Linux 9.4

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+--------------+---------+----------------------------+
| Port     | Service      | Origin  | Purpose                    |
+==========+==============+=========+============================+
| 22/tcp   | ssh          | ANY     | admin console access       |
+----------+--------------+---------+----------------------------+
| 25/tcp   | smtp         | local   | mail delivery to local MTA |
+----------+--------------+---------+----------------------------+
| 80/tcp   | http         | ANY     | redirect to https          |
+----------+--------------+---------+----------------------------+
| 443/tcp  | https        | ANY     | reverse proxy for kiwiirc  |
+----------+--------------+---------+----------------------------+
| 5666/tcp | nrpe         | monitor | remote monitoring service  |
+----------+--------------+---------+----------------------------+
| 6667/tcp | ircd         | ANY     | IRC                        |
+----------+--------------+---------+----------------------------+
| 7000/tcp | ircd         | ANY     | IRC (SSL)                  |
+----------+--------------+---------+----------------------------+
| 7001/tcp | ircd         | local   | IRC (services)             |
+----------+--------------+---------+----------------------------+
| 7778/tcp | kiwiirc      | local   | kiwiirc process            |
+----------+--------------+---------+----------------------------+
| 8080/tcp | irc-services | ANY     | IRC services               |
+----------+--------------+---------+----------------------------+

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
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
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
| kiwiirc            | IRC web client     | start script                           |
|                    |                    | :file:`/home/kiwiirc/KiwiIRC/kiwi`     |
|                    |                    | started by user kiwiirc                |
+--------------------+--------------------+----------------------------------------+
| nginx              | Reverse proxy for  | init script                            |
|                    | kiwiirc            | :file:`/etc/init.d/nginx`              |
+--------------------+--------------------+----------------------------------------+

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
   :RSA:     SHA256:MMH85BKVW7SUe7yyWjldjlggQD7dtXRuzO1XjZf0ZWc MD5:dc:8f:c3:d7:38:72:39:13:6f:97:db:3d:06:c6:83:db
   :DSA:     SHA256:c0pnKaB313x5rw6PRRh/iMJdfNECw0ruHnU9lkTJZbw MD5:52:73:d9:76:38:df:bd:18:37:4a:e3:9d:65:14:ac:39
   :ECDSA:   SHA256:uI+JjNUlGytuMVouJmhzdHt80jfA+SRYkWr5OORpT5Y MD5:61:9f:ca:c7:05:0e:46:a1:8f:6d:7f:3a:68:ce:5a:21
   :ED25519: SHA256:aNRLwh0FVQyKq2IWO5JXyFubzwpMqxyWrSymdLgDYBw MD5:79:2a:a2:ca:99:23:50:2c:1c:48:cf:8c:fe:b9:51:e5

Dedicated user roles
--------------------

+---------+-------------------------------------+
| User    | Purpose                             |
+=========+=====================================+
| votebot | used to run the votebot             |
+---------+-------------------------------------+
| kiwiirc | used to run the Kiwi IRC web client |
+---------+-------------------------------------+

Non-distribution packages and modifications
-------------------------------------------

Votebot
~~~~~~~

The :ref:`Votebot <votebot>` is a custom developed IRC daemon that is packaged
as a self contained Java jar archive. The bot is started manually as described
above. For improved maintainability it should be packaged and provide a start
mechanism that is better integrated with the system.

.. _votebot:

.. topic:: Votebot

   The vote bot is a Java based IRC bot developed at
   https://github.com/CAcertOrg/cacert-votebot. The bot is started manually by
   running

   .. code-block:: bash

      java -DvoteBot.meetingChn=SGM -cp VoteBot.jar \
        de.dogcraft.irc.CAcertVoteBot -u -h 10.0.0.14 -p 6667 --nick VoteBot

.. todo:: use a CAcert git repository for votebot

.. todo:: package votebot for Debian

.. todo:: provide a proper init script/and or systemd unit for votebot


Kiwi IRC
~~~~~~~~

Kiwi IRC is a nodejs based IRC web client. The software has been installed via
`Github <https://github.com/prawnsalad/KiwiIRC.git>`_ and npm as described in
https://kiwiirc.com/docs/installing and
https://kiwiirc.com/docs/installing/proxies. The software is running on the
local loopback interface and Internet access is provided by an nginx reverse
proxy that also provides https connectivity. NodeJS and npm have been installed
from Debian packages.

Risk assessments on critical packages
-------------------------------------

Votebot is a Java based application and therefore Java security patches should
be applied as soon as they become available.

Kiwi IRC is nodejs based and uses some third party npm packages. The
application is kept behind a reverse proxy but it is advisable to make sure
that available updates are applied.

.. todo:: implement some update monitoring for Kiwi IRC


Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: irc.cacert.org
   :altnames:   DNS:irc.cacert.org, DNS:ircserver.cacert.org
   :certfile:   /etc/ssl/public/irc.cacert.org.crt
   :keyfile:    /etc/ssl/private/irc.cacert.org.key
   :serial:     1381E8
   :expiration: Mar 16 09:35:36 2020 GMT
   :sha1fp:     42:F6:7C:4E:0C:AC:8A:42:7D:9A:94:55:7E:73:7E:E9:40:5C:87:91
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

Kiwi IRC configuration
----------------------

Kiwi IRC configuration is kept in :file:`/home/kiwiirc/KiwiIRC/config.js`. When
the configuration is changed it can be applied by running:

.. code-block:: bash

   sudo -s -u kiwi
   cd ~/KiwiIRC
   ./kiwi reconfig

nginx configuration
-------------------

The nginx configuration for reverse proxying Kiwi IRC is stored in
:file:`/etc/nginx/sites-available/default`. The same certificate and private
key are used for inspirced and nginx.


Tasks
=====

Planned
-------

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

Kiwi IRC documentation
   https://kiwiirc.com/docs/

nginx documentation
   http://nginx.org/en/docs/
