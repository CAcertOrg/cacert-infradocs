.. index::
   single: Systems; Jenkins

=======
Jenkins
=======

Purpose
=======

`Jenkins`_ continuous integration server for building software artifacts for
CAcert.org and this documentation.

.. _Jenkins: https://jenkins.io

Application Links
-----------------

Jenkins web interface
   https://jenkins.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| Jenkins     | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* jenkins-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` has :program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: reverse proxied from :doc:`web`
:IP Intranet: :ip:v4:`172.16.2.115`
:IP Internal: :ip:v4:`10.0.0.115`
:MAC address: :mac:`00:ff:a4:c9:aa:49` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Jenkins

Monitoring
----------

:internal checks: :monitor:`jenkins.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Jenkins

========================= ======== ====================================================================
Name                      Type     Content
========================= ======== ====================================================================
jenkins.cacert.org.       IN A     213.154.225.242
jenkins.cacert.org.       IN SSHFP 1 1 2CAEBE197C0F1C25404890ADFEDABB371FB05650
jenkins.cacert.org.       IN SSHFP 1 2 6110A42530A5197AB1180417EE32B2EB581813CA773498177481B11D969BB529
jenkins.cacert.org.       IN SSHFP 2 1 4CE4EEF515BDEE033D68B92419F71679880B2FD5
jenkins.cacert.org.       IN SSHFP 2 2 7E76D01B8DC48178535F3F6164C07EF35D3436F352DB8C62FFACD5B8E3C106A7
jenkins.cacert.org.       IN SSHFP 3 1 1CE55A42B27BF42A78E281440F146DA17255A97D
jenkins.cacert.org.       IN SSHFP 3 2 20763231FECF9518C2CECAB05AC76E4483F563C0853F8B8A53E469316DA75381
jenkins.intra.cacert.org. IN A     172.16.2.115
========================= ======== ====================================================================

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

.. use the values from this table or add new lines if applicable

+----------+---------+----------+----------------------------+
| Port     | Service | Origin   | Purpose                    |
+==========+=========+==========+============================+
| 22/tcp   | ssh     | ANY      | admin console access       |
+----------+---------+----------+----------------------------+
| 25/tcp   | smtp    | local    | mail delivery to local MTA |
+----------+---------+----------+----------------------------+
| 2022/tcp | Jenkins | internal | Jenkins ssh port           |
+----------+---------+----------+----------------------------+
| 5665/tcp | icinga2 | monitor  | remote monitoring service  |
+----------+---------+----------+----------------------------+
| 8080/tcp | Jenkins | internal | Jenkins web interface      |
+----------+---------+----------+----------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: exim
   single: icinga2
   single: jenkins
   single: openssh
   single: puppet agent
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| Exim           | SMTP server for local    | systemd unit ``exim4.service``   |
|                | mail submission          |                                  |
+----------------+--------------------------+----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``    |
|                | daemon                   |                                  |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| Jenkins        | Jenkins CI server        | systemd unit ``jenkins.service`` |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``     |
|                | remote administration    |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`git` for triggering Jenkins web hooks
* :doc:`monitor`
* :doc:`web` as reverse proxy for hostnames codedocs.cacert.org,
  funding.cacert.org and infradocs.cacert.org


Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`git` for fetching source code
* :doc:`proxyout` as HTTP proxy for APT and Jenkins plugin updates
* :doc:`puppet` for configuration management
* :doc:`webstatic` for publishing code documentation to codedocs.cacert.org and
  infrastructure documentation to infradocs.cacert.org
* arbitrary Internet HTTP, HTTPS, FTP, FTPS, git servers for fetching source
  code and build dependencies (via ``&CONTAINER_OUT_ELEVATED("jenkins");`` in
  :file:`/etc/ferm/ferm.d/jenkins.conf` on :doc:`infra02`).

Security
========

.. sshkeys::
   :RSA:     SHA256:YRCkJTClGXqxGAQX7jKy61gYE8p3NJgXdIGxHZabtSk MD5:75:83:f5:8f:81:4b:08:bd:fd:6b:ff:12:bc:d7:17:48
   :DSA:     SHA256:fnbQG43EgXhTXz9hZMB+8100NvNS24xi/6zVuOPBBqc MD5:cf:8a:2d:83:53:8d:42:5a:c9:21:7c:c4:6a:3b:81:71
   :ECDSA:   SHA256:IHYyMf7PlRjCzsqwWsduRIP1Y8CFP4uKU+RpMW2nU4E MD5:77:18:34:2b:25:4a:e5:f3:cd:d7:2e:c9:9d:6b:03:01
   :ED25519: SHA256:25iP8jSklIu8saYf8hwIDv7UVIJRQbCh0EGSH3hXNWI MD5:4a:e0:9f:06:d5:c3:c8:36:b9:1e:ef:2e:0b:54:82:58

Non-distribution packages and modifications
-------------------------------------------

* The Puppet agent package and a few dependencies are installed from the
  official Puppet APT repository because the versions in Debian are too old to
  use modern Puppet features.
* Jenkins from pkg.jenkins-ci.org

  package source is defined in :file:`/etc/apt/sources.list.d/jenkins.list`
* Few packages (i.e. go toolchain) from Debian testing

  package source is defined in :file:`/etc/apt/sources.list.d/buster.list`

Risk assessments on critical packages
-------------------------------------

Jenkins is a widely used CI server with regular updates. Security issues are
handled quickly by the upstream developers.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

.. todo:: move configuration of :doc:`jenkins` to Puppet code

Jenkins configuration
---------------------

Jenkins stores its configuration and working directories in
:file:`/var/lib/jenkins`. Jenkins administration is performed via an integrated
management web interface with role based access control.

Tasks
=====

Changes
=======

Planned
-------

* build more of CAcert's software on the Jenkins instance

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* https://jenkins.io/
