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
:IPv6:        :ip:v6:`2001:7b8:616:162:2::26`
:MAC address: :mac:`00:ff:c7:e5:66:ae` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Web

Monitoring
----------

:internal checks: :monitor:`web.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Web

+-----------------------+----------+----------------------------------------------------------------------+
| Name                  | Type     | Content                                                              |
+=======================+==========+======================================================================+
| web.cacert.org.       | IN A     | 213.154.225.242                                                      |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 1 1 85F5338D90930200CBBFCE1AAB56988B4C8F0F22                         |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 1 2 D39CBD51588F322F7B4384274CF0166F25B10F54A6CD153ED7251FF30B5B516E |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 2 1 906F0C17BB0E233B0F52CE33CFE64038D45AC4F2                         |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 2 2 DBF6221A8A403B4C9F537B676305FDAE07FF45A1C18D88B1141031402AF0250F |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 3 1 7B62D8D1E093C28CDA0F3D2444846128B41C10DE                         |
+-----------------------+----------+----------------------------------------------------------------------+
| web.cacert.org.       | IN SSHFP | 3 2 0917DA677C9E6CAF1818C1151EC2A813623A2B2955A1A850F260D64EF041400B |
+-----------------------+----------+----------------------------------------------------------------------+
| web.intra.cacert.org. | IN A     | 172.16.2.26                                                          |
+-----------------------+----------+----------------------------------------------------------------------+

.. todo:: add SSHFP for ED25519 key, remove SSHFP for DSA key, add AAAA record for IPv6

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.7

* Debian GNU/Linux 10.7

Services
========

Listening services
------------------

+----------+---------+---------+-------------------------------------+
| Port     | Service | Origin  | Purpose                             |
+==========+=========+=========+=====================================+
| 22/tcp   | ssh     | ANY     | admin console access                |
+----------+---------+---------+-------------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA          |
+----------+---------+---------+-------------------------------------+
| 80/tcp   | http    | ANY     | redirects to https                  |
+----------+---------+---------+-------------------------------------+
| 443/tcp  | https   | ANY     | https termination and reverse proxy |
+----------+---------+---------+-------------------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service           |
+----------+---------+---------+-------------------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: icinga2
   single: openssh
   single: postfix
   single: puppet agent
   single: rsyslog

+----------------+--------------------------+----------------------------------+
| Service        | Usage                    | Start mechanism                  |
+================+==========================+==================================+
| Apache httpd   | http redirector,         | systemd unit ``apache2.service`` |
|                | https reverse proxy      |                                  |
+----------------+--------------------------+----------------------------------+
| cron           | job scheduler            | systemd unit ``cron.service``    |
+----------------+--------------------------+----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service`` |
+----------------+--------------------------+----------------------------------+
| openssh server | ssh daemon for           | systemd unit ``ssh.service``     |
|                | remote administration    |                                  |
+----------------+--------------------------+----------------------------------+
| Postfix        | SMTP server for          | systemd unit ``postfix.service`` |
|                | local mail submission    |                                  |
+----------------+--------------------------+----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``  |
|                | management agent         |                                  |
+----------------+--------------------------+----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service`` |
+----------------+--------------------------+----------------------------------+

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
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

All keys and certificates are managed in the file
https://git.cacert.org/cacert-puppet.git/plain/hieradata/nodes/web.yaml in the
:cacertgit:`cacert-puppet`.

.. sslcert:: codedocs.cacert.org
   :altnames:   DNS:codedocs.cacert.org
   :certfile:   /etc/ssl/certs/codedocs.cacert.org.crt
   :keyfile:    /etc/ssl/private/codedocs.cacert.org.key
   :serial:     02E75E
   :expiration: Oct 02 15:38:42 2022 GMT
   :sha1fp:     E5:B7:3B:27:30:45:99:2B:04:8E:39:8F:12:E6:CC:CB:35:06:54:EC
   :issuer:     CAcert Class 3 Root

.. sslcert:: funding.cacert.org
   :altnames:   DNS:funding.cacert.org
   :certfile:   /etc/ssl/certs/funding.cacert.org.crt
   :keyfile:    /etc/ssl/private/funding.cacert.org.key
   :serial:     02EAF6
   :expiration: Jan 17 18:53:51 2023 GMT
   :sha1fp:     30:57:BC:90:4E:C7:A2:CD:D9:BF:AE:7D:5E:9E:FB:B8:3F:3E:0F:64
   :issuer:     CAcert Class 3 Root

.. sslcert:: infradocs.cacert.org
   :altnames:   DNS:infradocs.cacert.org
   :certfile:   /etc/ssl/certs/infradocs.cacert.org.crt
   :keyfile:    /etc/ssl/private/infradocs.cacert.org.key
   :serial:     02E102
   :expiration: May 04 18:37:30 2022 GMT
   :sha1fp:     29:9C:00:5E:14:27:C8:4F:5C:BE:07:F8:96:5B:0B:1F:B5:97:9F:64
   :issuer:     CAcert Class 3 Root

.. sslcert:: jenkins.cacert.org
   :altnames:   DNS:jenkins.cacert.org
   :certfile:   /etc/ssl/certs/jenkins.cacert.org.crt
   :keyfile:    /etc/ssl/private/jenkins.cacert.org.key
   :serial:     02EAF5
   :expiration: Jan 17 18:52:48 2023 GMT
   :sha1fp:     B9:88:8D:51:F4:FA:B1:56:64:8E:C8:23:C5:C4:FE:D8:42:B8:1B:72
   :issuer:     CAcert Class 3 Root

.. sslcert:: web.cacert.org
   :altnames:   DNS:web.cacert.org
   :certfile:   /etc/ssl/certs/web.cacert.org.crt
   :keyfile:    /etc/ssl/private/web.cacert.org.key
   :serial:     02DED2
   :expiration: Jan 22 20:06:47 2022 GMT
   :sha1fp:     30:C0:61:C5:F7:C6:5E:A3:06:DB:B5:2F:B1:2D:DD:DF:60:5F:D6:88
   :issuer:     CAcert Class 3 Root

* :file:`/usr/share/ca-certificates/CAcert/class3_X0E.crt` CAcert.org Class 3
  certificate for server certificate chains. The file is installed from the
  Debian package `ca-cacert`

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache httpd configuration
--------------------------

Apache httpd configuration is fully managed by Puppet. The VirtualHosts are
defined in
https://git.cacert.org/cacert-puppet.git/plain/hieradata/nodes/web.yaml and
the
configuration is done via the `web_proxy`_ profile.

.. _web_proxy: https://git.cacert.org/cacert-puppet.git/tree/sitemodules/profiles/manifests/web_proxy.pp

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
