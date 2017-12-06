from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings

from . import models
from .admin import ArticleTeaserInRowInlineAdmin


def get_template_file(plugin_nickname, flavor):
    choices = settings.ARTICLE_PLUGIN_SETTINGS[plugin_nickname]['choices']
    for choice in choices:
        if choice['flavor'] == flavor:
            return choice['template']


@plugin_pool.register_plugin
class ArticlePlugin(CMSPluginBase):
    model = models.ArticlePluginModel
    render_template = 'articles/plugins/article.html'
    cache = False


@plugin_pool.register_plugin
class SingleArticleTeaserPlugin(CMSPluginBase):
    model = models.SingleArticleTeaserPluginModel
    render_template = 'articles/plugins/single_article_teaser.html'
    cache = False


@plugin_pool.register_plugin
class RowOfArticleTeasersPlugin(CMSPluginBase):
    model = models.RowOfArticleTeasersPluginModel
    render_template = 'articles/plugins/row_of_article_teasers.html'
    inlines = (ArticleTeaserInRowInlineAdmin,)


@plugin_pool.register_plugin
class ArticleFeedPlugin(CMSPluginBase):
    model = models.ArticleFeedPluginModel
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('ArticleFeed', instance.flavor)


@plugin_pool.register_plugin
class EventFeedPlugin(CMSPluginBase):
    model = models.EventFeedPluginModel
    cache = False

    def get_render_template(self, context, instance, placeholder):
        return get_template_file('ArticleFeed', instance.flavor)
