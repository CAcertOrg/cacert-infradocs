Infra02
=======

The infrastructure host system Infra02 is a dedicated machine for the CAcert
infrastructure. The machine has been sponsored by Thomas Krenn and has the
following hardware parameters:

:Mainboard: Supermicro X9SCL/X9SCM Version 1.11A
:CPU: Intel(R) Xeon(R) CPU E3-1240 V2 @ 3.40GHz
:RAM: 16 GiB ECC
:Disks: 2 x 1TB WDC WD1003FBYX-01Y7B1
:NIC:

  * eth0 Intel Corporation 82579LM Gigabit Network Connection
  * eth1 Intel Corporation 82574L Gigabit Network Connection

There is a 2 TB USB backup disk attached to the system

Infra02 is the host system for all infrastructure containers. The containers
are setup using the Linux kernel's LXC_ system.

.. _LXC: https://linuxcontainers.org/

