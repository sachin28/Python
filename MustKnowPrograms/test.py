# to ip address
# Table
# 00:18:0A => 6
# 88:15:44 => 1
# E0:55:3D => 2
#
# EXamples
# 88:15:44:4F:85:E0 => 1.79.133.224
# 00:18:0A:5B:0C:10 => 6.91.12.16
# E0:55:3D:2D:02:23 => 2.45.23.34


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
    temp_list = mac_address.split(":")
    print "{}.{}.{}.{}".format(
        conversion_table[":".join((temp_list[0: 3]))],
        int(temp_list[3], 16),
        int(temp_list[4], 16),
        int(temp_list[5], 16),
    )
