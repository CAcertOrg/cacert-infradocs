.. index::
   single: Systems; Motion

======
Motion
======

Purpose
=======

This system provides the CAcert board motion system. The system replaced the
board voting system that had been provided on :doc:`webmail` at
https://community.cacert.org/board/.

Application Links
-----------------

   Board motion system
     https://motion.cacert.org/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

Application Administration
--------------------------

+---------------------+---------------------+
| Application         | Administrator(s)    |
+=====================+=====================+
| board motion system | :ref:`people_jandd` |
+---------------------+---------------------+

Contact
-------

* motion-admin@cacert.org

Additional People
-----------------

No other people have :program:`sudo` access on that machine.

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
:IP Internal: :ip:v4:`10.0.0.117`
:IPv6:        :ip:v6:`2001:7b8:616:162:2::117`
:MAC address: :mac:`00:ff:cc:ce:0d:24` (eth0)

.. seealso::

   See :doc:`../network`

.. index::
   single: Monitoring; Motion

Monitoring
----------

:internal checks: :monitor:`motion.infra.cacert.org`
:external checks: :monitor:`motion.cacert.org`

DNS
---

.. index::
   single: DNS records; Motion

======================== ======== ====================================================================
Name                     Type     Content
======================== ======== ====================================================================
motion.cacert.org.       IN A     213.154.225.241
motion.cacert.org.       IN AAAA  2001:7b8:616:162:2::241
motion.cacert.org.       IN SSHFP 1 1 f018202c72749af5f48d45d5d536422f9c364fbb
motion.cacert.org.       IN SSHFP 1 2 0d17bbfe2efa97edbb13ffe3e6bfd3b4b9be5117f3c831a2f1a55b6c50e92fd4
motion.cacert.org.       IN SSHFP 2 1 ee6f2e346a5d5164100721f99765a4d3d08c6dce
motion.cacert.org.       IN SSHFP 2 2 53dedfd2c566011db80311528eba15fd000b0a5092ab1fc8104ca5804490cd18
motion.cacert.org.       IN SSHFP 3 1 6d4a9ec30f30aa0634b8879cded8ce884498e290
motion.cacert.org.       IN SSHFP 3 2 325ee301da21844adb8f12c0011b8d73709be8b2b9f375829224ac79c8fdfa6e
motion.cacert.org.       IN SSHFP 4 1 78e1edee04907de6b56d9c0d4900178f9426c02d
motion.cacert.org.       IN SSHFP 4 2 ca108fc298cb08406fe02454d9245ee1cf26c7241691da9a5b6bc69c56afd5c1
motion.infra.cacert.org. IN A     10.0.0.117
======================== ======== ====================================================================

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.9

* Debian GNU/Linux 9.9

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
| 8443/tcp | https   | ANY     | board motion application   |
+----------+---------+---------+----------------------------+
| 5665/tcp | icinga2 | monitor | remote monitoring service  |
+----------+---------+---------+----------------------------+

The board motion system is reachable via :doc:`proxyin`. SSH is forwarded from
port 11722 on the public IP addresses.

Running services
----------------

.. index::
   single: cacert-boardvoting
   single: cron
   single: dbus
   single: exim4
   single: icinga2
   single: openssh
   single: puppet
   single: rsyslog

+--------------------+--------------------------+---------------------------------------------+
| Service            | Usage                    | Start mechanism                             |
+====================+==========================+=============================================+
| cacert-boardvoting | application              | systemd unit ``cacert-boardvoting.service`` |
+--------------------+--------------------------+---------------------------------------------+
| cron               | job scheduler            | systemd unit ``cron.service``               |
+--------------------+--------------------------+---------------------------------------------+
| dbus-daemon        | System message bus       | systemd unit ``dbus.service``               |
|                    | daemon                   |                                             |
+--------------------+--------------------------+---------------------------------------------+
| Exim               | SMTP server for          | systemd unit ``exim4.service``              |
|                    | local mail               |                                             |
|                    | submission               |                                             |
+--------------------+--------------------------+---------------------------------------------+
| icinga2            | Icinga2 monitoring agent | systemd unit ``icinga2.service``            |
+--------------------+--------------------------+---------------------------------------------+
| openssh server     | ssh daemon for           | systemd unit ``ssh.service``                |
|                    | remote                   |                                             |
|                    | administration           |                                             |
+--------------------+--------------------------+---------------------------------------------+
| Puppet agent       | configuration            | systemd unit ``puppet.service``             |
|                    | management agent         |                                             |
+--------------------+--------------------------+---------------------------------------------+
| rsyslog            | syslog daemon            | systemd unit ``rsyslog.service``            |
+--------------------+--------------------------+---------------------------------------------+

Databases
---------

+--------+------------------------------------------------------+--------------------+
| RDBMS  | Name                                                 | Used for           |
+========+======================================================+====================+
| SQLite | :file:`/srv/cacert-boardvoting/data/database.sqlite` | cacert-boardvoting |
+--------+------------------------------------------------------+--------------------+

