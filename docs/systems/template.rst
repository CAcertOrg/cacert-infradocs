.. index::
   single: Systems; <host>

==================
Systems - TEMPLATE
==================

Purpose
=======

.. <SHORT DESCRIPTION>

Application Links
-----------------

.. link1
     https://<hostname>/<path>

   link2
     https://<hostname>/<path2>


Administration
==============

System Administration
---------------------

.. people_<name> are defined in people.rst

* Primary: :ref:`people_primary`
* Secondary: :ref:`people_secondary`

Application Administration
--------------------------

+---------------+---------------------+
| Application   | Administrator(s)    |
+===============+=====================+
| <application> | :ref:`people_admin` |
+---------------+---------------------+

Contact
-------

* <system>-admin@cacert.org

Additional People
-----------------

:ref:`people_a` and :ref:`people_b` have :program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

.. <PHYSICAL HOST, VM GUEST, APACHE VIRTUAL HOST, etc.>

.. ## Use the following for containers on Infra02:

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

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

========================== ======== ==========================================
Name                       Type     Content
========================== ======== ==========================================
<HOST>.cacert.org.         IN A     <IP>
<HOST>.intra.cacert.org.   IN A     <IP>
========================== ======== ==========================================

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

.. index::
   single: Apache
   single: Icinga2
   single: MySQL
   single: OpenERP
   single: Postfix
   single: PostgreSQL
   single: cron
   single: nginx
   single: nrpe
   single: openssh

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

.. If the system has some dedicated user groups besides the sudo group used for
   administration it should be documented here Regular operating system groups
   should not be documented

+-------------+-----------------------------+
| Group       | Purpose                     |
+=============+=============================+
| <groupname> | <short purpose description> |
+-------------+-----------------------------+

Non-distribution packages and modifications
-------------------------------------------

.. * None
   or
   * List of non-distribution packages and modifications (with some
     explaination why no distribution package could be used)

Risk assessments on critical packages
-------------------------------------

.. add a paragraph for each known risk. The risk has to be described.
   Mitigation or risk acceptance has to be documented.

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

<service_x> configuration
-------------------------

.. add a section for the configuration of each service where configuration
   deviates from OS package defaults

Tasks
=====

Planned
-------

.. add a paragraph or todo directive for each larger planned task. You may want
   to link to specific issues if you use some issue tracker.

Changes
=======

System Future
-------------

.. use this section to describe any plans for the system future. These are
   larger plans like moving to another host, abandoning the system or replacing
   its funtionality with something else.

.. * No plans

Additional documentation
========================

.. add inline documentation

.. remove unneeded links from the list below, add other links that apply

.. seealso::

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
