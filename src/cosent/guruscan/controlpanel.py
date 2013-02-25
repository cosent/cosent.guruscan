from plone.z3cform import layout

from plone.app.registry.browser import controlpanel as base
from cosent.guruscan import interfaces
from cosent.guruscan import i18n


class ControlPanelForm(base.RegistryEditForm):
    schema = interfaces.IGuruscanSettings
    label = i18n.controlpanel_label
    description = i18n.controlpanel_desc

ControlPanelView = layout.wrap_form(ControlPanelForm,
                                    base.ControlPanelFormWrapper)
