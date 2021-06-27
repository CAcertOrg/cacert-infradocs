.. index::
   single: Systems; test2

=====
Test2
=====

Purpose
=======

This is a test system that is as close to the real :doc:`../critical/webdb`
system. It is used by the critical admin team to test patches before bringing
them into production.

Application Links
-----------------

Application
    https://test2.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: :ref:`people_dirk`

Application Administration
--------------------------

+------------------------+--------------------+
| Application            | Administrator(s)   |
+========================+====================+
| CAcert web application | :ref:`people_dirk` |
+------------------------+--------------------+

Contact
-------

* test2-admin@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.249`
:IP Intranet: :ip:v4:`172.16.2.249`
:IP Internal: :ip:v4:`10.0.0.249`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::249`
:MAC address: :mac:`00:ff:8a:60:d6:dd` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Test2

Monitoring
----------

.. todo:: setup monitoring for test2

DNS
---

.. index::
   single: DNS records; Test2

+-------------------+----------+--------------------------------------------------------------------------+
| Name              | Type     | Content                                                                  |
+===================+==========+==========================================================================+
| test2.cacert.org. | IN A     | ``213.154.225.249``                                                      |
+-------------------+----------+--------------------------------------------------------------------------+
| test2.cacert.org. | IN SSHFP | ``1 1 6CF47397AFD468336DC07A27F7FC00797693FE12``                         |
+-------------------+----------+--------------------------------------------------------------------------+
| test2.cacert.org. | IN SSHFP | ``1 2 C008E67B906AF92DF0C9CF30A1C5DF998D2B47CB518698FB2974193C07CE7F40`` |
+-------------------+----------+--------------------------------------------------------------------------+
| test2.cacert.org. | IN SSHFP | ``2 1 666DF52C894AAFA85FB3A890077BC29046DF9B96``                         |
+-------------------+----------+--------------------------------------------------------------------------+
| test2.cacert.org. | IN SSHFP | ``2 2 E5794CFF631FACB7C294CC6727A5335E15BD39041DF3E73E3440DB3A995EA43A`` |
+-------------------+----------+--------------------------------------------------------------------------+

.. todo:: add AAAA record for IPv6 address

.. todo:: add SSHFP records for ECDSA and ED25519 host keys

.. todo:: remove SSHFP records for DSA host key

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.11

* Debian GNU/Linux 8.11 Jessie

Services
========

Listening services
------------------

+----------+---------+---------+-------------------------------------------+
| Port     | Service | Origin  | Purpose                                   |
+==========+=========+=========+===========================================+
| 22/tcp   | ssh     | ANY     | admin console access                      |
+----------+---------+---------+-------------------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA                |
+----------+---------+---------+-------------------------------------------+
| 80/tcp   | http    | ANY     | Apache httpd for http://test.cacert.org/  |
+----------+---------+---------+-------------------------------------------+
| 123/tcp  | ntp     | local   | network time protocol server              |
| 123/udp  |         |         |                                           |
+----------+---------+---------+-------------------------------------------+
| 143/tcp  | imap    | testmgr | Dovecot IMAP server                       |
+----------+---------+---------+-------------------------------------------+
| 443/tcp  | https   | ANY     | Apache httpd for https://test.cacert.org/ |
+----------+---------+---------+-------------------------------------------+
| 3306/tcp | mysql   | local   | MySQL database for WebDB                  |
+----------+---------+---------+-------------------------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service                 |
+----------+---------+---------+-------------------------------------------+

Running services
----------------

.. index::
   single: Apache httpd
   single: MySQL
   single: acpid
   single: atop
   single: client.pl
   single: cron
   single: nrpe
   single: openssh
   single: postfix
   single: rsyslog
   single: signer.pl
   single: socat

