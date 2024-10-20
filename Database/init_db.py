import sqlite3
import logging
from Utility.parse_apple_ipsw_xml import get_apple_device_info_list




def init_database(conn):
    # conn = sqlite3.connect('Database/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists local (
            devicecode       TEXT not null primary key,
            buildversion     TEXT not null,
            productversion   TEXT not null,
            firmwareurl      TEXT not null,
            firmwarefilename TEXT not null,
            sha1             TEXT
)       ;
    ''')
    cursor.execute('''
            create table if not exists server (
                devicecode       TEXT not null primary key,
                buildversion     TEXT not null,
                productversion   TEXT not null,
                firmwareurl      TEXT not null,
                firmwarefilename TEXT not null,
                sha1             TEXT
    )       ;
        ''')
    cursor.execute("delete from server;")
    conn.commit()
    logging.info("Database initiated.")

    apple_ipsw_list = get_apple_device_info_list()
    for item in apple_ipsw_list:
        cursor.execute('''
            insert into server (
                                devicecode, 
                                buildversion, 
                                productversion, 
                                firmwareurl, 
                                firmwarefilename, 
                                sha1)values (?,?,?,?,?,?)
        ''',(
                                item.devicecode,
                                item.buildversion,
                                item.productversion,
                                item.firmwareurl,
                                item.firmwarefilename,
                                item.sha1
                        )
        )
    conn.commit()
    logging.info("Data from server saved.")