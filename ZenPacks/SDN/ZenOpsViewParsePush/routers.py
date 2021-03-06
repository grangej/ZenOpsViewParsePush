import models.zovpaccount
import models.serialization
import models.zovpserver

from Products.ZenUtils.Ext import DirectRouter, DirectResponse

import json



def _dmdRoot(dmdContext):
    return dmdContext.getObjByPath("/zport/dmd/")

def _success(model_obj, msg=None):
    obj_data = json.loads(json.dumps(model_obj, cls=models.serialization.JSONEncoder))
    return DirectResponse.succeed(msg=msg, data=obj_data)

class ZOVPushRouter(DirectRouter):
    def __init__(self, context, request=None):
        super(ZOVPushRouter, self).__init__(context, request)

    def get_zovp_accounts(self):
        dmdRoot = _dmdRoot(self.context)
        accounts = getattr(dmdRoot, 'zovp_accounts', [])
        return _success(accounts)

    def get_zovp_account(self, zovPushKey):
        dmdRoot = _dmdRoot(self.context)
        accounts = getattr(dmdRoot, 'zovp_accounts', [])

        for accountDetail in accounts:
            if accountDetail.zovPushKey == zovPushKey:
                return _success(accountDetail)

        return DirectResponse.fail()

    def update_zovp_account(self, zovPushKey=None , triggers=None):

        if zovPushKey == None:
            return DirectResponse.fail("Missing zovPushKey")

        dmdRoot = _dmdRoot(self.context)
        accounts = getattr(dmdRoot, 'zovp_accounts', [])

        this_account_details = models.zovpaccount.ZOVPAccount(zovPushKey, triggers)

        index = 0
        newaccount = True

        for accountDetails in accounts:
            if accountDetails.zovPushKey == zovPushKey:
                newaccount = False
                break
            else:
                index += 1


        if newaccount == True:
            accounts.append(this_account_details)
        else:
            accounts[index] = this_account_details

        setattr(dmdRoot, 'zovp_accounts', accounts)
        return DirectResponse.succeed("Account updated")

    def remove_zovp_account(self, zovPushKey=None):


        if zovPushKey == None:
            return DirectResponse.fail("Missing zovPushKey")

        dmdRoot = _dmdRoot(self.context)
        accounts = getattr(dmdRoot, 'zovp_accounts', [])

        foundaccount = False

        this_account_details = models.zovpaccount.ZOVPAccount("None", "None")

        for accountDetails in accounts:
            if accountDetails.zovPushKey == zovPushKey:
                foundaccount = True
                this_account_details = accountDetails
                break

        if foundaccount == True:
            accounts.remove(this_account_details)
            setattr(dmdRoot, 'zovp_accounts', accounts)
            return DirectResponse.succeed()
        else:
            return DirectResponse.fail("Account not found")

    def update_zovp_server(self, zovpServerKey=None, zovpServerEndPointURL=None):

        if zovpServerKey == None or zovpServerEndPointURL == None:
            return DirectResponse.fail("Missing zovpServerKey or zovpServerEndPointURL")


        zovp_server_details = models.zovpserver.ZOVPServer(zovpServerKey, zovpServerEndPointURL)
        dmdRoot = _dmdRoot(self.context)

        setattr(dmdRoot, 'zovp_server', zovp_server_details)

        return DirectResponse.succeed("Server set or updated")
