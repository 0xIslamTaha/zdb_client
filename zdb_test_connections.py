from zdb_client import ZDBCLIENT

zdb_servers = ["172.20.18.104:1026",
"172.20.18.120:1025",
"172.20.18.128:1024",
"172.20.18.137:1025",
"172.20.18.142:1030",
"172.20.18.146:1041",
"172.20.18.155:1026",
"172.20.18.175:1024",
"172.20.18.191:1025",
"172.20.18.38:1024",
"172.20.18.47:1025",
"172.20.18.51:1026",
"172.20.18.52:1027",
"172.20.18.54:1027",
"172.20.18.55:1028",
"172.20.18.69:1026",
"172.20.18.72:1027",
"172.20.18.78:1025",
"172.20.18.79:1027",
"172.20.18.86:1026",
"172.20.18.87:1025",
"172.20.18.92:1026",
"172.20.18.93:1026",
"172.20.18.97:1025",
"172.20.18.99:1026"]

for zdb_server in zdb_servers:
    ip, port = zdb_server.split(':')
    zdb_client = ZDBCLIENT(ip, port)
    try:
        zdb_client.ping()
        zdb_client.nslist()
    except:
        print(zdb_server)