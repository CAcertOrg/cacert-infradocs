.. index::
   single: Systems; Email

=====
Email
=====

Purpose
=======

This system handles email for @cacert.org addresses. It also provides users of
@cacert.org with IMAPs and POP3s access to their accounts. The system provides
the API part of the CAcert community self service system.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jselzer`
* Secondary: :ref:`people_jandd`

Application Administration
--------------------------

+------------------+---------------------+
| Application      | Administrator(s)    |
+==================+=====================+
| self service API | :ref:`people_jandd` |
+------------------+---------------------+

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
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.4

* Debian GNU/Linux 10.4

Services
========

Listening services
------------------

+----------+---------+-----------+-------------------------------------+
| Port     | Service | Origin    | Purpose                             |
+==========+=========+===========+=====================================+
| 22/tcp   | ssh     | ANY       | admin console access                |
+----------+---------+-----------+-------------------------------------+
| 25/tcp   | smtp    | ANY       | mail receiver for cacert.org        |
+----------+---------+-----------+-------------------------------------+
| 80/tcp   | http    | ANY       | redirect to https                   |
+----------+---------+-----------+-------------------------------------+
| 110/tcp  | pop3    | ANY       | POP3 access for cacert.org mail     |
|          |         |           | addresses                           |
+----------+---------+-----------+-------------------------------------+
| 143/tcp  | imap    | ANY       | IMAP access for cacert.org mail     |
|          |         |           | addresses                           |
+----------+---------+-----------+-------------------------------------+
| 443/tcp  | https   | ANY       | Webserver for community.cacert.org  |
+----------+---------+-----------+-------------------------------------+
| 465/tcp  | smtps   | ANY       | SMTPS for cacert.org mail addresses |
+----------+---------+-----------+-------------------------------------+
| 587/tcp  | smtp    | ANY       | mail submission for cacert.org mail |
|          |         |           | addresses                           |
+----------+---------+-----------+-------------------------------------+
| 993/tcp  | imaps   | ANY       | IMAPS access for cacert.org mail    |
|          |         |           | addresses                           |
+----------+---------+-----------+-------------------------------------+
| 995/tcp  | pop3s   | ANY       | POP3S access for cacert.org mail    |
|          |         |           | addresses                           |
+----------+---------+-----------+-------------------------------------+
| 4190/tcp | sieve   | ANY       | Manage sieve access for cacert.org  |
|          |         |           | mail addresses                      |
+----------+---------+-----------+-------------------------------------+
| 3306/tcp | mysql   | local     | MariaDB database server             |
+----------+---------+-----------+-------------------------------------+
| 5665/tcp | icinga2 | monitor   | remote monitoring service           |
+----------+---------+-----------+-------------------------------------+
| 9443/tcp | https   | community | self service API                    |
+----------+---------+-----------+-------------------------------------+

Running services
----------------

.. index::
   single: cacert-selfservice-api
   single: cron
   single: dbus
   single: dovecot
   single: icinga2
   single: mariadb
   single: nginx
   single: openssh
   single: postfix
   single: puppet
   single: rsyslog

+------------------------+--------------------------------------------+--------------------------------------------------+
| Service                | Usage                                      | Start mechanism                                  |
+========================+============================================+==================================================+
| cacert-selfservice-api | CAcert community self service API          | systemd unit ``cacert-selffservice-api.service`` |
+------------------------+--------------------------------------------+--------------------------------------------------+
| cron                   | job scheduler                              | systemd unit ``cron.service``                    |
+------------------------+--------------------------------------------+--------------------------------------------------+
| dbus-daemon            | System message bus daemon                  | systemd unit ``dbus.service``                    |
+------------------------+--------------------------------------------+--------------------------------------------------+
| dovecot                | IMAP(s), POP3(s) and sieve filter daemon   | systemd unit ``dovecot.service``                 |
+------------------------+--------------------------------------------+--------------------------------------------------+
| icinga2                | Icinga2 monitoring agent                   | systemd unit ``icinga2.service``                 |
+------------------------+--------------------------------------------+--------------------------------------------------+
| MariaDB                | MariaDB database server for email services | systemd unit ``mariadb.service``                 |
+------------------------+--------------------------------------------+--------------------------------------------------+
| nginx                  | Web server for community.cacert.org        | systemd unit ``nginx.service``                   |
+------------------------+--------------------------------------------+--------------------------------------------------+
| openssh server         | ssh daemon for remote administration       | systemd unit ``ssh.service``                     |
+------------------------+--------------------------------------------+--------------------------------------------------+
| Postfix                | SMTP server for cacert.org                 | systemd unit ``postfix.service``                 |
+------------------------+--------------------------------------------+--------------------------------------------------+
| Puppet agent           | configuration management agent             | systemd unit ``puppet.service``                  |
+------------------------+--------------------------------------------+--------------------------------------------------+
| rsyslog                | syslog daemon                              | systemd unit ``rsyslog.service``                 |
+------------------------+--------------------------------------------+--------------------------------------------------+

Databases
---------

+---------+---------------+----------------------------------+
| RDBMS   | Name          | Used for                         |
+=========+===============+==================================+
| MariaDB | cacertusers   | database for dovecot and postfix |
+---------+---------------+----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`community`
* all @cacert.org address owners have access to POP3 (STARTTLS and POP3S), IMAP
  (STARTTLS and IMAPS), SMTPS, SMTP submission (STARTTLS) and manage sieve

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`issue` for OTRS mail
* :doc:`lists` for mailing lists
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`webstatic` as backend for the community.cacert.org web content

* arbitrary Internet SMTP servers for outgoing mail

Security
========

.. sshkeys::
   :RSA:     SHA256:yLaPPrmoOQI5G3hoa0iFoxf6wPdLBJCnizLsu+6SHfE MD5:a1:d2:17:53:6b:0f:b6:a4:14:13:46:f7:04:ef:4a:23
   :ECDSA:   SHA256:oRTeePwmvQ3G+iIG18BFGeyHUCPPID5EbUu7vE4k2hk MD5:16:95:af:c9:71:f4:d8:f7:91:7f:f7:2f:25:b3:f1:63
   :ED25519: SHA256:1P4xZSBrppuvRkMlMThWF4mRhog3Xtiribz8RBFTUiE MD5:db:1e:68:3f:dd:b0:bb:68:c8:8b:cb:39:85:7d:f7:40

Non-distribution packages and modifications
-------------------------------------------

* CAcert community self service system API

  The system runs the CAcert community self service system API developed in the
  :cacertgit:`cacert-selfservice-api`.

  The software is installed from a Debian package that is hosted on :doc:`webstatic`.

  The software is built on :doc:`jenkins` via the `cacert-selfservice-api Job`_
  when there are changes in Git. The Debian package can be built using
  :program:`gbp`.

  The software is installed and configured via Puppet.

  .. _cacert-selfservice-api Job: https://jenkins.cacert.org/job/cacert-selfservice-api/

Building the cacert-selfservice-api Debian package
--------------------------------------------------

The cacert-selfservice-api git repository contains a debian branch that can be
used to build the package.

The Debian package can be built using :program:`gbp`. For a clean build
environment using sbuild/schroot is recommended.

.. code-block:: bash

  sudo sbuild-createchroot --arch=amd64 --chroot-prefix=buster-cacert \
    --extra-repository="deb http://deb.debian.org/debian buster-backports main" \
    buster /srv/chroot/buster-cacert-amd64 http://deb.debian.org/debian
  gbp buildpackage --git-builder="sbuild --build-dep-resolver=aptitude \
    -d buster-cacert

Uploads can be done via sftp with the debarchive user on :doc:`webstatic`. You
need an ssh public key in the user's :file:`~/.ssh/authorized_keys` file.
Packages are only accepted if they are signed with a GPG key whose public key
is stored in the keyring of the reprepro installation on :doc:`webstatic`.

Risk assessments on critical packages
-------------------------------------

Postfix and Dovecot have very good security reputation. The system is patched
regularly.

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

The CAcert community self service API software is developed using `Go
<https://golang.org/>`_ which handles a lot of common programming errors at
compile time and has a quite good security track record.

