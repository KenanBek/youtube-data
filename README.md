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

Example wrapper over search function of API:

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

Output:

        Categories for Germany
    Film & Animation
    Autos & Vehicles
    Music
    Pets & Animals
    Sports
    ...

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

Output:

    Title: Selena Gomez
    Desc: Official Selena Gomez YouTube Channel!
            Videos: 169
            Views: 346824466
            Comments: 1632729

    Title: JustinBieberVEVO
    Desc: Justin Bieber on Vevo - Official Music Videos, Live Performances, Interviews and more...
            Videos: 123
            Views: 16994139768
            Comments: 471563
    ...

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

Output:

    ...
    Title: PUMA
    Views: 178299677
    Videos:
    PUMA x NATUREL | Fresh and Futuristic
    Graphic artist Naturel's designs go far beyond the expected. His approach: a fusion of symbolism-heavy illustrations and inspiration from ne
    o-cubism, sport, fashion, and music. In his second...
    Tsugi Jun featuring The Weeknd
    Meet the next generation of Tsugi. The Tsugi Jun arrives with a sleek new profile and bold branding. It's for the makers of this world - tho
    se who can't help but envision, create, and hustle....
    Tsugi Netfit featuring The Weeknd
    The Tsugi NETFIT v2 is ready for whatever's next and whatever comes its way. Its progressive design is enhanced with NETFIT, a unique lacing
     system for customizable fit and style. Lace up....
    PUMA SOUTH AFRICA | #RunTheStreets X Anatii
    No such thing as losing. Only hustle. #ANATII Music by: Theevs Music - Last Night (Fight Night). OG Voice: Anatii Directed by: Abi Green.
    PUMA x SHANTELL MARTIN | Streetwear Redrawn
    Shantell Martin has created a language of lines. Part whimsical, part autobiographical, her inky world of characters and messages bridges th
    e gap between fine art, performance art, and everyday...
    ...

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

Output:

    Das neue Galaxy S9 | S9+
    Be┼ƒikta┼ƒ 3-1 Fenerbah├ºe Ma├º ├ûzeti 25 ┼₧ubat 2018
    Ich habe MiiMii getroffen | Leon Mach├¿re
    Huggle - die kuschelige Funktionskleidung - Das Ding des Jahres
    YOU LAUGH, YOU DIE

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

Output:

    Python for beginners - #2. Operators and Variables
    Learn Python Programming Tutorial Online Training by Durga Sir On 05-02-2018
    Learn Python Programming Tutorial Online Training by Durga Sir On 15-02-2018
    5th Grader Python Coding
    Extraire Des Sous Chaines  De Caracteres En Langage Python
