Glossary
========

.. glossary::
   :sorted:

   LXC
      LXC is a userspace interface to the Linux kernel containment features.
      See `The LXC introduction
      <https://linuxcontainers.org/lxc/introduction/>`_ on the Linux containers
      website for more information

   Container
      A container is an isolated system with a separate root file system and
      operating system userland. The containers share a common operating system
      kernel.

   LVM
      Logical volume manager. The LVM allows to allocate space on block
      devices more dynamically than with traditional partitions. The block
      devices are managed as physical volumes (PVs) that are grouped in volume
      groups (VGs). Space can be allocated as logical volumes (LVs) that can be
      formatted using regular file system tools. LVs can be resized without
      reboot. LVM provides snapshot functionality that is useful for backup and
      upgrade procedures.

   Infrastructure Team Lead
      This person is appointed to coordinate the non-critical infrastructure
      team by a board motion. The Infrastructure Team Lead works with
      :term:`Infrastructure Administrators <Infrastructure Administrator>` and
      the :term:`Critical System Administrators <Critical System
      Administrator>`.

   Infrastructure Administrator
      Infrastructure Administrators have :program:`sudo` access to one or
      multiple infrastructure systems. Most of them are :term:`Application
      Administrators <Application Administrator>` too.

   Critical System Administrator
      The Critical System Administrators take care of the critical systems
      required for the CA and RA operation, they have access to the Internet
      firewall and DNS setup.

   Application Administrator
      An Application Administrator takes care of the functionality of one or
      more server applications. Application Administrators do not necessarily
      need system level access if the managed application has other means of
      administration, for example a web based administration frontend.

   DKIM
   Domain Key Identified Mail
      A mechanism where legitimate mail for a domain is verifiable by a
      signature in a mail header and a corresponding public key in a specific
      :term:`DNS` record. Outgoing mail servers for the domain have to be
      configured to add the necessary signature to mails for their domains.

   DNS
   Domain Name System
      DNS maps names to other information, the most well known use case is
      mapping human readable names to IP addresses, but their are more
      applications for DNS like service discovery, storage of public keys and
      other public information.
