"""This module contains the general information for VnicIPv4Dns ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class VnicIPv4DnsConsts:
    PREF_ALTERNATE = "alternate"
    PREF_PREFERRED = "preferred"


class VnicIPv4Dns(ManagedObject):
    """This is VnicIPv4Dns class."""

    consts = VnicIPv4DnsConsts()
    naming_props = set([u'pref'])

    mo_meta = MoMeta("VnicIPv4Dns", "vnicIPv4Dns", "ipv4-dns-[pref]", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], [u'adaptorHostIscsiIf', u'adaptorVlan', u'vnicIPv4If', u'vnicIPv4IscsiAddr', u'vnicIPv4PooledIscsiAddr'], [], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x10, None, None, None, ["alternate", "preferred"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "pref": "pref", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, pref, **kwargs):
        self._dirty_mask = 0
        self.pref = pref
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIPv4Dns", parent_mo_or_dn, **kwargs)
