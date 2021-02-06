.. index::
   single: Systems; Monitor

=======
Monitor
=======

Purpose
=======

This system hosts an `Icinga 2`_ instance to centrally monitor the
services in the CAcert network (especially for security updates and certificate
expiry).

.. note::

   To access the system you need a client certificate where the first email
   address in the Subject Distinguished Name field is a cacert.org address.
   Subject Alternative Names are not checked.

   If you are the administrator of a service please ask the monitor admins to
   add your system to the monitoring configuration and add you as system
   contact to allow for notifications and tasks like service outage
   acknowledgement, adding notes, rescheduling checks or setting downtimes for
   your service.

.. _Icinga 2: https://www.icinga.org/

Application Links
-----------------

The Icingaweb 2 frontend
   https://monitor.cacert.org/

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
| Icinga 2    | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* monitor-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd` and :ref:`people_mario` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.230`
:IP Intranet: :ip:v4:`172.16.2.18`
:IP Internal: :ip:v4:`10.0.0.18`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::18`
:MAC address: :mac:`00:ff:73:b3:17:43` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Monitor

Monitoring
----------

:internal checks: :monitor:`monitor.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Monitor

=================== ======== =========================
Name                Type     Content
=================== ======== =========================
monitor.cacert.org. IN CNAME infrastructure.cacert.org
=================== ======== =========================

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

This is it :-)

.. seealso::

   :ref:`Setup package update monitoring for a new container
   <setup_apt_checking>`

Services
========

Listening services
------------------

+----------+----------+----------+---------------------------------+
| Port     | Service  | Origin   | Purpose                         |
+==========+==========+==========+=================================+
| 22/tcp   | ssh      | ANY      | admin console access            |
+----------+----------+----------+---------------------------------+
| 25/tcp   | smtp     | local    | mail delivery to local MTA      |
+----------+----------+----------+---------------------------------+
| 80/tcp   | http     | ANY      | Redirect to https               |
+----------+----------+----------+---------------------------------+
| 443/tcp  | https    | ANY      | Icingaweb 2 frontend            |
+----------+----------+----------+---------------------------------+
| 5665/tcp | icinga2  | monitor  | remote monitoring service       |
+----------+----------+----------+---------------------------------+
| 5432/tcp | pgsql    | local    | PostgreSQL database for IDO     |
+----------+----------+----------+---------------------------------+
| 8000/tcp | git-hook | internal | HTTP endpoint for git-pull-hook |
+----------+----------+----------+---------------------------------+

.. note::

   The ssh port is reachable via NAT on infrastructure.cacert.org:11822


Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: dbus
   single: git-pull-hook
   single: icinga2
   single: openssh
   single: postfix
   single: postgresql
   single: puppet agent
   single: rsyslog

+----------------+-----------------------+------------------------------------------------+
| Service        | Usage                 | Start mechanism                                |
+================+=======================+================================================+
| Apache httpd   | Webserver for         | systemd unit ``apache2.service``               |
|                | Icingaweb 2           |                                                |
+----------------+-----------------------+------------------------------------------------+
| cron           | job scheduler         | systemd unit ``cron.service``                  |
+----------------+-----------------------+------------------------------------------------+
| dbus-daemon    | System message bus    | systemd unit ``dbus.service``                  |
|                | daemon                |                                                |
+----------------+-----------------------+------------------------------------------------+
| git-pull-hook  | Custom Python3        | systemd unit ``icinga2-git-pull-hook.service`` |
|                | hook to pull git      |                                                |
|                | changes from the      |                                                |
|                | cacert-icinga2-conf_d |                                                |
|                | repository            |                                                |
+----------------+-----------------------+------------------------------------------------+
| Icinga2        | Icinga2 monitoring    | systemd unit ``icinga2.service``               |
|                | daemon                |                                                |
+----------------+-----------------------+------------------------------------------------+
| openssh server | ssh daemon for        | systemd unit ``ssh.service``                   |
|                | remote                |                                                |
|                | administration        |                                                |
+----------------+-----------------------+------------------------------------------------+
| Postfix        | SMTP server for       | systemd unit ``postfix.service``               |
|                | local mail            |                                                |
|                | submission            |                                                |
+----------------+-----------------------+------------------------------------------------+
| PostgreSQL     | PostgreSQL            | systemd unit ``postgresql.service``            |
|                | database server       |                                                |
+----------------+-----------------------+------------------------------------------------+
| Puppet agent   | configuration         | systemd unit ``puppet.service``                |
|                | management agent      |                                                |
+----------------+-----------------------+------------------------------------------------+
| rsyslog        | syslog daemon         | systemd unit ``rsyslog.service``               |
+----------------+-----------------------+------------------------------------------------+

