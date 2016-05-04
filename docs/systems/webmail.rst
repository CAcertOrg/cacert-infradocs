.. index::
   single: Systems; Webmail

===================
Webmail (Community)
===================

Purpose
=======

This container hosts the webmail system available at
https://community.cacert.org/ that provides web based mail access to users with
a @cacert.org email address.

The system also hosts the `board voting system`_, `staff list`_ and `email
password reset`_.

.. todo:: move `board voting system`_ to a separate container

.. todo::
   move `staff list`_ to a separate container or integrate it into some
   new self service system

.. _board voting system: https://community.cacert.org/board
.. _staff list: https://community.cacert.org/staff.php
.. _email password reset: https://community.cacert.org/password.php

Administration
==============

System Administration
---------------------

* Primary: None
* Secondary: None

.. todo:: find admins for webmail

Application Administration
--------------------------

+---------------------+-----------------------+
| Application         | Administrators        |
+=====================+=======================+
| Webmail             | :ref:`people_ulrich`, |
|                     | :ref:`people_jselzer` |
+---------------------+-----------------------+
| Board voting system | :ref:`people_jandd`   |
+---------------------+-----------------------+
| Staff list          | None                  |
+---------------------+-----------------------+
| Password reset      | None                  |
+---------------------+-----------------------+

Contact
-------

* webmail-admin@cacert.org

Additional People
-----------------

:ref:`people_jandd`, :ref:`people_mario` and :ref:`people_jselzer` have
:program:`sudo` access on that machine.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.228`
:IP Intranet: :ip:v4:`172.16.2.20`
:IP Internal: :ip:v4:`10.0.0.120`
:MAC address: :mac:`00:ff:9a:a7:64:78` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Webmail
   single: DNS records; Community

===================== ======== ================
Name                  Type     Content
===================== ======== ================
community.cacert.org. IN CNAME email.cacert.org
===================== ======== ================

.. seealso::

   See https://wiki.cacert.org/SystemAdministration/Procedures/DNSChanges

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Etch
   single: Debian GNU/Linux; 4.0

* Debian GNU/Linux 4.0

Applicable Documentation
------------------------

This is it :-)

.. seealso::

   * `Community Email Wiki Page <https://wiki.cacert.org/CommunityEmail>`_
   * `Email Account Policy <https://wiki.cacert.org/EmailAccountPolicy>`_

Services
========

Listening services
------------------

.. use the values from this table or add new lines if applicable

+----------+---------+---------+---------------------------+
| Port     | Service | Origin  | Purpose                   |
+==========+=========+=========+===========================+
| 22/tcp   | ssh     | ANY     | admin console access      |
+----------+---------+---------+---------------------------+
| 443/tcp  | https   | ANY     | Web server                |
+----------+---------+---------+---------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service |
+----------+---------+---------+---------------------------+

.. note::

   The ssh port is reachable via NAT on email.cacert.org:12022

Running services
----------------

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for      | init script                            |
|                    | Applications       | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* archive.debian.org as Debian mirror
* :doc:`email` for MySQL (3306/tcp) for webmail, password reset and staff list
* :doc:`email` IMAP (110/tcp), IMAPS (993/tcp), Manage Sieve (2001/tcp), SMTPS
  (465/tcp) and SMTP Submission (587/tcp) for the webmail system

Security
========

SSH host keys
-------------

+-----------+-----------------------------------------------------+
| Algorithm | Fingerprint                                         |
+===========+=====================================================+
| RSA       | ``82:91:22:22:10:75:ab:0e:55:05:9a:f9:98:cb:94:48`` |
+-----------+-----------------------------------------------------+
| DSA       | ``6b:6e:59:37:41:83:a5:89:2a:18:04:23:51:53:5d:cd`` |
+-----------+-----------------------------------------------------+
| ECDSA     | \-                                                  |
+-----------+-----------------------------------------------------+
| ED25519   | \-                                                  |
+-----------+-----------------------------------------------------+

.. warning::

   The system is too old to support ECDSA or ED25519 keys.

.. seealso::

   See :doc:`../sshkeys`

Non-distribution packages and modifications
-------------------------------------------

:file:`/var/www/roundcubemail` contains a `Roundcube`_ 0.2.1 installation,
probably with patches.

.. todo::

   Research wether Roundcube has been patched or not

:file:`/var/www/staff.php` is a custom built PHP script to show a list of
people with cacert.org email addresses.

:file:`/var/www/password.php` is a custom build PHP script to allow users to
reset their email password.

:file:`/var/www/board` contains the board voting system.

.. _Roundcube: https://roundcube.net/

Risk assessments on critical packages
-------------------------------------

The whole system is outdated, the PHP version is ancient, Roundcube is old.
Needs to be replaced as soon as possible.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

* :file:`/etc/ssl/certs/ssl-cert-community-cacert.crt` server certificate
* :file:`/etc/ssl/private/ssl-cert-community-cacert.key` server key
* :file:`/usr/share/ca-certificates/cacert.org/` directory containing the
  CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for
  client authentication and certificate chain for server certificate) with
  symbolic links with the :command:`openssl` hashed certificate names

.. seealso::

   * :doc:`../certlist`
   * https://wiki.cacert.org/SystemAdministration/CertificateList

Apache configuration
--------------------

The Apache httpd configuration is stored in
:file:`/etc/apache2/sites-available/webmail`.

:file:`/etc/hosts`
------------------

Defines some aliases for :doc:`email` that are used by Roundcube, the password
reset script and the staff list script.

Roundcube configuration
-----------------------

The Roundcube configuration is stored in files in the
:file:`/var/www/roundcubemail/config/` directory.


Staff list script
-----------------

The staff list contains its configuration in :file:`/var/www/staff.php` itself.

.. todo::

   Put the staff list script in a git repository

Password reset script
---------------------

The password reset script contains it configuration in
:file:`/var/www/password.php` itself.

.. todo::

   Put the password reset script in a git repository

Board voting system configuration
---------------------------------

The board voting system uses a SQLite database in
:file:`/var/www/board/database.sqlite`.

.. warning::

   The board voting system software seems to be checked out from a Subversion
   repository at https://svn.cacert.cl/Software/Voting/vote that does not exist
   anymore

.. todo::

   Put the current version of the board voting system in a git repository

Tasks
=====

Planned
-------

.. todo:: implement CRL checking

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

   * https://wiki.cacert.org/PostfixConfiguration

References
----------

Webmail URL
   https://community.cacert.org/ (redirects to
   https://community.cacert.org/roundcubemail/)

Board Voting System URL
   https://community.cacert.org/board/

Password reset
   https://community.cacert.org/password.php

Staff list
   https://community.cacert.org/staff.php

Wiki page for this system
   https://wiki.cacert.org/SystemAdministration/Systems/Community
