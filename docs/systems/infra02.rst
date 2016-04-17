.. index::
   single: Systems; Infra02

=======
Infra02
=======

Purpose
=======

The infrastructure host system Infra02 is a dedicated physical machine for the
CAcert infrastructure.

.. index::
   single: LXC
   single: Ferm

Infra02 is the host system for all infrastructure containers. The containers
are setup using the Linux kernel's LXC_ system. The firewall for infrastructure
is maintained on this machine using Ferm_.

.. _LXC: https://linuxcontainers.org/
.. _Ferm: http://ferm.foo-projects.org/

Administration
==============

System Administration
---------------------

* Primary: `Jan Dittberner`_
* Secondary: `Mario Lipinski`_

.. _Jan Dittberner: jandd@cacert.org
.. _Mario Lipinski: mario@cacert.org

Contact
-------

* infrastructure-admin@cacert.org

Basics
======

Physical Location
-----------------

The machine is located in a server rack at BIT B.V. in the Netherlands.

Physical Configuration
----------------------

The machine has been sponsored by Thomas Krenn and has the following hardware
parameters:

:Mainboard: Supermicro X9SCL/X9SCM Version 1.11A
:CPU: Intel(R) Xeon(R) CPU E3-1240 V2 @ 3.40GHz
:RAM: 16 GiB ECC
:Disks: 2 x 1TB WDC WD1003FBYX-01Y7B1
:NIC:

  * eth0 Intel Corporation 82579LM Gigabit Network Connection
  * eth1 Intel Corporation 82574L Gigabit Network Connection

There is a 2 TB USB backup disk attached to the system.

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/EquipmentList

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.230`
:IP Intranet: :ip:v4:`172.16.2.10`
:IP internal: :ip:v4:`10.0.0.1`
:IPv6: :ip:v6:`2001:7b8:616:162:1::10`
:IPv6 on br0: :ip:v6:`2001:7b8:616:162:2::10`
:MAC address:

  * :mac:`00:25:90:a9:66:e9` (eth0)
  * :mac:`fe:0e:ee:75:a3:a5` (br0)

.. seealso::

   :doc:`network`.

DNS
---

* infrastructure.cacert.org. IN A 213.154.225.230
* infrastructure.cacert.org. IN SSHFP 1 1 5A82D3C150AF002C05784F73250A067053AEED63
* infrastructure.cacert.org. IN SSHFP 1 2 63B0D74A3F1CE61865A5EB0497EF05243BC4067EC983C69AB8E62F3CB940CC82
* infrastructure.cacert.org. IN SSHFP 2 1 AF8D8E3386EAA72997709632ADF2B457E6FEF0DC
* infrastructure.cacert.org. IN SSHFP 2 2 3A0188FC47D1FDD14D70A2FB78F51792D06BA11EAE6AB16E73CB7BB8DD6A0DC8
* infrastructure.cacert.org. IN SSHFP 3 1 3E1B9EBF85B726CF831C76ECB8C17786AEDF40E8
* infrastructure.cacert.org. IN SSHFP 3 2 3AE7F0035C2172977E99BFE312C7A8299650DEA16A975EA13EECE8FDA426062A
* infra02.intra.cacert.org. IN A 172.16.2.10

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/Procedures/DNSChanges

Operating System
----------------

* Debian GNU/Linux 7.10

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 123/udp  | ntp       | ANY       | network time protocol for host,         |
|          |           |           | listening on the Internet IPv6 and IPv4 |
|          |           |           | addresses                               |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

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
| ntpd               | time server        | init script :file:`/etc/init.d/ntp`    |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission, ...    |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

.. Running Guests
   --------------

   .. some directive to list guests here

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`emailout`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates

Security
========

SSH host keys
-------------

+-----------+-----------------------------------------------------+
| Algorithm | Fingerprint                                         |
+===========+=====================================================+
| RSA       | ``86:d5:f8:71:2e:ab:5e:50:5d:f6:37:6b:16:8f:d1:1c`` |
+-----------+-----------------------------------------------------+
| DSA       | ``b4:fb:c2:74:33:eb:cc:f0:3e:31:38:c9:a8:df:0a:f5`` |
+-----------+-----------------------------------------------------+
| ECDSA     | ``79:c4:b8:ff:ef:c9:df:9a:45:07:8d:ab:71:7c:e9:c0`` |
+-----------+-----------------------------------------------------+
| ED25519   | ``25:d1:c7:44:1c:38:9e:ad:89:32:c7:9c:43:8e:41:c4`` |
+-----------+-----------------------------------------------------+

.. seealso::

   See :doc:`sshkeys`

Dedictated user roles
---------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments and critical packages
--------------------------------------

The system is the basis for all other infrastructure systems. Access to this
system has to be tightly controlled.

Tasks
=====

.. todo:: find out why the system logs are messed up
.. todo:: upgrade to Debian Jessie
.. todo:: document whether it is safe to reboot this system
.. todo:: document how to setup a new container
.. todo:: document how to setup firewall rules/forwarding
.. todo:: document how the backup system works

Planned
-------

* None

Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * https://wiki.cacert.org/PostfixConfiguration
