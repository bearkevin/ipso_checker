from dataclasses import dataclass
@dataclass
class DeviceIPSW:
    devicecode: str
    buildversion: str
    productversion: str
    firmwareurl: str
    firmwarefilename:str
    sha1: str