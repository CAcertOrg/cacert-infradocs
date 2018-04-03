.. index::
   single: Systems; Ircserver

=========
Ircserver
=========

Purpose
=======

This system provides the CAcert IRC service for private communications,
allowing usage of CAcert-secured SSL-Encrypted IRC traffic for our everyday
chat, meetings, and general support.

Application Links
-----------------

https://irc.cacert.org/
   HTTPS secured Web based IRC access

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
:IP Intranet: :ip:v4:`172.16.2.14`
:IP Internal: :ip:v4:`10.0.0.130`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::14`
:MAC address: :mac:`00:ff:9a:79:ca:b1` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Ircserver
   single: DNS records; Irc

=========================== ======== ====================================================================
Name                        Type     Content
=========================== ======== ====================================================================
irc.cacert.org.             IN A     213.154.225.233
irc.cacert.org.             IN AAAA  2001:7b8:616:162:2::14
irc.cacert.org.             IN SSHFP 1 1 39b6c81b9fe76bd3c112f891ad3198f7a6102f4c
irc.cacert.org.             IN SSHFP 1 2 30c1fce412955bb4947bbcb25a395d8e5820403eddb5746ecced578d97f46567
irc.cacert.org.             IN SSHFP 2 1 90fcff63476f93d5e4f5d634ba1407445323d3fe
irc.cacert.org.             IN SSHFP 2 2 734a6729a077d77c79af0e8f45187f88c25d7cd102c34aee1e753d9644c965bc
irc.cacert.org.             IN SSHFP 3 1 5b9191613e743082fd4aa64e1f3a4601ed77f366
irc.cacert.org.             IN SSHFP 3 2 b88f898cd5251b2b6e315a2e266873747b7cd237c0f92458916af938e4694f96
irc.cacert.org.             IN SSHFP 4 1 866a42ee920b7f38a86ca9f3b07af808aae9768c
irc.cacert.org.             IN SSHFP 4 2 68d44bc21d05550c8aab62163b9257c85b9bcf0a4cab1c96ad2ca674b803601c
ircserver.intra.cacert.org. IN A     172.16.2.14
=========================== ======== ====================================================================

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

Running services
----------------

.. index::
   single: atheme-services
   single: cron
   single: exim
   single: inspircd
   single: kiwiirc
   single: nginx
   single: nrpe
   single: openssh
   single: puppet agent
   single: rsyslog
   single: votebot

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| atheme-services    | IRC services       | init script                            |
|                    |                    | :file:`/etc/init.d/atheme-services`    |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| inspircd           | IRC daemon         | init script                            |
|                    |                    | :file:`/etc/init.d/inspircd`           |
+--------------------+--------------------+----------------------------------------+
| kiwiirc            | IRC web client     | start script                           |
|                    |                    | :file:`/home/kiwiirc/KiwiIRC/kiwi`     |
|                    |                    | started by user kiwiirc                |
+--------------------+--------------------+----------------------------------------+
| nginx              | Reverse proxy for  | init script                            |
|                    | kiwiirc            | :file:`/etc/init.d/nginx`              |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Puppet agent       | configuration      | init script                            |
|                    | management agent   | :file:`/etc/init.d/puppet`             |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| votebot            | CAcert vote bot    | init script (spring-boot)              |
|                    |                    | :file:`/etc/init.d/cacert-votebot`     |
+--------------------+--------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
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

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Votebot
~~~~~~~

The :ref:`Votebot <votebot>` is a custom developed IRC daemon that is packaged
as a self contained executable Spring-Boot jar archive. The bot is started via
init.

.. _votebot:

.. topic:: Votebot

   The vote bot is a Java based IRC bot developed at
   https://git.cacert.org/gitweb/?p=cacert-votebot.git and built at
   https://jenkins.cacert.org/job/cacert-votebot/. The bot is started
   automatically via its init script.

Kiwi IRC
~~~~~~~~

Kiwi IRC is a nodejs based IRC web client. The software has been installed via
`Github <https://github.com/prawnsalad/KiwiIRC.git>`_ and npm as described in
https://kiwiirc.com/docs/installing and
https://kiwiirc.com/docs/installing/proxies. The software is running on the
local loopback interface and Internet access is provided by an nginx reverse
proxy that also provides https connectivity. NodeJS and npm have been installed
from Debian packages.

.. todo:: setup init script for kiwiirc

Risk assessments on critical packages
-------------------------------------

Votebot is a Java based application and therefore Java security patches should
be applied as soon as they become available.

Kiwi IRC is nodejs based and uses some third party npm packages. The
application is kept behind a reverse proxy but it is advisable to make sure
that available updates are applied.

.. todo:: implement some update monitoring for Kiwi IRC

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

.. todo:: move configuration of :doc:`ircserver` to Puppet code

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

.. index::
   pair: Kiwi IRC; configuration

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

votebot configuration
---------------------

Votebot is configured via spring-boot mechanisms. The current configuration file
is :file:`/home/votebot/cacert-votebot-0.1.0-SNAPSHOT.conf` and configures
Votebot to connect to localhost as VoteBot. The bot uses the channels #agm and
#vote. Channels could be changed in an :file:`application.properties` file in
:file:`/home/votebot`. The available property names can be found in the `git
repository`_.

.. _git repository: https://git.cacert.org/gitweb/?p=cacert-votebot.git;a=blob;f=src/main/resources/application.properties

Tasks
=====

Planned
-------

- None

Changes
=======

- Nothing planned

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
