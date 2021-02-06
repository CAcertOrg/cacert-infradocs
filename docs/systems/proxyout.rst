.. index::
   single: Systems; Proxyout

========
Proxyout
========

Purpose
=======

This system provides an outgoing http/https proxy for controlled access to
external resources like APT repositories and code repositories. The decision
to setup this system has been made due to often changing IP addresses of
external repositories that lead to update problems on several other machines.

Application Links
-----------------

This machine has no externaly exposed URLs.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| Squid       | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* proxyout-admin@cacert.org

Additional People
-----------------

* None

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: None
:IP Intranet: None
:IP Internal: :ip:v4:`10.0.0.201`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::201`
:MAC address: :mac:`00:16:3e:15:b8:8c` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Proxyout

Monitoring
----------

:internal checks: :monitor:`proxyout.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Proxyout

.. todo:: setup DNS records (in infra.cacert.org zone)

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.8

* Debian GNU/Linux 10.8

Applicable Documentation
------------------------

The system is managed by :doc:`puppet`. The puppet repository is browsable at
https://git.cacert.org/gitweb/?p=cacert-puppet.git;a=summary.

Services
========

Listening services
------------------

+----------+---------+----------+----------------------------+
| Port     | Service | Origin   | Purpose                    |
+==========+=========+==========+============================+
| 22/tcp   | ssh     | ANY      | admin console access       |
+----------+---------+----------+----------------------------+
| 25/tcp   | smtp    | local    | mail delivery to local MTA |
+----------+---------+----------+----------------------------+
| 3128/tcp | http    | internal | squid http/https proxy     |
+----------+---------+----------+----------------------------+
| 5665/tcp | icinga2 | monitor  | remote monitoring service  |
+----------+---------+----------+----------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim
   single: icinga2
   single: openssh
   single: puppet
   single: rsyslog
   single: squid

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
| Puppet agent   | configuration management | systemd unit ``puppet.service``  |
|                | agent                    |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+
| Squid          | Caching and filtering    | systemd unit ``squid.service``   |
|                | http/https proxy for     |                                  |
|                | internal machines        |                                  |
+----------------+--------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`blog`
* :doc:`board`
* :doc:`bugs`
* :doc:`cats`
* :doc:`email`
* :doc:`emailout`
* :doc:`git`
* :doc:`ircserver`
* :doc:`jenkins`
* :doc:`lists`
* :doc:`monitor`
* :doc:`motion`
* :doc:`proxyin`
* :doc:`puppet`
* :doc:`svn`
* :doc:`test`
* :doc:`translations`
* :doc:`web`
* :doc:`webstatic`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* .debian.org Debian mirrors
* apt.puppetlabs.com as Debian repository for puppet packages
* HTTP and HTTPS servers specified in the squid configuration

Security
========

.. sshkeys::
   :RSA:     SHA256:TfsDuQ2tuWnTlpLnFILxlZa+IOpC97QmxDAlGgCa0/I MD5:1e:8e:1d:06:a5:fa:d6:08:95:e9:68:fb:ae:16:24:8f
   :ECDSA:   SHA256:d79XAVk0pspIVoI7i4ffohM7PjaBMJdh1J4yv+4Z5ms MD5:74:70:63:b9:3e:6b:9f:a2:34:0e:9a:92:77:dd:93:73
   :ED25519: SHA256:26yiJUT3NfqpFDLgAgXSsRL7ppMiIpNqKmfDiMxpAqc MD5:43:0d:1e:ec:1b:5f:c3:84:38:c7:75:b7:be:3c:1b:d4

Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

Squid is a proven http and https proxy installed from distribution packages
with low risk.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

Tasks
=====

Adding ACLs to Squid
--------------------

Add required lines to the ``profiles::squid::acls`` item in Hiera data for node
proxyout.

Changes
=======

Planned
-------

.. todo:: Change all infrastructure hosts to use this machine as APT proxy to
          avoid flaky firewall configurations on :doc:`infra02`.

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* http://www.squid-cache.org/
