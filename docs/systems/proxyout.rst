.. index::
   single: Systems; Proxyout

========
Proxyout
========

Purpose
=======

This system acts as outgoing HTTP and HTTPS proxy for access to APT
repositories.

Application Links
-----------------

This system has no publicly visible URLs.


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_jandd`
* Secondary: None

.. todo:: find an additional admin
.. people_<name> are defined in people.rst

Application Administration
--------------------------

+-------------+---------------------+
| Application | Administrator(s)    |
+=============+=====================+
| Squid       | :ref:`people_jandd` |
+-------------+---------------------+

Contact
-------

* proxyout-admin@cacert.org

Additional People
-----------------

* None

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
:IP Internal: :ip:v4:`10.0.0.200`
:MAC address: :mac:`00:16:3e:15:b8:8c` (eth0)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
   single: DNS records; Proxyout

.. todo:: setup DNS records (in infra.cacert.org zone)

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.1

* Debian GNU/Linux 9.1

Applicable Documentation
------------------------

The system is managed by :doc:`puppet`. The puppet repository is browsable at
https://git.cacert.org/gitweb/?p=cacert-puppet.git;a=summary.

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
| 3128/tcp | http      | internal  | squid http/https proxy                  |
+----------+-----------+-----------+-----------------------------------------+

Running services
----------------

.. index::
   single: puppet agent
   single: cron
   single: exim4
   single: squid
   single: openssh

+----------------+--------------------+--------------------------------------+
| Service        | Usage              | Start mechanism                      |
+================+====================+======================================+
| openssh server | ssh daemon for     | init script :file:`/etc/init.d/ssh`  |
|                | remote             |                                      |
|                | administration     |                                      |
+----------------+--------------------+--------------------------------------+
| cron           | job scheduler      | init script :file:`/etc/init.d/cron` |
+----------------+--------------------+--------------------------------------+
| Exim           | SMTP server for    | init script                          |
|                | local mail         | :file:`/etc/init.d/exim4`            |
|                | submission         |                                      |
+----------------+--------------------+--------------------------------------+
| Puppet agent   | local Puppet agent | init script                          |
|                |                    | :file:`/etc/init.d/puppet`           |
+----------------+--------------------+--------------------------------------+
| Squid          | Caching and        | init script                          |
|                | filtering http/    | :file:`/etc/init.d/squid`            |
|                | https proxy for    |                                      |
|                | internal machines  |                                      |
+----------------+--------------------+--------------------------------------+

Connected Systems
-----------------

* :doc:`motion`
* :doc:`proxyin`
* :doc:`puppet`
* :doc:`svn`

Outbound network connections
----------------------------

* DNS (53) resolving nameservers 172.16.2.2 and 172.16.2.3
* :doc:`emailout` as SMTP relay
* :doc:`puppet` (tcp/8140) as Puppet master
* .debian.org Debian mirrors
* apt.puppetlabs.com as Debian repository for puppet packages

Security
========

.. sshkeys::
   :ECDSA:   74:70:63:b9:3e:6b:9f:a2:34:0e:9a:92:77:dd:93:73
   :ED25519: 43:0d:1e:ec:1b:5f:c3:84:38:c7:75:b7:be:3c:1b:d4
   :RSA:     1e:8e:1d:06:a5:fa:d6:08:95:e9:68:fb:ae:16:24:8f

Risk assessments on critical packages
-------------------------------------

Squid is a proven http and https proxy installed from distribution packages
with low risk.

Critical Configuration items
============================

All configuration is managed in Puppet. There are no certificates or private
keys used on this machine.

Tasks
=====

Planned
-------

Change all infrastructure hosts to use this machine as APT proxy to avoid flaky
firewall configurations on :doc:`infra02`.

Additional documentation
========================

.. seealso::

   * :wiki:`Exim4Configuration`

References
----------

* http://www.squid-cache.org/
