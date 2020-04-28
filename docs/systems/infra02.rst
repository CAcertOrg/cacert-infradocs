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
   single: Ferm

Infra02 is the host system for all infrastructure :term:`containers
<Container>`. The containers are setup using the Linux kernel's :term:`LXC`
system. The firewall for infrastructure is maintained on this machine using
Ferm_. The machine provides a DNS resolver based on dnsmasq_ and gives answers
for the internal zone infra.cacert.org.

.. _Ferm: http://ferm.foo-projects.org/
.. _dnsmasq: http://www.thekelleys.org.uk/dnsmasq/doc.html

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: :ref:`people_mario`

Contact
-------

* infrastructure-admin@cacert.org

Additional People
-----------------

:ref:`people_wytze` and :ref:`people_mendel` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

The machine is located in a server rack at BIT B.V. in the Netherlands.

Physical Configuration
----------------------

The machine has been sponsored by `Thomas Krenn`_ and has the following hardware
parameters:

:Mainboard: Supermicro X9SCL/X9SCM Version 1.11A
:CPU: Intel(R) Xeon(R) CPU E3-1240 V2 @ 3.40GHz (4 Cores, 8 Threads)
:RAM: 16 GiB ECC
:Disks: 2 x 1TB WDC WD1003FBYX-01Y7B1
:NIC:

  * eth0 Intel Corporation 82579LM Gigabit Network Connection
  * eth1 Intel Corporation 82574L Gigabit Network Connection

There is a 2 TB USB WDC WD20EARS-00MVWB0 backup disk attached to the system.

.. seealso::

   See :wiki:`SystemAdministration/EquipmentList`

.. _Thomas Krenn: https://www.thomas-krenn.com/

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

   See :doc:`../network`

.. index::
   single: Monitoring; Infra02

Monitoring
----------

:internal checks: :monitor:`infra02.infra.cacert.org`
:external checks: :monitor:`infra02.cacert.org`

Remote Console
--------------

This system can be managed through a remote console, which may especially be
important during system upgrades and/or reboots.

The hardware of the system is equipped with a BMC Controller which supports the
Intelligent Platform Management Interface (IMPI).

Due the security design of the CAcert intranet, the network interface of this BMC
is not connected to the publicly reachable part of the CAcert intranet,
but rather to the management part, and is thus only reachable by members of the
critical system administrator team.

So the following instructions only apply to them.

The BMC interface can be reached from your local admin machine through the
CAcert hopper by setting up the following SSH port forwarding:

.. code:: bash

   IPMIHOST=infra02ilo.intra.cacert.org
   LOCALPORT=8082
   HTTPSPORT=443
   IKVMPORT=5900
   ssh -f -N -L ${LOCALPORT}:${IPMIHOST}:${HTTPSPORT} \
                           -L ${IKVMPORT}:${IPMIHOST}:${IKVMPORT} hopper

and then browsing to the web UI:

.. code:: bash

   firefox https://127.0.0.1:${LOCALPORT}/

To use the remote console facility, first install Oracle Java JRE 8.0_211 on
your admin machine. Then download the launch.jnlp script offered by the web UI
and save it in $HOME. Then use this script "console" to execute it:

.. code:: bash

   #! /bin/bash
   # console - run remote console for CAcert infra02 with Oracle Java environment

   export JAVADIR=/opt/java/jre1.8.0_211/bin
   export JAVA=${JAVADIR}/java
   export JAVAWS=${JAVADIR}/javaws

   LAUNCH=${HOME}/launch.jnlp

   if [ -f ${LAUNCH} ]
   then
         echo "Do not forget to use setupcon if the console keyboard mapping is lame" 1>&2
         sed -i -e 's/443/8082/' ${LAUNCH}
         exec ${JAVAWS} ${LAUNCH}
   else
         echo $0: cannot read ${LAUNCH} 1>&2
   fi

DNS
---

.. index::
   single: DNS records; Infra02

