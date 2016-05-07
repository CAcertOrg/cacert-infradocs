.. index::
   single: Systems; Email

=====
Email
=====

Purpose
=======

This system handles email for @cacert.org addresses. It also provides users of
@cacert.org with IMAPs and POP3s access to their accounts.

The database on this container is used by :doc:`webmail` too.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jselzer`
* Secondary: :ref:`people_jandd`

Contact
-------

* email-admin@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.228`
:IP Intranet: :ip:v4:`172.16.2.19`
:IP Internal: :ip:v4:`10.0.0.19`
:MAC address: :mac:`00:ff:8f:e0:4a:90` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Email

======================= ======== ============================================
Name                    Type     Content
======================= ======== ============================================
email.cacert.org.       IN A     213.154.225.228
email.cacert.org.       IN SSHFP 1 1 BF391FD72656A275524D1D25A624C6045B44AE90
email.cacert.org.       IN SSHFP 2 1 73B0D8ACB492A7187016DD3C5FC1519B309A550F
email.intra.cacert.org. IN A     172.16.2.19
======================= ======== ============================================

A DKIM record for cacert.org ist setup but no DKIM signing is active currently.

.. todo:: setup DKIM properly, see :bug:`696` for an older discussion

.. todo:: setup SPF records when the system is ready, see :bug:`492` for an
   older discussion

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Lenny
   single: Debian GNU/Linux; 5.0.10

* Debian GNU/Linux 5.0.10

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+---------+----------------+-----------------------------------------------+
| Port     | Service | Origin         | Purpose                                       |
+==========+=========+================+===============================================+
| 22/tcp   | ssh     | ANY            | admin console access                          |
+----------+---------+----------------+-----------------------------------------------+
| 25/tcp   | smtp    | ANY            | mail receiver for cacert.org                  |
+----------+---------+----------------+-----------------------------------------------+
| 110/tcp  | pop3    | ANY            | POP3 access for cacert.org mail addresses     |
+----------+---------+----------------+-----------------------------------------------+
| 143/tcp  | imap    | ANY            | IMAP access for cacert.org mail addresses     |
+----------+---------+----------------+-----------------------------------------------+
| 465/tcp  | smtps   | ANY            | SMTPS for cacert.org mail addresses           |
+----------+---------+----------------+-----------------------------------------------+
| 587/tcp  | smtp    | ANY            | mail submission for cacert.org mail addresses |
+----------+---------+----------------+-----------------------------------------------+
| 993/tcp  | imaps   | ANY            | IMAPS access for cacert.org mail addresses    |
+----------+---------+----------------+-----------------------------------------------+
| 995/tcp  | pop3s   | ANY            | POP3S access for cacert.org mail addresses    |
+----------+---------+----------------+-----------------------------------------------+
| 2000/tcp | sieve   | ANY            | Sieve access for cacert.org mail addresses    |
+----------+---------+----------------+-----------------------------------------------+
| 2001/tcp | sieve   | :doc:`webmail` | Sieve access for cacert.org mail              |
|          |         |                | addresses without TLS, accessible from        |
|          |         |                | ``172.16.2.20`` only                          |
+----------+---------+----------------+-----------------------------------------------+
| 3306/tcp | mysql   | local          | MySQL database server                         |
+----------+---------+----------------+-----------------------------------------------+
| 4433/tcp | http    | internal       | Apache httpd with phpmyadmin                  |
+----------+---------+----------------+-----------------------------------------------+
| 5666/tcp | nrpe    | monitor        | remote monitoring service                     |
+----------+---------+----------------+-----------------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: cron
   single: dovecot
   single: nrpe
   single: openssh
   single: pysieved
   single: rsyslog
   single: xinetd

