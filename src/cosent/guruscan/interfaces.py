from zope.interface import Interface
from zope import schema

from cosent.guruscan import i18n


class IGuruscanLayer(Interface):
    """Request marker installed via browserlayer.xml.
    """


class IGuruscanSettings(Interface):
    """Settings to access Guruscan web service. """

    activated = schema.Bool(
        title=i18n.activated,
        description=i18n.activated_desc,
    )

    developer_mode = schema.Bool(
        title=i18n.developer_mode,
        description=i18n.developer_mode_desc,
    )

    client_name = schema.ASCIILine(
        title=i18n.client_name,
        description=i18n.client_name_desc,
    )

    secret_key = schema.TextLine(
        title=i18n.secret_key,
        description=i18n.secret_key_desc,
    )
