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

Code Documentation
   https://codedocs.cacert.org/

Funding
   https://funding.cacert.org/

Infrastructure Documentation
   https://infradocs.cacert.org/

CAcert internal Debian repository
   https://webstatic.infra.cacert.org/

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

.. index::
   single: Monitoring; Webstatic

Monitoring
----------

:internal checks: :monitor:`webstatic.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Webstatic

=========================== ======== ====================================================================
Name                        Type     Content
=========================== ======== ====================================================================
codedocs.cacert.org.        IN CNAME web.cacert.org.
funding.cacert.org.         IN CNAME web.cacert.org.
infradocs.cacert.org.       IN CNAME web.cacert.org.
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
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.8

* Debian GNU/Linux 10.8

Services
========

Listening services
------------------

+----------+---------+---------+----------------------------+
| Port     | Service | Origin  | Purpose                    |
+==========+=========+=========+============================+
| 22/tcp   | ssh     | ANY     | admin console access       |
+----------+---------+---------+----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA |
+----------+---------+---------+----------------------------+
| 80/tcp   | http    | ANY     | application                |
+----------+---------+---------+----------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: dbus
   single: exim
   single: icinga2
   single: openssh
   single: puppet
   single: rsyslog

+----------------+---------------------------------------+----------------------------------+
| Service        | Usage                                 | Start mechanism                  |
+================+=======================================+==================================+
| Apache httpd   | Webserver for static content          | systemd unit ``apache2.service`` |
+----------------+---------------------------------------+----------------------------------+
| cron           | job scheduler                         | systemd unit ``cron.service``    |
+----------------+---------------------------------------+----------------------------------+
| dbus-daemon    | System message bus daemon             | systemd unit ``dbus.service``    |
+----------------+---------------------------------------+----------------------------------+
| Exim           | SMTP server for local mail submission | systemd unit ``exim4.service``   |
+----------------+---------------------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent              | systemd unit ``icinga2.service`` |
+----------------+---------------------------------------+----------------------------------+
| openssh server | ssh daemon for remote administration  | systemd unit ``ssh.service``     |
+----------------+---------------------------------------+----------------------------------+
| Puppet agent   | configuration management agent        | systemd unit ``puppet.service``  |
+----------------+---------------------------------------+----------------------------------+
| rsyslog        | syslog daemon                         | systemd unit ``rsyslog.service`` |
+----------------+---------------------------------------+----------------------------------+

Connected Systems
-----------------

* :doc:`jenkins` for publishing code documentation to codedocs.cacert.org and
  infrastructure documentation to infradocs.cacert.org
* :doc:`monitor`
* :doc:`web` as reverse proxy for hostnames funding.cacert.org and
  infradocs.cacert.org
* :doc:`email` as reverse proxy for the hostname community.cacert.org

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
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
| Role              | Purpose                                           |
+===================+===================================================+
| jenkins-infradocs | Used by :doc:`jenkins` to upload documentation to |
|                   | :file:`/var/www/codedocs.cacert.org/html/` and    |
|                   | :file:`/var/www/infradocs.cacert.org/html/`       |
+-------------------+---------------------------------------------------+

.. todo:: manage ``jenkins-infradocs`` user via Puppet

Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

Apache httpd is configured with a minimum of enabled modules to allow serving
static content and nothing else to reduce potential security risks.

Access to the jenkins-infradocs user is gated by a defined ssh key.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

The host does not provide own TLS services and therefore has no certificates.

Apache httpd configuration
--------------------------

Apache configuration is managed via the Puppet profile
``profiles::static_websites``.

Debian repository configuration
-------------------------------

The Debian repository is managed via the Puppet profile
``profiles::debarchive``. Packages that are uploaded to
:file:`/srv/upload/incoming` are automatically processed by
:program:`inoticoming` and :program:`reprepro`. Only packages signed by a known
PGP key (managed via Puppet) are accepted and provided at
https://webstatic.infra.cacert.org/.

The repository signing key is stored in
:file:`/srv/debarchive/.gnupg/private-keys-v1.d/223894064EE26851A245DE9208C5C0ABF772F7A7.key`.

Tasks
=====

Changes
=======

Planned
-------

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
* https://manpages.debian.org/buster/inoticoming/inoticoming.1.en.html
* https://manpages.debian.org/buster/reprepro/reprepro.1.en.html
