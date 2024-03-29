# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName

from cosent.guruscan.config import PROJECTNAME


def uninstall(portal, reinstall=False):
    if not reinstall:
        profile = 'profile-%s:uninstall' % PROJECTNAME
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile(profile)
        return "Ran all uninstall steps."
