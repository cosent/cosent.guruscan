# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import getMultiAdapter
from zope.component import getUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import logout
from plone.app.testing import setRoles
from plone.registry.interfaces import IRegistry

from cosent.guruscan.config import PROJECTNAME
from cosent.guruscan.interfaces import IGuruscanSettings
from cosent.guruscan.testing import INTEGRATION_TESTING

BASE_REGISTRY = 'cosent.guruscan.interfaces.IGuruscanSettings.%s'


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.controlpanel = self.portal['portal_controlpanel']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_controlpanel_has_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='guruscan-controlpanel')
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                          '@@guruscan-controlpanel')

    def test_controlpanel_installed(self):
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertTrue('cosent.guruscan.settings' in actions,
                        'control panel was not installed')

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertTrue('cosent.guruscan.settings' not in actions,
                        'control panel was not removed')

    def test_controlpanel_required_fields(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='guruscan-controlpanel')

        schema = view.form.schema
        self.assertEqual(len(schema.names()), 4)

        self.assertIn('secret_key', schema)
        self.assertIn('activated', schema)
        self.assertIn('client_name', schema)
        self.assertIn('developer_mode', schema)

        self.assertTrue(schema['secret_key'].required)
        self.assertTrue(schema['activated'].required)
        self.assertTrue(schema['client_name'].required)
        self.assertTrue(schema['developer_mode'].required)


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IGuruscanSettings)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_activated_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'activated'))
        self.assertEqual(self.settings.activated, None)

    def test_developer_mode_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'developer_mode'))
        self.assertEqual(self.settings.developer_mode, None)

    def test_client_name_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'client_name'))
        self.assertEqual(self.settings.client_name, None)

    def test_secret_key_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'secret_key'))
        self.assertEqual(self.settings.secret_key, None)

    def test_records_removed(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])

        records = [
            BASE_REGISTRY % 'activated',
            BASE_REGISTRY % 'developer_mode',
            BASE_REGISTRY % 'client_name',
            BASE_REGISTRY % 'secret_key',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
