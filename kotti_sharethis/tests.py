from pyramid.threadlocal import get_current_registry
from kotti.tests import UnitTestBase

from kotti_sharethis import (render_widget_assets,
                             render_sharethis_widget)


def settings():
    return get_current_registry().settings


class TestAnalyticsWidget(UnitTestBase):
    def test_render_widget_assets(self):
        self.assert_(render_widget_assets(None, None).startswith('<!-- ShareThis'))

    def test_render_sharethis_widget(self):
        self.assert_(render_sharethis_widget(None, None).startwith('<span '))

    # def test_render_settings(self):
    #     html = render_sharethis_widget(None, None)
    #     self.assert_(u"_gaq.push(['_setAccount', 'UA-1234567-8']);" not in html)
    #     settings()['kms_sharethis.tracking_id'] = 'UA-1234567-8'
    #     html = render_sharethis_widget(None, None)
    #     self.assert_(u"_gaq.push(['_setAccount', 'UA-1234567-8']);" in html)
