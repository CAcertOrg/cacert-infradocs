.. index::
   single: Systems; Issue

=====
Issue
=====

Purpose
=======

The purpose of the issue server is to serve the issue tracking system,
implemented with _`OTRS <https://www.otrs.com/>` used by :wiki:`Triage` and
:wiki:`Support` for handling requests going to the support@cacert.org mail
address. Usage for other teams e.g. Arbitration (currently used occasionally),
Organisation Assurance is planned in future.

Application Links
-----------------

OTRS URL
   https://issue.cacert.org/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_mario`
* Secondary: :ref:`people_neo`

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| OTRS        | :ref:`people_mario` |
|             | :ref:`people_nick`  |
|             | :ref:`people_ian`   |
|             | :ref:`people_neo`   |
+-------------+---------------------+

Contact
-------

* issue-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd` and :ref:`people_dirk` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.244`
:IP Intranet: :ip:v4:`172.16.2.28`
:IP Internal: :ip:v4:`10.0.0.28`
:MAC address: :mac:`00:ff:8c:94:e1:c8` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Issue

======================= ======== ============================================
Name                    Type     Content
======================= ======== ============================================
issue.cacert.org.       IN A     213.154.225.244
issue.intra.cacert.org. IN A     172.16.2.28
issue.cacert.org.       IN SSHFP 2 1 FD9A5C79C4A9057B87AE8E639FD223B386AF4BDB
issue.cacert.org.       IN SSHFP 1 1 3F55E52B51D142EF9D15EEAA9CA25B3AA30C7C6E
======================= ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.11

* Debian GNU/Linux 7.11

.. todo:: upgrade to Debian Jessie

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+---------+----------+--------------------------------------------------+
| Port     | Service | Origin   | Purpose                                          |
+==========+=========+==========+==================================================+
| 22/tcp   | ssh     | ANY      | admin console access                             |
+----------+---------+----------+--------------------------------------------------+
| 25/tcp   | smtp    | localnet | local mail pickup in order to send out           |
|          |         |          | notifications via                                |
|          |         |          | :doc:`emailout`, incoming mail from :doc:`email` |
+----------+---------+----------+--------------------------------------------------+
| 80/tcp   | http    | ANY      | HTTP access to issue, redirects to HTTPS         |
+----------+---------+----------+--------------------------------------------------+
| 443/tcp  | https   | ANY      | HTTPS access to issue                            |
+----------+---------+----------+--------------------------------------------------+
| 5666/tcp | nrpe    | monitor  | remote monitoring service                        |
+----------+---------+----------+--------------------------------------------------+
| 3306/tcp | mysql   | local    | MySQL database for OTRS                          |
+----------+---------+----------+--------------------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: cron
   single: nrpe
   single: openssh
   single: rsyslog

