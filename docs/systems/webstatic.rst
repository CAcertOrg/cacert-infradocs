.. index::
   single: Systems; Webstatic

=========
Webstatic
=========

Purpose
=======

This system provides a web server for serving static content. HTTP requests
for this system are proxied through :doc:`web` which also handles TLS
termination and redirects from http scheme URLs to https.

Application Links
-----------------

Funding
   https://funding.cacert.org/

Infrastructure Documentation
   https://infradocs.cacert.org/

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
| Apache httpd  | :ref:`people_jandd` |
+---------------+---------------------+
| Gitolite      | :ref:`people_jandd` |
+---------------+---------------------+

Contact
-------

* webstatic-admin@cacert.org

Additional People
-----------------

No additional people have access to this machine.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: reverse proxied from :doc:`web`
:IP Intranet: :ip:v4:`172.16.2.116`
:IP Internal: :ip:v4:`10.0.0.116`
:MAC address: :mac:`00:ff:67:39:23:f2` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; <machine>

=========================== ======== ====================================================================
Name                        Type     Content
=========================== ======== ====================================================================
funding.cacert.org.         IN CNAME webstatic.cacert.org.
infradocs.cacert.org.       IN CNAME webstatic.cacert.org.
webstatic.cacert.org.       IN A     213.154.225.242
webstatic.cacert.org.       IN SSHFP 1 1 30897A7A984D8350495946D54C6374E9331237EF
webstatic.cacert.org.       IN SSHFP 1 2 32BB10C5CF48532D077066E012230058DDF3CCE731C561F228E310EB7A546E3F
webstatic.cacert.org.       IN SSHFP 2 1 868361A51EC60607BFD964D0F8F3E4EE5E803FC6
webstatic.cacert.org.       IN SSHFP 2 2 A173BB85EC19F63ECB273BCA130EF63501FE1B89FD55B62997195E6816CAB547
webstatic.cacert.org.       IN SSHFP 3 1 7FC847CEC20B9D65296D4A0EDAFBA22A14EE9DC4
webstatic.cacert.org.       IN SSHFP 3 2 68879264E0ED5D0914797BF2292436FB32CCA24683DCF5D927A53589C1BFB6D7
webstatic.intra.cacert.org. IN A     172.16.2.116
=========================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.3

* Debian GNU/Linux 9.3

Applicable Documentation
------------------------

This is it :-)

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console and gitolite access       |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 80/tcp   | http      | ANY       | application                             |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: Exim
   single: cron
   single: nginx
   single: nrpe
   single: openssh

+--------------------+----------------------+----------------------------------------+
| Service            | Usage                | Start mechanism                        |
+====================+======================+========================================+
| openssh server     | ssh daemon for       | init script :file:`/etc/init.d/ssh`    |
|                    | remote               |                                        |
|                    | administration       |                                        |
|                    | and git access       |                                        |
+--------------------+----------------------+----------------------------------------+
| Apache httpd       | Webserver for static | init script                            |
|                    | content              | :file:`/etc/init.d/apache2`            |
+--------------------+----------------------+----------------------------------------+
| cron               | job scheduler        | init script :file:`/etc/init.d/cron`   |
+--------------------+----------------------+----------------------------------------+
| rsyslog            | syslog daemon        | init script                            |
|                    |                      | :file:`/etc/init.d/syslog`             |
+--------------------+----------------------+----------------------------------------+
| Exim               | SMTP server for      | init script                            |
|                    | local mail           | :file:`/etc/init.d/exim4`              |
|                    | submission           |                                        |
+--------------------+----------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring    | init script                            |
|                    | service queried by   | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`       |                                        |
+--------------------+----------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`jenkins` for publishing infrastructure documentation to
  infradocs.cacert.org
* :doc:`monitor`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT

Security
========

.. sshkeys::
   :RSA:     SHA256:MrsQxc9IUy0HcGbgEiMAWN3zzOcxxWHyKOMQ63pUbj8 MD5:da:e7:16:f9:98:b0:77:4f:38:a6:49:35:a5:5a:2a:c2
   :DSA:     SHA256:oXO7hewZ9j7LJzvKEw72NQH+G4n9VbYplxleaBbKtUc MD5:12:a5:87:27:6b:2f:e3:cd:d6:e5:fb:f2:43:2f:7c:be
   :ECDSA:   SHA256:aIeSZODtXQkUeXvyKSQ2+zLMokaD3PXZJ6U1icG/ttc MD5:5e:94:ad:e8:84:3b:e2:b0:0b:7f:44:ec:a9:99:95:b2
   :ED25519: SHA256:NC34l1qSufrBdjxjJk75oOnmhrQW1VkLILsOhJle77A MD5:da:58:d0:89:23:6f:ca:f7:b2:5f:a3:51:2f:6b:95:0d

Dedicated user roles
--------------------

+-------------------+---------------------------------------------------+
| Group             | Purpose                                           |
+===================+===================================================+
| git               | User for :program:`gitolite`                      |
+-------------------+---------------------------------------------------+
| jenkins-infradocs | Used by :doc:`jenkins` to upload documentation to |
|                   | :file:`/var/www/infradocs.cacert.org/html/`       |
+-------------------+---------------------------------------------------+

Non-distribution packages and modifications
-------------------------------------------

The used :program:`gitolite` version is from Debian Jessie and should either
be replaced by :program:`gitolite3` from Debian Stretch or a combination of
git repositories on :doc:`git` and web hooks for triggering updates.

.. todo:: replace :program:`gitolite` with a maintained service

Risk assessments on critical packages
-------------------------------------

Apache httpd is configured with a minimum of enabled modules to allow serving
static content and nothing else to reduce potential security risks.

Access to :program:`gitolite` and the jenkins-infradocs user is gated by a
defined set of ssh keys.

.. todo:: check access on gitolite repositories

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

The host does not provide TLS services and therefore has no certificates.

.. todo::
   move the TLS configuration for the served VirtualHosts to :doc:`webstatic`

Apache httpd configuration
--------------------------

The main configuration files for Apache httpd are:

* :file:`/etc/apache2/sites-available/000-default.conf`

  Defines the default VirtualHost for requests reaching this host with no
  specifically handled host name.

* :file:`/etc/apache2/sites-available/funding.cacert.org.conf`

  Defines the VirtualHost for https://funding.cacert.org/

* :file:`/etc/apache2/sites-available/infradocs.cacert.org.conf`

  Defines the VirtualHost for https://infradocs.cacert.org/


Tasks
=====

Planned
-------

* Manage the system using Puppet

Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* http://httpd.apache.org/docs/2.4/
* http://gitolite.com/gitolite/migr/