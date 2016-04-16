=======
Infra02
=======

Basics
======

Purpose
-------

The infrastructure host system Infra02 is a dedicated machine for the CAcert
infrastructure.

Infra02 is the host system for all infrastructure containers. The containers
are setup using the Linux kernel's LXC_ system. The firewall for infrastructure
is maintained on this machine using Ferm_.

.. _LXC: https://linuxcontainers.org/
.. _Ferm: http://ferm.foo-projects.org/

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

There is a 2 TB USB backup disk attached to the system

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

