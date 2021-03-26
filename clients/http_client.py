"""This module describes HttpClient class which used for sending http requests to a server. HttpClient reusing python
requests library. """
import requests


class HttpClient:
    """HttpClient provides getting response from a server."""

    @staticmethod
    def get(base_url, params=None, header=None, **kwargs):
        """This method sends GET request to a server
        :arg base_url (URL of a target server)
        :arg params (http request parameters, optional)
        :arg header (http request header, optional)
        :arg kwargs (any additional parameters of a request)
        :return http response object"""
        return requests.get(base_url, params=params, headers=header, **kwargs)

    @staticmethod
    def post(base_url, params=None, **kwargs):
        """This method sends POST request to a server
        :arg base_url (URL of a target server, optional)
        :arg params (http request header, optional)
        :arg kwargs (any additional parameters of a request)
        :return http response object"""
        return requests.post(base_url, params=params, **kwargs)

    @staticmethod
    def put(base_url, params=None, **kwargs):
        """This method sends PUT request to a server
        :arg base_url (URL of a target server, optional)
        :arg params (http request header, optional)
        :arg kwargs (any additional parameters of a request)
        :return http response object"""
        return requests.put(base_url, params=params, **kwargs)

    @staticmethod
    def delete(base_url, params=None, **kwargs):
        """This method sends DELETE request to a server
        :arg base_url (URL of a target server, optional)
        :arg params (http request header, optional)
        :arg kwargs (any additional parameters of a request)
        :return http response object"""
        return requests.delete(base_url, params=params, **kwargs)
