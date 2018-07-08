# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from googleapiclient.discovery import build


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs


class YouTubeAPI(object):
    """
    Wrapper class around Google's YouTube API for Python.
    
    For more information about YouTube Data APIv3 visit:
    https://developers.google.com/youtube/v3/
    
    This code also available as a separate library:
    https://github.com/KenanBek/python-youtube-apiv3
    
    """
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    def __init__(self, api_key):
        self.service = build(YouTubeAPI.API_SERVICE_NAME, YouTubeAPI.API_VERSION, developerKey=api_key)

    def channels_list(self, **kwargs):
        """
        Returns a collection of zero or more channel resources that match the request criteria.
        
        More details: https://developers.google.com/youtube/v3/docs/channels/list
        
        :param kwargs: 
        :return: 
        """
        kwargs = remove_empty_kwargs(**kwargs)

        results = self.service.channels().list(
            **kwargs
        ).execute()

        return results

    def video_categories_list(self, **kwargs):
        """
        Returns a list of categories that can be associated with YouTube videos.
        
        More details: https://developers.google.com/youtube/v3/docs/videoCategories/list
        
        :param kwargs: 
        :return: 
        """
        kwargs = remove_empty_kwargs(**kwargs)

        results = self.service.videoCategories().list(
            **kwargs
        ).execute()

        return results

    def videos_list(self, **kwargs):
        """
        Returns a list of videos that match the API request parameters.

        More details: https://developers.google.com/youtube/v3/docs/videos/list

        :param kwargs: 
        :return: 
        """
        kwargs = remove_empty_kwargs(**kwargs)

        results = self.service.videos().list(
            **kwargs
        ).execute()

        return results

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