========================== ======== ====================================================================
Name                       Type     Content
========================== ======== ====================================================================
infrastructure.cacert.org. IN A     213.154.225.230
infrastructure.cacert.org. IN SSHFP 1 1 5A82D3C150AF002C05784F73250A067053AEED63
infrastructure.cacert.org. IN SSHFP 1 2 63B0D74A3F1CE61865A5EB0497EF05243BC4067EC983C69AB8E62F3CB940CC82
infrastructure.cacert.org. IN SSHFP 2 1 AF8D8E3386EAA72997709632ADF2B457E6FEF0DC
infrastructure.cacert.org. IN SSHFP 2 2 3A0188FC47D1FDD14D70A2FB78F51792D06BA11EAE6AB16E73CB7BB8DD6A0DC8
infrastructure.cacert.org. IN SSHFP 3 1 3E1B9EBF85B726CF831C76ECB8C17786AEDF40E8
infrastructure.cacert.org. IN SSHFP 3 2 3AE7F0035C2172977E99BFE312C7A8299650DEA16A975EA13EECE8FDA426062A
infra02.intra.cacert.org.  IN A     172.16.2.10
========================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.0

* Debian GNU/Linux 10.0

Services
========

Listening services
------------------

+----------+---------+----------+-----------------------------------------+
| Port     | Service | Origin   | Purpose                                 |
+==========+=========+==========+=========================================+
| 22/tcp   | ssh     | ANY      | admin console access                    |
+----------+---------+----------+-----------------------------------------+
| 25/tcp   | smtp    | local    | mail delivery to local MTA              |
+----------+---------+----------+-----------------------------------------+
| 53/tcp   | dns     | internal | DNS resolver for infra.cacert.org       |
| 53/udp   |         |          |                                         |
+----------+---------+----------+-----------------------------------------+
| 123/udp  | ntp     | ANY      | network time protocol for host,         |
|          |         |          | listening on the Internet IPv6 and IPv4 |
|          |         |          | addresses                               |
+----------+---------+----------+-----------------------------------------+
| 5666/tcp | nrpe    | monitor  | remote monitoring service               |
+----------+---------+----------+-----------------------------------------+

Running services
----------------

.. index::
   single: acpid
   single: atop
   single: atopacctd
   single: cron
   single: dbus
   single: dnsmasq
   single: lxc
   single: mdadm
   single: nrpe
   single: ntpd
   single: openssh
   single: postfix
   single: radvd
   single: rsyslog
   single: smartd

+--------------------+----------------------+---------------------------------------------+
| Service            | Usage                | Start mechanism                             |
+====================+======================+=============================================+
| acpid              | ACPI daemon          | systemd unit ``acpid.service``              |
+--------------------+----------------------+---------------------------------------------+
| atop               | Advanced system      | systemd unit ``atop.service``               |
|                    | and process monitor  |                                             |
+--------------------+----------------------+---------------------------------------------+
| atopacctd          | Advanced system      | systemd unit ``atopacct.service``           |
|                    | and process monitor  |                                             |
|                    | accounting daemon    |                                             |
+--------------------+----------------------+---------------------------------------------+
| cron               | job scheduler        | systemd unit ``cron.service``               |
+--------------------+----------------------+---------------------------------------------+
| dbus-daemon        | System message bus   | systemd unit ``dbus.service``               |
|                    | daemon               |                                             |
+--------------------+----------------------+---------------------------------------------+
| dnsmasq            | DNS resolver         | systemd unit ``dnsmasq.service``            |
+--------------------+----------------------+---------------------------------------------+
| LXC                | Service for LXC      | systemd unit ``lxc.service``                |
|                    | container management |                                             |
+--------------------+----------------------+---------------------------------------------+
| mdadm              | RAID monitoring      | systemd unit ``mdmonitor.service``          |
+--------------------+----------------------+---------------------------------------------+
| Nagios NRPE server | remote monitoring    | systemd unit ``nagios-nrpe-server.service`` |
|                    | service queried by   |                                             |
|                    | :doc:`monitor`       |                                             |
+--------------------+----------------------+---------------------------------------------+
| ntpd               | time server          | systemd unit ``ntp.service``                |
+--------------------+----------------------+---------------------------------------------+
| openssh server     | ssh daemon for       | systemd unit ``ssh.service``                |
|                    | remote               |                                             |
|                    | administration       |                                             |
+--------------------+----------------------+---------------------------------------------+
| postfix            | SMTP server for      | systemd unit ``postfix.service``            |
|                    | local mail           |                                             |
|                    | submission, ...      |                                             |
+--------------------+----------------------+---------------------------------------------+
| radvd              | IPv6 route           | systemd unit ``radvd.service``              |
|                    | advertisement        |                                             |
+--------------------+----------------------+---------------------------------------------+
| rsyslog            | syslog daemon        | systemd unit ``rsyslog.service``            |
+--------------------+----------------------+---------------------------------------------+
| smartd             | S.M.A.R.T. HDD       | systemd unit ``smartd.service``             |
|                    | monitoring           |                                             |
+--------------------+----------------------+---------------------------------------------+

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
* all traffic of non-critical infrastructure systems

