import re
import sys

sys.path.append(r"C:\Program Files\National Instruments\VeriStand 2024")

from niveristand.systemdefinitionapi import SystemDefinition, Utilities
import System   # type: ignore

system_definition = SystemDefinition(
    "test",
    "This is an example System Definition file created using the System Definition API",
    "System Definition API",
    "1.0.0.0",
    "Controller",
    "Windows",
    r"C:\Users\nitest\Desktop\test.nivssdf",
)

target_section = system_definition.root.get_targets().get_target_list()[0]
user_channels_section = target_section.get_user_channels()
sources_section = user_channels_section.add_new_user_channels_folder("Sources", "")
destinations_section = user_channels_section.add_new_user_channels_folder("Destinations", "")

for i in range(1000):
    name = ["Foo", "Bar"][i % 2]
    sources_section.add_new_user_channel(f"{name} {i}", "", "", 0.)

for i in reversed(range(1000)):
    name = ["Alice", "Bob", "Carol"][i % 3]
    destinations_section.add_new_user_channel(f"{name} {i}", "", "", 0.)


class MatchingNumberComparer(System.Collections.Generic.IEqualityComparer[str]):
    """
    Compares the first integer in one string with the first integer in another.
    """

    # Must specify a namespace for our type to live in.
    __namespace__ = "MyApplication"
    
    def __init__(self):
        self.regex = re.compile(r"(\d+)")

    def Equals(self, x: str, y: str):
        x_match = self.regex.search(x)
        if not x_match:
            return False
        
        y_match = self.regex.search(y)
        if not y_match:
            return False
        
        return x_match.group(1) == y_match.group(1)
    
    def GetHashCode(self, o):
        match = self.regex.search(o)
        if not match:
            return System.Int32(hash(o) & 0x7FFF_FFFF)        
    
        return System.Int32(int(match.group(1)) & 0x7FFF_FFFF)
    
Utilities.auto_map_channels(sources_section, destinations_section, MatchingNumberComparer())

system_definition.save_system_definition_file()