+----------------+--------------------------------+----------------------------------------+
| Service        | Usage                          | Start mechanism                        |
+================+================================+========================================+
| Apache httpd   | Webserver for the CAcert       | init script                            |
|                | web application                | :file:`/etc/init.d/apache2`            |
+----------------+--------------------------------+----------------------------------------+
| MySQL          | MySQL database server          | init script                            |
|                | for the CAcert web application | :file:`/etc/init.d/mysql`              |
+----------------+--------------------------------+----------------------------------------+
| acpid          | ACPI daemon                    | systemd unit ``acpid.service``         |
+----------------+--------------------------------+----------------------------------------+
| atop           | atop process accounting top    | init script                            |
|                |                                | :file:`/etc/init.d/atop`               |
+----------------+--------------------------------+----------------------------------------+
| client.pl      | CAcert signer client           | init script                            |
|                |                                | :file:`/etc/init.d/commmodule`         |
+----------------+--------------------------------+----------------------------------------+
| cron           | job scheduler                  | init script                            |
|                |                                | :file:`/etc/init.d/cron`               |
+----------------+--------------------------------+----------------------------------------+
| dovecot        | Dovecot IMAP server            | init script                            |
|                |                                | :file:`/etc/init.d/dovecot`            |
+----------------+--------------------------------+----------------------------------------+
| Nagios NRPE    | remote monitoring              | init script                            |
| server         | service queried by             | :file:`/etc/init.d/nagios-nrpe-server` |
|                | :doc:`monitor`                 |                                        |
+----------------+--------------------------------+----------------------------------------+
| ntpd           | Network time protocol server   | init script                            |
|                |                                | :file:`/etc/init.d/ntp`                |
+----------------+--------------------------------+----------------------------------------+
| openssh server | ssh daemon for remote          | init script :file:`/etc/init.d/ssh`    |
|                | administration                 |                                        |
+----------------+--------------------------------+----------------------------------------+
| postfix        | SMTP server for local mail     | init script                            |
|                | submission                     | :file:`/etc/init.d/postfix`            |
+----------------+--------------------------------+----------------------------------------+
| rsyslog        | syslog daemon                  | init script                            |
|                |                                | :file:`/etc/init.d/syslog`             |
+----------------+--------------------------------+----------------------------------------+
| server.pl      | CAcert signer server           | init script                            |
|                |                                | :file:`/etc/init.d/commmodule-signer`  |
+----------------+--------------------------------+----------------------------------------+
| socat          | Emulate serial connection      | entry in                               |
|                | between CAcert signer          | :file:`/etc/rc.local` that executes    |
|                | client and server              | :file:`/usr/local/sbin/socat-signer`   |
|                |                                | inside a :program:`screen` session     |
+----------------+--------------------------------+----------------------------------------+

Databases
---------

+-------+--------+------------------------+
| RDBMS | Name   | Used for               |
+=======+========+========================+
| MySQL | cacert | CAcert web application |
+-------+--------+------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`proxyout` as HTTP proxy for APT and Github

Security
========

.. sshkeys::
   :RSA: SHA256:wAjme5Bq+S3wyc8wocXfmY0rR8tRhpj7KXQZPAfOf0A MD5:99:f4:e6:78:7a:57:d6:9d:a9:b8:ca:f3:ce:07:cc:57
   :DSA: SHA256:5XlM/2MfrLfClMxnJ6UzXhW9OQQd8+c+NEDbOplepDo MD5:0f:56:a7:04:b5:f4:48:b9:fa:2c:1e:58:de:d3:e8:cb

.. todo:: generate ECDSA and ED25519 host keys

.. todo:: remove DSA host key

Dedicated user roles
--------------------

+------------+----------------------------+
| User       | Purpose                    |
+============+============================+
| cacertmail | IMAP mailbox user          |
+------------+----------------------------+
| signer     | User for the CAcert signer |
+------------+----------------------------+

.. todo::

   clarify why the signer software on test2 is currently running as the root
   user

The directory :file:`/home/cacert/` is owned by root. The signer is running
from :file:`/home/signer/cacert-devel/CommModule/server.pl` the client is
running from :file:`/home/cacert/www/CommModule/client.pl`. Both are running as
root. Currently no process uses the *cacertsigner* user.

Non-distribution packages and modifications
-------------------------------------------

Apache httpd is running in a chroot :file:`/home/cacert/`, the configuration in
:file:`/etc/apache2` as well as the system binaries are not used. The Apache
httpd binary seems to be relatively up-to-date.

The CAcert WebDB application is stored in :file:`/home/cacert/www`.

The CAcert Signer code is stored in :file:`/home/signer/www/CommModule`.

.. todo::

   clarify the process how changes get into the WebDB and Signer directories
   and clarify differences to Git and :doc:`test`

Risk assessments on critical packages
-------------------------------------

The operating system on this container is no longer supported. The PHP version
in the file:`/home/cacert/` chroot is 5.6.40 which is no longer supported
upstream.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: cacert2.it-sls.de
   :certfile:   /home/cacert/etc/ssl/certs/cacert2_it-sls_de.crt
   :keyfile:    /home/cacert/etc/ssl/private/cacert2_it-sls_de.pem
   :serial:     4F66
   :expiration: Jun 20 15:24:50 2018 GMT
   :sha1fp:     61:D0:CF:1B:D7:36:EA:0A:41:02:72:9F:60:F0:E2:24:A1:9D:E7:01
   :issuer:     CAcert Testserver Root

