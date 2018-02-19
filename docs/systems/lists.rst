.. index::
   single: Systems; Lists

=====
Lists
=====

Purpose
=======

The system provides mailing list services under the lists.cacert.org hostname.

Application Links
-----------------

* Mailing list management and archives

  https://lists.cacert.org/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_mario`
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

+--------------+---------------------------------------------+
| Application  | Administrator(s)                            |
+==============+=============================================+
| Sympa        | :ref:`people_jandd`, :ref:`people_mario`,   |
|              | :ref:`people_ulrich`, :ref:`people_philipp` |
+--------------+---------------------------------------------+

Contact
-------

* email-admin@cacert.org

Additional People
-----------------

:ref:`people_jselzer` has :program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.231`
:IP Intranet: :ip:v4:`172.16.2.17`
:IP Internal: :ip:v4:`10.0.0.17`
:MAC address: :mac:`00:ff:d0:13:9a:22` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Lists

=================================== ======== ============================================
Name                                Type     Content
=================================== ======== ============================================
lists.cacert.org.                   IN A     213.154.225.231
lists.cacert.org.                   IN MX    10 email.cacert.org.
lists.cacert.org.                   IN SSHFP 1 1 87F75B9124326B566ED22DCF65A9740EEDE8F0FF
lists.cacert.org.                   IN SSHFP 2 1 8D79E68E731ED72667F3D286C477245DF653083B
lists.cacert.org.                   IN TXT   "v=spf1 ip4:213.154.225.231 -all"
cert.lists.cacert.org.              IN CNAME lists.cacert.org.
nocert.lists.cacert.org.            IN CNAME lists.cacert.org.
lists.intra.cacert.org.             IN A     172.16.2.17
17.2.16.172.in-addr.arpa            IN PTR   lists.intra.cacert.org.
231.225.154.213.in-addr.arpa        IN CNAME 231.224-27.225.154.213.in-addr.arpa.
231.224-27.225.154.213.in-addr.arpa IN PTR   lists.cacert.org.
=================================== ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.11

* Debian GNU/Linux 7.11

Applicable Documentation
------------------------

This is the administration documentation.

.. seealso::

   :wiki:`EmailListOverview` for user documentation

Services
========

Listening services
------------------

+----------+---------+-----------+-------------------------------------------+
| Port     | Service | Origin    | Purpose                                   |
+==========+=========+=================+=====================================+
| 22/tcp   | ssh     | ANY       | admin console access                      |
+----------+---------+-----------+-------------------------------------------+
| 25/tcp   | smtp    | monitor,  | mail delivery to local MTA/sympa          |
|          |         | email     |                                           |
+----------+---------+-----------+-------------------------------------------+
| 80/tcp   | http    | ANY       | redirect to https                         |
+----------+---------+-----------+-------------------------------------------+
| 443/tcp  | https   | ANY       | Sympa mailing list manager and archive    |
+----------+---------+-----------+-------------------------------------------+
| 4433/tcp | https   | LOCAL     | phpmyadmin access via ssh port forwarding |
+----------+---------+-----------+-------------------------------------------+
| 5666/tcp | nrpe    | monitor   | remote monitoring service                 |
+----------+---------+-----------+-------------------------------------------+
| 3306/tcp | mysql   | local     | MySQL database for Sympa                  |
+----------+---------+-----------+-------------------------------------------+

.. topic:: PHPMyAdmin access

   Administrators can use ssh to forward the Apache httpd port 4433 to their
   own machine:

   .. code-block:: bash

      ssh -L 4433:localhost:4433 -l username lists.cacert.org

   and access PHPMyAdmin at https://localhost:4433/phpmyadmin

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: Sympa
   single: cron
   single: nrpe
   single: openssh
   single: rsyslog

+--------------------+---------------------+----------------------------------------+
| Service            | Usage               | Start mechanism                        |
+====================+=====================+========================================+
| openssh server     | ssh daemon for      | init script :file:`/etc/init.d/ssh`    |
|                    | remote              |                                        |
|                    | administration      |                                        |
+--------------------+---------------------+----------------------------------------+
| Apache httpd       | Webserver for Sympa | init script                            |
|                    |                     | :file:`/etc/init.d/apache2`            |
+--------------------+---------------------+----------------------------------------+
| cron               | job scheduler       | init script :file:`/etc/init.d/cron`   |
+--------------------+---------------------+----------------------------------------+
| rsyslog            | syslog daemon       | init script                            |
|                    |                     | :file:`/etc/init.d/syslog`             |
+--------------------+---------------------+----------------------------------------+
| MySQL              | MySQL database      | init script                            |
|                    | server for Sympa    | :file:`/etc/init.d/mysql`              |
+--------------------+---------------------+----------------------------------------+
| Postfix            | SMTP server for     | init script                            |
|                    | local mail          | :file:`/etc/init.d/postfix`            |
|                    | submission and      |                                        |
|                    | incoming list mail  |                                        |
+--------------------+---------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring   | init script                            |
|                    | service queried by  | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`      |                                        |
+--------------------+---------------------+----------------------------------------+
| Sympa mailing list | mail list handling  | init script                            |
| services           |                     | :file:`/etc/init.d/sympa`              |
+--------------------+---------------------+----------------------------------------+

Databases
---------

+-------------+-------+-------------------------------+
| RDBMS       | Name  | Used for                      |
+=============+=======+===============================+
| MySQL       | sympa | Sympa mailing list management |
+-------------+-------+-------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`email`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`proxyout` as HTTP proxy for APT
* arbitrary Internet SMTP servers for delivery of list mails

