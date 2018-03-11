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
:MAC address: :mac:`00:ff:12:01:65:02` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Emailout

========================== ======== ====================================================================
Name                       Type     Content
========================== ======== ====================================================================
emailout.cacert.org.       IN A     213.154.225.239
emailout.cacert.org.       IN SSHFP 1 1 1ba1ab632911e8a68a69521130120695086d858c
emailout.cacert.org.       IN SSHFP 1 2 6e50d5b2034006b69eb7ba19d3f3fd2c48015bea2bb3d5e2a0f8cf25ff030055
emailout.cacert.org.       IN SSHFP 2 1 0e8888352604dbd1cc4d201bc1e985d80b9cf752
emailout.cacert.org.       IN SSHFP 2 2 a7402f014b47b805663c904dabbc9590db7d8d0f350cea6d9f63e12bc27bac0c
emailout.cacert.org.       IN SSHFP 3 1 527004f2091d2cef2c28b5f8241fc0e76307b2ba
emailout.cacert.org.       IN SSHFP 3 2 9094dcf8860523a83542ec4cc46fbcfed396f5525bc202cfecf42d1a7044136d
emailout.intra.cacert.org. IN A     172.16.2.32
========================== ======== ====================================================================

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

The following packages where installed after the container setup::

   apt-get install vim-nox screen aptitude git etckeeper postfix \
     postfix-pcre opendkim opendkim-tools man-db rsyslog logrotate \
     heirloom-mailx netcat-openbsd swaks

Services
========

Listening services
------------------

+----------+-----------+-----------+-----------------------------------------+
| Port     | Service   | Origin    | Purpose                                 |
+==========+===========+===========+=========================================+
| 22/tcp   | ssh       | ANY       | admin console access                    |
+----------+-----------+-----------+-----------------------------------------+
| 25/tcp   | smtp      | intranet  | mail delivery from intranet MTAs        |
+----------+-----------+-----------+-----------------------------------------+
| 5666/tcp | nrpe      | monitor   | remote monitoring service               |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: OpenDKIM
   single: Postfix
   single: cron
   single: nrpe
   single: openssh
   single: rsyslog

+--------------------+--------------------+----------------------------------------+
| Service            | Usage              | Start mechanism                        |
+====================+====================+========================================+
| openssh server     | ssh daemon for     | init script :file:`/etc/init.d/ssh`    |
|                    | remote             |                                        |
|                    | administration     |                                        |
+--------------------+--------------------+----------------------------------------+
| cron               | job scheduler      | init script :file:`/etc/init.d/cron`   |
+--------------------+--------------------+----------------------------------------+
| rsyslog            | syslog daemon      | init script                            |
|                    |                    | :file:`/etc/init.d/syslog`             |
+--------------------+--------------------+----------------------------------------+
| OpenDKIM           | DKIM signing       | init script                            |
|                    | daemon             | :file:`/etc/init.d/opendkim`           |
+--------------------+--------------------+----------------------------------------+
| Postfix            | SMTP server for    | init script                            |
|                    | local mail         | :file:`/etc/init.d/postfix`            |
|                    | submission, and    |                                        |
|                    | mail relay for     |                                        |
|                    | infrastructure     |                                        |
|                    | systems            |                                        |
+--------------------+--------------------+----------------------------------------+
| Nagios NRPE server | remote monitoring  | init script                            |
|                    | service queried by | :file:`/etc/init.d/nagios-nrpe-server` |
|                    | :doc:`monitor`     |                                        |
+--------------------+--------------------+----------------------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* SMTP (25/tcp) from other infrastructure systems

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`proxyout` as HTTP proxy for APT
* SMTP (25/tcp) to :doc:`email`, :doc:`issue` and :doc:`lists`

Security
========

.. sshkeys::
   :RSA:     SHA256:blDVsgNABraet7oZ0/P9LEgBW+ors9XioPjPJf8DAFU MD5:56:09:89:92:af:3c:15:e4:a3:06:11:63:0e:be:b6:a2
   :DSA:     SHA256:p0AvAUtHuAVmPJBNq7yVkNt9jQ81DOptn2PhK8J7rAw MD5:6c:8d:31:c4:92:de:f0:a8:95:eb:fe:20:83:91:ca:07
   :ECDSA:   SHA256:kJTc+IYFI6g1QuxMxG+8/tOW9VJbwgLP7PQtGnBEE20 MD5:cb:3c:69:c5:a1:90:c6:8e:55:40:83:6c:10:3f:09:b4
   :ED25519: SHA256:TOtIitF+p8jbFh/fM1fic9LqH+W+GDeUqs18S/36qKU MD5:04:ca:72:d0:21:0a:4a:8b:a5:f7:a2:2f:10:e5:3f:92

Non-distribution packages and modifications
-------------------------------------------

* None

Risk assessments on critical packages
-------------------------------------

Postfix has a very good security reputation. The system is patched regularly.

Critical Configuration items
============================

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

Planned
-------

.. todo:: setup IPv6

Changes
=======

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
