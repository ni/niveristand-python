import os
import tempfile
import clr


def base_assembly_path():
    try:
        return _getdevconfig()['BaseBinariesPath']
    except (IOError, KeyError):
        pass
    try:
        return _get_ref_assemblies_path()
    except IOError:
        return ''


def _get_ref_assemblies_path():
    latest_dir = _get_install_path()
    return os.path.join(latest_dir, 'nivs.lib', 'Reference Assemblies')


def _get_install_path():
    import sys
    if sys.version_info > (3, 0):
        import winreg
    else:
        import _winreg as winreg
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Wow6432Node\\National Instruments\\VeriStand\\') as vskey:
        r = winreg.QueryInfoKey(vskey)
        ver = '0'
        for k in range(r[0]):
            with winreg.OpenKey(vskey, winreg.EnumKey(vskey, k)) as this_key:
                this_ver = winreg.QueryValueEx(this_key, 'Version')[0]
                if this_ver > ver:
                    latest_dir = winreg.QueryValueEx(this_key, 'InstallDir')[0]
                    ver = this_ver
    return latest_dir if latest_dir is not None else ''


def _getdevconfig():
    import json
    cfgfile = os.environ["vsdev.json"]
    cfgfile = cfgfile.strip('"')
    with open(os.path.normpath(cfgfile), "r") as f:
        cfg = json.load(f)
    return cfg


clr.AddReference("System")
clr.AddReference("System.IO")
from System.IO import FileNotFoundException  # noqa: E402, I202 .net imports can't be at top of file.
try:
    # Try loading from the GAC first, dev/install folders second.
    clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi")
    clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities")
    clr.AddReference("NationalInstruments.VeriStand.DataTypes")
    clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
except FileNotFoundException:
    try:
        from sys import path
        path.append(base_assembly_path())
        clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi")
        clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities")
        clr.AddReference("NationalInstruments.VeriStand.DataTypes")
        clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
    except FileNotFoundException as e:
        raise IOError(e.Message)


def dummy():
    """
    Do nothing because you're just a dummy.

    This dummy can be used by any module that imports internal to get rid of PEP8 errors about
    an import not being used. This internal module takes care of loading C# references, so most
    times it will only be imported but not actually used.
    """
    pass


# set the temporary folder to C:\Users\$USER\AppData\Local\Temp\python_rt_sequences
tempfile.tempdir = os.path.join(tempfile.gettempdir(), 'python_rt_sequences')
if not os.path.exists(tempfile.tempdir):
    os.makedirs(tempfile.tempdir)
