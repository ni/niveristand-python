import os
import yaml


def getbinariesfolder():
    return _getdevconfig()['BaseBinariesPath']


def _getdevconfig():
    cfgfile = os.environ["vsdev.yaml"]
    with open(cfgfile, "r") as f:
        cfg = yaml.load(f)
    return cfg


def get_autotest_projects_path():
    return os.path.join(_getdevconfig()['TestAppData'], 'AutoTestProjects')
