.. index::
   single: Systems; test3

=====
Test3
=====

Purpose
=======

This is a test system for testing a version of the CAcert application software
revised to run with php-7.0 on Debian Stretch. When these tests are succesful,
the other test servers and the production server running on www.cacert.org can
be upgraded tot Debian Stretch. After that this server can probably be scrapped again.

Application Links
-----------------

Application via HTTP:
  http://test3.cacert.org:14980/

Application via HTTPS:
  https://test3.cacert.org:14943/


Administration
==============

System Administration
---------------------

* Primary: :ref:`people_wytze`
* Secondary: :ref:`people_jandd`


Application Administration
--------------------------

  +------------------------+---------------------------------------+
  | Application            | Administrator(s)                      |
  +========================+=======================================+
  | CAcert web application | :ref:`people_dirk`, :ref:`people_ted` |
  +------------------------+---------------------------------------+

Contact
-------

* test-admin@cacert.org

Additional People
-----------------

:ref:`people_dirk`, :ref:`people_gukk`, :ref:`people_mario`,
:ref:`people_mendel`, :ref:`people_neo` and :ref:`people_ted` have
:program:`sudo` access on that machine too.

Basics
======

Physical Location
-----------------

This system is located in an :term:`LXC` container on physical machine
:doc:`infra02`.

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.248`
:IP Intranet: :ip:v4:`172.16.2.149`
:IP Internal: :ip:v4:`10.0.0.149`
:IPv6         :ip:v6:`2001:7b8:616:162:2::149`
:MAC address: :mac:`00:ff:ce:d1:22:1d` (eth0)

Because this system is sharing its IPv4 internet address with test.cacert.org,
there are some special mappings in the infra02 firewall to get access to this system:

* test,cacert.org port 14922 maps to test3 port 22 (ssh)
* test.cacert.org port 14980 maps to test3 port 80 (http)
* test.cacert.org port 14943 maps to test3 port 443 (https)

.. seealso::

   See :doc:`../network`

DNS
---

.. index::
<<<<<<< HEAD
   single: DNS records; Test3

======================== ======== ============================================
Name                     Type     Content
======================== ======== ============================================
test3.cacert.org.        IN A     213.154.225.248
secure.test3.cacert.org. IN CNAME test3.cacert.org
www.test3.cacert.org.    IN CNAME test3.cacert.org
test3.cacert.org.        IN SSHFP 1 1 39fd3b77396529f83e095ff09c59994c47d9e0d3
test3.cacert.org.        IN SSHFP 1 2 680fe134289e79678f7eaa5689fdce3db5efed9f6ebefd5bcfadce04a96475c1
test3.cacert.org.        IN SSHFP 2 1 70f5730c127bd701fc5c4baba329e93346a975c1
test3.cacert.org.        IN SSHFP 2 2 364252b906aec15a00994620d5c90c0f692a41cbc8c6f3bfc229149511209328
test3.cacert.org.        IN SSHFP 3 1 e4d81b532dc90ebb6d087ae732ce016b87945ebd
test3.cacert.org.        IN SSHFP 3 2 71b5aedcc999e6ffc0f90eeb9254c8771ddaa6a4981cf55e8e2228f6bdee64ce
test3.cacert.org.        IN SSHFP 4 1 50b22453f5c8d845895bacccbc1fc325d033f65d
test3.cacert.org.        IN SSHFP 4 1 a928b84465769480d70dfc5ecd3af2e4cdb192ee11d1cffc4f31ea1fbed09d41
test.infra.cacert.org.   IN A     10.0.0.149
======================== ======== ============================================

.. todo:: add AAAA record for IPv6 address
.. todo:: add intra.cacert.org. A record

.. seealso::

   See :wiki:`SystemAdministration/Procedures/DNSChanges`

Operating System
----------------

.. index::
   single: Debian GNU/Linux; Stretch
   single: Debian GNU/Linux; 9.6

* Debian GNU/Linux 9.6

Applicable Documentation
------------------------

Notes about installing the CAcert application on test3.cacert.org.

* Starting point is a Debian Stretch LXC setup from Jan Dittberner

* install the following packages (and their dependencies):
  
  .. code-block:: bash

    $ sudo apt-get install \
      apache2 php7.0 php7.0-gmp php7.0-mysql php7.0-gd php7.0-recode php7.0-mbstring \
      default-mysql-server gettext locales locales-all recode \
      dnsutils whois locate rcs screen make ca-cacert \
      libdevice-serialport-perl libfile-counterfile-perl xdelta

* enable the CAcert root certificates for normal operation via:

  .. code-block:: bash

    $ sudo dpkg-reconfigure ca-certificates

* create empty cacert database:

  .. code-block:: bash

    $ sudo mysql
    > CREATE DATABASE cacert;
    > GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON cacert.* TO 'cacert'@'localhost' IDENTIFIED BY 'klodder';
    > \q

* dump current cacert database on test.cacert.org:

  .. code-block:: bash

    $ mysqldump -u cacert -p --single-transaction cacert >BACKUP

* copy over cacert database BACKUP from test.cacert.org to test3.cacert.org

* import the database backup into the empty cacert database:

  .. code-block:: bash

    $ mysql -u cacert -p cacert <BACKUP

* copy scripts :file:`/etc/rc.local` and :file:`/usr/local/sbin/socat` from test.cacert.org

* copy signer files with :file:`collect-signer-files` script from test.cacert.org

* make small adjustmenst to scripts and install signer stuff in :file:`/etc`

* generate certificates for test.cacert.org based on CAcert test root with
  :file:`~wytze/local/localcerts` script (using the locally installed signer config)

* copy :file:`/root/chroot` from test.cacert.org

* use updated :file:`mkchrootenv` script from
  http://svn.cacert.org/CAcert/SystemAdministration/webdb/mkchrootenv
  to setup :file:`/home/cacert`

* create :file:`/home/cacert/www/includes/mysql.php` from :file:`mysql.php.sample` prototype

* install commmodule client from :file:`/home/cacert/www/CommModule` in :file:`/etc/init.d`

* copy :file:`/etc/init.d/apache2` script to :file:`/etc/init.d/apache2-cacert` and modify
  it to use chroot to the :file:`/home/cacert` environment:

  .. code-block:: text

    --- apache2     2018-04-05 18:32:55.000000000 +0000
    +++ apache2-cacert      2018-11-20 16:05:38.740396894 +0000
    @@ -1,22 +1,26 @@
     #!/bin/sh
     ### BEGIN INIT INFO
    -# Provides:          apache2
    +# Provides:          apache2-cacert
     # Required-Start:    $local_fs $remote_fs $network $syslog $named
     # Required-Stop:     $local_fs $remote_fs $network $syslog $named
     # Default-Start:     2 3 4 5
     # Default-Stop:      0 1 6
     # X-Interactive:     true
    -# Short-Description: Apache2 web server
    +# Short-Description: Apache2 web server for CAcert
     # Description:       Start the web server
     #  This script will start the apache2 web server.
     ### END INIT INFO
    
    -DESC="Apache httpd web server"
    +DESC="Apache httpd web server for CAcert"
     NAME=apache2
     DAEMON=/usr/sbin/$NAME
    
    +CHRDIR=/home/cacert/
    +CHROOT="/usr/sbin/chroot ${CHRDIR}"
    +
     SCRIPTNAME="${0##*/}"
     SCRIPTNAME="${SCRIPTNAME##[KS][0-9][0-9]}"
    +SCRIPTNAME=apache2
     if [ -n "$APACHE_CONFDIR" ] ; then
            if [ "${APACHE_CONFDIR##/etc/apache2-}" != "${APACHE_CONFDIR}" ] ; then
                    DIR_SUFFIX="${APACHE_CONFDIR##/etc/apache2-}"
    @@ -53,8 +57,8 @@
    
    
     # Now, set defaults:
    -APACHE2CTL="$ENV apache2ctl"
    -PIDFILE=$(. $APACHE_ENVVARS && echo $APACHE_PID_FILE)
    +APACHE2CTL="${CHROOT} $ENV apache2ctl"
    +PIDFILE=$(. ${CHRDIR}$APACHE_ENVVARS && echo ${CHRDIR}$APACHE_PID_FILE)
     APACHE2_INIT_MESSAGE=""
    
     CONFTEST_OUTFILE=

* disable startup of :file:`apache2` and enable startup of :file:`apache2-cacert`:

  .. code-block:: bash

    $ sudo update-rc.d apache2 remove
    $ sudo update-rc.d apache2-cacert defaults

Services
========

Listening services
------------------

+----------+---------+---------+--------------------------------------------+
| Port     | Service | Origin  | Purpose                                    |
+==========+=========+=========+============================================+
| 22/tcp   | ssh     | ANY     | admin console access                       |
+----------+---------+---------+--------------------------------------------+
| 25/tcp   | smtp    | local   | mail delivery to local MTA                 |
+----------+---------+---------+--------------------------------------------+
| 80/tcp   | http    | ANY     | Apache httpd for http://test3.cacert.org/  |
+----------+---------+---------+--------------------------------------------+
| 443/tcp  | https   | ANY     | Apache httpd for https://test3.cacert.org/ |
+----------+---------+---------+--------------------------------------------+
| 3306/tcp | mysql   | local   | MySQL database for ...                     |
+----------+---------+---------+--------------------------------------------+

Running services
----------------

.. index::
   single: Apache
   single: MySQL
   single: Postfix
   single: client.pl
   single: cron
   single: openssh
   single: Puppet agent
   single: rsyslog
   single: server.pl
   single: socat

+----------------+--------------------------------+----------------------------------------+
| Service        | Usage                          | Start mechanism                        |
+================+================================+========================================+
| Apache httpd   | Webserver for the CAcert       | init script                            |
|                | web application                | :file:`/etc/init.d/apache2-cacert`     |
+----------------+--------------------------------+----------------------------------------+
| MySQL          | MariaDB database server        | init script                            |
|                | for the CAcert web application | :file:`/etc/init.d/mysql`              |
+----------------+--------------------------------+----------------------------------------+
| Postfix        | SMTP server for local mail     | init script                            |
|                | submission                     | :file:`/etc/init.d/postfix`            |
+----------------+--------------------------------+----------------------------------------+
| client.pl      | CAcert signer client           | init script                            |
|                |                                | :file:`/etc/init.d/commmodule`         |
+----------------+--------------------------------+----------------------------------------+
| cron           | job scheduler                  | init script                            |
|                |                                | :file:`/etc/init.d/cron`               |
+----------------+--------------------------------+----------------------------------------+
| openssh server | ssh daemon for remote          | init script :file:`/etc/init.d/ssh`    |
|                | administration                 |                                        |
+----------------+--------------------------------+----------------------------------------+
| Puppet agent   | configuration                  | init script                            |
|                | management agent               | :file:`/etc/init.d/puppet`             |
+----------------+--------------------------------+----------------------------------------+
| rsyslog        | syslog daemon                  | init script                            |
|                |                                | :file:`/etc/init.d/syslog`             |
+----------------+--------------------------------+----------------------------------------+
| server.pl      | CAcert signer server           | init script                            |
|                |                                | :file:`/etc/init.d/commmodule-signer`  |
+----------------+--------------------------------+----------------------------------------+
| socat          | Emulate serial connection      | entry in                               |
|                | between CAcert signer          | :file:`/etc/rc.local` that executes    |
|                | client and server              | :file:`/usr/local/sbin/socat-signer`   |
|                |                                | inside a :program:`screen` session     |
+----------------+--------------------------------+----------------------------------------+

Databases
---------

+-------+--------+------------------------+
| RDBMS | Name   | Used for               |
+=======+========+========================+
| MySQL | cacert | CAcert web application |
+-------+--------+------------------------+

Connected Systems
-----------------

* (future) :doc:`monitor`
* (future) :doc:`testmgr` has access to imap and MySQL

Outbound network connections
----------------------------

* :doc:`infra02` as resolving nameserver
* :doc:`puppet` (tcp/8140) as Puppet master
* :doc:`proxyout` as HTTP proxy for APT and Github
* crl.cacert.org (rsync) for getting CRLs
* ocsp.cacert.org (HTTP and HTTPS) for OCSP queries
* translations.cacert.org (HTTP and HTTPS) for obtaining fresh translations
* arbitrary Internet SMTP servers for outgoing mail

Security
========

.. sshkeys::
   :RSA:     SHA256:aA/hNCieeWePfqpWif3OPbXv7Z9uvv1bz63OBKlkdcE MD5:ff:56:e4:71:17:f0:6c:27:d9:a8:bc:45:c6:f9:3e:57
   :DSA:     SHA256:NkJSuQauwVoAmUYg1ckMD2kqQcvIxvO/wikUlREgkyg MD5:d3:88:96:39:08:bd:71:97:37:99:7c:a7:99:30:4d:e4
   :ECDSA:   SHA256:cbWu3MmZ5v/A+Q7rklTIdx3apqSYHPVejiIo9r3uZM4 MD5:96:65:fe:5a:4d:e6:b0:31:01:b8:4a:40:62:4a:86:61
   :ED25519: SHA256:qSi4RGV2lIDXDfxezTry5M2xku4R0c/8TzHqH77QnUE MD5:20:10:47:d4:b8:04:e5:ed:2a:10:65:31:79:66:fc:c3

Dedicated user roles
--------------------

.. If the system has some dedicated user groups besides the sudo group used for
   administration it should be documented here Regular operating system groups
   should not be documented

+--------------+----------------------------+
| User         | Purpose                    |
+==============+============================+
| cacertmail   | IMAP mailbox user          |
+--------------+----------------------------+

.. todo::

   clarify why the signer software on test3 is currently running as the root
   user

The directory :file:`/home/cacert/` is owned by root. The signer is running
from :file:`/home/signer/www/CommModule/server.pl` the client is
running from :file:`/home/cacert/www/CommModule/client.pl`. Both are running as
root. Currently no process uses the *cacertsigner* user.

Non-distribution packages and modifications
-------------------------------------------

The setup is similar to :doc:`test`.

Risk assessments on critical packages
-------------------------------------

The operating system is up-to-date

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: secure.test3.cacert.org
   :altnames:   DNS:secure.test3.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/secure_test3_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/secure_test3_cacert_org.pem
   :serial:     50DA
   :expiration: Nov 20 09:29:36 2019 GMT
   :sha1fp:     BA:C8:CB:B8:EB:DF:24:A8:A3:7A:D4:45:86:86:E5:01:97:F7:88:29
   :issuer:     CAcert Testserver Root

.. sslcert:: test3.cacert.org
   :altnames:   DNS:test3.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/test3_cacert_org.crt
   :keyfile:    /home/cacert/etc/ssl/private/test3_cacert_org.pem
   :serial:     50D9
   :expiration: Nov 20 09:29:35 2019 GMT
   :sha1fp:     F2:3C:3A:74:DE:33:69:6C:7E:EF:E4:D1:D1:51:CC:7B:5F:37:BF:2E
   :issuer:     CAcert Testserver Root

**CA certificates on test3**:

These test root certficates are copies from the ones on
:doc:`test`

.. note::

   There are two directories :file:`/etc/root3/` and :file:`/etc/root4/` that
   are supported by the signer but do not contain actual keys and certificates.

.. seealso::

   * :wiki:`SystemAdministration/CertificateList`

<<<<<<< HEAD
openssl configuration for the signer server
-------------------------------------------

There are some openssl configuration files that are used by the server.pl
signer that are stored in :file:`/etc/ssl/{caname}-{purpose}.cnf`.

These files are modified with respect to the reference version in
http://svn.cacert.org/CAcert/SystemAdministration/signer/ssl/,
the modifications involve recent development patches (CRL serial numbers)
and test server adjustments (copied over from test.cacert.org).

Apache httpd configuration
--------------------------

Apache httpd is running in a chroot :file:`/home/cacert/` its configuration is
stored in :file:`/home/cacert/etc/apache2`.

Postfix configuration
---------------------

Postfix configuration is stored in :file:`/etc/postfix`.

Postfix is configured to accept mail for ``test3.cacert.org`` and ``localhost``
all mail is delivered to the mailbox of the *cacertmail* user in
:file:`/var/mail/cacertmail` via :file:`/etc/postfix/virtual.regexp`.

Tasks
=====

Planned
-------

.. todo:: implement git workflows for updates maybe using :doc:`jenkins`

Changes
=======

System Future
-------------

.. * No plans

Additional documentation
========================

.. seealso::

   * :wiki:`PostfixConfiguration`
   * https://codedocs.cacert.org/

References
----------

Apache httpd documentation
  http://httpd.apache.org/docs/2.4/
Apache Debian wiki page
  https://wiki.debian.org/Apache
openssl documentation
  https://www.openssl.org/docs/
Postfix documentation
  http://www.postfix.org/documentation.html
Postfix Debian wiki page
  https://wiki.debian.org/Postfix
