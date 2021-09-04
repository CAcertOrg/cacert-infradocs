.. index::
   single: Systems; Community

=========
Community
=========

Purpose
=======

This system provides the community self service system and the webmail
interface for the community email service.

Application Links
-----------------

Community self service
   https://selfservice.cacert.org/

Webmail
   https://webmail.cacert.org/


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

:ref:`people_mario`, :ref:`people_dirk` and :ref:`people_jselzer` have
:program:`sudo` access on that machine too.

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
   single: Debian GNU/Linux; 10.9

* Debian GNU/Linux 10.9

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
| 443/tcp  | http    | ANY     | Apache httpd                            |
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
|                    | and redirect from http to https       |                                             |
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
* :doc:`email` for self service API access as well as IMAP (110/tcp), IMAPS
  (993/tcp), Manage Sieve (2001/tcp), SMTPS (465/tcp) and SMTP Submission
  (587/tcp) for the webmail system
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
  when there are changes in Git.

  The software is installed and configured via Puppet.

  .. _cacert-selfservice Job: https://jenkins.cacert.org/job/cacert-selfservice/

Building the cacert-selfservice Debian package
----------------------------------------------

The cacert-selfservice git repository contains a debian branch that can be used
to build the package.

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

.. sslcert:: webmail.cacert.org
   :altnames:   DNS:community.cacert.org, DNS:webmail.cacert.org
   :certfile:   /etc/ssl/public/webmail.cacert.org.crt.pem
   :keyfile:    /etc/ssl/private/webmail.cacert.org.key.pem
   :serial:     02E37C
   :expiration: Jun 06 11:10:41 2022 GMT
   :sha1fp:     70:EF:DA:32:E7:F9:86:F4:0C:85:54:71:A7:90:E8:68:0A:9F:8D:FD
   :issuer:     CAcert Class 3 Root

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
* :file:`/etc/ssl/public/webmail.cacert.org.chain.pem` contains the certificate
  for ``webmail.cacert.org`` concatenated with the CA chain.

The certificates are rolled out by Puppet. All changes to the certificates need
to be made to the file :file:`hieradata/nodes/community.yaml` in the
:cacertgit:`cacert-puppet` repository.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

:file:`/etc/hosts`
------------------

Defines an alias for :doc:`email` that is required by the Roundcube
installation to reach the email system via its internal IP address with the
correct hostname.

.. index::
   pair: Roundcube; configuration

Roundcube configuration
-----------------------

Roundcube configuration is managed by Puppet.

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

.. todo::

   Switch ingest traffic for webmail to proxyin and drop http redirector
   configuration from Apache httpd

System Future
-------------

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

* https://httpd.apache.org/docs/2.4/
* https://github.com/roundcube/roundcubemail/wiki
* https://www.php.net/manual/en/
