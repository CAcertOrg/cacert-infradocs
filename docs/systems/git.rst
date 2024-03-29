.. index::
   single: Systems; Git

===
Git
===

Purpose
=======

`Git`_ server for the :wiki:`Software` development and :wiki:`System
Administration <SystemAdministration/Team>` teams.

.. _Git: https://www.git-scm.com/

Application Links
-----------------

Gitweb
   http://git.cacert.org/gitweb/

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| Git         | :ref:`people_jandd` |
+-------------+---------------------+
| Gitweb      | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* git-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` and :ref:`people_neo` have :program:`sudo` access on that
machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.250`
:IP Intranet: :ip:v4:`172.16.2.250`
:IP Internal: :ip:v4:`10.0.0.250`
:MAC address: :mac:`00:ff:2e:b0:4b:1b` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Git

Monitoring
----------

:internal checks: :monitor:`git.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Git

===================== ======== ============================================
Name                  Type     Content
===================== ======== ============================================
git.cacert.org.       IN A     213.154.225.250
git.cacert.org.       IN SSHFP 1 1 23C7622D6DB5822C809152C1C0FD9EA7838F76C6
git.cacert.org.       IN SSHFP 1 2 DABBE1766C7933071C4E6942A1DFC72C26D9D867D8DEE84BEDA210C8EF9EA2C5
git.cacert.org.       IN SSHFP 2 1 8509DB491902FE10AB84C8F24B02F10C1ADF0E7F
git.cacert.org.       IN SSHFP 2 2 00C20C26B6B9A026BBB11B5C45CBEC5D3AB44A039DC0F097CAD88374D3567D01
git.cacert.org.       IN SSHFP 3 1 60DE5788BD83ABC7F315B667F634BDA5DA8502ED
git.cacert.org.       IN SSHFP 3 2 132BD98483440124F6B8117148B02A66645477F53C18F974E4DECB32A7495644
git.cacert.org.       IN SSHFP 4 1 13D611007B43D073CF4D89784510398116623EB7
git.cacert.org.       IN SSHFP 4 2 40A61A25488FE01C056EAAFF703EF0FF9C6B01BEE00580A91B95741DFAA59751
git.intra.cacert.org. IN A     172.16.2.250
===================== ======== ============================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.9

* Debian GNU/Linux 10.9

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
| 80/tcp   | http    | ANY     | application                 |
+----------+---------+---------+-----------------------------+
| 443/tcp  | https   | ANY     | application                 |
+----------+---------+---------+-----------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service   |
+----------+---------+---------+-----------------------------+
| 9418/tcp | git     | ANY     | Git daemon port             |
+----------+---------+---------+-----------------------------+

.. todo:: disable insecure git-daemon port and http for git, replace these with
   https for read access and git+ssh for write access

Running services
----------------

.. index::
   single: Apache httpd
   single: Postfix
   single: cron
   single: nrpe
   single: openssh
   single: rsyslog
   single: git-daemon

+--------------------+---------------------+----------------------------------------+
| Service            | Usage               | Start mechanism                        |
+====================+=====================+========================================+
| openssh server     | ssh daemon for      | init script :file:`/etc/init.d/ssh`    |
|                    | remote              |                                        |
|                    | administration      |                                        |
+--------------------+---------------------+----------------------------------------+
| Apache httpd       | Webserver for       | init script                            |
|                    | gitweb              | :file:`/etc/init.d/apache2`            |
|                    |                     |                                        |
+--------------------+---------------------+----------------------------------------+
| cron               | job scheduler       | init script :file:`/etc/init.d/cron`   |
+--------------------+---------------------+----------------------------------------+
| rsyslog            | syslog daemon       | init script                            |
|                    |                     | :file:`/etc/init.d/syslog`             |
+--------------------+---------------------+----------------------------------------+
| Postfix            | SMTP server for     | init script                            |
|                    | local mail          | :file:`/etc/init.d/postfix`            |
|                    | submission          |                                        |
+--------------------+---------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring   | init script                            |
|                    | service queried by  | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`      |                                        |
+--------------------+---------------------+----------------------------------------+
| runit              | service supervision | :file:`/etc/inittab` entry             |
|                    | for git-daemon      |                                        |
+--------------------+---------------------+----------------------------------------+
| git-daemon         | Daemon for native   | runit service description in           |
|                    | Git protocol        | :file:`/etc/sv/git-daemon/run`         |
|                    | access              |                                        |
+--------------------+---------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`jenkins` for git repository access

Outbound network connections
----------------------------

