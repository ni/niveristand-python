import os
from examples.engine_demo.engine_demo_basic import run_engine_demo
from niveristand import run_py_as_rtseq
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand


def sdf_deploy_with_deploy_option():
    """Use legacy API to deploy a system definition along with deploy option."""
    # Ensures NI VeriStand is running.
    NIVeriStand.LaunchNIVeriStand()
    NIVeriStand.WaitForNIVeriStandReady()
    # Uses the ClientAPI interface to get a reference to Workspace2
    # For deployment in RT, make sure the model added in system definition is linux compatible. Make sure RT is in good state.
    # (E.g., Public\Documents\National Instruments\NI VeriStand *\Examples\Stimulus Profile\Engine Demo\Model\EngineDemo_linux.vsmodel)
    workspace = NIVeriStand.Workspace2("localhost")
    engine_demo_path = os.path.join(
        os.path.expanduser("~public"),
        "Documents",
        "National Instruments",
        "NI VeriStand 2021",
        "Examples",
        "Stimulus Profile",
        "Engine Demo",
        "Engine Demo.nivssdf",
    )
    
    try:
        # Example : Deploys the system definition with deploy option.
        # calibration_file : path of calibration file
        # filtered_targets : list of strings (target)
        calibration_file = ""
        filtered_targets = None
        workspace.ConnectToSystem(engine_demo_path, True, 120000, calibration_file, filtered_targets)
        print("Test Success")
    except RunError as e:
        print("Test Failed: %d -  %s" % (int(e.error.error_code), e.error.message))
    finally:
        # You can now disconnect from the system, so the next test can run.
        workspace.DisconnectFromSystem("", True)


if __name__ == "__main__":
    sdf_deploy_with_deploy_option()
