=====
Webdb
=====

.. copy content structure from critical/template.rst and adapt to the needs for
   this system

Basics
======

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.245`, :ip:v4:`213.154.225.246`, :ip:v4:`213.154.225.247`

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: www.cacert.org
   :altnames:   DNS:cacert.com, DNS:cacert.net, DNS:cacert.org, DNS:secure.cacert.org, DNS:www.cacert.com, DNS:www.cacert.net, DNS:www.cacert.org, DNS:wwwmail.cacert.org
   :certfile:   /home/cacert/etc/ssl/certs/cacert.crt
   :keyfile:    /home/cacert/etc/ssl/certs/cacert.crt
   :serial:     02C1A1
   :expiration: Apr 04 19:42:41 2020 GMT
   :sha1fp:     2B:9F:9D:2F:CF:0A:95:BB:B6:A0:D1:2B:DB:7A:C8:60:13:F3:16:E8
   :issuer:     CAcert Class 3 Root