+--------------------+-----------------------------------+----------------------------------------+
| Service            | Usage                             | Start mechanism                        |
+====================+===================================+========================================+
| openssh server     | ssh daemon for                    | init script :file:`/etc/init.d/ssh`    |
|                    | remote                            |                                        |
|                    | administration                    |                                        |
+--------------------+-----------------------------------+----------------------------------------+
| Apache httpd       | Webserver for OTRS                | init script                            |
|                    |                                   | :file:`/etc/init.d/apache2`            |
+--------------------+-----------------------------------+----------------------------------------+
| cron               | job scheduler                     | init script :file:`/etc/init.d/cron`   |
+--------------------+-----------------------------------+----------------------------------------+
| rsyslog            | syslog daemon                     | init script                            |
|                    |                                   | :file:`/etc/init.d/syslog`             |
+--------------------+-----------------------------------+----------------------------------------+
| MySQL              | MySQL database                    | init script                            |
|                    | server for OTRS                   | :file:`/etc/init.d/mysql`              |
+--------------------+-----------------------------------+----------------------------------------+
| Postfix            | SMTP server for                   | init script                            |
|                    | local mail                        | :file:`/etc/init.d/postfix`            |
|                    | submission and for receiving mail |                                        |
|                    | directed to OTRS addresses        |                                        |
+--------------------+-----------------------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring                 | init script                            |
|                    | service queried by                | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`                    |                                        |
+--------------------+-----------------------------------+----------------------------------------+

Databases
---------

+-------+------+-------------------+
| RDBMS | Name | Used for          |
+=======+======+===================+
| MySQL | otrs | database for OTRS |
+-------+------+-------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`email`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`email` as SMTP submission relay (587, tcp) for specific addresses (see
  :ref:`postfix_configuration` below)
* ftp.nl.debian.org as Debian mirror* security.debian.org for Debian security updates
* crl.cacert.org (rsync) for getting CRLs

Security
========

.. add the MD5 fingerprints of the SSH host keys

.. sshkeys::
   :RSA:     61:32:04:12:e3:4f:0b:b7:14:2d:d1:8f:82:b2:c7:47
   :DSA:     a8:57:20:2f:09:a2:f3:d6:24:7a:29:35:2f:28:5e:4e
   :ECDSA:   f1:a9:da:27:1a:ef:a8:67:51:d1:b4:e2:b7:83:c8:82

.. todo:: setup ED25519 host key

Non-distribution packages and modifications
-------------------------------------------

:program:`OTRS` is installed from Debian packages but has been patched. The
OTRS packages must not be updated from Debian packages without reapplying the
patch.

:file:`/usr/share/otrs/Kernel/Output/HTML/Layout.pm`

.. literalinclude:: ../patches/otrs/Layout.pm.patch
   :language: diff

Risk assessments on critical packages
-------------------------------------

Patching OTRS implies the danger of delayed security updates. The package is
set on hold via :command:`echo otrs hold | dpkg --set-selections` and must be
updated explicitly. OTRS 3.1 is not supported by upstream anymore.

The used Apache httpd has a good reputation. OTRS is integrated into Apache
httpd via mod_perl2.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

The following certificate and its corresponding private key is used by Apache
httpd and Postfix:

.. sslcert:: issue.cacert.org
   :altnames:   DNS:issue.cacert.org
   :certfile:   /etc/ssl/certs/issue.cacert.org.pem
   :keyfile:    /etc/ssl/private/issue.cacert.org.key
   :serial:     11E87C
   :expiration: Mar 31 20:51:43 18 GMT
   :sha1fp:     03:78:A8:C2:2C:53:00:29:41:A2:94:34:3D:3B:53:F2:43:2E:1E:03
   :issuer:     CA Cert Signing Authority

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache httpd configuration
--------------------------

* :file:`/etc/apache2/sites-available/default`

  HTTP virtualhost configuration that redirects to HTTPS

* :file:`/etc/apache2/sites-available/default-ssl`

  HTTPS virtualhost configuration, /cgi-bin/ is aliased to /usr/lib/cgi-bin/
  which contains a symbolic link to the OTRS CGIs

OTRS configuration
------------------

* :file:`/etc/otrs/`

  OTRS configuration

* :file:`/etc/otrs/database.pm`

  OTRS's database configuration


.. _postfix_configuration:

Postfix configuration
---------------------

* :file:`/etc/postfix`

  Postfix configuration

* :file:`/etc/postfix/sender_relay`

  Defines a list of sender addresses that are relayed via :doc:`email`

* :file:`/etc/postfix/sender_rewrite`

  Configures rewriting of all but a short list of addresses to
  returns@cacert.org

Tasks
=====

Planned
-------

Ideas
-----

* The system should be upgraded to a newer Debian release.

* Deployment

  * implement access for other teams

* OTRS

  * change to CAcert corporate design (low priority)
  * should be updated to a newer release that is supported by upstream

* Monitoring

  * create a list of services to monitor

* Configuration management

  * Implement :wiki:`SystemAdministration/Procedures/OperatingSystemPatches`,
    see also
    https://lists.cacert.org/wws/arc/cacert-sysadm/2009-08/msg00007.html

* X.509 Authentication

* Use centralised logging


Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

Creating new OTRS user accounts
-------------------------------

* Go to Admin -> Users -> Add
* Fill out user details

  * Use a securely random generated password (min. 12 chars, mixed of capital-
    non-capital letters, numbers and special chars), send it to the user via
    encrypted mail (also include URL of the issue tracking system, username and
    some initial instructions or a link to documentation if available)
  * Use CAcert email addresses only

* Set the preferences for the user. Good standards are:

  * Show tickets: 25
  * New ticket notification: Yes (or No for high volume queues having agents regulary looking at
  * Follow up notification: Yes
  * Ticket lock timeout notification: Yes
  * Move notification: Yes (or No if the queues for the user get many new tickets)
  * Spelling Dictionary: English 

* Submit
* Do NOT set any groups for the user.
* Go to Admin -> Users -> Roles <-> Users
* Choose the newly created user
* Set the roles the user has
* Submit
* Now you are done :) 


.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

* http://doc.otrs.com/doc/manual/admin/3.2/en/html/index.html
