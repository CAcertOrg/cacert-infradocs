.. index::
   single: Systems; Emailout

========
Emailout
========

Purpose
=======

This system is used as outgoing mail relay for other infrastructure services.

Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: :ref:`people_jselzer`

Contact
-------

* emailout-admin@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.239`
:IP Intranet: :ip:v4:`172.16.2.10` (outbound SNAT) and :ip:v4:`172.16.2.32`
:IP Internal: :ip:v4:`10.0.0.32`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::239`
:MAC address: :mac:`00:ff:12:01:65:02` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Emailout

Monitoring
----------

:internal checks: :monitor:`emailout.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; Emailout

+----------------------------+----------+----------------------------------------------------------------------+
| Name                       | Type     | Content                                                              |
+============================+==========+======================================================================+
| emailout.cacert.org.       | IN A     | 213.154.225.239                                                      |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN AAAA  | 2001:7b8:616:162:2::239                                              |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 1 1 1ba1ab632911e8a68a69521130120695086d858c                         |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 1 2 6e50d5b2034006b69eb7ba19d3f3fd2c48015bea2bb3d5e2a0f8cf25ff030055 |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 3 1 527004f2091d2cef2c28b5f8241fc0e76307b2ba                         |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 3 2 9094dcf8860523a83542ec4cc46fbcfed396f5525bc202cfecf42d1a7044136d |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 4 1 63f40df8536052d33d2d515eceb111ccb7983619                         |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.cacert.org.       | IN SSHFP | 4 2 4ceb488ad17ea7c8db161fdf3357e273d2ea1fe5be183794aacd7c4bfdfaa8a5 |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.intra.cacert.org. | IN A     | 172.16.2.32                                                          |
+----------------------------+----------+----------------------------------------------------------------------+
| emailout.infra.cacert.org. | IN A     | 10.0.0.32                                                            |
+----------------------------+----------+----------------------------------------------------------------------+

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.0

* Debian GNU/Linux 10.0

Applicable Documentation
------------------------

The following packages where installed after the container setup::

   apt-get install vim-nox screen git etckeeper postfix postfix-pcre opendkim \
     opendkim-tools man-db rsyslog logrotate \
     heirloom-mailx netcat-openbsd swaks

Services
========

Listening services
------------------

+----------+---------+----------+----------------------------------+
| Port     | Service | Origin   | Purpose                          |
+==========+=========+==========+==================================+
| 22/tcp   | ssh     | ANY      | admin console access             |
+----------+---------+----------+----------------------------------+
| 25/tcp   | smtp    | intranet | mail delivery from intranet MTAs |
+----------+---------+----------+----------------------------------+
| 5665/tcp | icinga2 | monitor  | remote monitoring service        |
+----------+---------+----------+----------------------------------+

Running services
----------------

.. index::
   single: cron
   single: dbus
   single: icinga2
   single: opendkim
   single: openssh
   single: postfix
   single: puppet agent
   single: rsyslog

+----------------+--------------------------+-----------------------------------+
| Service        | Usage                    | Start mechanism                   |
+================+==========================+===================================+
| cron           | job scheduler            | systemd unit ``cron.service``     |
+----------------+--------------------------+-----------------------------------+
| dbus-daemon    | System message bus       | systemd unit ``dbus.service``     |
|                | daemon                   |                                   |
+----------------+--------------------------+-----------------------------------+
| icinga2        | Icinga2 monitoring agent | systemd unit ``icinga2.service``  |
+----------------+--------------------------+-----------------------------------+
| OpenDKIM       | DKIM signing daemon      | systemd unit ``opendkim.service`` |
+----------------+--------------------------+-----------------------------------+
| openssh server | ssh daemon for remote    | systemd unit ``ssh.service``      |
|                | administration           |                                   |
+----------------+--------------------------+-----------------------------------+
| Postfix        | SMTP server for          | systemd unit ``postfix.service``  |
|                | local mail submission,   |                                   |
|                | and mail relay for       |                                   |
|                | infrastructure systems   |                                   |
+----------------+--------------------------+-----------------------------------+
| Puppet agent   | configuration            | systemd unit ``puppet.service``   |
|                | management agent         |                                   |
+----------------+--------------------------+-----------------------------------+
| rsyslog        | syslog daemon            | systemd unit ``rsyslog.service``  |
+----------------+--------------------------+-----------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* SMTP (25/tcp) from other infrastructure systems

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* :doc:`puppet` (tcp/8140) as Puppet master
* SMTP (25/tcp) to :doc:`email`, :doc:`issue` and :doc:`lists`

Security
========

.. sshkeys::
   :RSA:     SHA256:blDVsgNABraet7oZ0/P9LEgBW+ors9XioPjPJf8DAFU MD5:56:09:89:92:af:3c:15:e4:a3:06:11:63:0e:be:b6:a2
   :ECDSA:   SHA256:kJTc+IYFI6g1QuxMxG+8/tOW9VJbwgLP7PQtGnBEE20 MD5:cb:3c:69:c5:a1:90:c6:8e:55:40:83:6c:10:3f:09:b4
   :ED25519: SHA256:TOtIitF+p8jbFh/fM1fic9LqH+W+GDeUqs18S/36qKU MD5:04:ca:72:d0:21:0a:4a:8b:a5:f7:a2:2f:10:e5:3f:92

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

Postfix has a very good security reputation. The system is patched regularly.

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

.. todo:: setup a proper certificate for incoming STARTTLS

.. index::
   pair: DKIM; Private Key
   see: DKIM; OpenDKIM

* :file:`/etc/dkim/2015.private` contains the RSA private key to be used for
  :term:`DKIM` signing by OpenDKIM.

.. index::
   pair: DKIM; DNS
   see: DNS; OpenDKIM

* :file:`/etc/dkim/2015.txt` contains a textual DNS record representation for
  the public component of the DKIM signing key

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: Postfix; configuration

Postfix configuration
---------------------

Postfix has been configured as outgoing email relay with very little changes to
the default configuration.

The mailname has been set to ``cacert.org`` in :file:`/etc/mailname`.

Postfix configuration file:`/etc/postfix/main.cf` and :file:`/etc/postfix/dynamic_maps.cf` have been modified to:

* set infrastructure related host and network parameters
* allow regular expressions in maps
* activate opportunistic TLS
* prepare for DKIM support
* disable local delivery

.. literalinclude:: ../configdiff/emailout/postfix-main.cf
   :language: text

Emails sent to specific intranet hostnames are rewritten to their respective
admin addresses in :file:`/etc/postfix/canonical_maps`:

.. literalinclude:: ../configdiff/emailout/canonical_maps
   :language: text

Emails sent to specific cacert.org hostnames are forwarded via
:file:`/etc/postfix/transport`:

.. literalinclude:: ../configdiff/emailout/transport
   :language: text

:file:`/etc/postfix/transport` has to be rehashed if it is changed because
Postfix uses a binary representation in :file:`/etc/postfix/transport.db`. To
perform the rehashing and restart Postfix use::

   postmap hash:/etc/postfix/transport
   service postfix restart

.. index::
   pair: OpenDKIM; configuration

OpenDKIM configuration
----------------------

.. todo::
   enable OpenDKIM in Postfix configuration when the DNS record is in place and
   :doc:`email` is ready for DKIM too or is configured to send mail via
   emailout.

The OpenDKIM configuration is stored in :file:`/etc/opendkim.conf`. The
following lines have been added:

.. code:: diff

   --- opendkim.conf.dpkg-dist     2017-09-04 00:17:50.000000000 +0000
   +++ opendkim.conf       2018-02-16 13:38:55.545110292 +0000
   @@ -13,6 +13,11 @@
    #Domain                        example.com
    #KeyFile               /etc/dkimkeys/dkim.key
    #Selector              2007
   +Domain                  cacert.org
   +KeyFile                 /etc/dkim/2015.private
   +Selector                2015
   +
   +InternalHosts           /etc/dkim/internalhosts

    # Commonly-used options; the commented-out versions show the defaults.
    #Canonicalization      simple
   @@ -31,7 +36,7 @@
    # ##  local:/path/to/socket       to listen on a UNIX domain socket
    #
    #Socket                  inet:8892@localhost
   -Socket                 local:/var/run/opendkim/opendkim.sock
   +Socket                  local:/var/spool/postfix/opendkim/opendkim.sock

    ##  PidFile filename
    ###      default (none)

The key has been generated with::

   mkdir /etc/dkim
   cd /etc/dkim
   opendkim-genkey -d cacert.org -s 2015

Internal networks have been defined in :file:`/etc/dkim/internalhosts` as::

   127.0.0.1
   10.0.0.0/24
   172.16.2.0/24


Tasks
=====

Changes
=======

Planned
-------

.. todo:: upgrade to Debian 10 (when Puppet is available)

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Postfix documentation
  http://www.postfix.org/documentation.html
Postfix Debian wiki page
  https://wiki.debian.org/Postfix
OpenDKIM documentation
  http://www.opendkim.org/docs.html
