# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.flaktveit


class MedialogFlaktveitLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.flaktveit)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.flaktveit:default')


MEDIALOG_FLAKTVEIT_FIXTURE = MedialogFlaktveitLayer()


MEDIALOG_FLAKTVEIT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_FLAKTVEIT_FIXTURE,),
    name='MedialogFlaktveitLayer:IntegrationTesting',
)


MEDIALOG_FLAKTVEIT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_FLAKTVEIT_FIXTURE,),
    name='MedialogFlaktveitLayer:FunctionalTesting',
)


MEDIALOG_FLAKTVEIT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_FLAKTVEIT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogFlaktveitLayer:AcceptanceTesting',
)
