import Globals
from zope.interface import implements
from Products.ZenUtils.guid.guid import GUIDManager
from Products.ZenModel.interfaces import IAction
from Products.ZenModel.actions import _signalToContextDict, ActionExecutionException
from Products.ZenModel.NotificationSubscription import NotificationEventContextWrapper
from Products.Zuul.form.interfaces import IFormBuilder

import urllib
import urllib2
import httplib
import json

class IActionBase(object):

    def configure(self, options):
        self.options = options


class sendZOP(IActionBase):
    implements(IAction)

    id = 'sendZOP'
    name = 'Send Alert to Zen Ops View 2'