* crl.cacert.org (rsync) for getting CRLs
* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`jenkins` for triggering web hooks

Security
========

.. sshkeys::
   :RSA:     SHA256:2rvhdmx5MwccTmlCod/HLCbZ2GfY3uhL7aIQyO+eosU MD5:b6:85:16:ad:57:a1:45:3c:33:e5:f1:64:04:0d:7a:ab
   :DSA:     SHA256:AMIMJra5oCa7sRtcRcvsXTq0SgOdwPCXytiDdNNWfQE MD5:27:e5:f3:95:b8:4e:73:48:b5:f2:28:8f:32:5a:96:70
   :ECDSA:   SHA256:EyvZhINEAST2uBFxSLAqZmRUd/U8GPl05N7LMqdJVkQ MD5:b2:f4:80:77:98:95:46:17:7a:9e:7d:73:65:6e:f4:9c
   :ED25519: SHA256:QKYaJUiP4BwFbqr/cD7w/5xrAb7gBYCpG5V0Hfqll1E MD5:38:6b:90:f7:8b:c7:b2:cf:cd:86:29:5c:e4:03:fa:35

Dedicated user roles
--------------------

+-----------------+----------------------------------------------------+
| Group           | Purpose                                            |
+=================+====================================================+
| git-birdshack   | access to :wiki:`BirdShack` git repositories       |
+-----------------+----------------------------------------------------+
| softass         | Software assessors                                 |
+-----------------+----------------------------------------------------+
| git-boardvoting | access to board voting git repository              |
+-----------------+----------------------------------------------------+
| git-rccrtauth   | access to Roundcube certificate authentication git |
|                 | repository                                         |
+-----------------+----------------------------------------------------+
| git-infra       | access to infrastructure git repositories          |
+-----------------+----------------------------------------------------+

.. todo:: think about regulating git access by a proper git repository manager
   like gitolite or gitea

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

The package git-daemon-run exposes the git native protocol which is prone to
man in the middle attacks that could hand out modified code to users. There are
alternatives (ssh, https) and git-daemon support should be disabled.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: git.cacert.org
   :altnames:   DNS:git.cacert.org
   :certfile:   /etc/ssl/public/git.cacert.org.chain.pem
   :keyfile:    /etc/ssl/private/git.cacert.org.key.pem
   :serial:     151DAF
   :expiration: Jan 20 16:24:43 2024 GMT
   :sha1fp:     F7:33:6D:CB:02:70:82:0D:4E:92:16:0F:15:C0:42:46:5E:4A:0E:ED
   :issuer:     CA Cert Signing Authority

The :file:`/etc/ssl/public/git.c.o.chain.crt` contains the CAcert.org Class 1
certificate too.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index:: Git repositories

Git repositories
----------------

.. index::
   pair: Apache httpd; configuration

Apache httpd configuration
--------------------------

Apache httpd serves the gitweb interface via http and https. The http
VirtualHost redirects all traffic to https. The following changes have been
applied to the Debian package's Apache httpd configuration:

.. literalinclude:: ../configdiff/git/git-apache-config.diff
   :language: diff

.. index::
   pair: Gitweb; configuration

Gitweb configuration
--------------------

Gitweb is configured in :file:`/etc/gitweb.conf` which has the following
changes to the version contained in the distribution package:

.. literalinclude:: ../configdiff/git/gitweb.conf.diff
   :language: diff

.. index::
   pair: runit; configuration
   pair: git-daemon; configuration

git-daemon configuration
------------------------

The git-daemon is started by runit. The configuration is stored in
:file:`/etc/sv/git-daemon/run` and has the following changes to the version
contained in the distribution package git-daemon-run:

.. literalinclude:: ../configdiff/git/git-daemon-run.diff
   :language: diff

The runit service handling is triggered through :file:`/etc/inittab`.

Tasks
=====

Changes
=======

Planned
-------

.. todo:: enable IPv6

System Future
-------------

* No plans

Additional documentation
========================

Adding a git repository
-----------------------

The git repositories are stored in :file:`/var/cache/git/`. To create a new
repository use:

.. code-block:: shell

   cd /var/cache/git/
   git init --bare --shared=group <reponame.git>
   chgrp -R <groupname> <reponame.git>

The gitweb index is built from all repositories that contain a file
:file:`git-daemon-export-ok`. You should also put a description in the
repository's :file:`description` file and set the repository owner via:

.. code-block:: shell

   cd <reponame.git>
   git config gitweb.owner "Owner information"

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Apache httpd documentation
   http://httpd.apache.org/docs/2.4/
