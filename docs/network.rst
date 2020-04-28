Network
=======

.. this page contains information from the IP address list at
   :wiki:`SystemAdministration/IPList`

.. seealso::

   :wiki:`SystemAdministration/IPList`

.. nwdiag::
   :caption: IPv4 network

   nwdiag {
     network internet {
       extmon [address="116.203.192.12"]
       router [address="213.154.225.224/27"]
     }
     network intranet {
       address = "172.16.2.0/24"

       router [address="172.17.2.3"]
       infra02 [address="172.16.2.10"]
     }
     network br0 {
       address = "10.0.0.0/24"

       infra02 [address="10.0.0.1"]
       container1;
       container2;
       containerX;
     }
   }

.. nwdiag::
   :caption: IPv6 network

   nwdiag {
     network internet {
       extmon [address="2a01:4f8:c2c:a5b9::1"]
       router;
     }
     network intranet {
       address = "2001:7b8:616:162:1::/80"

       router;
       infra02 [address="...:1::10"]
     }
     network br0 {
       address = "2001:7b8:616:162:2::/80"

       infra02 [address="...:2::1"]
       container1;
       container2;
       containerX;
     }
   }
  

Internet
--------

CAcert has a public Internet IPv4 address range and some of the Internet IP
addresses are mapped to the infrastructure systems.

The infrastructure systems use IPv4 addresses from the
:ip:v4range:`213.154.225.224/27` subnet.

IPv6 connectivity is also available. The infrastructure IPv6 addresses are
taken from the :ip:v6range:`2001:7b8:616:162:1::/80` and
:ip:v6range:`2001:7b8:616:162:2::/80` ranges.

External monitoring is provided from the ranges :ip:v4range:`116.203.192.12/32`
and :ip:v6range:`2a01:4f8:c2c:a5b9::1/128`.


Intranet
--------

CAcert's infrastructure systems are using a private network range that is
accessible from other CAcert systems. The Intranet IPv4 addresses are in the
:ip:v4range:`172.16.2.0/24` subnet.


Internal
--------

The infrastructure host :doc:`systems/infra02` has a local bridge interface
*br0* that is used to connect the containers on that machine and allows
explicit routing as well as services that are purely internal and are not
reachable from the Internet or Intranet machines in the IP range mentioned
above.

The local bridge uses IPv4 addresses from the :ip:v4range:`10.0.0.0/24` range.
IPv6 addresses are directly assigned to containers from the
:ip:v6range:`2001:7b8:616:162:2::/80` range.
