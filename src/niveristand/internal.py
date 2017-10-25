import yaml
import os
import clr


def base_assembly_path():
    try:
        return _getdevconfig()['BaseBinariesPath']
    except:
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
