from zope.i18nmessageid import MessageFactory
_ = MessageFactory("cosent.guruscan")

activated = _(u"label_activated",
              default=u"Activate")

activated_desc = _(u"label_activated_desc",
                   default=u"Activate Guruscan integration for Plone")

developer_mode = _(u"label_developer_mode",
                   default=u"Developer mode")

developer_mode_desc = _(
    u"label_developer_mode_desc",
    default=u"Mark this box to use Guruscan in developer mode")

client_name = _(u"label_client_name",
                default=u"Client name")

client_name_desc = _(u"label_client_name_desc",
                     default=u"The client name as registered on Guruscan.")

secret_key = _(u"label_secret_key",
               default=u"Secret Key")

secret_key_desc = _(
    u"label_secret_key_desc",
    default=u"The secret md5 seed to authenticate with Guruscan.")

controlpanel_label = _(u"label_controlpanel",
                       default=u"Guruscan settings")
controlpanel_desc = _(
    u"help_controlpanel",
    default=u"Fill this form to configure Guruscan integration for Plone")
