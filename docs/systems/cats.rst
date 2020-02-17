.. index::
   single: Systems; CATS

====
CATS
====

Purpose
=======

This system provides the CAcert Assurer Training System (CATS), which is used
to perform the Assurer Challenge.

Application Links
-----------------

CATS
    https://cats.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_ted`
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

+-------------+-------------------+
| Application | Administrator(s)  |
+=============+===================+
| CATS        | :ref:`people_ted` |
+-------------+-------------------+

Contact
-------

* cats-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` and :ref:`people_wytze` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.243`
:IP Intranet: :ip:v4:`172.16.2.27`
:IP Internal: :ip:v4:`10.0.0.27`
:MAC address: :mac:`00:ff:53:2d:a0:65` (interfacename)

.. seealso::

   See :doc:`../network`

Monitoring
----------

:internal checks: :monitor:`cats.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; CATS

====================== ======== ====================================================================
Name                   Type     Content
====================== ======== ====================================================================
cats.cacert.org.       IN A     213.154.225.243
cats.cacert.org.       IN SSHFP 1 1 D29D4CC4662D5CB5F42C02823CA8677F05439589
cats.cacert.org.       IN SSHFP 1 2 605AF57CE0F1ECF8EEAC5C71901F1434BF65C06FC0796B932D0F10F21DDF65FE
cats.cacert.org.       IN SSHFP 2 1 0342EB1E7325EB90A1C0483DE3D6597E36E569C8
cats.cacert.org.       IN SSHFP 2 2 0835241A5B1905097C332B176FAEC92E05C690169BA125184F3FE2C9612D9718
cats.cacert.org.       IN SSHFP 3 1 CC7F9EDC6F2B9CE4A3F3953FF97C951572BA0F8C
cats.cacert.org.       IN SSHFP 3 2 1F54953C96DE0E93CD19E66CA25085D6773CEEFD3C376BE2E77C1A337CCD008D
cats.intra.cacert.org. IN A     172.16.2.27
====================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.11

* Debian GNU/Linux 7.11

Services
========

Listening services
------------------

+----------+---------+---------+-----------------------------+
| Port     | Service | Origin  | Purpose                     |
+==========+=========+=========+=============================+
| 22/tcp   | ssh     | ANY     | admin console access        |
+----------+---------+---------+-----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA  |
+----------+---------+---------+-----------------------------+
| 80/tcp   | http    | ANY     | CATS                        |
+----------+---------+---------+-----------------------------+
| 443/tcp  | https   | ANY     | CATS                        |
+----------+---------+---------+-----------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service   |
+----------+---------+---------+-----------------------------+
| 3306/tcp | mysql   | local   | MySQL database for CATS     |
+----------+---------+---------+-----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: mysql
   single: nrpe
   single: openssh
   single: postfix

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for CATS | init script                            |
|                    |                    | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| MySQL              | MySQL database     | init script                            |
|                    | server for CATS    | :file:`/etc/init.d/mysql`              |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Databases
---------

.. index::
   pair: MySQL database; cats_cats

+------------+--------------+---------------------------+
| RDBMS      | Name         | Used for                  |
+============+==============+===========================+
| MySQL      | cats_cats    | CATS database             |
+------------+--------------+---------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* crl.cacert.org (rsync) for getting CRLs
* HTTPS (443/tcp) to :doc:`secure.cacert.org <../critical/webdb>` for pushing
  test results
* HTTPS (443/tcp) to :doc:`svn` for subversion access
* HTTPS (443/tcp) to `github.com <https://github.com>`_

.. todo:: disable subversion access

Security
========

.. sshkeys::
   :RSA:   SHA256:YFr1fODx7PjurFxxkB8UNL9lwG/AeWuTLQ8Q8h3fZf4 MD5:d4:1f:0a:c9:a6:18:7a:a4:72:6b:42:5d:8e:63:44:1f
   :DSA:   SHA256:CDUkGlsZBQl8MysXb67JLgXGkBaboSUYTz/iyWEtlxg MD5:0c:0a:94:fc:99:b2:49:a2:41:3a:59:3f:dd:3d:e4:33
   :ECDSA: SHA256:H1SVPJbeDpPNGeZsolCF1nc87v08N2vi53waM3zNAI0 MD5:bc:28:fb:72:b9:e3:cb:0f:a0:ff:d2:38:8a:ac:6d:93

.. todo:: setup ED25519 host key (needs update to Jessie)

Dedicated user roles
--------------------

+-------+----------------------------------------------------------+
| Group | Purpose                                                  |
+=======+==========================================================+
| cats  | The cats group is meant to maintain the CATS application |
+-------+----------------------------------------------------------+

Non-distribution packages and modifications
-------------------------------------------

The CATS software is a custom PHP based system. The application is contained in
:file:`/home/cats/public_html`. The current repository is at
https://github.com/CAcertOrg/cats, historic versions are available at
https://svn.cacert.org/CAcert/Education/CATS. `Instructions for CATS setup
<https://github.com/CAcertOrg/cats/blob/release/INSTALL.txt>`_ can be found in
the git repository.

