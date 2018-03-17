.. index::
   single: Systems; Monitor

=======
Monitor
=======

Purpose
=======

This system hosts an `Icinga`_ instance to centrally monitor the services in
the CAcert network (especially for security updates and certificate
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

.. _Icinga: https://www.icinga.org/

Application Links
-----------------

The Icinga classic frontend
   https://monitor.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+-------------+-----------------------+
| Application | Administrator(s)      |
+=============+=======================+
| Icinga      | :ref:`people_jandd`   |
+-------------+-----------------------+

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
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.4

* Debian GNU/Linux 9.4

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

+----------+---------+---------+-----------------------------+
| Port     | Service | Origin  | Purpose                     |
+==========+=========+=========+=============================+
| 22/tcp   | ssh     | ANY     | admin console access        |
+----------+---------+---------+-----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA  |
+----------+---------+---------+-----------------------------+
| 80/tcp   | http    | ANY     | Icinga classic web frontend |
+----------+---------+---------+-----------------------------+
| 443/tcp  | https   | ANY     | Icinga classic web frontend |
+----------+---------+---------+-----------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service   |
+----------+---------+---------+-----------------------------+
| 5432/tcp | pgsql   | local   | PostgreSQL database for IDO |
+----------+---------+---------+-----------------------------+

.. note::

   The ssh port is reachable via NAT on infrastructure.cacert.org:11822


Running services
----------------

.. index::
   single: Apache
   single: Icinga
   single: IDO2DB
   single: Postfix
   single: PostgreSQL
   single: cron
   single: nrpe
   single: openssh

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for      | init script                            |
|                    | Icinga classic     | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| Icinga             | Icinga monitoring  | init script                            |
|                    | daemon             | :file:`/etc/init.d/icinga`             |
+--------------------+--------------------+----------------------------------------+
| IDO2DB             | IDO database       | init script                            |
|                    | writer daemon      | :file:`/etc/init.d/ido2db`             |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for IDO            |                                        |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service  by        | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | this system itself |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+------------+--------+-----------------+
| RDBMS      | Name   | Used for        |
+============+========+=================+
| PostgreSQL | icinga | Icinga IDO data |
+------------+--------+-----------------+

Connected Systems
-----------------

None

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* crl.cacert.org (rsync) for getting CRLs
* all :ip:v4range:`10.0.0.0/24` and :ip:v4range:`172.16.2.0/24` systems for
  monitoring their services

.. todo:: add IPv6 ranges when they are monitored

Security
========

.. sshkeys::
   :RSA:     SHA256:8iOQQGmuqi4OrF2Qkqt9665w8G7Dwl6U9J8bFfYz7V0 MD5:df:98:f5:ea:05:c1:47:52:97:58:8f:42:55:d6:d9:b6
   :DSA:     SHA256:Sh/3OWrodFWc8ZbVTV1/aJDbpt5ztGrwSSWLECTNrOI MD5:07:2b:10:b1:6d:79:35:0f:83:aa:fc:ba:d6:2f:51:dc
   :ECDSA:   SHA256:GWvYqhQUt9INh/7VRVu6Z2YORoy/YzgBxNBmX+ZvMsk MD5:48:46:b1:5a:4e:05:64:8a:c3:76:33:77:20:91:14:70
   :ED25519: SHA256:L5roC867bvxDJ0ckbhIQOt2A9Nh1RQBVuIJFWwrPLG0 MD5:10:94:56:09:5b:a2:28:ab:11:e0:0f:6e:e4:0c:38:bb


Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

Icinga and the classic frontend are a bit aged but have a good security track
record.

Apache httpd has a good reputation and is a low risk package.

NRPE is flawed and should be replaced. The risk is somewhat mitigated by
firewalling on :doc:`the infrastructure host <infra02>`.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: monitor.cacert.org
   :altnames:   DNS:monitor.cacert.org, DNS:monitor.intra.cacert.org
   :certfile:   /etc/ssl/certs/monitor.c.o.pem
   :keyfile:    /etc/ssl/private/monitor.c.o.priv
   :serial:     1381FF
   :expiration: Mar 16 11:41:06 2020 GMT
   :sha1fp:     64:34:16:0D:2C:1B:38:5D:61:38:17:6E:D5:1B:90:B9:CF:DC:A9:75
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

The Icinga configuration is stored in the :file:`/etc/icinga/` directory.
Database configuration for IDO is stored in :file:`ido2db.cfg`. The Icinga
classic frontend configuration is stored in :file:`cgi.cfg`. Host and service
configurations are defined in the :file:`objects/` subdirectory.

Tasks
=====

Planned
-------

.. todo:: switch to Icinga2 and Icingaweb2

Changes
=======

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