Security
========

.. sshkeys::
   :RSA:     SHA256:Y7DXSj8c5hhlpesEl+8FJDvEBn7Jg8aauOYvPLlAzII MD5:86:d5:f8:71:2e:ab:5e:50:5d:f6:37:6b:16:8f:d1:1c
   :DSA:     SHA256:OgGI/EfR/dFNcKL7ePUXktBroR6uarFuc8t7uN1qDcg MD5:b4:fb:c2:74:33:eb:cc:f0:3e:31:38:c9:a8:df:0a:f5
   :ECDSA:   SHA256:OufwA1whcpd+mb/jEseoKZZQ3qFql16hPuzo/aQmBio MD5:79:c4:b8:ff:ef:c9:df:9a:45:07:8d:ab:71:7c:e9:c0
   :ED25519: SHA256:eXWoP7L/A25p/YW3vmj+4NFy2lEEVcRaLnNhcelBar8 MD5:25:d1:c7:44:1c:38:9e:ad:89:32:c7:9c:43:8e:41:c4

Dedictated user roles
---------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments and critical packages
--------------------------------------

The system is the host system for all other infrastructure systems. Access to
this system has to be tightly controlled.

Critical Configuration items
============================

.. index::
   pair: dnsmasq; configuration

Dnsmasq configuration
---------------------

Dnsmasq serves the local DNS zone infra.cacert.org to the `br0` interface. It
is configured by :file:`/etc/dnsmasq.d/00infra` and uses :file:`/etc/hosts` as
source for IP addresses.

.. index::
   pair: Ferm; configuration

Ferm firewall configuration
---------------------------

The `Ferm`_ based firewall setup is located in :file:`/etc/ferm` and its
subdirectories.

.. index::
   pair: LXC; configuration

Container configuration
-----------------------

The container configuration is contained in files named
:file:`/var/lib/lxc/<container>/config`.

The root filesystems of the containers are stored on :term:`LVM` volumes that
are mounted in :file:`/var/lib/lxc/<container>/rootfs` for each container.

Tasks
=====

.. todo:: document how to setup a new container
.. todo:: document how to setup firewall rules/forwarding
.. todo:: document how the backup system works

Reboot
------

The system can be rebooted safely since the Debian Buster installation on
2019-07-13:

.. code-block:: bash

   systemctl reboot

Restarting the firewall
-----------------------

To restart the firewall setup perform a configuration syntax check and use
systemctl to reload ferm's configuration.

.. code-block:: bash

   ferm -n /etc/ferm/ferm.conf
   systemctl reload ferm.service

Changes
=======

Planned
-------

.. todo:: add DNS setup for IPv6 address
.. todo:: switch to Puppet management
.. todo:: replace nrpe with icinga2 agent
.. todo:: replace ferm with nftables setup

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Ferm documentation
   http://ferm.foo-projects.org/download/2.3/ferm.html
Ferm Debian Wiki page
   https://wiki.debian.org/ferm
LXC Debian Wiki page
   https://wiki.debian.org/LXC
