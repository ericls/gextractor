# -*- coding: utf-8 -*-
import requests
import six
from pyquery import PyQuery as Pq


class TopLevelExtractor(type):
    def __new__(mcs, name, bases, attrs):
        super_new = super(TopLevelExtractor, mcs).__new__
        attrs['cls_name'] = name
        parents = [b for b in bases if isinstance(b, TopLevelExtractor)]
        if not parents:
            return super_new(mcs, name, bases, attrs)

        meta = attrs.get('meta', dict())
        attrs['encoding'] = meta.get('encoding', 'UTF-8')
        attrs['absolute_link'] = meta.get('absolute_link', False)
        attrs['base_url'] = meta.get('base_url')
        attrs['_dom'] = ''

        return super_new(mcs, name, bases, attrs)


class BaseExtractor(six.with_metaclass(TopLevelExtractor)):

    def __init__(self, url=None, dom=None, *args, **kwargs):
        self.url = url
        if dom:
            self._dom = dom
        if (not url) and (not dom):
            raise ValueError('Url or dom must be provided')

    @property
    def dom(self):
        if not self._dom:
            d = requests.get(self.url)
            d.encoding = self.encoding
            __dom = Pq(d.text)
            if self.absolute_link:
                try:
                    __dom.make_links_absolute(base_url=self.base_url)
                except ValueError:
                    raise ValueError('When absolute_link is enabled, a base_url must be specified')
            self._dom = __dom
        return self._dom
