from googleapiclient.discovery import build


class YouTubeAPI(object):
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    def __init__(self, api_key):
        self.build_obj = build(YouTubeAPI.API_SERVICE_NAME, YouTubeAPI.API_VERSION, developerKey=api_key)
