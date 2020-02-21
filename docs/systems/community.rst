.. index::
   single: Systems; Community

=========
Community
=========

Purpose
=======

This system provides the community self service system and will replace the
:doc:`webmail` system in the future.

Application Links
-----------------

   Community self service
      https://selfservice.cacert.org/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+--------------+---------------------+
| Application  | Administrator(s)    |
+==============+=====================+
| self service | :ref:`people_jandd` |
+--------------+---------------------+

Contact
-------

* community-admin@cacert.org

Additional People
-----------------

:ref:`people_mario` and :ref:`people_jselzer` have :program:`sudo` access on
that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: None
:IP Intranet: None
:IP Internal: :ip:v4:`10.0.0.118`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::118`
:MAC address: :mac:`00:ff:67:c2:08:53` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Community

Monitoring
----------

:internal checks: :monitor:`community.infra.cacert.org`

DNS
---

.. index::
   single: DNS records; <machine>

+-------------------------+---------+------------------------+
| Name                    | Type    | Content                |
+=========================+=========+========================+
| selfservice.cacert.org. | IN A    | 213.154.225.241        |
| selfservice.cacert.org. | IN AAAA | 2001:7b8:616:162:2::35 |
+-------------------------+---------+------------------------+

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Buster
   single: Debian GNU/Linux; 10.3

* Debian GNU/Linux 10.3

Services
========

Listening services
------------------

+----------+---------+---------+-----------------------------------------+
| Port     | Service | Origin  | Purpose                                 |
+==========+=========+=========+=========================================+
| 22/tcp   | ssh     | ANY     | admin console access                    |
+----------+---------+---------+-----------------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA              |
+----------+---------+---------+-----------------------------------------+
| 80/tcp   | http    | ANY     | Apache httpd                            |
+----------+---------+---------+-----------------------------------------+
| 3306/tcp | mariadb | local   | MariaDB database for roundcube settings |
+----------+---------+---------+-----------------------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service               |
+----------+---------+---------+-----------------------------------------+
| 8443/tcp | https   | ANY     | Community self-service application      |
+----------+---------+---------+-----------------------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cacert-selfservice
   single: cron
   single: dbus
   single: icinga2
   single: mariadb
   single: openssh
   single: postfix
   single: puppet
   single: rsyslog

+--------------------+---------------------------------------+---------------------------------------------+
| Service            | Usage                                 | Start mechanism                             |
+====================+=======================================+=============================================+
| Apache httpd       | Webserver for Roundcube webmailer     | systemd unit ``apache2.service``            |
+--------------------+---------------------------------------+---------------------------------------------+
| cacert-selfservice | Community self service application    | systemd unit ``cacert-selfservice.service`` |
+--------------------+---------------------------------------+---------------------------------------------+
| cron               | job scheduler                         | systemd unit ``cron.service``               |
+--------------------+---------------------------------------+---------------------------------------------+
| dbus-daemon        | System message bus daemon             | systemd unit ``dbus.service``               |
+--------------------+---------------------------------------+---------------------------------------------+
| icinga2            | Icinga2 monitoring agent              | systemd unit ``icinga2.service``            |
+--------------------+---------------------------------------+---------------------------------------------+
| MariaDB            | MariaDB database server               | systemd unit ``mariadb.service``            |
+--------------------+---------------------------------------+---------------------------------------------+
| openssh server     | ssh daemon for remote administration  | systemd unit ``ssh.service``                |
+--------------------+---------------------------------------+---------------------------------------------+
| Postfix            | SMTP server for local mail submission | systemd unit ``postfix.service``            |
+--------------------+---------------------------------------+---------------------------------------------+
| Puppet agent       | configuration management agent        | systemd unit ``puppet.service``             |
+--------------------+---------------------------------------+---------------------------------------------+
| rsyslog            | syslog daemon                         | systemd unit ``rsyslog.service``            |
+--------------------+---------------------------------------+---------------------------------------------+

Databases
---------

+---------+-----------+----------------------------+
| RDBMS   | Name      | Used for                   |
+=========+===========+============================+
| MariaDB | roundcube | RoundCube webmail settings |
+---------+-----------+----------------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`proxyin` for incoming application traffic

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`email` for self service API access
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT and Puppet

Security
========

.. sshkeys::
   :RSA:     SHA256:bb05y6dWnOxrKuCLUFAPajtH9GsvuyFmDSOeDbj5xZg MD5:ca:42:d9:26:46:16:a1:31:1f:a0:ca:d4:79:c5:b4:06
   :ECDSA:   SHA256:ucfyZPkyfKYsVnglXXFrWm8Fvng8vbfETvJ48wUzcO8 MD5:21:18:06:8e:77:ee:eb:f6:2e:9f:57:77:3d:e2:31:a4
   :ED25519: SHA256:RBGmoIIOuBFHS81x6C8AwAcDC3m/8R35cdHBvxpcyP8 MD5:af:11:72:ce:f8:64:a8:c0:d9:95:45:db:50:37:4f:d8

Dedicated user roles
--------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* CAcert community self service system

  The system runs the CAcert community self service system developed in the
  :cacertgit:`cacert-selfservice`.

  The software is installed from a Debian package that is hosted on :doc:`webstatic`.

  The software is built on :doc:`jenkins` via the `cacert-selfservice Job`_
  when there are changes in Git. The Debian package can be built using
  :program:`gbp`.

  The software is installed and configured via Puppet.

  .. _cacert-selfservice Job: https://jenkins.cacert.org/job/cacert-selfservice/
  .. todo:: describe build and deployment of Debian package for self-service

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

The CAcert community self service software is developed using `Go
<https://golang.org/>`_ which handles a lot of common programming errors at
compile time and has a quite good security track record.

The CAcert community self service system is run as a separate user
``cacert-selfservice`` and is built as a small self-contained static binary.
Access is restricted via https.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

.. sslcert:: selfservice.cacert.org
   :altnames:   DNS:selfservice.cacert.org
   :certfile:   /etc/cacert-selfservice/certs/server.crt.pem
   :keyfile:    /etc/cacert-selfservice/private/server.key.pem
   :serial:     02D94E
   :expiration: Aug 15 20:58:13 2021 GMT
   :sha1fp:     4D:F9:BD:F3:11:E6:A5:0C:26:7B:87:88:90:8C:CB:17:72:6F:78:8D
   :issuer:     CAcert Class 3 Root

* :file:`/etc/cacert-selfservice/certs/api_cas.pem` contains the trust anchor
  to validate the selfservice API certificate.
* :file:`/etc/cacert-selfservice/certs/client_cas.pem` contains the CAcert.org
  Class 1 and Class 3 CA certificates that are used to validate client
  certificates for the CAcert community self service system

The certificates are rolled out by Puppet. All changes to the certificates need
to be made to the file :file:`hieradata/nodes/community.yaml` in the
:cacertgit:`cacert-puppet` repository.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

.. index::
   pair: cacert-selfservice; configuration

cacert-selfservice configuration
--------------------------------

The service configuration is contained in `/etc/cacert-selfservice/config.yaml`
and is managed by the Puppet manifest profiles::cacert_selfservice.

Tasks
=====

* None

Changes
=======

Planned
-------

.. todo:: finish the roundcube setup on :doc:`community` to allow
          decommisioning of :doc:`webmail`.

System Future
-------------

* Become the replacement for :doc:`webmail`

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

.. could reference Apache httpd, PHP and roundcube documentation
