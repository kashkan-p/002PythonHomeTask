import requests


class HttpClient:
    """HttpClient provides getting response from a server."""

    @staticmethod
    def get(base_url, params=None, header=None, **kwargs):
        return requests.get(base_url, params=params, headers=header, **kwargs)

    @staticmethod
    def post(base_url, params=None, **kwargs):
        return requests.post(base_url, params=params, **kwargs)

    @staticmethod
    def put(base_url, params=None, **kwargs):
        return requests.put(base_url, params=params, **kwargs)

    @staticmethod
    def delete(base_url, params=None, **kwargs):
        return requests.delete(base_url, params=params, **kwargs)
