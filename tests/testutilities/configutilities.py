import os
import json


def getbinariesfolder():
    from niveristand import _internal
    return _internal.base_assembly_path()


def _getdevconfig():
    cfgfile = os.environ["vsdev.json"]
    with open(cfgfile, "r") as f:
        cfg = json.load(f)
    return cfg


def get_autotest_projects_path():
    return os.path.join(_getdevconfig()['TestAppData'], 'AutoTestProjects')