+--------------------+---------------------+----------------------------------------+
| Service            | Usage               | Start mechanism                        |
+====================+=====================+========================================+
| Apache httpd       | Webserver for       | init script                            |
|                    | phpmyadmin          | :file:`/etc/init.d/apache2`            |
+--------------------+---------------------+----------------------------------------+
| cron               | job scheduler       | init script :file:`/etc/init.d/cron`   |
+--------------------+---------------------+----------------------------------------+
| dovecot            | IMAP(s) and POP3(s) | init script                            |
|                    | daemon              | :file:`/etc/init.d/dovecot`            |
+--------------------+---------------------+----------------------------------------+
| MySQL              | MySQL database      | init script                            |
|                    | server for email    | :file:`/etc/init.d/mysql`              |
|                    | services            |                                        |
+--------------------+---------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring   | init script                            |
|                    | service queried by  | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`      |                                        |
+--------------------+---------------------+----------------------------------------+
| openssh server     | ssh daemon for      | init script :file:`/etc/init.d/ssh`    |
|                    | remote              |                                        |
|                    | administration      |                                        |
+--------------------+---------------------+----------------------------------------+
| Postfix            | SMTP server for     | init script                            |
|                    | cacert.org          | :file:`/etc/init.d/postfix`            |
+--------------------+---------------------+----------------------------------------+
| rsyslog            | syslog daemon       | init script                            |
|                    |                     | :file:`/etc/init.d/syslog`             |
+--------------------+---------------------+----------------------------------------+
| xinetd             | socket listener     | init script                            |
|                    | for pysieved        | :file:`/etc/init.d/xinetd`             |
+--------------------+---------------------+----------------------------------------+

Databases
---------

+-------+----------------+----------------------------------+
| RDBMS | Name           | Used for                         |
+=======+================+==================================+
| MySQL | cacertusers    | database for dovecot and postfix |
+-------+----------------+----------------------------------+
| MySQL | postfixpolicyd | empty database                   |
+-------+----------------+----------------------------------+
| MySQL | roundcubemail  | roundcube on :doc:`webmail`      |
+-------+----------------+----------------------------------+

.. todo:: check whether the empty postfixpolicyd database is required

.. todo:: consider moving the databases to a new central MySQL service

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`webmail`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* archive.debian.org as Debian mirror
* :doc:`issue` for OTRS mail
* :doc:`lists` for mailing lists
* arbitrary internet smtp servers for outgoing mail

Security
========

.. sshkeys::
   :RSA: a1:d2:17:53:6b:0f:b6:a4:14:13:46:f7:04:ef:4a:23
   :DSA: f4:eb:0a:36:40:1c:55:6b:75:a2:26:34:ea:18:7e:91

.. warning::

   The system is too old to support ECDSA or ED25519 keys.

Non-distribution packages and modifications
-------------------------------------------

Tlslite in :file:`/usr/local/lib/tlslite-0.3.8/` has been patched to handle
GeneratorExit exceptions. The original tlslite 0.3.8 is stored in
:file:`/usr/local/lib/tlslite-0.3.8-orig/`.

Pysieved in :file:`/usr/local/lib/pysieved.neale/` seems to be a git clone from
2009 originating from http://woozle.org/~neale/repos/pysieved at commit
``d9b67036387a9a7aca954a17ff6fec44a8d309e0`` with no local modifications.

:file:`/usr/local/lib/pysieved` is a symbolic link to
:file:`/usr/local/lib/pysieved.neale/`.

.. todo:: use pysieved, python-tlslite and dovecot-sieve from distribution
   packages after OS upgrade


Risk assessments on critical packages
-------------------------------------

The whole system is outdated, it needs to be replaced as soon as possible.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

Server certificate for SMTP communication from the Internet and PHPMyAdmin.

.. sslcert:: email.cacert.org
   :certfile:   /etc/ssl/certs/ssl-cert-email-cacert.pem
   :keyfile:    /etc/ssl/private/ssl-cert-email-cacert.key
   :serial:     11e84a
   :expiration: Mar 31 19:50:03 2018 GMT
   :sha1fp:     49:5E:55:35:F4:D5:69:B1:BD:92:14:94:38:CD:40:6D:97:A7:2A:0A
   :issuer:     CAcert.org Class 1 Root CA

Server certificate for community email services (SMTPS, SMTP submission in
Postfix and IMAP with STARTTLS, IMAPS, POP3 with STARTTLS, POP3S and pysieved)

.. sslcert:: community.cacert.org
   :certfile:  /etc/ssl/certs/ssl-cert-community-cacert.pem
   :keyfile:   /etc/ssl/private/ssl-cert-community-cacert.key
   :serial:    11e846
   :secondary:

* :file:`/etc/postfix/dh_1024.pem` and :file:`/etc/postfix/dh_512.pem`
  Diffie-Hellman parameter files for Postfix

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache configuration
--------------------

:file:`/etc/apache2/sites-available/adminssl` configures a VirtualHost that
allows dedicated users to access a PHPMyAdmin instance. The allowed users are
authenticated by client certificates and are authorized by an entry in
:file:`/etc/apache2/phpmyadmin.passwd`.

.. note::

   to authorize a user you need the subject distinguished name of the user's
   client certificate which can be extracted with::

      openssl x509 -noout -subject -in certificate.crt

   A line with the subject distinguished name and the fake password
   ``xxj31ZMTZzkVA`` separated by colon have to be added to
   :file:`/etc/apache2/phpmyadmin.passwd`::

      /CN=Example User/emailAddress=example@cacert.org:xxj31ZMTZzkVA

.. seealso::

   FakeBasicAuth option of the `SSLOptions
   <https://httpd.apache.org/docs/2.2/mod/mod_ssl.html#ssloptions>`_
   directive in the mod_ssl reference documentation.

