.. index::
   single: Systems; test

====
Test
====

Purpose
=======

This is a test system for the software from cacertgit:`cacert-devel`'s
*release* branch running on www.cacert.org.

Application Links
-----------------

Application
     https://test.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_wytze`
* Secondary: :ref:`people_jandd`


Application Administration
--------------------------

+------------------------+---------------------------------------+
| Application            | Administrator(s)                      |
+========================+=======================================+
| CAcert web application | :ref:`people_dirk`, :ref:`people_ted` |
+------------------------+---------------------------------------+

Contact
-------

* test-admin@cacert.org

Additional People
-----------------

:ref:`people_dirk`, :ref:`people_gukk`, :ref:`people_mario`,
:ref:`people_mendel`, :ref:`people_neo` and :ref:`people_ted` have
:program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.248`
:IP Intranet: :ip:v4:`172.16.2.248`
:IP Internal: :ip:v4:`10.0.0.248`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::248`
:MAC address: :mac:`00:ff:91:10:5d:cd` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Test

Monitoring
----------

:internal checks: :monitor:`test.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Test

====================== ======== ============================================
Name                   Type     Content
====================== ======== ============================================
test.cacert.org.       IN A     213.154.225.248
test.cacert.org.       IN SSHFP 1 1 11BCB0AB4D1FD39547426D9527B88AFB8FF85209
test.cacert.org.       IN SSHFP 2 1 3414C17E5AE898B2F5DB7B3DDF9E34C2F5E816AC
test.intra.cacert.org. IN A     172.16.2.248
test.infra.cacert.org. IN A     10.0.0.248
====================== ======== ============================================

.. todo:: add AAAA record for IPv6 address

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.11

* Debian GNU/Linux 8.11

Applicable Documentation
------------------------

There is no additional documentation for this system.

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
| 993/tcp  | imaps   | testmgr | Dovecot IMAP server                       |
+----------+---------+---------+-------------------------------------------+
| 3306/tcp | mysql   | local   | MySQL database for ...                    |
+----------+---------+---------+-------------------------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service                 |
+----------+---------+---------+-------------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: atop
   single: client.pl
   single: cron
   single: dovecot
   single: nrpe
   single: ntpd
   single: openssh
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
| Postfix        | SMTP server for local mail     | init script                            |
|                | submission                     | :file:`/etc/init.d/postfix`            |
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
* :doc:`testmgr` has access to imap and MySQL

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`proxyout` as HTTP proxy for APT and Github
* crl.cacert.org (rsync) for getting CRLs
* ocsp.cacert.org (HTTP and HTTPS) for OCSP queries
* arbitrary Internet SMTP servers for outgoing mail

Security
========

.. todo:: add the SHA-256 fingerprints of the SSH host keys

.. sshkeys::
   :RSA:   fd:19:a1:64:ae:ef:c2:50:a2:be:a4:c5:9f:f7:9d:98
   :DSA:   1c:8c:39:5e:9e:0b:db:8e:c3:66:89:e3:3d:94:5e:13
   :ECDSA: ac:fb:c8:88:d1:dd:e5:38:99:34:7b:29:54:e1:f2:f1

.. todo:: add ED25519 key for test

Dedicated user roles
--------------------

.. If the system has some dedicated user groups besides the sudo group used for
   administration it should be documented here Regular operating system groups
   should not be documented

+--------------+----------------------------+
| User         | Purpose                    |
+==============+============================+
| cacertmail   | IMAP mailbox user          |
+--------------+----------------------------+
| cacertsigner | User for the CAcert signer |
+--------------+----------------------------+

.. todo::

   clarify why the signer software on test is currently running as the root
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

The CAcert web application code as well as the CAcert signer client code come
from :cacertgit:`cacert-devel`'s *release* branch.

The signer in :file:`/home/signer/cacert-devel/CommModule/server.pl` has a few
uncommitted manual modifications. And the whole working copy in
`/home/signer/cacert-devel` is based on an old repository at
git://git-cacert.it-sls.de/cacert-devel.git that is no longer available. The
last commit in the working copy is::

   commit 2262fe14e4bf1e0afb4ab7f9340e18a9f281ddfe
   Merge: c33bbc5 a3d0b8a
   Author: Michael Tänzer <neo@nhng.de>
   Date:   Wed Apr 10 00:03:42 2013 +0200

       Merge branch 'bug-1159' into signer

.. todo::

   integrate or revert the changes to server.pl on test, use the current
   *release* branch version from :cacertgit:`cacert-devel`

Risk assessments on critical packages
-------------------------------------

The operating system on this container is no longer supported. The PHP version
in the file:`/home/cacert/` chroot is 5.6.38 which is no longer supported
upstream

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: cats.test.cacert.org
   :altnames:   DNS:cats.test.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/cats_test_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/cats_test_cacert_org.pem
   :serial:     50D3
   :expiration: Sep 28 13:47:31 2019 GMT
   :sha1fp:     6C:03:0D:4F:91:56:EA:74:A4:E4:70:4A:91:B1:4C:A3:99:CC:9C:4B
   :issuer:     CAcert Testserver Root

.. sslcert:: mgr.test.cacert.org
   :altnames:   DNS:mgr.test.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/mgr_test_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/mgr_test_cacert_org.pem
   :serial:     50D2
   :expiration: Sep 28 13:47:31 2019 GMT
   :sha1fp:     C2:4B:F2:00:9B:A0:61:57:27:14:1C:08:47:50:6A:41:5B:D2:6F:05
   :issuer:     CAcert Testserver Root

.. sslcert:: secure.test.cacert.org
   :altnames:   DNS:secure.test.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/secure_test_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/secure_test_cacert_org.pem
   :serial:     50D1
   :expiration: Sep 28 13:47:30 2019 GMT
   :sha1fp:     95:9A:3A:1B:C2:03:D6:90:F5:01:4A:F7:52:62:2D:B8:61:BD:B7:4B
   :issuer:     CAcert Testserver Root

.. sslcert:: test.cacert.org (dovecot)
   :certfile:   /etc/dovecot/dovecot.pem
   :keyfile:    /etc/dovecot/private/dovecot.pem
   :serial:     C362AEFE86DA5BFE
   :expiration: Jun 26 12:38:31 2024 GMT
   :sha1fp:     1E:60:68:36:53:BC:95:A8:35:AC:A0:38:09:69:29:74:10:52:04:1A
   :issuer:     test.cacert.org

.. sslcert:: test.cacert.org
   :altnames:   DNS:test.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/test_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/cacert.pem
   :serial:     50D0
   :expiration: Sep 28 13:47:30 2019 GMT
   :sha1fp:     94:FE:B0:94:F6:7C:F2:E2:57:75:49:05:17:86:99:5C:CE:40:24:AD
   :issuer:     CAcert Testserver Root

**CA certificates on test**:

.. sslcert:: CAcert Testserver Root
   :certfile:   /etc/ssl/CA/cacert.crt
   :keyfile:    /etc/ssl/CA/cacert.pem
   :serial:     00
   :expiration: Mar 26 20:45:20 2021 GMT
   :sha1fp:     5B:26:E7:61:8C:C1:A1:EB:F3:E1:28:22:03:7A:D6:9B:55:53:C3:9B
   :issuer:     CAcert Testserver Root

.. sslcert:: CAcert Testserver Root
   :certfile:   /etc/ssl/CA/root_256.crt
   :keyfile:    /etc/ssl/CA/cacert.pem
   :serial:     0F
   :expiration: Mar 26 20:45:20 2021 GMT
   :sha1fp:     5E:7E:EE:06:07:0A:F6:A1:49:F9:E1:B1:13:14:D8:C2:A3:3C:07:52
   :issuer:     CAcert Testserver Root

.. sslcert:: CAcert Testserver Class 3
   :altnames:
   :certfile:   /etc/ssl/class3/cacert.md5.crt
   :keyfile:    /etc/ssl/class3/cacert.pem
   :serial:     01
   :expiration: Mar 26 22:06:10 2021 GMT
   :sha1fp:     F5:72:FF:19:C8:B5:3C:7C:29:1A:8D:90:92:09:5F:DD:24:C6:F8:41
   :issuer:     CAcert Testserver Root

.. sslcert:: CAcert Testserver Class 3
   :altnames:
   :certfile:   /etc/ssl/class3/cacert.crt
   :keyfile:    /etc/ssl/class3/cacert.pem
   :serial:     101B
   :expiration: Apr 28 18:25:09 2021 GMT
   :sha1fp:     52:F9:80:58:5F:55:A0:F6:51:F0:A2:BC:75:20:FE:2C:48:96:79:55
   :issuer:     CAcert Testserver Root

.. note::

   There are two directories :file:`/etc/root3/` and :file:`/etc/root4/` that
   are supported by the signer but do not contain actual keys and certificates.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

openssl configuration for the signer server
-------------------------------------------

There are some openssl configuration files that are used by the server.pl
signer that are stored in :file:`/etc/ssl/{caname}-{purpose}.cnf`.

.. todo::

   check whether the openssl configuration files on test are equal to those in
   http://svn.cacert.org/CAcert/SystemAdministration/signer/ssl/

Apache httpd configuration
--------------------------

Apache httpd is running in a chroot :file:`/home/cacert/` its configuration is
stored in :file:`/home/cacert/etc/apache2`.

Postfix configuration
---------------------

Postfix configuration is stored in :file:`/etc/postfix`.

Postfix is configured to accept mail for ``test.cacert.org`` and ``localhost``
all mail is delivered to the mailbox of the *cacertmail* user in
:file:`/var/mail/cacertmail` via :file:`/etc/postfix/virtual.regexp`.

Dovecot configuration
---------------------

Dovecot is configured to use pam for authentication and to support SSL and IMAP
and to use mbox style mailboxes in /var/mail/%u in the following files:

- :file:`/etc/dovecot/conf.d/10-auth.conf`
- :file:`/etc/dovecot/conf.d/10-mail.conf`
- :file:`/etc/dovecot/conf.d/20-imap.conf`
- :file:`/etc/dovecot/conf.d/auth-system.conf`

.. note::

   dovecot uses an old self-signed certificate for test.cacert.org

Tasks
=====

Changes
=======

Planned
-------

.. todo::

   Upgrade test to Debian Stretch when the software is ready.


System Future
-------------

.. * No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`
   * https://codedocs.cacert.org/

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
