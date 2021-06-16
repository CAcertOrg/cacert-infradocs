.. index::
   single: Systems; Infra03

=======
Infra03
=======

Purpose
=======

The infrastructure host system Infra03 is a dedicated physical machine for the
CAcert infrastructure.

.. index::
   single: nftables
   single: LXC

Infra03 is a host system for infrustructure :term:`containers <Container>`. The
containers are setup using the Linux kernel's :term:`LXC` system. The firewall
for the running containers is maintained using nftables_. The machine provides
a DNS resolver based on dnsmasq_ and gives answers for the internal zone
infra.cacert.org.

.. _nftables: https://wiki.nftables.org/
.. _dnsmasq: https://www.thekelleys.org.uk/dnsmasq/doc.html

.. todo::
   implement synchronization between :doc:`infra02`'s dnsmasq and this system's
   dnsmasq

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: :ref:`people_dirk`

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

The machine has the following hardware parameters:

:Mainboard: IBM System x3550 M2 49Y6512
:CPU: Intel(R) Xeon(R) CPU E5506 @ 2.13GHz (4 Cores, 4 Threads)
:RAM: 48 GiB (8 GB DDR3-1600 Registered ECC)
:Disks: 3 x 1TB Seagate Constellation 2 SATA ST91000640NS
:NIC:

  * eno1 Broadcom Limited NetXtreme II BCM5709 Gigabit Ethernet (rev 20)
  * eno2 Broadcom Limited NetXtreme II BCM5709 Gigabit Ethernet (rev 20)

.. seealso::

   See :wiki:`SystemAdministration/EquipmentList`

Logical Location
----------------

:IP Internet: None yet
:IP Intranet: :ip:v4:`172.16.2.3`
:IP Internal: :ip:v4:`10.0.3.1`
:IPv6:        :ip:v6:`2001:7b8:616:162:1::9`
:MAC address:

  * :mac:`e4:1f:13:2e:67:86` (eno2)
  * :mac:`fe:2c:b2:f9:c5:41` (br0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Infra03

Monitoring
----------

:internal checks: :monitor:`infra03.infra.cacert.org`
:external checks: :monitor:`infra03.cacert.org`

DNS
---

.. index::
   single: DNS records; Infra03

.. ========================== ======== ==========================================
.. Name                       Type     Content
.. ========================== ======== ==========================================
.. ========================== ======== ==========================================

.. todo:: add DNS records for Infra03

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.9

* Debian GNU/Linux 10.9

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

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: dm-event
   single: dnsmasq
   single: exim4
   single: ntp
   single: openssh
   single: puppet
   single: rsyslog
   single: smartd

+----------------+---------------------------------------+----------------------------------+
| Service        | Usage                                 | Start mechanism                  |
+================+=======================================+==================================+
| cron           | job scheduler                         | systemd unit ``cron.service``    |
+----------------+---------------------------------------+----------------------------------+
| dbus-daemon    | System message bus                    | systemd unit ``dbus.service``    |
+----------------+---------------------------------------+----------------------------------+
| Exim           | SMTP server for local mail submission | systemd unit ``exim4.service``   |
+----------------+---------------------------------------+----------------------------------+
| openssh server | ssh daemon for remote administration  | systemd unit ``ssh.service``     |
+----------------+---------------------------------------+----------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``  |
+----------------+---------------------------------------+----------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service`` |
+----------------+---------------------------------------+----------------------------------+

.. todo:: add Icinga 2 system monitoring

.. Running Guests
   --------------

   .. some directive to list guests here

Connected Systems
-----------------

.. * :doc:`monitor`

None yet

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master

.. * :doc:`proxyout` as HTTP proxy for APT
.. * crl.cacert.org (rsync) for getting CRLs

.. todo:: use proxyout for outgoing http/https traffic

Security
========

.. sshkeys::
   :RSA:     SHA256:zdFI2N/R/yT5n+KbeQh+qXJ3p/bjp+A8BOyTeN+Eh3g MD5:bb:00:36:35:8c:02:97:7d:1b:c4:25:77:60:e6:ec:19
   :ECDSA:   SHA256:In12bkuY6JktIOpsBw5By89ip6ovWhi4Er8GaQzsbrI MD5:1b:32:4d:f3:83:28:04:ac:cf:4f:a9:48:80:b2:2b:0b
   :ED25519: SHA256:m2CBwhLqO47H5iiEoS7YK7mAgoXLeIEjmEdhzNImTPQ MD5:e8:c5:9c:ce:f3:5f:52:98:78:c8:5e:88:b6:e2:3c:37

Dedicated user roles
--------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

The system is the host system for other infrastructure systems. Access to this
system has to be tightly controlled.

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Tasks
=====

Adding a new container
----------------------

.. todo::

   describe how to add a new container, setup nftables rules, routing,
   proxying, outgoing mail and monitoring

Changes
=======

Planned
-------

* Setup Icinga2 monitoring
* Setup containers for MariaDB, Nextcloud, Taiga.io and other services

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
