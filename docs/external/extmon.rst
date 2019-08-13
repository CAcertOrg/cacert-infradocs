.. index::
   single: Systems; Extmon

======
Extmon
======

Purpose
=======

Extmon is used as an external Icinga2 agent that monitors the availability of
CAcert service from the Internet. The system is sponsored by
:ref:`people_jandd` and is running on a Hetzner cloud instance in Germany.

Application Links
-----------------

Service checks executed by extmon
  https://monitor.cacert.org/monitoring/list/servicegroups#!/monitoring/list/services?servicegroup_name=external-checks

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+---------------+---------------------+
| Application   | Administrator(s)    |
+===============+=====================+
| icinga2 agent | :ref:`people_jandd` |
+---------------+---------------------+

Contact
-------

* extmon-admin@cacert.org

Additional People
-----------------

No other people have :program:`sudo` access on that machine.

Basics
======

Physical Location
-----------------

This system is a virtual KVM machine hosted on a Hetzner cloud server in
Nürnberg, Germany.

Physical Configuration
----------------------

* 1 VCPU
* 2 GB RAM
* 20 GB local disc

Logical Location
----------------

:IP Internet: :ip:v4:`116.203.192.12`
:IPv6:        :ip:v6:`2a01:4f8:c2c:a5b9::1`
:MAC address: :mac:`96:00:00:2c:89:82` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Extmon

Monitoring
----------

:internal checks: :monitor:`extmon.infra.cacert.org`

DNS
---

The system has no DNS entries.

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

+----------+---------+---------+-------------------------------+
| Port     | Service | Origin  | Purpose                       |
+==========+=========+=========+===============================+
| 22/tcp   | ssh     | ANY     | admin console access          |
+----------+---------+---------+-------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA    |
+----------+---------+---------+-------------------------------+
| 68/udp   | dhcp    | hetzner | dynamic network configuration |
+----------+---------+---------+-------------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service     |
+----------+---------+---------+-------------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: openssh
   single: puppet
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``    |
|                | daemon                   |                                  |
+----------------+--------------------------+----------------------------------+
| Exim           | SMTP server for          | systemd unit ``exim4.service``   |
|                | local mail submission    |                                  |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``     |
|                | remote administration    |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

Databases
---------

* None

Connected Systems
-----------------

* :doc:`../systems/monitor`

Outbound network connections
----------------------------

* DNS (53) Hetzner cloud nameservers
* :doc:`../systems/puppet` (tcp/8140) as Puppet master
* checked CAcert systems on publicly opened ports

Security
========

.. sshkeys::
   :RSA:     SHA256:pRCCUOzQbNf2MSDyq3mt/zCYrf9Cowo0tUp+cLcP5ZU MD5:89:07:d2:68:02:37:73:86:a3:f0:53:46:e9:93:3c:b5
   :DSA:     SHA256:qQmdmDcCrj9CgGK/LsT0zz8d90wCmn0HlSmt9WRqIF8 MD5:8c:f0:fa:e2:18:98:22:fb:ae:ed:c3:84:78:0e:70:5f
   :ECDSA:   SHA256:+5X1KhHfqCSfVzNhT6xXpKYwsS/bZvI5rOM7hPogcWo MD5:f3:65:d0:12:a6:e9:cc:91:f4:55:32:c0:ca:75:59:17
   :ED25519: SHA256:lxUPfNgUMZ/JrZHVG9Qc33x7vqyKGgmIJ54rgx+dZow MD5:39:b7:17:91:05:2d:1c:ad:4b:5a:5e:e0:e6:01:2c:a5

Dedicated user roles
--------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

The system provides no public services besides an Icinga2 agent that executes
commands sent from :doc:`../systems/monitor`.

The Puppet agent package and a few dependencies are installed from the
official Puppet APT repository because the versions in Debian are too old to
use modern Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

* None

Tasks
=====

Add a service to be checked by extmon
-------------------------------------

Service monitoring is configured in the :cacertgit:`cacert-icinga2-conf_d`.

All checks for services on hosts with the following block will be executed by
extmon:

.. code-block::

   vars.external = true

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

* None

References
----------

* https://icinga.com/docs/icinga2/latest/
