.. index::
   single: Systems; mariadb

=======
MariaDB
=======

Purpose
=======

The system provides a central MariaDB database server for other CAcert
infrastructure services.

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
| mariadb     | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* mariadb-admin@cacert.org

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra03`.

Logical Location
----------------

:IP Internal: :ip:v4:`10.0.3.11`
:IPv6:        :ip:v6:`2001:7b8:616:162:3::11`
:MAC address: :mac:`00:ff:8f:bc:23:47` (eth0@if12)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; mariadb

Monitoring
----------

:internal checks: :monitor:`mariadb.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; mariadb

+---------------------------+---------+------------------------+
| Name                      | Type    | Content                |
+===========================+=========+========================+
| mariadb.cacert.org.       | IN AAAA | 2001:7b8:616:162:3::11 |
+---------------------------+---------+------------------------+
| mariadb.infra.cacert.org. | IN A    | 10.0.3.11              |
+---------------------------+---------+------------------------+
| mariadb.infra.cacert.org. | IN AAAA | 2001:7b8:616:162:3::11 |
+---------------------------+---------+------------------------+

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
| 3306/tcp | mariadb | infra   | mariadb database service   |
+----------+---------+---------+----------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: mariadb
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
| mariadb        | MariaDB database server               | systemd unit ``mariadb.service`` |
+----------------+---------------------------------------+----------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``  |
+----------------+---------------------------------------+----------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service`` |
+----------------+---------------------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`nextcloud` Nextcloud service

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA: SHA256:BAoKSGc5ri54/upuMwCAIZbSaOqAGTnLPAavMcNOoRA MD5:36:fc:66:82:dc:94:3b:e3:50:97:83:fc:5a:5e:36:61
   :ECDSA: SHA256:q2d/j0gU2/akCdqYz6o1dS5gP1gh6JMI5msIbeR8k3Q MD5:ea:64:f2:2e:6d:39:a0:61:6d:b2:07:ba:db:17:5c:81
   :ED25519: SHA256:6jpSzqsnKON8WrgimzmRBeMhOj23WfTHdB9Nh9FCr5I MD5:04:1a:a8:a9:29:c4:67:8b:68:3d:40:55:fc:0d:7b:39

Non-distribution packages and modifications
-------------------------------------------

None

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

.. todo:: manage mariadb configuration in Puppet code

Tasks
=====

Adding new databases
--------------------

Database setup should be coordinated via mariadb-admin@cacert.org.

Changes
=======

Nothing planned.

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
