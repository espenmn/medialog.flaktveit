# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from plone import api
from plone.app.textfield.value import RichTextValue



@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'medialog.flaktveit:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


    all_items = context.portal_catalog(portal_type='EasyForm')


    #for item in all_items:
        #myitem = item.getObject()
        #import pdb; pdb.set_trace()
        #myitem.body_footer = RichTextValue('Mottatt:', 'text/html', 'text/x-html-safe')
        #import transaction; transaction.commit()




def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
