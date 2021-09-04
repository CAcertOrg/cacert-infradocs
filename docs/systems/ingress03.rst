.. index::
   single: Systems; Ingress03

=========
Ingress03
=========

Purpose
=======

This system provides an incoming IPv4 TLS and HTTP proxy using `nginx`_ to
share one public IPv4 address for multiple services on :doc:`infra03`.

.. _nginx: https://nginx.org/

Application Links
-----------------

No direct links, applications run on other systems.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| nginx       | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* ingress03-admin@cacert.org

Additional People
-----------------

No other people have :program:`sudo` access on that machine.

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
:IP Internal: :ip:v4:`10.0.3.10`
:IPv6:        :ip:v6:`2001:7b8:616:162:3::10`
:MAC address: :mac:`00:ff:8f:34:8c:dd` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Ingress03

Monitoring
----------

:internal checks: :monitor:`ingress03.infra.cacert.org`
:external checks: :monitor:`ingress03.cacert.org`

DNS
---

.. index::
   single: DNS records; Ingress03

+-----------------------+---------+------------------------+
| Name                  | Type    | Content                |
+=======================+=========+========================+
| ingress03.cacert.org. | IN A    | 213.154.225.249        |
+-----------------------+---------+------------------------+
| ingress03.cacert.org. | IN AAAA | 2001:7b8:616:162:3::10 |
+-----------------------+---------+------------------------+

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
| 80/tcp   | http    | ANY     | nginx reverse proxy        |
+----------+---------+---------+----------------------------+
| 443/tcp  | https   | ANY     | nginx SNI proxy            |
+----------+---------+---------+----------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+
| 465/udp  | syslog  | local   | syslog port                |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: nginx
   single: openssh
   single: puppet
   single: rsyslog

+----------------+---------------------------------------+----------------------------------+
| Service        | Usage                                 | Start mechanism                  |
+================+=======================================+==================================+
| cron           | job scheduler                         | systemd unit ``cron.service``    |
+----------------+---------------------------------------+----------------------------------+
| dbus-daemon    | System message bus                    | systemd unit ``dbus.service``    |
+----------------+---------------------------------------+----------------------------------+
| Exim           | SMTP server for local mail submission | systemd unit ``exim4.service``   |
+----------------+---------------------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent              | systemd unit ``icinga2.service`` |
+----------------+---------------------------------------+----------------------------------+
| openssh server | ssh daemon for remote administration  | systemd unit ``ssh.service``     |
+----------------+---------------------------------------+----------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``  |
+----------------+---------------------------------------+----------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service`` |
+----------------+---------------------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA:     SHA256:EhpGxNuCNirP/I/e9A85p7M1xe7PuQej4jrNJBSsTAg MD5:b9:df:fb:fb:4e:8e:34:e4:6a:5d:e7:18:bb:5c:43:82
   :ECDSA:   SHA256:o7ACxl0hkiYobV+gmnrV3eaF09dttdh69K2T6bkO7jE MD5:a9:c3:df:2a:13:38:14:ad:a6:15:f4:ff:4b:5e:75:2d
   :ED25519: SHA256:HA8qzC8T62WpiAHt6IClWxwhp2hpg9CjJucPPKyPvUw MD5:92:00:a9:29:5b:c0:42:da:d8:8e:3b:9a:c2:cf:41:bb

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There is no
configuration items outside of the :cacertgit:`cacert-puppet`.

Tasks
=====

Adding a new forward entry
--------------------------

Add an entry to the ``profiles::sniproxy::forwarded`` item in
:file:`hieradata/nodes/ingress03.yaml` in :cacertgit:`cacert-puppet` and adjust
the firewall configuration on :doc:`infra03`. You will need to request DNS
changes from the critical team if you want to switch an existing service to use
the SNI proxy service.

Changes
=======

Planned
-------

* None

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* https://nginx.org/en/docs/
