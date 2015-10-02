# -*- coding: utf-8 -*-
from pyquery import PyQuery as Pq
import re

class PQField(object):

    def __init__(self, selector, format='text'):
        """
        :param selector: css selector, refer to pyquery
        :param format: 'text' - calls text() of selected element(s)
                       'element' - returns the PyQuery object of selected element(s)
                       'html' - calls html() of selected element(s)
        """
        self.selector = selector
        self._type = format

    def __get__(self, instance, owner):
        _selected = instance.dom(self.selector)
        if self._type == 'text':
            return _selected.text()
        elif self._type == 'element':
            return _selected
        elif self._type == 'html':
            return _selected.html()


class PQListField(PQField):

    def __get__(self, instance, owner):
        _selected = instance.dom(self.selector)
        l = []
        for item in _selected.items():
            if self._type == 'text':
                l.append(item.text())
            elif self._type == 'element':
                l.append(item)
            elif self._type == 'html':
                l.append(item.html())
        return l


class RegField(object):

    def __init__(self, regex):
        """
        :param regex: regex pattern that is used in `finditer` to match from the HTML code of the page
        """
        self.regex = re.compile(regex)
        self._type = format

    def __get__(self, instance, owenr):
        if isinstance(instance.dom, Pq):
            return self.regex.finditer(instance.dom.html())
        else: # TODO: Other conditions, may be?
            return self.regex.finditer(instance)


# TODO: implement custom `parser` to fields
