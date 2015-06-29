import json
import serialization

class ZOVPServer(object):
    def __init__(self, zovpServerKey, zovpServerEndPointURL):
        self.zovpServerKey = zovpServerKey
        self.zovpServerEndPointURL = zovpServerEndPointURL

    def __json__(self):
        return json.dumps(self, cls=serialization.JSONEncoder)