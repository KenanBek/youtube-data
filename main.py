# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import iso3166
from youtube import YouTubeAPI


def enc(text):
    """
    Return correctly encoded string.
    
    :param text: 
    :return: 
    """
    if isinstance(text, str):
        return unicode(text, 'utf-8')  # TODO: fix in Python 3
    elif isinstance(text, unicode):
        return text.encode('utf-8')
    else:
        raise Exception("Unsupported encode format.")


def demo_categories(api):
    # List categories by country

    countries = [
        iso3166.countries.get('us'),
        iso3166.countries.get('de'),
    ]

    # We can use simple list instead of iso3166, but with ISO module we have all countries with details
    # If you want to uncomment this then you need to modify code bellow to access dict items:
    # so, instead of country.alpha2 put country['alpha2']
    #
    # countries = [
    #     {'name': 'United States', 'alpha2': 'US'},
    #     {'name': 'Germany', 'alpha2': 'DE'},
    # ]

    for country in countries:
        categories = api.video_categories_list(
            part='snippet',
            regionCode=country.alpha2
        )

        print("\n\tCategories for {}".format(country.name))
        for category in categories['items']:
            print(category['snippet']['title'])


def demo_channels(api):
    channels = [
        'selgomez',
        'JustinBieberVEVO',
        'puma',
    ]

    for channel in channels:
        channel_info = api.channels_list(
            part='snippet,contentDetails,statistics',
            forUsername=channel,
        )

        channel_title = enc(channel_info['items'][0]['snippet']['title'])
        channel_desc = enc(channel_info['items'][0]['snippet']['localized']['description'])

        print("Title: {}".format(channel_title))
        print("Desc: {}".format(channel_desc))
        print("\tVideos: {}".format(channel_info['items'][0]['statistics']['videoCount']))
        print("\tViews: {}".format(channel_info['items'][0]['statistics']['viewCount']))
        print("\tComments: {}".format(channel_info['items'][0]['statistics']['commentCount']))
        print('')


def demo_channel_videos(api):
    channels = [
        'selgomez',
        'JustinBieberVEVO',
        'puma',
    ]

    for channel in channels:
        channel_info = api.channels_list(
            part='snippet,contentDetails,statistics',
            forUsername=channel,
        )
        channel_id = channel_info['items'][0]['id']
        channel_title = enc(channel_info['items'][0]['snippet']['title'])

        print("Title: {}".format(channel_title))
        print("Views: {}".format(channel_info['items'][0]['statistics']['viewCount']))

        channel_videos = api.search_list(
            channelId=channel_id,
            part='snippet',
            order='date',
        )

        print("Videos:")
        for channel_video in channel_videos['items']:
            video_title = enc(channel_video['snippet']['title'])
            video_desc = enc(channel_video['snippet']['description'])
            print(video_title)
            print(video_desc)
        print('')


def demo_trending_videos(api):
    popular_videos = api.videos_list(
        part='snippet',
        chart='mostPopular',
        regionCode=iso3166.countries.get('de').alpha2,
    )

    for popular_video in popular_videos['items']:
        video_title = enc(popular_video['snippet']['title'])
        print(video_title)


def demo_search(api, query):
    popular_videos = api.search_list(
        part='snippet',
        q=query,
        order='rating',
        regionCode=iso3166.countries.get('de').alpha2,
    )

    for popular_video in popular_videos['items']:
        video_title = enc(popular_video['snippet']['title'])
        print(video_title)


def demo(command):
    api = YouTubeAPI('api-key')  # see https://developers.google.com/api-client-library/python/guide/aaa_apikeys
    if command.categories:
        demo_categories(api)
    if command.channels:
        demo_channels(api)
    if command.channel_videos:
        demo_channel_videos(api)
    if command.trending_videos:
        demo_trending_videos(api)
    if command.query:
        demo_search(api, command.query)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_subparsers = argument_parser.add_subparsers(help="use following sub-commands")

    command_demo = argument_subparsers.add_parser("demo", help='demo commands')
    command_demo.add_argument(
        '-c',
        '--categories',
        dest="categories",
        action="store_true",
        help="show categories in the given regions"
    )
    command_demo.add_argument(
        '-ch',
        '--channels',
        dest="channels",
        action="store_true",
        help="show channel basic statistics"
    )
    command_demo.add_argument(
        '-cv',
        '--ch-videos',
        dest="channel_videos",
        action="store_true",
        help="show channel's most recent videos"
    )
    command_demo.add_argument(
        '-tv',
        '--tr-videos',
        dest="trending_videos",
        action="store_true",
        help="show trending videos in germany"
    )
    command_demo.add_argument(
        '-q',
        '--query',
        dest="query",
        help="search and order by rating (in DE)"
    )
    command_demo.set_defaults(func=demo)

    args = argument_parser.parse_args()
    args.func(args)
