from Database.init_db import init_database
from Database.utility_db import get_updated_devices,get_list_firmware_url
import sqlite3

def main():
    device_config = 'Database/device.yaml'
    conn = sqlite3.connect('Database/database.db')
    init_database(conn)
    device_list = get_updated_devices(conn, device_config)
    url_list = get_list_firmware_url(conn)
    for version, devices in device_list:
        print(f"new version {version} found for devices below:")
        print(devices)
        print('-'*20)
    print('Totally', len(url_list),'file(s) need downloaded.')


if __name__ == '__main__':
    main()