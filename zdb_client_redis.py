import redis


class ZDBCLIENT:
    def __init__(self, ip, port=9900):
        self.zdb_server_ip = ip
        self.zdb_server_port = port
        self._connect_to_zdb_server()

    def _connect_to_zdb_server(self):
        self.zdb_client = redis.StrictRedis(host=self.zdb_server_ip, port=self.zdb_server_port, db=0)

    def execute_command(self, cmd):
        return self.zdb_client.execute_command(cmd)

    def send_receive(self, cmd):
        cmd = cmd.lower()
        response = self.zdb_client.execute_command(cmd)
        try:
            return response.decode()
        except:
            return response

    def ping(self):
        cmd = 'PING'
        return self.send_receive(cmd)

    def set(self, key, value):
        cmd = 'SET {} {}'.format(key, value)
        return self.send_receive(cmd)

    def get(self, key):
        cmd = 'GET {}'.format(key)
        return self.send_receive(cmd)

    def delete(self, key):
        cmd = 'DEL {}'.format(key)
        return self.send_receive(cmd)

    def stop(self):
        cmd = 'STOP'
        return self.send_receive(cmd)

    def exists(self, key):
        cmd = 'EXISTS {}'.format(key)
        return self.send_receive(cmd)

    def check(self, key):
        cmd = 'CHECK {}'.format(key)
        return self.send_receive(cmd)

    def info(self):
        cmd = 'INFO'
        return self.send_receive(cmd)

    def nsnew(self, namespace):
        cmd = 'NSNEW {}'.format(namespace)
        return self.send_receive(cmd)

    def nsdel(self, namespace):
        cmd = 'NSDEL {}'.format(namespace)
        return self.send_receive(cmd)

    def nsinfo(self, namespace):
        cmd = 'NSINFO {}'.format(namespace)
        return self.send_receive(cmd)

    def nslist(self):
        cmd = 'NSLIST'
        return self.send_receive(cmd)

    def nsset(self, namespace, property, value):
        if property not in ['maxsize', 'password', 'public']:
            return " [-] property should be in ['maxsize', 'password', 'public'] "

        cmd = 'NSSET {} {} {} '.format(namespace, property, value)
        return self.send_receive(cmd)

    def select(self, namespace, password=''):
        cmd = 'SELECT {} {}'.format(namespace, password)
        return self.send_receive(cmd)

    def dbsize(self):
        cmd = 'DBSIZE'
        return self.send_receive(cmd)

    def time(self):
        cmd = 'TIME'
        return self.send_receive(cmd)

    def auth(self, password):
        cmd = 'AUTH {}'.format(password)
        return self.send_receive(cmd)

    def scan(self, key=''):
        cmd = 'SCAN {}'.format(key)
        return self.send_receive(cmd)

    def rscan(self, key=''):
        cmd = 'RSCAN {}'.format(key)
        return self.send_receive(cmd)
