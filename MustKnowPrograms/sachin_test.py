conversion_table = {
    "00:18:0A": 6,
    "88:15:44": 1,
    "E0:55:3D": 2
}

mac_addresses = [
    "88:15:44:4F:85:E0",
    "00:18:0A:5B:0C:10",
    "E0:55:3D:2D:02:23"
]

for mac_address in mac_addresses:
    temp_data = mac_address.split(":")
    print "{}.{}.{}.{}".format(
        conversion_table[
            ":".join(temp_data[0:3])
        ],
        int(temp_data[3], 16),
        int(temp_data[4], 16),
        int(temp_data[5], 16),

    )
