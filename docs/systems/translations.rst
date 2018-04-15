.. index::
   single: Systems; Translations

============
Translations
============

Purpose
=======

This system runs a `Pootle`_ translation server.

.. _Pootle: http://pootle.translatehouse.org/


Application Links
-----------------

Pootle web interface
     https://translations.cacert.org/

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
| Pootle      | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* translations-admin@cacert.org

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

:IP Internet: :ip:v4:`213.154.225.240`
:IP Intranet: :ip:v4:`172.16.2.31`
:IP Internal: :ip:v4:`10.0.0.31`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::31`
:MAC address: :mac:`00:ff:6c:7d:5b:c5` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Translations

============================== ======== ====================================================================
Name                           Type     Content
============================== ======== ====================================================================
l10n.cacert.org.               IN CNAME translations.cacert.org.
translations.cacert.org.       IN A     213.154.225.240
translations.cacert.org.       IN AAAA  2001:7b8:616:162:2::31
translations.cacert.org.       IN SSHFP 1 1 1128972FB54F927477A781718E2F9C114E9CA383
translations.cacert.org.       IN SSHFP 1 2 F223904069AEAA2E0EAC5D9092AB7DEBAE70F06EC3C25E94F49F1B15F633ED5D
translations.cacert.org.       IN SSHFP 2 1 3A36E5DF06304C481F01FC723FD88A086E82D986
translations.cacert.org.       IN SSHFP 2 2 4A1FF7396AE874559CF196D54D5D7F6890DBA6DE73B46AF049258B1024CDACE2
translations.cacert.org.       IN SSHFP 3 1 0F0CBD9C188D619D743859A249238F684D6CCA5F
translations.cacert.org.       IN SSHFP 3 2 441D76EB651022A8C5810C6946CBDEC47504E97AD669B073EC9D6E27791A7C4D
translations.cacert.org.       IN SSHFP 4 1 A4102E1FBF1BE1ACD53F2E7653DD8898E567C437
translations.cacert.org.       IN SSHFP 4 2 6FE3334B51E68F9F650B00D13F504306029B71A76C5AFF54873D72B24ED19DD5
translations.intra.cacert.org. IN A     172.16.2.31
============================== ======== ====================================================================

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

+----------+---------+---------+----------------------------+
| Port     | Service | Origin  | Purpose                    |
+==========+=========+=========+============================+
| 22/tcp   | ssh     | ANY     | admin console access       |
+----------+---------+---------+----------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA |
+----------+---------+---------+----------------------------+
| 80/tcp   | http    | ANY     | redirect to https          |
+----------+---------+---------+----------------------------+
| 443/tcp  | https   | ANY     | application                |
+----------+---------+---------+----------------------------+
| 3306/tcp | mysql   | local   | MySQL database for Pootle  |
+----------+---------+---------+----------------------------+
| 5666/tcp | nrpe    | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+
| 6379/tcp | redis   | local   | Redis in memory cache      |
+----------+---------+---------+----------------------------+

Running services
----------------

.. index::
   single: apache httpd
   single: cron
   single: mariadb
   single: nrpe
   single: openssh
   single: postfix
   single: puppet agent
   single: redis
   single: rsyslog
   single: supervisord

+--------------------+------------------------------+-----------------------------------------------------+
| Service            | Usage                        | Start mechanism                                     |
+====================+==============================+=====================================================+
| Apache httpd       | Webserver for                | init script                                         |
|                    | Pootle                       | :file:`/etc/init.d/apache2`                         |
+--------------------+------------------------------+-----------------------------------------------------+
| cron               | job scheduler                | init script :file:`/etc/init.d/cron`                |
+--------------------+------------------------------+-----------------------------------------------------+
| MySQL              | MySQL database               | init script                                         |
|                    | server for Pootle            | :file:`/etc/init.d/mysql`                           |
+--------------------+------------------------------+-----------------------------------------------------+
| Postfix            | SMTP server for              | init script                                         |
|                    | local mail                   | :file:`/etc/init.d/postfix`                         |
|                    | submission                   |                                                     |
+--------------------+------------------------------+-----------------------------------------------------+
| Puppet agent       | local Puppet agent           | init script                                         |
|                    |                              | :file:`/etc/init.d/puppet`                          |
+--------------------+------------------------------+-----------------------------------------------------+
| Nagios NRPE server | remote monitoring            | init script                                         |
|                    | service queried by           | :file:`/etc/init.d/nagios-nrpe-server`              |
|                    | :doc:`monitor`               |                                                     |
+--------------------+------------------------------+-----------------------------------------------------+
| openssh server     | ssh daemon for               | init script :file:`/etc/init.d/ssh`                 |
|                    | remote                       |                                                     |
|                    | administration               |                                                     |
+--------------------+------------------------------+-----------------------------------------------------+
| Redis              | Job queue for Pootle         | init script :file:`/etc/init.d/redis-server`        |
+--------------------+------------------------------+-----------------------------------------------------+
| rsyslog            | syslog daemon                | init script                                         |
|                    |                              | :file:`/etc/init.d/syslog`                          |
+--------------------+------------------------------+-----------------------------------------------------+
| Supervisord        | Supervisor for background    | init script :file:`/etc/init.d/supervisor`          |
|                    | tasks                        |                                                     |
+--------------------+------------------------------+-----------------------------------------------------+
| Pootle rqworker    | Worker for Pootle background | supervisor task in                                  |
|                    | tasks                        | :file:`/etc/supervisor/conf.d/pootle-rqworker.conf` |
+--------------------+------------------------------+-----------------------------------------------------+

Databases
---------

+-------+--------+----------+
| RDBMS | Name   | Used for |
+=======+========+==========+
| MySQL | pootle | Pootle   |
+-------+--------+----------+

Connected Systems
-----------------

* :doc:`monitor`

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT
* arbitrary Internet HTTP, HTTPS, FTP, FTPS, git servers for fetching Pootle
  dependencies (via ``&CONTAINER_OUT_ELEVATED("translations");`` in
  :file:`/etc/ferm/ferm.d/translations.conf` on :doc:`infra02`).

Security
========

.. sshkeys::
   :RSA:     SHA256:8iOQQGmuqi4OrF2Qkqt9665w8G7Dwl6U9J8bFfYz7V0 MD5:df:98:f5:ea:05:c1:47:52:97:58:8f:42:55:d6:d9:b6
   :DSA:     SHA256:Sh/3OWrodFWc8ZbVTV1/aJDbpt5ztGrwSSWLECTNrOI MD5:07:2b:10:b1:6d:79:35:0f:83:aa:fc:ba:d6:2f:51:dc
   :ECDSA:   SHA256:RB1262UQIqjFgQxpRsvexHUE6XrWabBz7J1uJ3kafE0 MD5:0a:39:d9:22:39:3a:48:5d:fb:a3:27:15:d9:30:a8:64
   :ED25519: SHA256:b+MzS1Hmj59lCwDRP1BDBgKbcadsWv9Uhz1ysk7RndU MD5:ca:a6:93:70:8c:38:23:26:16:68:5b:87:16:ee:70:17

Dedicated user roles
--------------------

+---------------+----------------------------------+
| Group         | Purpose                          |
+===============+==================================+
| pootle-update | Planned translation update group |
+---------------+----------------------------------+

Non-distribution packages and modifications
-------------------------------------------

Pootle is a Python/Django application that has been installed in a Python
virtualenv. Pootle and all its dependencies have been installed using:

   .. code-block:: bash

      cd /var/www/pootle
      virtualenv pootle-2.8.2
      ln -s pootle-2.8.2 current
      chown -R pootle.www-data pootle-2.8.2
      sudo -s -u pootle
      . pootle-2.8.2/bin/activate
      pip install --process-dependency-links Pootle[mysql]
      pootle migrate

Pootle is installed in a versioned directory. The used version is a symlink in
:file:`/var/www/pootle/current`. The rationale is to avoid changes to many
different configuration files when updating to a newer Pootle version.

The installation needs an installed :program:`gcc` and a few library development
packages.

.. todo::

   consider building the virtualenv on :doc:`jenkins` to avoid development tools
   on this system

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

Risk assessments on critical packages
-------------------------------------

System access is limited to http/https via Apache httpd which is restricted to
a minimal set of modules.

The system uses third party packages with a good security track record and
regular updates. The attack surface is small due to the tightly restricted
access to the system. The puppet agent is not exposed for access from outside
the system.

Pootle is based on Django 1.10 and should be updated to a newer version when it
becomes available. Pootle is run as a dedicated system user `pootle` that is
restricted via filesystem permissions.

The following change has been made to the translation toolkit filters that are
used by Pootle in :file:`/var/www/pootle/pootle-2.8.2/lib/python2.7/site-packages/translate/filters/checks.py`
to add CAcert specific translation checks:

   .. code-block:: diff

      commit 4d107e5019f4794b4581cadaf4e9a8339868f6a4
      Author: Jan Dittberner <jandd@cacert.org>
      Date:   Fri Feb 23 20:39:03 2018 +0000

          Add CAcert checkers

          Signed-off-by: Jan Dittberner <jandd@cacert.org>

      diff --git a/filters/checks.py b/filters/checks.py
      index db10937..45b464c 100644
      --- a/filters/checks.py
      +++ b/filters/checks.py
      @@ -2475,6 +2475,24 @@ class IOSChecker(StandardChecker):
               StandardChecker.__init__(self, **kwargs)


      +cacertconfig = CheckerConfig(
      +    notranslatewords = ["CAcert", "Assurer"],
      +    criticaltests = ["printf"],
      +)
      +
      +
      +class CAcertChecker(StandardChecker):
      +
      +    def __init__(self, **kwargs):
      +        checkerconfig = kwargs.get("checkerconfig", None)
      +        if checkerconfig is None:
      +            checkerconfig = CheckerConfig()
      +            kwargs["checkerconfig"] = checkerconfig
      +
      +        checkerconfig.update(cacertconfig)
      +        StandardChecker.__init__(self, **kwargs)
      +
      +
       projectcheckers = {
           "minimal": MinimalChecker,
           "standard": StandardChecker,
      @@ -2490,6 +2508,7 @@ projectcheckers = {
           "terminology": TermChecker,
           "l20n": L20nChecker,
           "ios": IOSChecker,
      +    "cacert": CAcertChecker,
       }


Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the Puppet repository.

.. todo:: move configuration of :doc:`translations` to Puppet code

Keys and X.509 certificates
---------------------------

.. sslcert:: translations.cacert.org
   :altnames:   DNS:l10n.cacert.org, DNS:translations.cacert.org
   :certfile:   /etc/ssl/public/translations.c.o.chain.crt
   :keyfile:    /etc/ssl/private/translations.c.o.key
   :serial:     138202
   :expiration: Mar 16 11:47:46 2020 GMT
   :sha1fp:     09:D7:6C:BA:EC:60:45:4A:93:77:39:D0:0A:FA:9B:0A:3D:17:3C:CA
   :issuer:     CA Cert Signing Authority

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

Apache configuration
--------------------

The main configuration files for Apache httpd are:

* :file:`/etc/apache2/sites-available/pootle-nossl.conf`

  defines the HTTP VirtualHost that redirects all requests to
  https://translations.cacert.org/

* :file:`/etc/apache2/sites-available/pootle-ssl.conf`

  defines the HTTPS VirtualHost for Pootle including the TLS and WSGI setup

Pootle configuration
--------------------

The main Pootle configuration file is
:file:`/var/www/pootle/current/pootle.conf`. The file defines the database
and CAcert specific settings.

Pootle runs some background jobs that are queued via redis and run from a
worker process. The worker process lifecycle is managed via
:program:`supervisord`. The supervisor configuration for this worker is in
:file:`/etc/supervisor/conf.d/pootle-rqworker.conf`.

The WSGI_ runner for Pootle is contained in :file:`/var/www/pootle/wsgi.py`
it references the symlinked Pootle instance directory
:file:`/var/www/pootle/current` and should not need changes when a new
Pootle version is installed.

.. _WSGI: https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

There are scripts in :file:`/usr/local/bin` that were implemented for an older
Pootle version and have to be checked/updated.

Tasks
=====

Planned
-------

.. todo::

   integrate the pootle projects with version control systems. The templates
   (.pot files) in :file:`/var/www/pootle/po` can be updated and loaded into
   Pootle by invoking::

      pootle update_stores --project=<project_id> --language=templates

   see the `Pootle documentation <http://docs.translatehouse.org/projects/pootle/en/stable-2.8.x/server/project_setup.html#project-setup-updating-strings>`_

.. todo::

   update and improve the scripts in :file:`/usr/local/bin` and integrate
   them with the :program:`sudo` system to allow members of the `pootle-update`
   group to run them in the context of the `pootle` system user

Changes
=======

System Future
-------------

* keep Pootle up to date

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`

References
----------

Apache httpd documentation
   http://httpd.apache.org/docs/2.4/
MariaDB knowledge base
   https://mariadb.com/kb/en/
mod_wsgi documentation
   https://modwsgi.readthedocs.io/en/develop/
Pootle documentation
   http://docs.translatehouse.org/projects/pootle/en/stable-2.8.x/
Redis documentation
   https://redis.io/documentation
Supervisord documentation
   http://supervisord.org/