Security
========

.. sshkeys::
   :RSA:   MD5:9a:64:3d:ab:38:91:90:88:2b:73:cb:05:8c:56:f9:c9
   :DSA:   MD5:dd:ab:a6:c2:29:91:e9:81:fa:29:3c:f7:88:76:1f:f6
   :ECDSA: MD5:3c:8d:f2:a7:e8:75:1c:9a:11:13:11:2a:58:aa:9b:d1

.. todo:: setup ED25519 host key (needs update to Jessie)

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

Apache httpd, Postfix and Sympa have a good security track record. Apache httpd
is configured with the minimum of required modules. PHPMyAdmin is only reachable
via ssh port forwarding.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

Server certificate for Apache httpd for Sympa and phpmyadmin and Postfix:

.. sslcert:: lists.cacert.org
   :altnames:   DNS:cert.lists.cacert.org, DNS:lists.cacert.org, DNS:nocert.lists.cacert.org
   :certfile:   /etc/ssl/certs/ssl-cert-lists-cacert-multialtname.pem
   :keyfile:    /etc/ssl/private/ssl-cert-lists-cacert-multialtname.pem
   :serial:     11E87F
   :expiration: Mar 31 21:00:36 18 GMT
   :sha1fp:     6B:EE:7B:51:4A:E9:E7:E3:EF:C8:63:6D:51:97:F7:DC:BF:F1:4A:C9
   :issuer:     CA Cert Signing Authority

* :file:`/usr/share/ca-certificates/cacert.org/cacert.org.crt`
  CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for
  client certificates)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache httpd configuration
--------------------------

* :file:`/etc/apache2/sites-available/000-default.conf`

  default HTTP VirtualHost configuration that redirects to
  https://lists.cacert.org/

* :file:`/etc/apache2/sites-available/sympa-include.conf`

  common configuration for the three Sympa VirtualHost definitions

* :file:`/etc/apache2/sites-available/lists.cacert.org.conf`

  HTTPS VirtualHost configuration for https://lists.cacert.org/ that supports
  optional client certificate authentication

* :file:`/etc/apache2/sites-available/cert.lists.cacert.org.conf`

  HTTPS VirtualHost configuration for https://cert.lists.cacert.org/ that
  requires client certificate authentication

* :file:`/etc/apache2/sites-available/nocert.lists.cacert.org.conf`

  HTTPS VirtualHost configuration for https://nocert.lists.cacert.org/ that
  does not support client certificates

* :file:`/etc/apache2/sites-available/localhost_4433_phpmyadmin.conf`

  HTTPS VirtualHost configuration for https://localhost:4433/phpmyadmin

Sympa configuration
-------------------

Sympa configuration is stored in :file:`/etc/sympa/`.

* :file:`/etc/sympa/aliases`

  generated by Sympa and included in Postfix's :file:`/etc/postfix/main.cf`.
  The file contains alias definitions that pipe list emails into Sympa
  processes.

* :file:`/etc/sympa/data_sources/`

  data sources shared accross lists (things we didn't want to define more than
  once). The `board` data source is defined in
  :file:`/etc/sympa/data_sources/board.incl`

  .. seealso::

     `Sympa manual`_

* :file:`/etc/sympa/sympa.conf`

  main Sympa configuration file. S/MIME configuration items must be set even if
  they appear to be the default values. Supported_lang must be a subset of the
  supported system locales (see :file:`/usr/lib/sympa/locale/`) otherwise user's
  cannot change their locale in Sympa.

* :file:`/etc/sympa/wwsympa.conf`

  configuration for the Sympa web interface

* :file:`/var/lib/sympa/expl/{listname}/{cert.pem,private_key}`

  list private key and certificate for `listname`

* :file:`/var/lib/sympa/x509-user-certs/{emailaddress}`

  user X.509 certificates used by Sympa


Postfix configuration
---------------------

Postfix configuration is stored in :file:`/etc/postfix/`

.. note::

   The file :file:`/etc/aliases.db` must be writable by the `sympa` group to
   allow running :program:`newaliases` when defining new lists.

Tasks
=====

Adding a list
-------------

1. Login to Sympa https://lists.cacert.org/wws using the
   listmaster@lists.cacert.org (password stored in
   :file:`/root/sympa-listmanagerpassword.txt`)

2. Use the GUI to create the list. Set the list so that support@cacert.org can
   send email to the list without confirmation using the cacert main web
   interface, login and validate the list address issue a WoT certificate for
   the list user export/backup the WoT certificate out of your browser copy the
   p12 exported certificate to the list server.

3. use::

      openssl pkcs12 -in cacert-listname\@lists.cacert.org.p12 -nodes

   to export the certificate without a password.

4. copy the certificate and private key to the location described below and
   setup permissions::

      chown sympa:sympa /var/lib/sympa/expl/<list>/cert.pem
      chown sympa:sympa /var/lib/sympa/expl/<list>/private_key
      chmod 0600 /var/lib/sympa/expl/<list>/private_key
      chmod 0644 /var/lib/sympa/expl/<list>/cert.pem

5. add subscribers/ other owners

Planned
-------

.. todo:: upgrade the lists system OS to Debian 9 (Stretch)

.. todo:: manage the lists system using Puppet

Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Apache httpd documentation
   http://httpd.apache.org/docs/2.4/
Sympa manual
   http://www.sympa.org/manual/
Postfix documentation
   http://www.postfix.org/documentation.html
Postfix Debian wiki page
   https://wiki.debian.org/Postfix

.. _Sympa manual: http://www.sympa.org/manual/list-definition#data_inclusion_file
