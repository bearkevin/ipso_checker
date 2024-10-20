import requests
import plistlib
from Model.constant import REQUEST_HEADERS



def get_xml(xml_address:str) -> dict:
    """
    read remote xml information
    :rtype: object
    :param xml_address: remote xml url
    :return: a dict object includes xml information
    """
    apple_xml_resp = requests.get(xml_address, stream=True, headers=REQUEST_HEADERS)
    apple_xml_resp.raise_for_status()
    plist_data = plistlib.loads(apple_xml_resp.content)
    return plist_data


def get_deep_value(data,keys,default = None):
    for key in keys:
        data = data.get(key,default)
        if data is default:
            return key + ' Not Found'
    return data