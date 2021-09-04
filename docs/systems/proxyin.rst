.. index::
   single: Systems; Proxyin

=======
Proxyin
=======

Purpose
=======

This system provides an incoming TLS proxy using `nginx`_ to share one public
IPv4 address between multiple services.

.. _nginx: https://nginx.org/

Application Links
-----------------

No direct links, applications run on other systems.

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
| nginx       | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* proxyin-admin@cacert.org

Additional People
-----------------

No other people have :program:`sudo` access on that machine.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.241`
:IP Intranet: :ip:v4:`172.16.2.241`
:IP Internal: :ip:v4:`10.0.0.35`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::35`
:MAC address: :mac:`00:16:3e:3c:c8:a6` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Proxyin

Monitoring
----------

:internal checks: :monitor:`proxyin.infra.cacert.org`
:external checks: :monitor:`proxyin.cacert.org`

DNS
---

.. index::
   single: DNS records; Proxyin

========================= ======== =====================================================================
Name                      Type     Content
========================= ======== =====================================================================
proxyin.cacert.org.       IN A     213.154.225.241
proxyin.cacert.org.       IN AAAA  2001:7b8:616:162:2::35
proxyin.cacert.org.       IN SSHFP 1 1 c7c559bc06d236b4128e6d720a573d805a27727a
proxyin.cacert.org.       IN SSHFP 1 2 affa8cc26dffa7f0803db2d027ab23f013aeabfb3b2d1b1a16659e38dba14528
proxyin.cacert.org.       IN SSHFP 2 1 19bb944a917067131f02be4e9a709ade68c260f8
proxyin.cacert.org.       IN SSHFP 2 2 b9b5860f3427ea9c3460c62a880527a41470c77000e5083ffffb7defa0d42e4e
proxyin.cacert.org.       IN SSHFP 3 1 b9581a544ca96fe071341acb450a2cf74b1b7c9f
proxyin.cacert.org.       IN SSHFP 3 2 be3dd21fde37042659a25143cb5171b39d22ea2c846745af9c098003a9004185
proxyin.cacert.org.       IN SSHFP 4 1 9b4ba8c78b6585abaf2b46bce78a6f366f1e9bac
proxyin.cacert.org.       IN SSHFP 4 2 59125e8706a208fa8eed2b5994ec60f7ba8e31b1c26d90ce909d78a0027359ef
proxyin.intra.cacert.org. IN A     172.16.2.241
proxyin.infra.cacert.org. IN A     10.0.0.35
========================= ======== =====================================================================

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

+----------+---------+---------+----------------------------+
| Port     | Service | Origin  | Purpose                    |
+==========+=========+=========+============================+
| 22/tcp   | ssh     | ANY     | admin console access       |
+----------+---------+---------+----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA |
+----------+---------+---------+----------------------------+
| 80/tcp   | http    | ANY     | nginx                      |
+----------+---------+---------+----------------------------+
| 443/tcp  | https   | ANY     | nginx                      |
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
   single: nginx
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
| nginx          | TLS SNI proxy and        | systemd unit ``nginx.service``   |
|                | http to https redirector |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

Databases
---------

* None

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT

The mapping from host names to target backends is managed via Puppet and
configured in the profiles::sniproxy::https_forwards map in
https://git.cacert.org/cacert-puppet.git/tree/hieradata/nodes/proxyin.yaml.

Security
========

.. sshkeys::
   :RSA:     SHA256:r/qMwm3/p/CAPbLQJ6sj8BOuq/s7LRsaFmWeONuhRSg MD5:9d:ab:4f:2d:48:81:a1:86:68:99:8a:49:d5:01:07:6f
   :DSA:     SHA256:ubWGDzQn6pw0YMYqiAUnpBRwx3AA5Qg///t976DULk4 MD5:2c:33:c7:bd:f2:6b:1a:03:ea:cd:c3:da:d8:a7:fa:c2
   :ECDSA:   SHA256:vj3SH943BCZZolFDy1Fxs50i6iyEZ0WvnAmAA6kAQYU MD5:7d:ac:f4:ce:fb:4f:17:72:4d:5a:c4:b4:08:5d:8b:7c
   :ED25519: SHA256:WRJehwaiCPqO7StZlOxg97qOMbHCbZDOkJ14oAJzWe8 MD5:14:6d:9e:24:de:97:f7:96:bc:cd:45:28:1b:b5:52:7e

Dedicated user roles
--------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

The system is stripped down to the bare minimum. :program:`nginx` is security
supported. The :program:`nginx-full` package is used for `nginx` to support
streaming after SNI.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

The host does not provide own TLS services and therefore has no certificates.

nginx configuration
-------------------

:program:`nginx` is configured via Puppet profile ``profiles::sniproxy`` and
just redirects all http traffic to https.

nginx configuration
-------------------

:program:`nginx` is configured via Puppet profile ``profiles::sniproxy``, TCP
traffic on port 80 is redirected to the https port and https traffic is
forwarded to the target hosts as configured in
:file:`hieradata/nodes/proxyin.yaml`.

Tasks
=====

Adding a new forward entry
--------------------------

Add an entry to the ``profiles::sniproxy::forwarded`` item in
:file:`hieradata/nodes/proxyin.yaml` in :cacertgit:`cacert-puppet` and adjust
the firewall configuration on :doc:`infra02`. You will need to request DNS
changes from the critical team if you want to switch an existing service to use
the SNI proxy service.

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

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* https://nginx.org/en/docs/