Connected Systems
-----------------

* :doc:`monitor`
* :doc:`proxyin` for incoming application traffic

Outbound network connections
----------------------------

* DNS (53) resolver at 10.0.0.1 (:doc:`infra02`)
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT and Puppet

Security
========

.. sshkeys::
   :RSA:     SHA256:DRe7/i76l+27E//j5r/TtLm+URfzyDGi8aVbbFDpL9Q MD5:8a:a8:61:d2:07:79:27:6a:37:f8:30:2a:36:aa:d9:4f
   :DSA:     SHA256:U97f0sVmAR24AxFSjroV/QALClCSqx/IEEylgESQzRg MD5:ec:76:0a:d5:5e:ff:29:1e:f4:b4:78:5f:5e:0f:2a:af
   :ECDSA:   SHA256:Ml7jAdohhErbjxLAARuNc3Cb6LK583WCkiSsecj9+m4 MD5:3f:38:14:95:9e:fb:10:79:c5:72:d6:c6:79:a8:84:cf
   :ED25519: SHA256:yhCPwpjLCEBv4CRU2SRe4c8mxyQWkdqaW2vGnFav1cE MD5:c5:40:79:42:09:9d:5e:47:45:d6:ab:e9:58:af:eb:26

Dedicated user roles
--------------------

* None

Non-distribution packages and modifications
-------------------------------------------

* Board motion system

  The system runs the board motion system developed in the
  :cacertgit:`cacert-boardvoting`.

  The software is installed from a Debian package that is hosted on
  :doc:`webstatic`.

  The sofware is built on :doc:`jenkins` via the `cacert-boardvoting Job`_ when
  there are changes in Git. The Debian package can be built using
  :program:`gbp`.

  The software is installed and configured via Puppet.

  .. _cacert-boardvoting Job: https://jenkins.cacert.org/job/cacert-boardvoting/
  .. todo:: describe more in-depth how to build the Debian package

Risk assessments on critical packages
-------------------------------------

The Puppet agent package and a few dependencies are installed from the official
Puppet APT repository because the versions in Debian are too old to use modern
Puppet features.

The system is stripped down to the bare minimum. The CAcert board voting system
software is developed using `Go <https://golang.org/>`_ which handles a lot of
common programming errors at compile time and has a quite good security track
record.

The board motion tool is run as a separate system user ``cacert-boardvoting``
and is built as a small self-contained static binary. Access is restricted via
https.

Critical Configuration items
============================

The system configuration is managed via Puppet profiles. There should be no
configuration items outside of the :cacertgit:`cacert-puppet`.

Keys and X.509 certificates
---------------------------

.. sslcert:: motion.cacert.org
   :altnames:   DNS:motion.cacert.org
   :certfile:   /srv/cacert-boardvoting/data/server.crt
   :keyfile:    /srv/cacert-boardvoting/data/server.key
   :serial:     02D8A3
   :expiration: Aug 01 18:06:22 2021 GMT
   :sha1fp:     90:B8:A7:CE:ED:56:94:D0:58:7B:65:94:FF:D5:5A:43:08:2C:2A:62
   :issuer:     CAcert Class 3 Root

* :file:`/srv/cacert-boardvoting/data/cacert_class3.pem` CAcert class 3 CA
  certificate (allowed CA certificate for client certificates)

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

cacert-boardvoting configuration
--------------------------------

:program:`cacert-boardvoting` is configured via Puppet profile
``profiles::cacert-boardvoting``.

Tasks
=====

Add/Remove voters
-----------------

An :term:`Application Administrator` can add and remove voters from the CAcert
board voting system using the :program:`sqlite3` program:

.. code-block:: bash

   cd /srv/cacert-boardvoting/data
   # open database
   sqlite3 database.sqlite

.. code-block:: sql

   -- find existing voters
   select * from voters where enabled=1;

   -- disable voters that should not be able to vote using Ids from the result
   -- of the previous query
   update voters set enabled=0 where id in (1, 2, 3);

   -- find existing accounts of voter John Doe and Jane Smith
   select * from voters where name like 'John%' or name like 'Jane%';

   -- John has an account with id 4, Jane is not in the system
   -- enable John
   update voters set enabled=1 where id=4;

   -- insert Jane
   insert into voters (name, enabled, reminder) values ('Jane Doe', 1,
     'jane.doe@cacert.org');

   -- find voter id for Jane
   select id from voters where name='Jane Doe';

   -- Jane has id 42
   -- insert email address mapping for Jane (used for authentication)
   insert into emails (voter, address) values (42, 'jane.doe@cacert.org');

Changes
=======

Planned
-------

.. todo:: update to Debian 10 (when Puppet is available)
.. todo:: implement user administration inside the application

System Future
-------------

* No plans

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* https://git.cacert.org/gitweb/?p=cacert-boardvoting.git;a=blob_plain;f=README.md;hb=HEAD
