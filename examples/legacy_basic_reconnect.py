import sys
import time
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand

# This is an example script to demonstrate the usage of NIVeriStand Python API.
# This script requires Python 32b(tested on Python 3.9.6) and NIVeriStand Python API.
# It can be downloaded here: https://niveristand-python.readthedocs.io/en/latest/index.html

# This script deploys example project on the selected GATEWAY and it prints two channel values every 100ms
# This script requires VeriStand serwer to be running. It is ran automatically after launching VeriStand.
# You can also start it manually from the command line.
# Default veristand-server.exe location:
# "C:\Program Files (x86)\National Instruments\VeriStand 2020\veristand-server.exe"
# Press Ctrl + C to stop the program.

PROJECTDIR = r"C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects"
SDF = PROJECTDIR + r"\Example\Sinewave Delay.nivssdf"

GATEWAY = "localhost"  # GATEWAY address
TARGET = "Controller"

SINE_WAVE = 'Aliases/SineWave'
LOOP_RATE = 'Targets/Controller/System Channels/Actual Loop Rate'
# channel adresses can be entered as full paths or aliases


def sleep():
    time.sleep(0.1)


wks = NIVeriStand.Workspace2(GATEWAY)  # create workspace object
try:
    # print("Running %s" % SDF)
    # wks.ConnectToSystem(SDF,True,60000)  # connect to system, deploy project, 60s timeout
    print("Connecting to the gateway %(gateway)s, target %(target)s" % {'gateway': GATEWAY, "target": TARGET})
    wks.ReconnectToSystem(TARGET, True, None, 60000)  # reconnect to already deployed system
    print("NI VeriStand Running and Client Connected!")
    input("Press Enter to start printing data values, then you can press Ctrl+C to disconnect.")

    while (1):
        print("Actual Loop Rate: ", wks.GetSingleChannelValue(LOOP_RATE))
        print("Sine wave:", wks.GetSingleChannelValue(SINE_WAVE))
        print('')
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
    wks.DisconnectFromSystem('', True)  # undeploy project
    # pass