Databases
---------

+------------+------------+--------------------------------------------+
| RDBMS      | Name       | Used for                                   |
+============+============+============================================+
| PostgreSQL | icinga2    | Icinga 2 performance and alerting data     |
+------------+------------+--------------------------------------------+
| PostgreSQL | icingaweb2 | Icingaweb 2 group and user preference data |
+------------+------------+--------------------------------------------+

Connected Systems
-----------------

* :doc:`../external/extmon`
* :doc:`git` for triggering the git-pull-hook on newly pushed commits to the
  cacert-icinga2-conf_d repository

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`git` to fetch new commits from the cacert-icinga2-conf_d repository
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT
* crl.cacert.org (rsync) for getting CRLs
* all :ip:v4range:`10.0.0.0/24`, :ip:v4range:`172.16.2.0/24` and
  :ip:v6range:`2001:7b8:616:162:2::/80` systems for monitoring their services


Security
========

.. sshkeys::
   :RSA:     SHA256:8iOQQGmuqi4OrF2Qkqt9665w8G7Dwl6U9J8bFfYz7V0 MD5:df:98:f5:ea:05:c1:47:52:97:58:8f:42:55:d6:d9:b6
   :DSA:     SHA256:Sh/3OWrodFWc8ZbVTV1/aJDbpt5ztGrwSSWLECTNrOI MD5:07:2b:10:b1:6d:79:35:0f:83:aa:fc:ba:d6:2f:51:dc
   :ECDSA:   SHA256:GWvYqhQUt9INh/7VRVu6Z2YORoy/YzgBxNBmX+ZvMsk MD5:48:46:b1:5a:4e:05:64:8a:c3:76:33:77:20:91:14:70
   :ED25519: SHA256:L5roC867bvxDJ0ckbhIQOt2A9Nh1RQBVuIJFWwrPLG0 MD5:10:94:56:09:5b:a2:28:ab:11:e0:0f:6e:e4:0c:38:bb


Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

Icinga 2 and Icingaweb 2 are well maintained community projects with a good
security track record.

Apache httpd has a good reputation and is a low risk package.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

.. todo:: move more configuration of :doc:`monitor` to Puppet code

Keys and X.509 certificates
---------------------------

.. sslcert:: monitor.cacert.org
   :altnames:   DNS:monitor.cacert.org, DNS:monitor.intra.cacert.org
   :certfile:   /etc/ssl/certs/monitor.c.o.pem
   :keyfile:    /etc/ssl/private/monitor.c.o.priv
   :serial:     147C5F
   :expiration: Feb 16 20:15:55 2022 GMT
   :sha1fp:     68:A0:FA:C9:9A:52:AB:2C:F2:41:58:FC:D1:25:64:8B:4A:93:3C:E5
   :issuer:     CA Cert Signing Authority

* :file:`/etc/ssl/certs/cacert.allcerts.pem` CAcert.org Class 1 and Class 3 CA
  certificates (allowed CA certificates for client certificates and the
  certificate chain for the server certificate)
* :file:`/var/local/ssl/crls/`

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

CRL fetch job
-------------

The script :file:`/etc/cron.hourly/update-crls` is used to fetch CRLs once per
hour.

Apache httpd configuration
--------------------------

The HTTP and HTTPS VirtualHost configuration is defined in
:file:`/etc/apache2/sites-available/icinga-nossl` and
:file:`/etc/apache2/sites-available/icinga` the HTTP VirtualHost redirects to
the HTTPS VirtualHost.

Icinga configuration
--------------------

The Icinga 2 configuration is stored in the :file:`/etc/icinga2/` directory.
The :file:`/etc/icinga2/conf.d/` directory is managed in
:cacertgit:`cacert-icinga2-conf_d` repository which has a post-receive hook to
trigger updates of the Icinga 2 configuration and performs a graceful reload
when configuration has changed.

Tasks
=====

Changes
=======

Planned
-------

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Wiki page for this system
   :wiki:`SystemAdministration/Systems/Monitor`
