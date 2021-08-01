.. index::
   single: Systems; ocsp

====
Ocsp
====

.. copy content structure from critical/template.rst and adapt to the needs for
   this system

Basics
======

Logical Location
----------------

:IP Internet: :ip:v4:`213.154.225.237`

Critical Configuration items
============================

Keys and X.509 certificates
---------------------------

.. sslcert:: ocsp.cacert.org
   :altnames:   DNS:ocsp.cacert.org
   :certfile:   /etc/lighttpd/ssl/ocsp.cacert.org.crt
   :keyfile:    /etc/lighttpd/ssl/ocsp.cacert.org.key
   :serial:     02CC47
   :expiration: Nov 18 19:03:01 2020 GMT
   :sha1fp:     85:42:E3:DC:42:F2:7C:C2:B2:02:9F:47:16:34:02:55:BE:92:AA:17
   :issuer:     CAcert Class 3 Root

.. sslcert:: ocsp.cacert.org class1 (issued with X509v3 Extended Key Usage: OCSP Signing)
   :altnames:
   :certfile:   /usr/local/etc/ocspd/certs/class1.crt
   :keyfile:    /usr/local/etc/ocspd/private/class1.key
   :serial:     144847
   :expiration: Aug 24 14:12:48 2021 GMT
   :sha1fp:     6A:F9:88:26:25:F2:58:D2:4F:0D:A9:FB:F2:27:DE:A1:49:0B:84:B2
   :issuer:     CAcert Class 1 Root

.. sslcert:: ocsp.cacert.org class3 (issued with X509v3 Extended Key Usage: OCSP Signing)
   :altnames:
   :certfile:   /usr/local/etc/ocspd/certs/class3.crt
   :keyfile:    /usr/local/etc/ocspd/private/class1.key
   :serial:     2d99d
   :expiration: Aug 24 14:14:29 2021 GMT
   :sha1fp:     3A:53:54:CF:57:83:5D:F5:DC:0F:53:D2:7E:30:22:AF:68:83:24:B8
   :issuer:     CAcert Class 3 Root

Note: generating a CSR with OCSP Signing flag set can be done with an openssl config file like this:

.. code-block:: text

   [ req ]
   distinguished_name      = req_distinguished_name
   prompt                  = no
   req_extensions          = ocsp_req
   
   [ req_distinguished_name ]
   countryName             = AU
   stateOrProvinceName     = NSW
   localityName            = Sydney
   0.organizationName      = CAcert Inc.
   organizationalUnitName  = Server Administration
   commonName              = ocsp.cacert.org
   emailAddress            = critical-admin@cacert.org
   
   [ ocsp_req ]
   basicConstraints=CA:FALSE
   extendedKeyUsage=1.3.6.1.5.5.7.3.2, 1.3.6.1.5.5.7.3.1, 1.3.6.1.5.5.7.3.9

To sign such a CSR while retaining the OCSP Signing flag in the generated certificate, there is some dark magic involved: you have to have the admin flag set and check a box deep down on the second page of the new cert process. 
