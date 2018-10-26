.. index::
   single: Systems; Web

===
Web
===

Purpose
=======

Reverse proxy for different websites that handles http to https redirection and
TLS handshakes. The following services are currently proxied by this system:

* Jenkins on :doc:`jenkins`
* codedocs.cacert.org, funding.cacert.org and infradocs.cacert.org on
  :doc:`webstatic`

The proxy should be used for all web applications that do not need access to the
TLS parameters (client certificates, other peer information). Applications that
need to perform TLS handshakes themselves can be proxied through :doc:`proxyin`.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+---------------+---------------------+
| Application   | Administrator(s)    |
+===============+=====================+
| Apache httpd  | :ref:`people_jandd` |
+---------------+---------------------+

Contact
-------

* web-admin@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.242`
:IP Intranet: :ip:v4:`172.16.2.26`
:IP Internal: :ip:v4:`10.0.0.26`
:MAC address: :mac:`00:ff:c7:e5:66:ae` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Web

===================== ======== ====================================================================
Name                  Type     Content
===================== ======== ====================================================================
web.cacert.org.       IN A     213.154.225.242
web.cacert.org.       IN SSHFP 1 1 85F5338D90930200CBBFCE1AAB56988B4C8F0F22
web.cacert.org.       IN SSHFP 1 2 D39CBD51588F322F7B4384274CF0166F25B10F54A6CD153ED7251FF30B5B516E
web.cacert.org.       IN SSHFP 2 1 906F0C17BB0E233B0F52CE33CFE64038D45AC4F2
web.cacert.org.       IN SSHFP 2 2 DBF6221A8A403B4C9F537B676305FDAE07FF45A1C18D88B1141031402AF0250F
web.cacert.org.       IN SSHFP 3 1 7B62D8D1E093C28CDA0F3D2444846128B41C10DE
web.cacert.org.       IN SSHFP 3 2 0917DA677C9E6CAF1818C1151EC2A813623A2B2955A1A850F260D64EF041400B
web.intra.cacert.org. IN A     172.16.2.26
===================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.4

* Debian GNU/Linux 9.4

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
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | local     | mail delivery to local MTA              |
+----------+-----------+-----------+-----------------------------------------+
| 80/tcp   | http      | ANY       | redirects to https                      |
+----------+-----------+-----------+-----------------------------------------+
| 443/tcp  | https     | ANY       | https termination and reverse proxy     |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: nrpe
   single: openssh
   single: postfix
   single: puppet agent
   single: rsyslog

+--------------------+---------------------+----------------------------------------+
| Service            | Usage               | Start mechanism                        |
+====================+=====================+========================================+
| Apache httpd       | http redirector,    | init script                            |
|                    | https reverse proxy | :file:`/etc/init.d/apache2`            |
+--------------------+---------------------+----------------------------------------+
| cron               | job scheduler       | init script :file:`/etc/init.d/cron`   |
+--------------------+---------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring   | init script                            |
|                    | service queried by  | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`      |                                        |
+--------------------+---------------------+----------------------------------------+
| openssh server     | ssh daemon for      | init script :file:`/etc/init.d/ssh`    |
|                    | remote              |                                        |
|                    | administration      |                                        |
+--------------------+---------------------+----------------------------------------+
| Postfix            | SMTP server for     | init script                            |
|                    | local mail          | :file:`/etc/init.d/postfix`            |
|                    | submission          |                                        |
+--------------------+---------------------+----------------------------------------+
| Puppet agent       | configuration       | init script                            |
|                    | management agent    | :file:`/etc/init.d/puppet`             |
+--------------------+---------------------+----------------------------------------+
| rsyslog            | syslog daemon       | init script                            |
|                    |                     | :file:`/etc/init.d/syslog`             |
+--------------------+---------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`jenkins` as backend for the jenkins.cacert.org VirtualHost
* :doc:`webstatic` as backend for the codedocs.cacert.org, funding.cacert.org
  and infradocs.cacert.org VirtualHosts

Security
========

.. sshkeys::
   :RSA:     SHA256:05y9UViPMi97Q4QnTPAWbyWxD1SmzRU+1yUf8wtbUW4 MD5:6d:e5:7e:1d:72:d5:5e:f8:43:80:94:a8:b1:0d:9b:81
   :DSA:     SHA256:2/YiGopAO0yfU3tnYwX9rgf/RaHBjYixFBAxQCrwJQ8 MD5:00:27:11:fe:58:9d:d8:e5:c5:35:34:27:bb:79:86:16
   :ECDSA:   SHA256:CRfaZ3yebK8YGMEVHsKoE2I6KylVoahQ8mDWTvBBQAs MD5:7f:91:92:80:f2:b5:2f:5d:8e:11:3f:9b:62:48:e7:18
   :ED25519: SHA256:IHm9Gjf0u753ADO+WDYLFuHwPK3ReAe101xG/NeCwYk MD5:82:ab:13:33:ee:69:cf:09:18:20:d0:9c:b9:a0:0e:61

Non-distribution packages and modifications
-------------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

Apache httpd is configured with a minimum of enabled modules to allow proxying
and TLS handling only to reduce potential security risks.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

