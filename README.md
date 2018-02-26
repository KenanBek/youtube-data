# YouTube Data

Example application to demonstrate some YouTube Data APIv3 features.

### Setup

    git clone https://github.com/KenanBek/python-data
    cd python-data
    virtualenv env
    source env/bin/activate (or .\env\Scripts\activate)
    pip install -r requirements.txt

### Usage

To see all demo commands use

    python main.py demo -h

All communication goes through (python-youtube-apiv3)[https://github.com/KenanBek/python-youtube-apiv3].
It is basic wrapper around Google's API. Here we use it just by creating new instance of the API with API key.

    api = YouTubeAPI('API-KEY')

See https://developers.google.com/api-client-library/python/guide/aaa_apikeys to get your API key.

Example of search function:

    def search_list(self, **kwargs):
        """
        Returns a collection of search results that match the query parameters specified in the API request. 
        By default, a search result set identifies matching video, channel, and playlist resources, 
        but you can also configure queries to only retrieve a specific type of resource.

        More details: https://developers.google.com/youtube/v3/docs/search/list

        :param kwargs: 
        :return: 
        """
        kwargs = remove_empty_kwargs(**kwargs)

        results = self.service.search().list(
            **kwargs
        ).execute()

        return results

### Demo Commands

#### List YouTube categories for given country list

    python main.py demo -c

Code:

    countries = [
        iso3166.countries.get('us'),
        iso3166.countries.get('de'),
    ]
    for country in countries:
        categories = api.video_categories_list(
            part='snippet',
            regionCode=country.alpha2
        )
        print("\n\tCategories for {}".format(country.name))
        for category in categories['items']:
            print(category['snippet']['title'])

#### Show basic info and stats for given channels

    python main.py demo -ch

Code:

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

#### Show most recent videos of given channels

    python main.py demo -cv

Code:

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

#### Show most popular videos in the Germany

    python main.py demo -tv

Code:

    popular_videos = api.videos_list(
        part='snippet',
        chart='mostPopular',
        regionCode=iso3166.countries.get('de').alpha2,
    )

    for popular_video in popular_videos['items']:
        video_title = enc(popular_video['snippet']['title'])
        print(video_title)

#### Search for given term and order results by rating in the Germany

    python main.py demo -q python

Code:

    popular_videos = api.search_list(
        part='snippet',
        q=query,
        order='rating',
        regionCode=iso3166.countries.get('de').alpha2,
    )

    for popular_video in popular_videos['items']:
        video_title = enc(popular_video['snippet']['title'])
        print(video_title)
