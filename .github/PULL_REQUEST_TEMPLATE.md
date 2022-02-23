[x] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/niveristand-python/blob/master/CONTRIBUTING.md).

### What does this Pull Request accomplish?

This pull Request updates legacy API, Worskpace2 class with the missing ReconnectToSystem function along with the basic use example.
It also fixes the GetSystemState function - it stopped working due to the PythonNET update.

### Why should this Pull Request be merged?

This Pull Request adds missing and useful feature and fixes bug.

### What testing has been done?

ReconnectToSystemTest was prepared and is included in the Pull Request. It uses project SineWave Delay which is being shipped along
with the VeriStand 2020. It was tested using VeriStand 2020 and it's working properly.
ReconnnectToSystemTest also tests GetSystemState function.