.. todo:: move configuration of :doc:`web` to Puppet code

Keys and X.509 certificates
---------------------------

.. sslcert:: codedocs.cacert.org
   :altnames:   DNS:codedocs.cacert.org
   :certfile:   /etc/ssl/certs/codedocs.cacert.org.crt
   :keyfile:    /etc/ssl/private/codedocs.cacert.org.key
   :serial:     02CB3D
   :expiration: Oct 25 22:35:23 2020 GMT
   :sha1fp:     49:FA:0B:01:C0:9F:74:EF:12:15:8F:CA:8E:D3:2C:FA:0C:7E:3C:F7
   :issuer:     CAcert Class 3 Root

.. sslcert:: funding.cacert.org
   :altnames:   DNS:funding.cacert.org
   :certfile:   /etc/ssl/certs/funding.cacert.org.crt
   :keyfile:    /etc/ssl/private/funding.cacert.org.key
   :serial:     02A770
   :expiration: Feb 16 12:07:35 2019 GMT
   :sha1fp:     36:E0:A1:86:7A:FA:C6:F4:86:9F:CC:9C:61:4D:B9:A4:7C:0F:9F:C9
   :issuer:     CAcert Class 3 Root

.. sslcert:: infradocs.cacert.org
   :altnames:   DNS:infradocs.cacert.org
   :certfile:   /etc/ssl/certs/infradocs.cacert.org.crt
   :keyfile:    /etc/ssl/private/infradocs.cacert.org.key
   :serial:     02C448
   :expiration: May 18 08:21:31 2020 GMT
   :sha1fp:     87:E7:21:19:24:61:D9:82:60:DB:65:41:7C:6C:0A:4E:63:0E:27:F7
   :issuer:     CAcert Class 3 Root

.. sslcert:: jenkins.cacert.org
   :altnames:   DNS:jenkins.cacert.org
   :certfile:   /etc/ssl/certs/jenkins.cacert.org.crt
   :keyfile:    /etc/ssl/private/jenkins.cacert.org.key
   :serial:     02A76F
   :expiration: Feb 16 12:07:29 2019 GMT
   :sha1fp:     D1:E3:5B:73:63:28:C6:31:0F:35:4A:2F:0D:12:B5:6C:3F:72:08:3D
   :issuer:     CAcert Class 3 Root

.. sslcert:: web.cacert.org
   :altnames:   DNS:web.cacert.org
   :certfile:   /etc/ssl/certs/web.cacert.org.crt
   :keyfile:    /etc/ssl/private/web.cacert.org.key
   :serial:     02BE3D
   :expiration: Feb 19 11:44:47 2020 GMT
   :sha1fp:     D5:20:E8:4D:C1:FC:6E:DF:7E:D3:5D:03:03:3D:1B:CB:27:4B:3D:85
   :issuer:     CAcert Class 3 Root

* :file:`/usr/share/ca-certificates/CAcert/class3.crt` CAcert.org Class 3
  certificate for server certificate chains. The Apache httpd configuration
  files reference the symlinked version at :file:`/etc/ssl/certs/class3.pem`.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache httpd configuration
--------------------------

* :file:`/etc/apache2/sites-available/000-default.conf`

  Defines the default VirtualHost for requests reaching this host with no
  specifically handled host name.

* :file:`/etc/apache2/sites-available/codedocs.cacert.org.conf`

  Defines the VirtualHost http://codedocs.cacert.org/ that redirects to
  https://codedocs.cacert.org/ and the VirtualHost
  https://codedocs.cacert.org/ that provides reverse proxy functionality for
  the same host name on :doc:`webstatic`.

* :file:`/etc/apache2/sites-available/funding.cacert.org.conf`

  Defines the VirtualHost http://funding.cacert.org/ that redirects to
  https://funding.cacert.org/ and the VirtualHost https://funding.cacert.org/
  that provides reverse proxy functionality for the same host name on
  :doc:`webstatic`.

* :file:`/etc/apache2/sites-available/infradocs.cacert.org.conf`

  Defines the VirtualHost http://infradocs.cacert.org/ that redirects to
  https://infradocs.cacert.org/ and the VirtualHost
  https://infradocs.cacert.org/ that provides reverse proxy functionality for
  the same host name on :doc:`webstatic`.

* :file:`/etc/apache2/sites-available/jenkins.cacert.org.conf`

  Defines the VirtualHost http://jenkins.cacert.org/ that redirects to
  https://jenkins.cacert.org/ and the VirtualHost https://jenkins.cacert.org/
  that provides reverse proxy functionality for the Jenkins instance on
  :doc:`jenkins`.

Tasks
=====

Planned
-------

.. todo:: manage the web system using Puppet

Changes
=======

System Future
-------------

* No plans

Additional documentation
========================

.. note::
   The system hosted the Drupal based community portal https://www.cacert.eu/
   in the past. The DNS records for this portal have been changed to point to
   the regular https://www.cacert.org/ site. All unreachable VirtualHosts have
   been archived to the backup disk at :doc:`infra02`.

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

* http://httpd.apache.org/docs/2.4/
