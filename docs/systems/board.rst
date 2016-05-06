.. index::
   single: Systems; Board

=====
Board
=====

Purpose
=======

This system hosts an OpenERP instance available at board.cacert.org.

Application Links
-----------------

OpenERP URL
   https://board.cacert.org/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_gero`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+-------------+--------------------------------------------------+
| Application | Administrator(s)                                 |
+=============+==================================================+
| OpenERP     | :ref:`people_gero`, :ref:`people_neo`, Treasurer |
+-------------+--------------------------------------------------+

.. note:: use personalized accounts only

Contact
-------

* board-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd`, :ref:`people_mario` and :ref:`people_neo` have
:program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.252`
:IP Intranet: :ip:v4:`172.16.2.34`
:IP Internal: :ip:v4:`10.0.0.34`
:MAC address: :mac:`00:ff:80:a9:e8:4d` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Board

====================== ======== ============================================
Name                   Type     Content
====================== ======== ============================================
board.cacert.org.      IN A     213.154.225.252
board.cacert.org.      IN SSHFP 1 1 F5C02A860A1CC07AEEFBF802540680C7476BDE6E
board.cacert.org.      IN SSHFP 2 1 7B6EEB0CCDFB2E2CFE479E0AECE36FF995FDD1F4
board.intra.cacert.org IN A     172.16.2.34
====================== ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Wheezy
   single: Debian GNU/Linux; 7.10

* Debian GNU/Linux 7.10

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+---------+---------+---------------------------------+
| Port     | Service | Origin  | Purpose                         |
+==========+=========+=========+=================================+
| 22/tcp   | ssh     | ANY     | admin console access            |
+----------+---------+---------+---------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA      |
+----------+---------+---------+---------------------------------+
| 80/tcp   | http    | ANY     | Webserver redirecting to HTTPS  |
+----------+---------+---------+---------------------------------+
| 443/tcp  | https   | ANY     | Webserver for OpenERP           |
+----------+---------+---------+---------------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service       |
+----------+---------+---------+---------------------------------+
| 5432/tcp | pgsql   | local   | PostgreSQL database for OpenERP |
+----------+---------+---------+---------------------------------+
| 8069/tcp | xmlrpc  | local   | OpenERP XML-RPC service         |
+----------+---------+---------+---------------------------------+

Running services
----------------

.. index::
   single: openssh
   single: Apache
   single: cron
   single: PostgreSQL
   single: OpenERP
   single: Postfix
   single: nrpe

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for      | init script                            |
|                    | OpenERP            | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| PostgreSQL         | PostgreSQL         | init script                            |
|                    | database server    | :file:`/etc/init.d/postgresql`         |
|                    | for OpenERP        |                                        |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+
| OpenERP server     | OpenERP WSGI       | init script                            |
|                    | application        | :file:`/etc/init.d/openerp`            |
+--------------------+--------------------+----------------------------------------+

Databases
---------

+------------+---------+----------+
| RDBMS      | Name    | Used for |
+============+=========+==========+
| PostgreSQL | openerp | OpenERP  |
+------------+---------+----------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* HTTP (80/tcp) to nightly.openerp.com
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
| RSA       | ``c7:a0:3f:63:a5:cb:9a:8f:1f:eb:55:63:46:c3:8d:f1`` |
+-----------+-----------------------------------------------------+
| DSA       | ``f6:b7:e5:52:24:27:1e:ea:32:c8:f1:2e:45:f7:24:d3`` |
+-----------+-----------------------------------------------------+
| ECDSA     | ``0f:fc:76:f8:24:99:95:f7:d2:28:59:6e:f0:1e:39:ac`` |
+-----------+-----------------------------------------------------+
| ED25519   | \-                                                  |
+-----------+-----------------------------------------------------+

.. todo:: setup ED25519 host key

.. seealso::

   See :doc:`../sshkeys`

Non-distribution packages and modifications
-------------------------------------------

:program:`OpenERP` is installed from non-distribution packages from
http://nightly.openerp.com/7.0/nightly/deb/. The package source is disabled in
:file:`/etc/apt/sources.lists.d/openerp.list` to avoid accidential updates that
cause damage to the customization.

Local modifications to OpenERP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenERP has been modified. The init script :file:`/etc/init.d/openerp` has the
following line added to the :func:`do_start()` function to make a request to
the OpenERP daemon that causes that daemon to load its configuration and start
regular cleanup tasks (like sending scheduled mails):

.. code:: bash

   sleep 1; curl --silent localhost:8069 > /dev/null

Some files have been patched to either fix bugs in the upstream OpenERP code or
to add customizations for CAcert's needs.

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/web/static/lib/py.js/lib/py.js`

.. literalinclude:: ../patches/openerp/py.js.patch
   :language: diff

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/account/account.py`

.. literalinclude:: ../patches/openerp/account.py.patch
   :language: diff

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/account/edi/invoice.py`

.. literalinclude:: ../patches/openerp/invoice.py.patch
   :language: diff

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/account_followup/account_followup.py`

This patch includes a Paypal link in payment reminders.

.. literalinclude:: ../patches/openerp/account_followup_paypal.patch
   :language: diff

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/account_followup/report/account_followup_print.py`

This patch causes OpenERP to include non-overdue but open payments in reminders.

.. literalinclude:: ../patches/openerp/account_followup_print.patch
   :language: diff

:file:`/usr/lib/python2.7/dist-packages/openerp/addons/web/static/src/js/view_form.js`

Fix form display.

.. todo:: check whether the form display issue has been fixed upstream

.. literalinclude:: ../patches/openerp/view_form.js.patch
   :language: diff

Risk assessments on critical packages
-------------------------------------

Using a customized OpenERP version that is not updated causes a small risk to
miss upstream security updates. The risk is mitigated by restricting the access
to the system to a very small group of users that are authenticated using
personalized client certificates.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: board.cacert.org
   :certfile:   /etc/ssl/certs/board.crt
   :keyfile:    /etc/ssl/private/board.key
   :serial:     11e839
   :expiration: Mar 31 16:47:11 2018 GMT
   :sha1fp:     2C:AC:8C:F8:D6:4A:9E:1D:B0:35:B8:E4:5E:24:B1:43:E3:69:98:46
   :issuer:     CAcert.org Class 1 Root CA

* :file:`/etc/ssl/certs/cacert.org.pem` CAcert.org Class 1 and Class 3 CA
  certificates (allowed CA certificates for client certificates)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache configuration files
--------------------------

* :file:`/etc/apache2/conf.d/openerp-httpd.conf`

  Defines the WSGI setup for OpenERP

* :file:`/etc/apache2/sites-available/default`

  Defines the HTTP to HTTPS redirection

* :file:`/etc/apache2/sites-available/default-ssl`

  Defines the HTTPS and client authentication configuration

* :file:`/var/local/ssl/http_fake_auth.passwd`

  Defines the authorized users based on the DN in their client certificate

CRL update job
--------------

:file:`/etc/cron.hourly/update-crls`

OpenERP configuration
---------------------

:file:`/etc/openerp/openerp-server.conf`

This file configures the database that is used by OpenERP and the interface
that the XML-RPC service binds to.

Tasks
=====

Planned
-------

.. todo:: disable unneeded Apache modules

.. todo:: setup IPv6

.. todo:: consider using a centralized PostgreSQL instance

Changes
=======

System Future
-------------

.. todo:: system should be updated to Debian 8

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Wiki page for this system
   :wiki:`SystemAdministration/Systems/Board`
