import json
import os


def getdevconfig():
    cfgfile = os.environ["vsdev.json"]
    with open(cfgfile, "r") as f:
        cfg = json.load(f)
    return cfg


def getbinariesfolder():
    return getdevconfig()['BaseBinariesPath']
