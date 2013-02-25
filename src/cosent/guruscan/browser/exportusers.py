from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from datetime import datetime
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from cosent.guruscan.interfaces import IGuruscanSettings


class ExportUsers(BrowserView):

    index = ViewPageTemplateFile("exportusers.pt")

    def __call__(self):
        self.request.response.setHeader('Content-Type',
                                        'text/xml;;charset="utf-8"')
        return self.index()  # render template associated in ZCML

    def get_users(self):
        mtool = getToolByName(self.context, "portal_membership")
        for user in mtool.listMembers():
            username = user.getUserName()
            fullname = user.getProperty('fullname')
            if ' ' in fullname:
                firstname = fullname.split(' ')[0]
                lastname = ' '.join(fullname.split(' ')[1:])
            else:
                firstname = ''
                lastname = fullname
            portrait = user.getPersonalPortrait(username)
            yield dict(username=username,
                       firstname=firstname,
                       lastname=lastname,
                       email=user.getProperty('email'),
                       location=user.getProperty('location'),
                       picture=portrait.absolute_url())

    def get_client_name(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IGuruscanSettings)
        return settings.client_name

    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S%Z")
