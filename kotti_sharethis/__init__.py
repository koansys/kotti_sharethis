from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderBelowContent
from kotti.views.slots import RenderAboveContent
from kotti.views.slots import RenderInHead

SHARETHIS_WIDGET_DEFAULTS = {
    'sharethis': True,
    'facebook': True,
    'twitter': True,
    'linkedin': True,
    'gplus': True,
    'pinterest': False,
    'email': True,
    }


def render_widget_assets(context, request, name=''):
    return render('templates/widget_assests.pt', request)


def render_sharethis_widget(context, request, name=''):
    prefix = 'kotti_sharethis.sharethis_widget.'
    if name:
        prefix += name + '.'
    variables = SHARETHIS_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/sharethis_widget.pt', variables, request)


def include_sharethis_widget(config, where=RenderBelowContent):  # pragma: no cover
    config.add_static_view(name='static', path='kotti_jtweetanywhere:static')
    register(RenderInHead, None, render_widget_assets)
    register(where, None, render_sharethis_widget)


def include_sharethis_widget_above(config):  # pragma: no cover
    include_sharethis_widget(config, RenderAboveContent)