MySQL configuration
-------------------

MySQL configuration is stored in the :file:`/etc/mysql/` directory.

NSS configuration
-----------------

The libc name service switch is configured to use MySQL lookups for passwd,
group and shadow via :file:`/etc/nsswitch.conf`. The queries are configured in
:file:`/etc/libnss-mysql.cfg` and the root user for reading shadow information
is configured in :file:`/etc/libnss-mysql-root.cfg`.

PHPMyAdmin configuration
------------------------

PHPMyAdmin configuration is stored in the :file:`/etc/phpmyadmin/` directory.

Dovecot configuration
---------------------

Dovecot configuration is stored in the :file:`/etc/dovecot/` directory. The
database settings are stored in
:file:`dovecot-sql-masterpassword-webmail.conf`.

Postfix configuration
---------------------

Postfix configuration is stored in the :file:`/etc/postfix/` directory. The
following files are special for this setup:

+----------------+-------------------------------------------------------------+
| File           | Used for                                                    |
+================+=============================================================+
| arbitration    | rewrite recipients matching specific regular expressions to |
|                | support+deletedaccounts@cacert.org and                      |
|                | support@issue.cacert.org                                    |
+----------------+-------------------------------------------------------------+
| cacert-inc-bcc | used as recipient_bcc_maps for specific functional mail     |
|                | addresses                                                   |
+----------------+-------------------------------------------------------------+
| main.cf        | the main configuration file                                 |
+----------------+-------------------------------------------------------------+
| master.cf      | adds configuration for the community SMTPS and SMTP         |
|                | submission transports                                       |
+----------------+-------------------------------------------------------------+
| mysql-\*.cf    | configuration of several MySQL queries for alias mapping,   |
|                | Postfix operates on views for the user table                |
+----------------+-------------------------------------------------------------+
| transport      | forward email for lists.cacert.org to :doc:`lists` and for  |
|                | issue.cacert.org to :doc:`issue`                            |
+----------------+-------------------------------------------------------------+

.. todo:: consider to send all outgoing mail via :doc:`emailout`

.. todo:: remove unused transports from :file:`master.cf`

PySieved configuration
----------------------

:file:`/usr/local/etc/pysieved.ini` and
:file:`/usr/local/etc/pysieved-notls.ini`. Pysieved uses dovecot for
authentication.

Rsyslog configuration
---------------------

Rsyslog is configured in :file:`/etc/rsyslog.conf` which includes files in
:file:`/etc/rsyslog.d/`. Consumption of kernel log messages and network input
is disabled. :file:`/etc/rsyslog.d/postfix.conf` configures a separate unix
socket to receive log messages from postfix and
:file:`/etc/rsyslog.d/remotelog.conf` contains commented settings for a
non-existant remote syslog server.

.. todo:: setup remote logging when a central logging container is available

Xinetd configuration
--------------------

Xinetd listens on tcp ports 2000 and 2001 and spawn pysieved. Configuration for
these listeners is stored in :file:`/etc/xinetd.d/pysieved` and
:file:`/etc/xinetd.d/pysieved-notls`.

Tasks
=====

Planned
-------

.. todo:: implement CRL checking

.. todo:: setup IPv6

Changes
=======

System Future
-------------

.. todo::
   The system has to be replaced with a new system using a current operating
   system version

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Wiki page for this system
   :wiki:`SystemAdministration/Systems/Email`
