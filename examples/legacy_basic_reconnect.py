import sys
import time
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand

# This is an example script to demonstrate the usage of ReconnectToSystem function.
# This script requires cPython(tested on cPython 3.9.6) and (obviously) NIVeriStand Python API.

# This script deploys example project on the selected GATEWAY and it prints two channel values every 100ms
# This script requires the example SineWave Delay Project(shipped with LabVIEW 2020) to be deployed.
# SineWave Delay project file path:
#    C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects\Example\Sinewave Delay.nivsproj
# Press Ctrl + C to stop the program.

GATEWAY = "localhost"
TARGET = "Controller"

SINE_WAVE = "Aliases/SineWave"
LOOP_RATE = "Targets/Controller/System Channels/Actual Loop Rate"
# channel adresses can be entered as full paths or aliases


def sleep():
    time.sleep(0.1)


wks = NIVeriStand.Workspace2(GATEWAY)  # create workspace object
try:
    print(
        "Connecting to the gateway %(gateway)s, target %(target)s"
        % {"gateway": GATEWAY, "target": TARGET}
    )
    wks.ReconnectToSystem(TARGET, True, None, 60000)  # reconnect to already deployed system
    print("NI VeriStand Running and Client Connected!")
    input("Press Enter to start printing data values, then you can press Ctrl+C to disconnect.")

    while 1:
        print("Actual Loop Rate: ", wks.GetSingleChannelValue(LOOP_RATE))
        print("Sine wave:", wks.GetSingleChannelValue(SINE_WAVE))
        print("")
        sleep()

except RunError as err:
    TEST_COMMENT = "Unexpected Exception " + err.error.message()
    print(TEST_COMMENT)
    time.sleep(10)
except KeyboardInterrupt:
    print("Press any button to exit script.")
except Exception:
    print(sys.exc_info())
    time.sleep(10)
finally:
    wks.DisconnectFromSystem("", True)  # undeploy project
