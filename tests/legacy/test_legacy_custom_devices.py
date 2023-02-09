import pytest
import time

from niveristand.legacy import NIVeriStand


# Set the custom device input channels to some value. The custom devices are designed to add 1000 to this and send it to a corresponding output. The outputs
# correspond by name, but not necessarily by order in the EU array. We use this to check that the data gets mapped correctly.
def _test_device(workspace, base_name, multiplier):
    print("Processing %s device type..." % base_name)
    a = range(1, 100)

    for x in a:
        channel_in = "%s.In%d" % (base_name, x)
        value_in = multiplier*x
        print("Setting channel " + channel_in + " to value %f" % value_in)
        workspace.SetSingleChannelValue(channel_in, value_in)

    time.sleep(3)

    for x in a:
        channel_out = "%s.Out%d" % (base_name, x)
        value_out = workspace.GetSingleChannelValue(channel_out)
        print("Response channel " + channel_out + " has value %f" % value_out)
        assert (abs(value_out - (multiplier*x + 1000)) > 0.1), "Test failed! Channel value out of range for channel pair %d in device type %s." % (x, base_name)


@pytest.mark.skip('custom device test not able to find file in folder that is there')
def test_custom_devices_legacy():
    import random
    #Getting a handle to the workspace API
    #Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace2('localhost')
    #print(statement take a string and it is piped out to a single trace file in the background, for your tracing needs.)
    print("")

    #standard way of running a configuration file.  VSTANDPROJECTDIR is configured to the location where test project files get sync. So just append your folder and rig file.
    system_definition = r"C:\Users\virtual\Desktop\AutoTestProjects\CustomDevices\CustomDevices.nivssdf"
    print("[b] Deploying %s" % system_definition )
    workspace.ConnectToSystem(system_definition, 1, 20000)

    try:
        #Verify the TEST_ID var on test file.
        #Every test should have a user variable that have a test ID number to ensure that you are running the correct test configuration.
        TEST_ID = 10239
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert (test_ID == TEST_ID), "Deployed wrong test file"

        #Get Parameter from test system if necessary, if you are being passed an argument from the test system then you will need to get the parameters. The following
        #python code is recommended practice:
        #Declare variable to store the parameter with a default value since you will always want to trouble shoot your test script without running the full LabVIEW auto test.
        #TEST_PARAM_IPADDRESS  = "localhost" #set default IP address to localhost for manual run.
        #if EnvVars.ARG_LIST.has_key( "IPADDRESS"):
        #	TEST_PARAM_IPADDRESS = EnvVars.ARG_LIST["IPADDRESS"]
        #repeat the above process for all parameters you expect to be passed in by the LabVIEW test system.

        _test_device(workspace, "Async", 100*random.random())
        _test_device(workspace, "HW", 200*random.random())
        _test_device(workspace, "Mdl", 300*random.random())

        print("Test PASSED")
    finally:
        #Always stop the engine.
        workspace.DisconnectFromSystem("",1)