CATS requires client certificate authentication setup in the Apache httpd
server.

.. todo:: add a Vagrantfile to allow easy CATS testing setups


Risk assessments on critical packages
-------------------------------------

CATS as a PHP application is vulnerable to common PHP problems. The system
has to be kept up-to-date with OS patches.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

The server certificate for the CATS web application.

.. sslcert:: cats.cacert.org
   :altnames:   DNS:cats.cacert.org
   :certfile:   /home/cats/ssl/certs/cats_cert.pem
   :keyfile:    /home/cats/ssl/private/cats_privatekey.pem
   :serial:     147C65
   :expiration: Feb 16 21:58:48 2022 GMT
   :sha1fp:     67:69:C2:82:21:72:BD:DD:D8:AB:9D:B1:C8:CD:C2:09:72:10:2C:37
   :issuer:     CA Cert Signing Authority

.. _cats_client_cert:

Client certificate for pushing results to secure.cacert.org.

.. sslcert:: cats@cacert.org
   :altnames:   EMAIL:cats@cacert.org
   :certfile:   /home/cats/private/cert_201605.pem
   :keyfile:    /home/cats/private/key_201605.pem
   :serial:     0266AE
   :expiration: May  7 21:14:39 2016 GMT
   :sha1fp:     F9:8D:DC:67:68:30:5D:46:84:DE:77:F1:70:1A:E1:F7:9C:F4:DC:9A
   :issuer:     CAcert Class 3 Root

.. todo:: move certificates to :file:`/etc/ssl/public` and keys to
   :file:`/etc/ssl/private`

* :file:`/usr/share/ca-certificates/cacert.org/cacert.org.crt` CAcert.org Class
  1 and Class 3 CA certificates (allowed CA certificates for client certificates
  and certificate chain for server certificate)
* :file:`/home/cats/public_html/education.txt` is a symbolic link pointing to
  the most current client certificate issued to the education@cacert.org
  address.

.. index::
   pair: CATS; configuration

CATS configuration
------------------

CATS configuration is stored in files in
:file:`/home/cats/public_html/index.php` (roughly based on
:file:`index.php.template` from git) and
:file:`/home/cats/public_html/includes/db_connect.inc`.

.. todo:: move CATS configuration to :file:`/etc/`
.. todo:: refactor CATS to not store configuration in the PHP session

CATS uses two cronjobs in the cats user's crontab::

   # m h  dom mon dow   command
   MAILTO=bernhard@cacert.org
   */5 * * * * /home/cats/tools/do_upload
   # Reduced upload rate during problems...
   #0 * * * * /home/cats/tools/do_upload
   35 4 * * * /home/cats/tools/do_backup

The :file:`do_upload` job uses the client :ref:`certificate for cats@cacert.org
<cats_client_cert>` to authenticate to secure.cacert.org.

The :file:`do_backup` job creates a backup of the *cats_cats* MySQL database.
The backups are rotated (9 copies are kept) and encrypted to PGP keys of
:ref:`people_ted` and :ref:`people_philipp`. The job also attempts to fetch a
database dump from http://cats1.it-sls.de/dump.gz and store it in
:file:`/home/cats/dumps/dump.dev.gz`. This functionality is broken.

.. todo:: either fix fetching from the test system or remove this functionality
.. todo:: use :file:`/etc/cron.d` instead of user specific crontab
.. todo:: put the scripts in :file:`/home/cats/tools/` into git

.. seealso::

   Instructions for `CATS translation
   <https://wiki.cacert.org/Brain/Study/EducationTraining/CATSTranslation>`_

.. index::
   pair: Apache httpd; configuration

Apache httpd configuration
--------------------------

The Apache httpd configuration in the directory :file:`/etc/apache2/` has been
modified to improve TLS settings and define an HTTP and an HTTPS VirtualHost
for cats.cacert.org.

.. literalinclude:: ../configdiff/cats/apache/cats-apache-config.diff
   :language: diff

.. index::
   pair: logrotate; configuration

logrotate configuration
-----------------------

CATS specific Apache httpd logfiles are rotated by logrotate. The rotation is
controlled by a separate configuration in :file:`/etc/logrotate.d/cats`:

.. literalinclude:: ../configdiff/cats/logrotate/cats

.. index::
   pair: MySQL; configuration

MySQL configuration
-------------------

MySQL configuration is stored in the :file:`/etc/mysql/` directory.

.. index::
   pair: Postfix; configuration

Tasks
=====

.. todo:: document how to update the CATS software

Changes
=======

Planned
-------

.. todo:: switch to Puppet management
.. todo:: replace nrpe with icinga2 agent
.. todo:: update to Debian 8/9/10
.. todo:: setup IPv6
.. todo:: setup CRL checks

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

PHP documentation
   https://secure.php.net/manual/en/
