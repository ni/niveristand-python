import os
import clr
import yaml


def base_assembly_path():
    try:
        return _getdevconfig()['BaseBinariesPath']
    except (IOError, KeyError):
        return ''


def _getdevconfig():
    cfgfile = os.environ["vsdev.yaml"]
    cfgfile = cfgfile.strip('"')
    with open(os.path.normpath(cfgfile), "r") as f:
        cfg = yaml.load(f.read())
    return cfg


clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference(os.path.join(base_assembly_path(),
                              "NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll"))
clr.AddReference(os.path.join(base_assembly_path(),
                              "NationalInstruments.VeriStand.DataTypes.dll"))


def dummy():
    """
    Do nothing because you're just a dummy.

    This dummy can be used by any module that imports internal to get rid of PEP8 errors about
    an import not being used. This internal module takes care of loading C# references, so most
    times it will only be imported but not actually used.
    """
    pass