The CAcert community self service API system is run as a separate user
``cacert-selfservice-api`` and is built as a small self-contained static
binary. Access is restricted via https and authenticated with eliptic curve
public key cryptography.

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
   :altnames:   DNS:cert.community.cacert.org, DNS:cert.email.cacert.org, DNS:community.cacert.org, DNS:email.cacert.org, DNS:nocert.community.cacert.org, DNS:nocert.email.cacert.org
   :certfile:   /etc/ssl/certs/ssl-cert-community-cacert.crt
   :keyfile:    /etc/ssl/private/ssl-cert-community-cacert.key
   :serial:     147CB0
   :expiration: Feb 18 11:39:53 2022 GMT
   :sha1fp:     B2:90:DE:4D:8D:D9:3A:FE:22:3A:67:95:E2:CD:F7:30:55:4B:38:AC
   :issuer:     CA Cert Signing Authority

.. sslcert:: community.cacert.org
   :certfile:  /etc/ssl/public/community.cacert.org.crt.pem
   :keyfile:   /etc/ssl/private/community.cacert.org.key.pem
   :serial:    147CB0
   :secondary:

The server certificate for the CAcert community self service API

.. sslcert:: email.infra.cacert.org
   :altnames:   DNS:email.infra.cacert.org
   :certfile:   /etc/cacert-selfservice-api/certs/server.crt.pem
   :keyfile:    /etc/cacert-selfservice-api/private/server.key.pem
   :serial:     02D954
   :expiration: Aug 16 10:01:04 2021 GMT
   :sha1fp:     C7:34:5A:CF:3F:82:8E:82:4D:2C:90:55:48:7D:BF:5A:17:53:F2:E7
   :issuer:     CAcert Class 3 Root

The certificate is rolled out by Puppet. All changes to the certificate need to
be made to the file :file:`hieradata/nodes/email.yaml` in the
:cacertgit:`cacert-puppet` repository.

.. note::

   Postfix uses the email.cacert.org certificate for client authentication if
   requested by a target server.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: cacert-selfservice-api; configuration

cacert-selfservice-api configuration
------------------------------------

The service configuration is contained in
`/etc/cacert-selfservice-api/config.yaml` and is managed by the Puppet manifest
profiles::cacert_selfservice_api.

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
   pair: MariaDB; configuration

MariaDB configuration
---------------------

MariaDB configuration is stored in the :file:`/etc/mysql/` directory.

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

Email admins can create new email user accounts via
https://selfservice.cacert.org/create-email-account. The contact email address
entered in the web form will receive an email that contains a link to allow
setting an initial password. Setting the initial password only works if the
user authenticates with a valid client certificate for the contact email
address.

.. note::

   * users can reset their password via
     https://selfservice.cacert.org/password-reset

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

.. todo:: implement CRL checking

.. todo::
   throttle brute force attack attempts using fail2ban or similar mechanism

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
