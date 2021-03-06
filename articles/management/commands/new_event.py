from django.conf import settings
import djclick as click
from e_time.parser import parse_single_event
import pytz

from articles.models import Article


@click.command()
@click.argument('title')
@click.argument('when')
@click.argument('location')
@click.argument('tags')
@click.argument('url')
@click.argument('url_title')
@click.option('--subtitle')
def command(title, when, location, tags, url, url_title, subtitle):
    local_tz = pytz.timezone(settings.TIME_ZONE)
    tags = [tag.strip() for tag in tags.split(',')]

    starts_at, ends_at = parse_single_event(when, local_tz=local_tz)
    article_args = dict(
        flavor=Article.EVENT,
        visible=True,
        title=title,
        starts_at=starts_at,
        ends_at=ends_at,
        location=location,
    )

    if subtitle:
        article_args['subtitle'] = subtitle

    article = Article(**article_args)
    article.full_clean()
    article.save()

    for tag in tags:
        article.tags.add(tag)
    article.articlerelatedurl_set.create(
        url=url, title=url_title
    )
