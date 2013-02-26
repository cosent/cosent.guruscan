import md5
from datetime import datetime
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from cosent.guruscan.interfaces import IGuruscanSettings


class GuruscanView(BrowserView):
    """Embeds a Guruscan IFRAME"""

    index = ViewPageTemplateFile("guruscan.pt")

    __call__ = index

    def userid(self):
        """The logged in user"""
        mtool = getToolByName(self.context, 'portal_membership')
        return mtool.getAuthenticatedMember().getId()

    def secret_key(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        return settings.secret_key

    def client_name(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        return settings.client_name

    def dt(self):
        return datetime.now().strftime("%Y%m%d%H%M")

    def userHash(self):
        plaintext = "%s.%s.%s" % (self.userid(),
                                  self.dt(),
                                  self.secret_key())
        return md5.new(plaintext).hexdigest()

    def get_url(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        if not settings.activated or not settings.client_name:
            return None

        url = "http://%s.guruscan.net" % self.client_name()
        url += "/guruscan/participant.htm"
        url += "?userName=%s" % self.userid()
        url += "&userHash=%s" % self.userHash()
        return url
