==================
Systems - TEMPLATE
==================

Purpose
=======

.. <SHORT DESCRIPTION>

Basics
======

Physical Location
-----------------

.. <PHYSICAL HOST, VM GUEST, APACHE VIRTUAL HOST, etc.>

.. ## Use the following for containers on Infra02:

This system is located in an LXC_ container on physical machine :doc:`infra02`.

Physical Configuration
----------------------

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/EquipmentList

Logical location
----------------

 * IP Internet: <IP>
 * IP Intranet: <IP>
 * IP Internal: <IP>
 * MAC address: <MAC> (interfacename)

.. seealso::

   See :doc:`network`

DNS
---

 * <HOSTNAME>.cacert.org. IN A <IP>
 * <HOSTNAME>.intra.cacert.org. IN A <IP>

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/Procedures/DNSChanges

Operating System
----------------

 * Debian GNU/Linux x.y

Applicable Documentation
------------------------

This is it :-)

Administration
==============

System Administration
---------------------

* Primary: <SYSADMIN's NAME>
* Secondary: <secondary name>

Contact
-------

 * <system>-admin@cacert.org

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
| 443/tcp  | https     | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

.. below are some definitions of commonly open ports, choose those that are applicable and order the table by port number
   || 3306/tcp || mysql || local || MySQL database for ... ||
   || 5432/tcp || pgsql || local || PostgreSQL database for ... ||
   || 465/udp || syslog || local || syslog port ||

Running services
----------------

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for ...  | init script                            |
|                    |                    | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for ...            |                                        |
+--------------------+--------------------+----------------------------------------+
| MySQL              | MySQL database     | init script                            |
|                    | server for ...     | :file:`/etc/init.d/mysql`              |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission, ...    |                                        |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission, ...    |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+-------------+--------------+---------------------------+
| RDBMS       | Name         | Used for                  |
+=============+==============+===========================+
| MySQL       | application1 | fictional application one |
+-------------+--------------+---------------------------+
| PostgreSQL  | application2 | fictional application two |
+-------------+--------------+---------------------------+

Running Guests
--------------

+----------------+-------------+---------------+---------+---------------+
| Machine        | IP Intranet | IP Internet   | Ports   | Purpose       |
+================+=============+===============+=========+===============+
| :doc:`machine` | <LOCAL IP>  | <INTERNET IP> | <PORTS> | <DESCRIPTION> |
+----------------+-------------+---------------+---------+---------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* ftp.nl.debian.org as Debian mirror
* security.debian.org for Debian security updates
* crl.cacert.org (rsync) for getting CRLs

Security
========

SSH host keys
-------------

+-----------+-----------------------------------------------------+
| Algorithm | Fingerprint                                         |
+===========+=====================================================+
| RSA       |                                                     |
+-----------+-----------------------------------------------------+
| DSA       |                                                     |
+-----------+-----------------------------------------------------+
| ECDSA     |                                                     |
+-----------+-----------------------------------------------------+
| ED25519   |                                                     |
+-----------+-----------------------------------------------------+

.. seealso::

   See :doc:`sshkeys`

Dedicated user roles
--------------------

.. If the system has some dedicated user groups besides the sudo group used for administration it should be documented here
   Regular operating system groups should not be documented

.. || '''Group''' || '''Purpose''' ||
   || goodguys || Shell access for the good guys ||

Non-distribution packages and modifications
-------------------------------------------

.. * None
   or
   * List of non-distribution packages and modifications

Risk assessments on critical packages
-------------------------------------

Tasks
=====

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

* :file:`/etc/apache2/ssl/<path to certificate>` server certificate (valid until <datetime>)
* :file:`/etc/apache2/ssl/<path to server key>` server key

.. * `/etc/apache2/ssl/cacert-certs.pem` CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for client certificates)
   * `/etc/apache2/ssl/cacert-chain.pem` CAcert.org Class 1 certificate (certificate chain for server certificate)

.. seealso::

   See :doc:`certlist`

Changes
=======

Planned
-------

System Future
.............

.. * No plans

Document Stuff
..............

.. add a paragraph for each larger planned task that seems to be worth
   mentioning. You may want to link to specific issues if you use some issue
   tracker.

Potential Similiar Configurations
.................................

* https://wiki.cacert.org/Exim4Configuration
* https://wiki.cacert.org/PostfixConfiguration
* https://wiki.cacert.org/QmailConfiguration
* https://wiki.cacert.org/SendmailConfiguration
* https://wiki.cacert.org/StunnelConfiguration

Potential System Procedures
...........................

* https://wiki.cacert.org/SystemAdministration/Procedures/DNSChanges
* https://wiki.cacert.org/SystemAdministration/CertificateList

References
==========

.. can be used to provide links to reference documentation
   * http://product.site.com/docs/
   * [[http://product.site.com/whitepaper/document.pdf|Paper on how to setup...]]

Links
=====

.. || [[https://<system>.cacert.org/]] || <System> URL ||
   may contain more URLs if there are multiple useful entry points

