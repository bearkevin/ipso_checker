import sqlite3
import yaml
from collections import defaultdict


# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

quest_distinct_url = """
SELECT distinct new.firmwareurl
FROM server AS new
LEFT OUTER JOIN local AS old ON new.devicecode = old.devicecode;

"""

quest_different_devices = """
SELECT new.devicecode, new.productversion
FROM server AS new
LEFT OUTER JOIN local AS old ON new.devicecode = old.devicecode;
"""


def get_list_firmware_url(conn):
    cursor = conn.cursor()
    cursor.execute(quest_distinct_url)
    urls = cursor.fetchall()
    return urls


def get_updated_devices(conn,device_config):
    cursor = conn.cursor()
    cursor.execute(quest_different_devices)
    updated_devices = cursor.fetchall()
    with open(device_config, 'r') as f:
        devices = yaml.safe_load(f)
    device_mapping = {item['code']: item['name'] for item in devices}
    result = defaultdict(set)
    for device, version in updated_devices:
        device_name = device_mapping.get(device, f"Unknown({device})")
        result[version].add(device_name)
    merged_result = [(version, '\n'.join(sorted(devices))) for version, devices in result.items()]
    return merged_result

#
# a = get_list_firmware_url()
# print(a)


