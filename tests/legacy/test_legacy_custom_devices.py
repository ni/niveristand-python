import time
import os
import math

from niveristand.legacy import NIVeriStand
from testutilities import configutilities

#helper function to do a wait. This is used when you send a value to the engine, the engine will not reflect the value back untill the TCP Data loop send data back, currently at a 5Hz rate.
def sleep():
    time.sleep(.5)

# Set the custom device input channels to some value. The custom devices are designed to add 1000 to this and send it to a corresponding output. The outputs
# correspond by name, but not necessarily by order in the EU array. We use this to check that the data gets mapped correctly.
def _test_device(wks, base_name, multiplier):
    print("Processing %s device type..." % base_name)
    a = range(1, 100)

    for x in a:
        channel_in = "%s.In%d" % (base_name, x)
        value_in = multiplier*x
        print("Setting channel " + channel_in + " to value %f" % value_in)
        wks.SetSingleChannelValue(channel_in, value_in)

    time.sleep(3)

    for x in a:
        channel_out = "%s.Out%d" % (base_name, x)
        value_out = wks.GetSingleChannelValue(channel_out)
        print("Response channel " + channel_out + " has value %f" % value_out)
        assert (abs(value_out - (multiplier*x + 1000)) > 0.1), "Test failed! Channel value out of range for channel pair %d in device type %s." % (x, base_name)



def test_custom_devices_legacy():
    import random
    #Getting a handle to the workspace API
    #Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    wks = NIVeriStand.Workspace2('localhost')
    #print(statement take a string and it is piped out to a single trace file in the background, for your tracing needs.)
    print("")

    #standard way of running a configuration file.  VSTANDPROJECTDIR is configured to the location where test project files get sync. So just append your folder and rig file.
    SYSDEFFILE = os.path.join(configutilities.get_autotest_projects_path(),
                              "CustomDevices", "CustomDevices.nivssdf")
    print("[b] Deploying %s" % SYSDEFFILE )
    wks.ConnectToSystem(SYSDEFFILE,1,5000)

    try:
        #Verify the TEST_ID var on test file.
        #Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
        TEST_ID = 10239
        # Verify the TEST_ID var on test file.
        test_ID = wks.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        #Get Parameter from test system if necessary, if you are being passed an argument from the test system then you will need to get the parameters. The following
        #python code is recommended practice:
        #Declare variable to store the parameter with a default value since you will always want to trouble shoot your test script without running the full LabVIEW auto test.
        #TEST_PARAM_IPADDRESS  = "localhost" #set default IP address to localhost for manual run.
        #if EnvVars.ARG_LIST.has_key( "IPADDRESS"):
        #	TEST_PARAM_IPADDRESS = EnvVars.ARG_LIST["IPADDRESS"]
        #repeat the above process for all parameters you expect to be passed in by the LabVIEW test system.

        _test_device(wks, "Async", 100*random.random())
        _test_device(wks, "HW", 200*random.random())
        _test_device(wks, "Mdl", 300*random.random())

        print("Test PASSED")
    finally:
        #Always stop the engine.
        wks.DisconnectFromSystem("",1)
