from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
#from plone.app.testing import FunctionalTesting
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

FIXTURE = CosentGuruscan()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE, ),
    name="CosentGuruscan:Integration")
