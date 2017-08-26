.. index::
   single: Systems; Svn

===
Svn
===

Purpose
=======

This system hosts the `Subversion`_ repository that is used for some CAcert
documents and code that has not been moved to :doc:`git` yet, for example:

* Events
* Policy development
* Documentation

.. _Subversion: http://subversion.apache.org/

Application Links
-----------------

The subversion repository
     https://svn.cacert.org/CAcert/

Anonymous read-only HTTP access
     http://svn.cacert.org/CAcert/

Username/password authenticated HTTPS access
     https://nocert.svn.cacert.org/CAcert/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin

Application Administration
--------------------------

+---------------+---------------------+
| Application   | Administrator(s)    |
+===============+=====================+
| Subversion    | :ref:`people_jandd` |
+---------------+---------------------+

Contact
-------

* svn-admin@cacert.org

Additional People
-----------------

:ref:`Mario Lipinski <people_mario>` has :program:`sudo` access on that machine
too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.238`
:IP Intranet: :ip:v4:`172.16.2.15`
:IP Internal: :ip:v4:`10.0.0.20`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::15`
:MAC address: :mac:`00:16:3e:13:87:bb` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Svn

========================== ======== ============================================
Name                       Type     Content
========================== ======== ============================================
svn.cacert.org.            IN SSHFP 1 1 1128972FB54F927477A781718E2F9C114E9CA383
svn.cacert.org.            IN SSHFP 2 1 3A36E5DF06304C481F01FC723FD88A086E82D986
svn.cacert.org.            IN A     213.154.225.238
cert.svn.cacert.org.       IN CNAME svn.cacert.org.
nocert.svn.cacert.org      IN CNAME svn.cacert.org
========================== ======== ============================================

.. todo:: add AAAA record for IPv6 address

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Jessie
   single: Debian GNU/Linux; 8.8

* Debian GNU/Linux 8.8

Applicable Documentation
------------------------

Access to specific paths in the repository is granted on request if approved by
team leaders/officers.

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 80/tcp   | http      | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 443/tcp  | https     | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: Exim
   single: Puppet agent
   single: cron
   single: nrpe
   single: openssh

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| Apache httpd       | Webserver for      | init script                            |
|                    | Subversion         | :file:`/etc/init.d/apache2`            |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| Exim               | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/exim4`              |
|                    | submission         |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+
| Puppet agent       | configuration      | init script                            |
|                    | management agent   | :file:`/etc/init.d/puppet`             |
+--------------------+--------------------+----------------------------------------+

Connected Systems
-----------------

* Connection from :doc:`blog` because blog uses some resources served from svn
* Connection from https://www.cacert.org/ because blog posts are embedded there
* :doc:`monitor`

Outbound network connections
----------------------------

* crl.cacert.org (rsync) for getting CRLs
* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA:     df:98:f5:ea:05:c1:47:52:97:58:8f:42:55:d6:d9:b6
   :DSA:     07:2b:10:b1:6d:79:35:0f:83:aa:fc:ba:d6:2f:51:dc
   :ECDSA:   f9:10:2c:bb:1d:2f:d4:c4:b3:74:b6:f9:26:4c:64:54
   :ED25519: 56:88:68:0d:3a:32:13:6b:da:bd:ae:d7:cc:9b:b8:f5


Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

Apache httpd is configured with a minimum of enabled modules to allow TLS and
Subversion but nothing else to reduce potential security risks.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: svn.cacert.org
   :altnames:   DNS:cert.svn.cacert.org, DNS:nocert.svn.cacert.org, DNS:svn.cacert.org
   :certfile:   /etc/apache2/ssl/svn.cacert.org.crt.pem
   :keyfile:    /etc/apache2/ssl/svn.cacert.org.key.pem
   :serial:     028B8D
   :expiration: Mar 24 10:57:53 18 GMT
   :sha1fp:     E2:E2:26:B3:5D:8A:FA:96:C0:94:A2:E5:11:9D:89:C7:AC:C7:B3:2D
   :issuer:     CAcert Class 3 Root

* `/etc/apache2/ssl/cacert-certs.pem` CAcert.org Class 1 and Class 3 CA certificates (allowed CA certificates for client certificates)
* `/etc/apache2/ssl/cacert-chain.pem` CAcert.org Class 1 certificate (certificate chain for server certificate)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: Apache httpd; configuration

Apache httpd configuration
--------------------------

The main configuration files for Apache httpd are:

* :file:`/etc/apache2/sites-available/cert.svn.cacert.org`

  Defines the https VirtualHost for IPv4 and IPv6 on port 443 using client
  certificate authentication. The SNI server names svn.cacert.org and
  cert.svn.cacert.org are handled by the VirtualHost configuration in this
  file.

* :file:`/etc/apache2/sites-available/nocert.svn.cacert.org`

  Defines the https VirtualHost for IPv4 and IPv6 on port 443 using
  username/password authentication. The SNI server name nocert.svn.cacert.org
  is handled by the VirtualHost configuration in this file.

* :file:`/etc/apache2/sites-available/000-default`

  Defines the http read-only VirtualHost for IPv4 and IPv6 on port 80.

These files include the following files to configure Subversion and
authentication/authorization:

* :file:`/etc/apache2/sites-available/ssl_config.include`

  contains VirtualHost specific TLS configuration

* :file:`/etc/apache2/sites-available/svn_anonymous_config.include`

  configure anonymous SVN access without defining a password file and thus
  restricting SVN paths that require authentication

* :file:`/etc/apache2/sites-available/svn_pwauth_config.include`

  configure username/password authenticated access to SVN using the password
  file :file:`/srv/dav_svn.passwd`.

* :file:`/etc/apache2/sites-available/svn_certauth_config.include`

  configure TLS client certificate authenticated access to SVN using the first
  email address in the client certificate's Subject Distinguished name as user
  name

Subversion configuration
------------------------

Subversion authorization (aliases, groups and ACLs) is configured in
:file:`/srv/dav_svn.authz` in the format specified in `path based authorization
<http://svnbook.red-bean.com/de/1.8/svn.serverconfig.pathbasedauthz.html>`_ in
the Subversion book.

The repository data is stored in :file:`/srv/svnrepo`.

CRL update job
--------------

CRLs are updated by :file:`/etc/cron.daily/fetchcrls`.


Tasks
=====

Planned
-------

The configuration of this system will be migrated to a setup fully managed by
Puppet.

X.509 Auth for policy
---------------------

* Documentation officer has endorsed
* Waiting on Org-assurer word as to org-assurer policy stuff

Mail notifications
------------------

* commit hooks on policy to policy list?

Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`
   * :wiki:`Technology/KnowledgeBase/ClientCerts#SVN`
   * :wiki:`SystemAdministration/Systems/Svn/Setup`

References
----------

* http://svnbook.red-bean.com/en/1.5/svn.reposadmin.html
