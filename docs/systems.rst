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

.. topic:: Setup package update monitoring for a new container

   For Icinga to be able to check the update status of packages on you server
   you need to install NRPE, a helper service. Install the necessary packages::

      sudo aptitude install nagios-plugins-basic nagios-nrpe-server

   Put :doc:`systems/monitor` on the list of allowed hosts to access the NRPE
   service by adding the following line to :file:`/etc/nagios/nrpe_local.cfg`::

      allowed_hosts=172.16.2.18

   Tell the NRPE service that there is such a thing as the check_apt command by
   creating the file :file:`/etc/nagios/nrpe.d/apt.cfg` with the following
   contents::

      # 'check_apt' command definition
      command[check_apt]=/usr/lib/nagios/plugins/check_apt

      # 'check_apt_distupgrade' command definition
      command[check_apt_distupgrade]=/usr/lib/nagios/plugins/check_apt -d

   Restart the NRPE service::

      sudo service nagios-nrpe-server restart

   Check that everything went well by going to https://monitor.cacert.org/,
   going to the APT service on the host and clicking :guilabel:`"Re-schedule
   the next check of this service"`. Make sure that :guilabel:`"Force Check"`
   is checked and click :guilabel:`"Commit"`. Now you should see a page with a
   green background. If not something went wrong, please contact the
   :doc:`systems/monitor` administrators with the details.

   That's it, now the package update status should be properly displayed in
   Icinga.

.. todo:: think about replacing nrpe with Icinga2 satellites

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

.. todo:: document how to setup the system-admin alias on the email system
