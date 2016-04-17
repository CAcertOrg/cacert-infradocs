.. index::
   single: Systems; <host>

==================
Systems - TEMPLATE
==================

Purpose
=======

.. <SHORT DESCRIPTION>

Administration
==============

System Administration
---------------------

* Primary: `Primary Name`_
* Secondary: `Secondary Name`_

.. _Primary Name: primary@cacert.org
.. _Secondary Name: secondary@cacert.org

Application Administration
--------------------------

* <application>: <sysadmin's name>

Contact
-------

* <system>-admin@cacert.org

Additional People
-----------------

`Person A`_ and `Person B`_ have sudo access on that machine too.

.. _Person A: persona@cacert.org
.. _Person B: personb@cacert.org

Basics
======

Physical Location
-----------------

.. <PHYSICAL HOST, VM GUEST, APACHE VIRTUAL HOST, etc.>

.. ## Use the following for containers on Infra02:

This system is located in an LXC_ container on physical machine :doc:`infra02`.

.. _LXC: https://linuxcontainers.org/

Physical Configuration
----------------------

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/EquipmentList

Logical Location
----------------

:IP Internet: :ip:v4:`<IP>`
:IP Intranet: :ip:v4:`<IP>`
:IP Internal: :ip:v4:`<IP>`
:MAC address: :mac:`<MAC>` (interfacename)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; <machine>

========================== ======== ====================================================================
Name                       Type     Content
========================== ======== ====================================================================
<HOST>.cacert.org.         IN A     <IP>
<HOST>.intra.cacert.org.   IN A     <IP>
========================== ======== ====================================================================

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/Procedures/DNSChanges

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Codename
   single: Debian GNU/Linux; x.y

* Debian GNU/Linux x.y

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

.. use the values from this table or add new lines if applicable

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
| 3306/tcp | mysql     | local     | MySQL database for ...                  |
+----------+-----------+-----------+-----------------------------------------+
| 5432/tcp | pgsql     | local     | PostgreSQL database for ...             |
+----------+-----------+-----------+-----------------------------------------+
| 465/udp  | syslog    | local     | syslog port                             |
+----------+-----------+-----------+-----------------------------------------+

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

   See :doc:`../sshkeys`

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

   * :doc:`../certlist`
   * https://wiki.cacert.org/SystemAdministration/CertificateList

Tasks
=====

Planned
-------

.. add a paragraph for each larger planned task that seems to be worth
   mentioning. You may want to link to specific issues if you use some issue
   tracker.

Changes
=======

System Future
-------------

.. * No plans

Additional documentation
========================

.. add inline documentation

.. remove unneeded links from the list below, add other links that apply

.. seealso:

   * https://wiki.cacert.org/Exim4Configuration
   * https://wiki.cacert.org/PostfixConfiguration
   * https://wiki.cacert.org/QmailConfiguration
   * https://wiki.cacert.org/SendmailConfiguration
   * https://wiki.cacert.org/StunnelConfiguration

References
----------

.. can be used to provide links to reference documentation
   * http://product.site.com/docs/
   * [[http://product.site.com/whitepaper/document.pdf|Paper on how to setup...]]
