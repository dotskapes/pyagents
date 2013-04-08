#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseAdapter(object):
    """This serves as a base class for all Data Adapters in the system."""

    def __init__(self):
        super(BaseAdapter, self).__init__()

    def adapt(self, data):
        """Transforms input data into GeoJSON and return that GeoJSON buffer.

        :param data: A string containing the input data to be adapted
        :returns: A string containing the resulting GeoJSON.
        """
        return NotImplemented