.. sslcert:: ca-mgr2.it-sls.de
   :certfile:   /home/cacert/etc/ssl/certs/ca-mgr2_it-sls_de.crt
   :keyfile:    /home/cacert/etc/ssl/private/ca-mgr2_it-sls_de.pem
   :serial:     4F68
   :expiration: Jun 20 15:24:51 2018 GMT
   :sha1fp:     00:C6:36:22:DF:D7:3B:97:A2:B3:20:07:BC:B8:84:0F:61:42:20:11
   :issuer:     CAcert Testserver Root

.. sslcert:: mgr.test2.cacert.org
   :altnames:   DNS:mgr.test2.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/mgr_test2_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/mgr_test2_cacert_org.pem
   :serial:     4F7E
   :expiration: Sep 11 06:47:03 2020 GMT
   :sha1fp:     04:C9:9B:5E:BB:BF:18:9F:1D:78:4B:0F:92:67:F7:35:D7:0D:5A:05
   :issuer:     CAcert Testserver Root

.. sslcert:: secure2.it-sls.de
   :certfile:   /home/cacert/etc/ssl/certs/secure2_it-sls_de.crt
   :keyfile:    /home/cacert/etc/ssl/private/secure2_it-sls_de.pem
   :serial:     4F67
   :expiration: Jun 20 15:24:50 2018 GMT
   :sha1fp:     90:A5:52:72:7D:59:D7:16:99:5F:1A:FA:6F:49:40:1C:F0:82:95:C3
   :issuer:     CAcert Testserver Root

.. sslcert:: secure.test2.cacert.org
   :altnames:   DNS:secure.test2.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/secure_test2_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/secure_test2_cacert_org.pem
   :serial:     4F7D
   :expiration: Sep 11 06:47:03 2020 GMT
   :sha1fp:     EB:72:5A:37:B0:51:3C:46:77:7E:C4:1E:16:1E:87:F6:10:B1:A1:A5
   :issuer:     CAcert Testserver Root

.. sslcert:: test2.cacert.org
   :altnames:   DNS:test2.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/test2_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/test2_cacert_org.pem
   :serial:     4F7C
   :expiration: Sep 11 06:47:03 2020 GMT
   :sha1fp:     7D:BE:55:1A:C4:37:C5:BC:D9:98:2F:F5:09:A1:B9:83:22:CF:2D:56
   :issuer:     CAcert Testserver Root

.. todo::

   clarify whether old it-sls.de certificates can be decommissioned

**CA certificates on test**:

.. sslcert:: CAcert Testserver Root
   :certfile:   /etc/ssl/CA/cacert.crt
   :keyfile:    /etc/ssl/CA/cacert.pem
   :serial:     00
   :secondary:

.. sslcert:: CAcert Testserver Class 3
   :certfile:   /etc/ssl/class3/cacert.crt
   :keyfile:    /etc/ssl/class3/cacert.pem
   :serial:     101B
   :secondary:

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

openssl configuration for the signer server
-------------------------------------------

There are some openssl configuration files that are used by the server.pl
signer that are stored in :file:`/etc/ssl/{caname}-{purpose}.cnf`.

.. todo::

   check whether the openssl configuration files on test2 are equal to those in
   http://svn.cacert.org/CAcert/SystemAdministration/signer/ssl/

Apache httpd configuration
--------------------------

Apache httpd is running in a chroot :file:`/home/cacert/` its configuration is
stored in :file:`/home/cacert/etc/apache2`.

Postfix configuration
---------------------

Postfix configuration is stored in :file:`/etc/postfix`.

Postfix is configured to accept mail for ``cacert2.it-sls.de``,
``localhost.it-sls.de`` and ``localhost`` all mail is delivered to the mailbox
of the *cacertmail* user in :file:`/var/mail/cacertmail` via
:file:`/etc/postfix/virtual.regexp`.

.. todo::

   reconfigure postfix on test2 to use the correct hostnames

Dovecot configuration
---------------------

Dovecot is configured via configuration in :file:`/etc/dovecot`.

.. todo::

   check dovecot configuration on test2, compare with test and/or production
   webdb system

Tasks
=====

Changes
=======

Planned
-------

.. todo::

   ensure that test2 is really similar to webdb, implement a proper deployment
   process to support real staging

System Future
-------------

.. * No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Apache httpd documentation
  http://httpd.apache.org/docs/2.4/
Apache Debian wiki page
  https://wiki.debian.org/Apache
Dovecot documentation
  https://wiki2.dovecot.org/FrontPage
openssl documentation
  https://www.openssl.org/docs/
Postfix documentation
  http://www.postfix.org/documentation.html
Postfix Debian wiki page
  https://wiki.debian.org/Postfix
