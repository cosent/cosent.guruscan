from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CosentGuruscan(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import cosent.guruscan
        xmlconfig.file('configure.zcml',
                       cosent.guruscan,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cosent.guruscan:default')

COSENT_GURUSCAN_FIXTURE = CosentGuruscan()
COSENT_GURUSCAN_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COSENT_GURUSCAN_FIXTURE, ),
                       name="CosentGuruscan:Integration")