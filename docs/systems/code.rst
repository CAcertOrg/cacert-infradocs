.. index::
   single: Systems; code

====
Code
====

Purpose
=======

The system provides a Gitea instance for hosting CAcert code. It will replace
:doc:`git` and probably :doc:`svn`.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: none

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| PostgreSQL  | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* code-admin@cacert.org

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
:IP Internal: :ip:v4:`10.0.3.15`
:IPv6:        :ip:v6:`2001:7b8:616:162:3::15`
:MAC address: :mac:`00:ff:8f:61:e0:32` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; code

Monitoring
----------

:internal checks: :monitor:`code.infra.cacert.org`
:external checks: :monitor:`code.cacert.org`

DNS
---

.. index::
   single: DNS records; code

+------------------------+---------+------------------------+
| Name                   | Type    | Content                |
+========================+=========+========================+
| code.infra.cacert.org. | IN A    | 10.0.3.15              |
+------------------------+---------+------------------------+
| code.infra.cacert.org. | IN AAAA | 2001:7b8:616:162:3::15 |
+------------------------+---------+------------------------+

.. todo:: add DNS records for code

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Bullseye
   single: Debian GNU/Linux; 11.2

* Debian GNU/Linux 11.2

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
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: cron
   single: exim4
   single: icinga2
   single: openssh
   single: puppet
   single: rsyslog

+----------------+---------------------------------------+----------------------------------+
| Service        | Usage                                 | Start mechanism                  |
+================+=======================================+==================================+
| cron           | job scheduler                         | systemd unit ``cron.service``    |
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
* :doc:`pgsql` as PostgreSQL database server

Security
========

.. sshkeys::
   :ECDSA:   SHA256:VOQv2awhDNa9PsHKdbgL9FhetHYGpAtGJ9GRbzVdy58 MD5:1d:bd:66:b3:07:60:32:20:db:67:1c:31:b2:46:59:09
   :ED25519: SHA256:zOA6Jk7EuUfUow3cK4b+gPxz1R91G6qDT/HshIGBuOs MD5:e2:fa:ed:f4:e9:c7:e4:9a:ae:cb:af:01:86:8a:12:44
   :RSA:     SHA256:NMyZblaN2+kzVPKEpSvWBgI5Wg4fy4d3DhkPvJfdnOc MD5:18:d1:56:0c:6c:f0:3c:53:2f:94:09:b9:cb:fe:15:80

Non-distribution packages and modifications
-------------------------------------------

The Puppet agent packages and a few dependencies are installed from the
official Puppet APT repository because the versions in Debian are too old to
use modern Puppet features.

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

.. todo:: manage Gitea and configuration in Puppet code

Changes
=======

Nothing planned.

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
   * https://docs.gitea.io/
