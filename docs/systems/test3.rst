.. index::
   single: Systems; test

=====
Test3
=====

Purpose
=======

This is a test system for the software from cacertgit:`cacert-devel`'s
*release* branch running on www.cacert.org.

Application Links
-----------------

Application
     https://test3.cacert.org:14943/

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
:IP Intranet: :ip:v4:`172.16.2.149`
:IP Internal: :ip:v4:`10.0.0.149`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::149`
:MAC address: :mac:`00:ff:ce:d1:22:1d` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Test3

======================= ======== ====================================================================
Name                    Type     Content
======================= ======== ====================================================================
test3.cacert.org.       IN SSHFP 1 1 39FD3B77396529F83E095FF09C59994C47D9E0D3
test3.cacert.org.       IN SSHFP 1 2 680FE134289E79678F7EAA5689FDCE3DB5EFED9F6EBEFD5BCFADCE04A96475C1
test3.cacert.org.       IN SSHFP 2 1 70F5730C127BD701FC5C4BABA329E93346A975C1
test3.cacert.org.       IN SSHFP 2 2 364252B906AEC15A00994620D5C90C0F692A41CBC8C6F3BFC229149511209328
test3.cacert.org.       IN SSHFP 3 1 E4D81B532DC90EBB6D087AE732CE016B87945EBD
test3.cacert.org.       IN SSHFP 3 2 71B5AEDCC999E6FFC0F90EEB9254C8771DDAA6A4981CF55E8E2228F6BDEE64CE
test3.cacert.org.       IN SSHFP 4 1 50B22453F5C8D845895BACCCBC1FC325D033F65D
test3.cacert.org.       IN SSHFP 4 2 A928B84465769480D70DFC5ECD3AF2E4CDB192EE11D1CFFC4F31EA1FBED09D41
test3.cacert.org.       IN A     213.154.225.248
test3.infra.cacert.org. IN A     10.0.0.149
======================= ======== ====================================================================

.. todo:: add AAAA record for IPv6 address
.. todo:: add intra.cacert.org. A record

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.6

* Debian GNU/Linux 9.6

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
   single: puppet agent
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
| Puppet agent   | configuration                  | init script                            |
|                | management agent               | :file:`/etc/init.d/puppet`             |
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
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT and Github
* crl.cacert.org (rsync) for getting CRLs
* ocsp.cacert.org (HTTP and HTTPS) for OCSP queries
* arbitrary Internet SMTP servers for outgoing mail

Security
========

.. sshkeys::
   :RSA:     SHA256:aA/hNCieeWePfqpWif3OPbXv7Z9uvv1bz63OBKlkdcE MD5:ff:56:e4:71:17:f0:6c:27:d9:a8:bc:45:c6:f9:3e:57
   :DSA:     SHA256:NkJSuQauwVoAmUYg1ckMD2kqQcvIxvO/wikUlREgkyg MD5:d3:88:96:39:08:bd:71:97:37:99:7c:a7:99:30:4d:e4
   :ECDSA:   SHA256:cbWu3MmZ5v/A+Q7rklTIdx3apqSYHPVejiIo9r3uZM4 MD5:96:65:fe:5a:4d:e6:b0:31:01:b8:4a:40:62:4a:86:61
   :ED25519: SHA256:qSi4RGV2lIDXDfxezTry5M2xku4R0c/8TzHqH77QnUE MD5:20:10:47:d4:b8:04:e5:ed:2a:10:65:31:79:66:fc:c3

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

.. todo::

   clarify why the signer software on test3 is currently running as the root
   user

Non-distribution packages and modifications
-------------------------------------------

The setup is similar to :doc:`test`.

Risk assessments on critical packages
-------------------------------------

The operating system is up-to-date

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. todo:: document certificates on test3

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. todo:: document openssl configuration for the signer server on test3

.. todo:: document Apache httpd configuration on test3

.. todo:: document Postfix configuration on test3

.. todo:: document Dovecot configuration

Tasks
=====

Planned
-------

.. todo:: implement git workflows for updates maybe using :doc:`jenkins`

Changes
=======

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
