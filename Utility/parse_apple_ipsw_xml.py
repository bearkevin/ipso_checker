from Model.constant import APPLE_IPSW_XML
from Model.custom_class import DeviceIPSW
from Utility.utility_get_xml import get_xml,get_deep_value
from urllib.parse import urlparse
import os


def get_latest_version_node() -> dict:
    obj_plist = get_xml(APPLE_IPSW_XML)
    version_keys_in_plist = get_deep_value(obj_plist, ('MobileDeviceSoftwareVersionsByVersion',)).keys()
    latest_version_key_in_plist = str(max(int(key) for key in version_keys_in_plist))
    node_firmware_by_device_code = get_deep_value(obj_plist, ('MobileDeviceSoftwareVersionsByVersion',
                                                              latest_version_key_in_plist,
                                                              'MobileDeviceSoftwareVersions'))
    return node_firmware_by_device_code


def get_apple_device_info_list():
    device_list = []
    node = get_latest_version_node()
    for k,v in node.items():
        if 'Unknown' in v.keys():
            child_node = get_deep_value(node,(k,'Unknown','Universal','Restore'))
            device_code = k
            buildver_version = get_deep_value(child_node,('BuildVersion',))
            product_version = get_deep_value(child_node,('ProductVersion',))
            firmware_url = get_deep_value(child_node,('FirmwareURL',))
            parsedurl = urlparse(firmware_url)
            firmware_filename = os.path.basename(parsedurl.path)
            sha1 = get_deep_value(child_node,('FirmwareSHA1',))
            device = DeviceIPSW(
                devicecode=device_code,
                buildversion=buildver_version,
                productversion=product_version,
                firmwareurl=firmware_url,
                firmwarefilename=firmware_filename,
                sha1=sha1
            )
            device_list.append(device)
    return device_list




if __name__ == '__main__':
    a = get_apple_device_info_list()
    print(a)

