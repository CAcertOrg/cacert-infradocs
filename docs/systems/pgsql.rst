.. index::
   single: Systems; postgresql

==========
PostgreSQL
==========

Purpose
=======

The system provides a central PostgreSQL database server for other CAcert
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
| PostgreSQL  | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* pgsql-admin@cacert.org

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra03`.

Logical Location
----------------

:IP Internal: :ip:v4:`10.0.3.13`
:IPv6:        :ip:v6:`2001:7b8:616:162:3::13`
:MAC address: :mac:`00:ff:8f:1a:43:b5` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; pgsql

Monitoring
----------

:internal checks: :monitor:`pgsql.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; pgsql

+-------------------------+------+-----------+
| Name                    | Type | Content   |
+=========================+======+===========+
| pgsql.infra.cacert.org. | IN A | 10.0.3.13 |
+-------------------------+------+-----------+

.. todo:: add DNS records for pgsql

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

+----------+------------+---------+-----------------------------+
| Port     | Service    | Origin  | Purpose                     |
+==========+============+=========+=============================+
| 22/tcp   | ssh        | ANY     | admin console access        |
+----------+------------+---------+-----------------------------+
| 25/tcp   | smtp       | local   | mail delivery to local MTA  |
+----------+------------+---------+-----------------------------+
| 5432/tcp | postgresql | infra   | PostgreSQL database service |
+----------+------------+---------+-----------------------------+
| 5665/tcp | icinga2    | monitor | remote monitoring service   |
+----------+------------+---------+-----------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: openssh
   single: postgresql
   single: puppet
   single: rsyslog

+----------------+---------------------------------------+-------------------------------------+
| Service        | Usage                                 | Start mechanism                     |
+================+=======================================+=====================================+
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
| PostgreSQL     | central PostgreSQL database service   | systemd unit ``postgresql.service`` |
+----------------+---------------------------------------+-------------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``     |
+----------------+---------------------------------------+-------------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service``    |
+----------------+---------------------------------------+-------------------------------------+

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
   :ECDSA:   SHA256:kObv0Q2Z4I5tIAJhzbiz5nmJIct+jUSg//oqq+XzHoE MD5:84:a5:2d:83:ed:7d:da:0a:d6:a2:6c:af:ac:83:bd:49
   :ED25519: SHA256:QxmSn/fC3Q7cxp0f7CuPZgc329G6jUn3GdrdrOtNCNE MD5:cb:3b:05:4b:5a:97:7e:7b:9d:b1:6a:0d:ef:12:7b:aa
   :RSA:     SHA256:tMpaVFpoAeI8L3UZOsO9pl41JHUM1YjvijpwkQTuAfU MD5:7f:36:2e:f9:7b:ec:b2:41:4e:44:17:4e:94:87:04:09

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

.. todo:: manage PostgreSQL server configuration in Puppet code

Tasks
=====

Adding new databases
--------------------

Database setup should be coordinated via pgsql-admin@cacert.org.

Changes
=======

Nothing planned.

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
   * https://www.postgresql.org/docs/13/index.html
