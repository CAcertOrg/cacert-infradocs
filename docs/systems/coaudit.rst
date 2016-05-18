.. index::
   single: Systems; Coaudit

=======
Coaudit
=======

Purpose
=======

Planned replacement for :wiki:`fiddle.it </SystemAdministration/Systems/fiddle>`.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_martin`
* Secondary: None

.. todo:: find an additional admin

Contact
-------

* coaudit-admin@cacert.org

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
:IP Intranet: :ip:v4:`172.16.2.118`
:IP Internal: :ip:v4:`10.0.0.118`
:MAC address: :mac:`00:ff:67:c2:08:53` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Coaudit

=================== ======== ==========================
Name                Type     Content
=================== ======== ==========================
coaudit.cacert.org. IN CNAME infrastructure.cacert.org.
=================== ======== ==========================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.4

* Debian GNU/Linux 8.4

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 80/tcp   | http      | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: cron
   single: exim
   single: nrpe
   single: openssh

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver          | init script                            |
|                    |                    | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates

Security
========

.. sshkeys::
   :RSA:   07:e1:eb:c0:4d:01:b7:a1:16:b1:01:8b:6b:5f:59:43
   :DSA:   66:ac:19:2c:a1:73:5b:6c:6c:55:3b:5b:52:cb:7e:ec
   :ECDSA: 51:c7:bf:c6:f1:50:45:b7:cd:31:d7:41:40:60:b4:3c

Critical Configuration items
============================

Apache httpd configuration
--------------------------

The system contains an uncustomized Apache httpd configuration.

Changes
=======

System Future
-------------

.. todo:: either setup some application or remove the container

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
