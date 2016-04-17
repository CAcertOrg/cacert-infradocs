Network
=======

.. this page contains information from the IP address list at
   https://wiki.cacert.org/SystemAdministration/IPList

.. seealso::

   https://wiki.cacert.org/SystemAdministration/IPList


Internet
--------

CAcert has a public Internet IPv4 address range and some of the Internet IP
addresses are mapped to the infrastructure systems.

The infrastructure systems use IPv4 addresses from the
:ip:v4range:`213.154.225.0/24` subnet.

IPv6 connectivity is also available. The infrastructure IPv6 addresses are
taken from the :ip:v6range:`2001:7b8:616:162:1::/80` and
:ip:v6range:`2001:7b8:616:162:2::/80` ranges.


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
