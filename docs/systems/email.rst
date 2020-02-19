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
:IPv6:        :ip:v6:`2001:7b8:616:162:2::228`
:MAC address: :mac:`00:ff:8f:e0:4a:90` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Email

Monitoring
----------

:internal checks: :monitor:`email.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Email

+-------------------------+-----------+----------------------------------------------------------------------+
| Name                    | Type      | Content                                                              |
+=========================+===========+======================================================================+
| email.cacert.org.       | IN A      | 213.154.225.228                                                      |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  AAAA  | 2001:7b8:616:162:2::228                                              |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 1 1 bf391fd72656a275524d1d25a624c6045b44ae90                         |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 1 2 c8b68f3eb9a83902391b78686b4885a317fac0f74b0490a78b32ecbbee921df1 |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 3 1 5ffbc51c37cdff52db9c488c08b89af9ffee06a0                         |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 3 2 a114de78fc26bd0dc6fa2206d7c04519ec875023cf203e446d4bbbbc4e24da19 |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 4 1 18418515e94817f0624bf0a192331addf878ff66                         |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.cacert.org.       | IN  SSHFP | 4 2 d4fe3165206ba69baf4643253138561789918688375ed8ab89bcfc4411535221 |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.intra.cacert.org. | IN A      | 172.16.2.19                                                          |
+-------------------------+-----------+----------------------------------------------------------------------+
| email.infra.cacert.org. | IN A      | 10.0.0.19                                                            |
+-------------------------+-----------+----------------------------------------------------------------------+

A DKIM record for cacert.org ist setup but no DKIM signing is active currently.

.. todo:: setup DKIM properly, see :bug:`696` for an older discussion

.. todo:: setup SPF records when the system is ready, see :bug:`492` for an
   older discussion

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.9

* Debian GNU/Linux 9.9

Services
========

Listening services
------------------

+----------+---------+---------+-------------------------------------+
| Port     | Service | Origin  | Purpose                             |
+==========+=========+=========+=====================================+
| 22/tcp   | ssh     | ANY     | admin console access                |
+----------+---------+---------+-------------------------------------+
| 25/tcp   | smtp    | ANY     | mail receiver for cacert.org        |
+----------+---------+---------+-------------------------------------+
| 110/tcp  | pop3    | ANY     | POP3 access for cacert.org mail     |
|          |         |         | addresses                           |
+----------+---------+---------+-------------------------------------+
| 143/tcp  | imap    | ANY     | IMAP access for cacert.org mail     |
|          |         |         | addresses                           |
+----------+---------+---------+-------------------------------------+
| 465/tcp  | smtps   | ANY     | SMTPS for cacert.org mail addresses |
+----------+---------+---------+-------------------------------------+
| 587/tcp  | smtp    | ANY     | mail submission for cacert.org mail |
|          |         |         | addresses                           |
+----------+---------+---------+-------------------------------------+
| 993/tcp  | imaps   | ANY     | IMAPS access for cacert.org mail    |
|          |         |         | addresses                           |
+----------+---------+---------+-------------------------------------+
| 995/tcp  | pop3s   | ANY     | POP3S access for cacert.org mail    |
|          |         |         | addresses                           |
+----------+---------+---------+-------------------------------------+
| 4190/tcp | sieve   | ANY     | Manage sieve access for cacert.org  |
|          |         |         | mail addresses                      |
+----------+---------+---------+-------------------------------------+
| 3306/tcp | mysql   | local   | MariaDB database server             |
+----------+---------+---------+-------------------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service           |
+----------+---------+---------+-------------------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: dovecot
   single: icinga2
   single: mariadb
   single: openssh
   single: postfix
   single: puppet
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``    |
|                | daemon                   |                                  |
+----------------+--------------------------+----------------------------------+
| dovecot        | IMAP(s), POP3(s) and     | systemd unit ``dovecot.service`` |
|                | sieve filter daemon      |                                  |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| MariaDB        | MariaDB database         | systemd unit ``mariadb.service`` |
|                | server for email         |                                  |
|                | services                 |                                  |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for remote    | systemd unit ``ssh.service``     |
|                | administration           |                                  |
+----------------+--------------------------+----------------------------------+
| Postfix        | SMTP server for          | systemd unit ``postfix.service`` |
|                | cacert.org               |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

Databases
---------

+-------+----------------+----------------------------------+
| RDBMS | Name           | Used for                         |
+=======+================+==================================+
| MySQL | cacertusers    | database for dovecot and postfix |
+-------+----------------+----------------------------------+
| MySQL | roundcubemail  | roundcube on :doc:`webmail`      |
+-------+----------------+----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`webmail`
* all @cacert.org address owners have access to POP3 (STARTTLS and POP3S), IMAP
  (STARTTLS and IMAPS), SMTPS, SMTP submission (STARTTLS) and manage sieve

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`issue` for OTRS mail
* :doc:`lists` for mailing lists
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`puppet` (tcp/8140) as Puppet master
* arbitrary Internet SMTP servers for outgoing mail

Security
========

.. sshkeys::
   :RSA:     SHA256:yLaPPrmoOQI5G3hoa0iFoxf6wPdLBJCnizLsu+6SHfE MD5:a1:d2:17:53:6b:0f:b6:a4:14:13:46:f7:04:ef:4a:23
   :ECDSA:   SHA256:oRTeePwmvQ3G+iIG18BFGeyHUCPPID5EbUu7vE4k2hk MD5:16:95:af:c9:71:f4:d8:f7:91:7f:f7:2f:25:b3:f1:63
   :ED25519: SHA256:1P4xZSBrppuvRkMlMThWF4mRhog3Xtiribz8RBFTUiE MD5:db:1e:68:3f:dd:b0:bb:68:c8:8b:cb:39:85:7d:f7:40

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

Postfix and Dovecot have very good security reputation. The system is patched
regularly.

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

.. todo: move Postfix, Dovecot, ssh and MariaDB configuration to Puppet

Keys and X.509 certificates
---------------------------

Server certificate for SMTP communication from the Internet.

.. sslcert:: email.cacert.org
   :altnames:   DNS:email.cacert.org
   :certfile:   /etc/ssl/certs/ssl-cert-email-cacert.pem
   :keyfile:    /etc/ssl/private/ssl-cert-email-cacert.key
   :serial:     147CB5
   :expiration: Feb 18 12:09:04 2022 GMT
   :sha1fp:     81:52:26:1E:92:82:17:17:26:AA:AB:4B:96:1A:DC:DC:A1:CE:3D:49
   :issuer:     CA Cert Signing Authority

Server certificate for community email services (SMTPS, SMTP submission in
Postfix and IMAP with STARTTLS, IMAPS, POP3 with STARTTLS, POP3S and pysieved)

.. sslcert:: community.cacert.org
   :certfile:  /etc/ssl/certs/ssl-cert-community-cacert.pem
   :keyfile:   /etc/ssl/private/ssl-cert-community-cacert.key
   :serial:    147CB0
   :secondary:

.. note::

   Postfix uses the email.cacert.org certificate for client authentication if
   requested by a target server.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: MariaDB; configuration

MariaDB configuration
---------------------

MySQL configuration is stored in the :file:`/etc/mysql/` directory.

.. index::
   pair: MySQL; NSS
   single: libnss-mysql

.. _nss:

.. index::
   pair: dovecot; configuration

Dovecot configuration
---------------------

Dovecot configuration is stored in the :file:`/etc/dovecot/` directory. The
database settings are stored in
:file:`dovecot-sql.conf.ext`.

.. index::
   pair: dovecot; authentication

.. topic:: Dovecot authentication

   There is a special master password so that webmail can do the authentication
   for dovecot using certificates. This is defined in
   :file:`/etc/dovecot/dovecot-sql.conf.ext`.

.. index::
   pair: Postfix; configuration

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

Email storage
-------------

Mail for :samp:`{user}` is stored in :samp:`/home/mailboxes/{user}/Maildir`.

.. todo::
   move mail storage to a separate data volume to allow easier backup and OS
   upgrades

Tasks
=====

.. index::
   single: add email users

Adding email users
------------------

1. create user in the database table ``cacertusers.user``:

   .. code-block:: bash

      mysql -p cacertusers

   .. code-block:: sql

      INSERT INTO user (username, fullnamealias, realname, password)
      VALUES ('user', 'user.name', 'User Name', '$1$salt$passwordhash')

2. create the user's home directory and Maildir:

   :samp:`install -o {user} -g {user} -m 0755 -d /home/{user}/Maildir`

.. note::

   * a valid password hash for the password ``secret`` is
     ``$1$caea3837$gPafod/Do/8Jj5M9HehhM.``
   * users can reset their password via
     https://community.cacert.org/password.php on :doc:`webmail`
   * use the :download:`mail template
     <../downloads/template_new_community_mailaddress.rfc822>` to send out to a
     user's non-cacert.org mail account and make sure to encrypt the mail to a
     known public key of that user

.. todo::
   implement tooling to automate password salt generation and user creation

Setting up mail aliases
-----------------------

There are two types of aliases.

1. The first type are those that are never sent from. e.g.
   postmaster@cacert.org.  All these aliases are defined in
   :file:`/etc/aliases`.  Don't forget to run

   .. code-block:: bash

      postalias /etc/aliases

   after any changes. Aliases for issue tracking are installed here as
   :samp:`{issuetrackingaddress} : {issuetrackingaddress}@issue.cacert.org`.

2. The second type are those aliases that are used to send email too, e.g
   pr@cacert.org. These aliases are recorded in the aliases table on the
   cacertusers database. The reason for this implementation is to only allow
   the designated person to send email from this email address.

Client certificate authentication
---------------------------------

There were plans for X.509 certificate authentication for mail services, but
there is no progress so far.

Changes
=======

Planned
-------

.. todo:: update to Debian 10 (when Puppet is available)

.. todo:: implement CRL checking

.. todo::
   throttle brute force attack attempts using fail2ban or similar mechanism

.. todo::
   consider to use LDAP to consolidate user, password and email information

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`
   * :wiki:`SystemAdministration/Systems/Email` for some discussion on legal
     implications related to mail archiving

References
----------

Postfix documentation
   http://www.postfix.org/documentation.html
Postfix Debian wiki page
   https://wiki.debian.org/Postfix
Dovecot 2.x wiki
   http://wiki2.dovecot.org/FrontPage
