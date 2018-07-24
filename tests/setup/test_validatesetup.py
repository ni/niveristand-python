from os import path
from testutilities import configutilities

__vs_binaries__ = ["NationalInstruments.VeriStand.dll"]


def _inc(x):
    return x + 1


def test_pass():
    """Just make sure asserts work."""
    assert _inc(4) == 5


def test_pythonnetworks():
    import clr
    clr.AddReference("System")
    from System import String
    s = String("teststring")
    assert "teststring" == str(s)


def test_binariesfound():
    folder = configutilities.getbinariesfolder()
    assert path.isdir(folder)
    for binary in __vs_binaries__:
        assert path.isfile(path.join(folder, binary))


def test_getinstalledbinariespath():
    from niveristand._internal import _get_install_path
    try:
        bindir = _get_install_path()
        assert bindir is not None
    except (IOError, WindowsError):
        pass
