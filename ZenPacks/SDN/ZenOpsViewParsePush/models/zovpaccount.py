import json
import serialization

class ZOVPAccount(object):
    def __init__(self, zovPushKey, triggerIDs):
        self.zovPushKey = zovPushKey
        self.triggerIDs = triggerIDs

    def __json__(self):
        return json.dumps(self, cls=serialization.JSONEncoder)
