Systems
=======

.. toctree::
   :maxdepth: 1

   systems/infra02
   systems/arbitration
   systems/blog
   systems/board
   systems/emailout
   systems/monitor
   systems/webmail

General
-------

.. todo:: consider whether a central MySQL service should be setup

   Many containers contain their own instance of MySQL. It might be a better
   idea to centralize the MySQL setups in a single container.

.. todo:: consider whether a central PostgreSQL service should be setup

.. todo::

   setup a central syslog service and install syslog clients in each container

Checklist
---------

.. index::
   single: etckeeper
   single: nrpe

* All containers should be monitored by :doc:`systems/monitor` and should
  therefore have :program:`nagios-nrpe-server` installed
* All containers should use :program:`etckeeper` to put their local setup into
  version control. All local setup should use :file:`/etc` to make sure it is
  handled by :program:`etckeeper`
* All infrastructure systems must send their mail via :doc:`systems/emailout`
* All infrastructure systems should have an system-admin@cacert.org alias to
  reach their admins
* The installation of :index:`systemd-sysv` in containers can be blocked by
  putting the following lines in :file:`/etc/apt/preferences.d/systemd-sysv`::

    Package: systemd-sysv
    Pin: release a=stable
    Pin-Priority: -1

.. todo:: think about replacing nrpe with Icinga2 satellites
.. todo:: document how to setup the system-admin alias on the email system
