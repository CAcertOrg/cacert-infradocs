.. index::
   single: Systems; Testmgr

=======
Testmgr
=======

Purpose
=======

This system is used for managing test users and reading mails from the test
system inbox.

Application Links
-----------------

Testmgr application
   https://test.cacert.org:14843/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_ted`
* Secondary: :ref:`people_dirk`

Application Administration
--------------------------

+--------------+-------------------+
| Application  | Administrator(s)  |
+==============+===================+
| Test manager | :ref:`people_ted` |
+--------------+-------------------+

Contact
-------

* bernhard@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.248`
:IP Intranet: :ip:v4:`172.16.2.248`
:IP Internal: :ip:v4:`10.0.0.148`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::148`
:MAC address: :mac:`00:16:3e:13:87:cc` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; testmgr

Monitoring
----------

.. add links to monitoring checks

:internal checks: :monitor:`template.infra.cacert.org`
:external checks: :monitor:`template.cacert.org`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 8.10

* Debian GNU/Linux 8.10

Services
========

Listening services
------------------

+----------+---------+--------+-----------------------------+
| Port     | Service | Origin | Purpose                     |
+==========+=========+========+=============================+
| 22/tcp   | ssh     | ANY    | admin console access        |
+----------+---------+--------+-----------------------------+
| 25/tcp   | smtp    | local  | mail delivery to local MTA  |
+----------+---------+--------+-----------------------------+
| 80/tcp   | http    | ANY    | application                 |
+----------+---------+--------+-----------------------------+
| 443/tcp  | https   | ANY    | application                 |
+----------+---------+--------+-----------------------------+
| 3306/tcp | mysql   | local  | MySQL database for testmgr  |
+----------+---------+--------+-----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: mysql
   single: openssh
   single: postfix
   single: rsyslog

+----------------+-----------------------+-----------------------------------------+
| Service        | Usage                 | Start mechanism                         |
+================+=======================+=========================================+
| Apache httpd   | Webserver for testmgr | init script :file:`/etc/init.d/apache2` |
+----------------+-----------------------+-----------------------------------------+
| cron           | job scheduler         | init script :file:`/etc/init.d/cron`    |
+----------------+-----------------------+-----------------------------------------+
| MySQL          | MySQL database        | init script                             |
|                | server for testmgr    | :file:`/etc/init.d/mysql`               |
+----------------+-----------------------+-----------------------------------------+
| openssh server | ssh daemon for        | init script :file:`/etc/init.d/ssh`     |
|                | remote administration |                                         |
+----------------+-----------------------+-----------------------------------------+
| Postfix        | SMTP server for       | init script :file:`/etc/init.d/postfix` |
|                | local mail submission |                                         |
+----------------+-----------------------+-----------------------------------------+
| rsyslog        | syslog daemon         | init script :file:`/etc/init.d/rsyslog` |
+----------------+-----------------------+-----------------------------------------+

Databases
---------

+--------+-------------+-----------------------------+
| RDBMS  | Name        | Used for                    |
+========+=============+=============================+
| MySQL  | ca_mgr      | testmgr                     |
+--------+-------------+-----------------------------+
| MySQL  | cats_db     | CATS test instance          |
+--------+-------------+-----------------------------+

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA: SHA256:CPeGCQX1p4hITy3IbTURQSZUQDBg9gg8I5jgf3m9+hs MD5:16:60:fe:47:49:e3:4a:5e:de:86:ae:be:66:29:b7:1e

Non-distribution packages and modifications
-------------------------------------------

The testmgr software is a custom PHP application installed in
/var/www/ca-mgr1.it-sls.de.

The CATS test setup is a custom PHP application installed in
/var/www/cats1.it-sls.de.

Risk assessments on critical packages
-------------------------------------

The system uses an unsupported OS version and needs to be updated as soon as
possible.

Critical Configuration items
============================

The system uses certificates issued by a test CA.

Keys and X.509 certificates
---------------------------

.. sslcert:: mgr.test.cacert.org
   :altnames:   DNS:mgr.test.cacert.org
   :certfile:   /etc/ssl/certs/mgr_test_cacert_org.crt
   :keyfile:    /etc/ssl/private/mgr_test_cacert_org.pem
   :serial:     5BAB
   :expiration: Nov 04 22:07:32 2019 GMT
   :sha1fp:     92:C4:CE:9F:C1:24:E2:93:52:AC:74:1F:8A:9B:F6:06:65:5F:D7:2E
   :issuer:     CAcert Testserver Class 3

.. sslcert:: cats.test.cacert.org
   :altnames:   DNS:cats.test.cacert.org
   :certfile:   /etc/ssl/certs/cats_test_cacert_org.crt
   :keyfile:    /etc/ssl/private/cats_test_cacert_org.pem
   :serial:     5BAA
   :expiration: Nov 04 22:06:48 2019 GMT
   :sha1fp:     53:EA:FA:7E:C7:6E:F3:74:5E:6F:80:46:24:CD:D1:E9:48:25:8F:8D
   :issuer:     CAcert Testserver Class 3

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache2 configuration
---------------------

The Apache web server is configured using the usual Debian :file:`/etc/apache2`
configuration directory. The VirtualHost entries are linked to
:file:`/etc/apache2/sites-enabled`.

Changes
=======

Planned
-------

.. todo:: setup monitoring for testmgr

.. todo:: make testmgr available on default ports via :doc:`proxyin`

.. todo:: setup proper DNS entries for testmgr

.. todo::

   upgrade testmgr to a supported OS version (depends on upgraded CATS and
   testmgr software)

.. todo:: use Puppet to manage testmgr

System Future
-------------

The testmgr system should support all test systems/stages. The testmgr
application should either be rolled out multiple times or should have support
for multiple test systems. This needs to be discussed in a broader group of
software development, software assessment and system administration teams.

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`
