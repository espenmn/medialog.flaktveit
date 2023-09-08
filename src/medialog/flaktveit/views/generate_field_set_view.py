# -*- coding: utf-8 -*-

from medialog.flaktveit import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class GenerateFieldSetView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('generate_field_set_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    def fieldsettitle(self):
        return self.context.fjeldset_name

    def fieldsetlabel(self):
        return self.fieldsettitle.lower().replace(" ", "_")

    def fieldtitle(self):
        return self.context.produktnavn

    def fieldname(self):
        return self.fieldtitle.lower().replace(" ", "_")

    def fieldtext(self):
        return 'Dummy text'

    def fieldsprice(self):
        return self.context.pris


    def fieldsizes(self):
        return self.context.st_rrelser


    def colors(self):
        return self.context.farge


 