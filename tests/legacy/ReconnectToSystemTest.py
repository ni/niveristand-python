import pytest

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
from niveristand.errors import RunError

PROJECTDIR = r"C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects"
SDF = PROJECTDIR + r"\Example\Sinewave Delay.nivssdf"
# Prior to running this test the SDF file above must be deployed

GATEWAY = "localhost"
TARGET = "Controller"
SINE_WAVE = 'Aliases/SineWave'
LOOP_RATE = 'Targets/Controller/System Channels/Actual Loop Rate'


def sleep():
    import time
    time.sleep(1)


TEST_RESULT = 0 #Testresult set to false in beginning
TEST_COMMENT = "" #Test  comment to append to result
TEST_ID = 124123

def test_reconnect_to_system():
    wks = NIVeriStand.Workspace2(GATEWAY)
    print("")
    print("Connecting to the gateway %(gateway)s, target %(target)s" % {'gateway': GATEWAY, "target": TARGET})
    wks.ReconnectToSystem(TARGET, True, None, 60000)

    try:

        result = wks.GetSystemState()
        assert(result['systemdefinition_file'] == SDF), "System definition file is not the same as deployed"

        print("Get System Node Children")
        result = wks.GetSystemNodeChildren(r"Controller/Simulation Models/Models/sinewave/Execution")
        assert(len(result) == 4), "Model Exceution should return 4 node"

        #test we can still get system node children with full path.
        result = wks.GetSystemNodeChildren(r"Targets/Controller/Simulation Models/Models/sinewave/Execution")
        assert(len(result) == 4), "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = wks.GetSystemNodeChannelList('')
        assert(len(result) >= 100), "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = wks.GetAliasList()
        assert(len(result) == 6), "Expected 6 aliases but get something different %d" % len(result)
        assert(result['SineWave'] == r"Targets/Controller/Simulation Models/Models/sinewave/Signals/sine/SineWave"), "Alias for SineWave incorrect"

        #Mix up different mode of how we look up system nodes data: full path and also relative to Targets Section.
        nodes = (SINE_WAVE, LOOP_RATE)
        result = wks.GetMultipleSystemNodesData(nodes)
        assert(len(result) == 2), "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert(section['isChannel'] == 1), "Expected channel, got something different."

        testNode = result[1]
        print(testNode)
        assert(testNode['isChannel'] == 1), "Expected channel, got something different."

        print("Test PASSED")
        print("")

    finally:
        pass
        wks.DisconnectFromSystem("", True)
