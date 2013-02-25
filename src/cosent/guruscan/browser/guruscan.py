import md5
from datetime import datetime
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plonesocial.network.browser.profile import ProfileView

from cosent.guruscan.interfaces import IGuruscanSettings


class GuruscanView(ProfileView):
    """An extended plonesocial profile view that embeds a Guruscan IFRAME"""

    index = ViewPageTemplateFile("guruscan.pt")

    def get_key(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        return settings.secret_key

    def get_client_name(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        return settings.client_name

    def get_dt(self):
        return datetime.now().strftime("%Y%m%d%H%M")

    def userHash(self):
        plaintext = "%s.%s.%s" % (self.viewer_id,
                                  self.get_dt(),
                                  self.get_key())
        return md5.new(plaintext).hexdigest()

    def get_url(self):
        url = "http://%s.guruscan.net" % self.get_client_name()
        url += "/guruscan/participant.htm"
        url += "?userName=%s" % self.viewer_id
        url += "&userHash=%s" % self.userHash()
        if self.userid != self.viewer_id:
            url += "&goTo=/guruscan/participant/searchparticipants.htm"
            url += "&participantUserId=%s" % self.userid
        return url
