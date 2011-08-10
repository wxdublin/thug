#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property


class HTMLStyleElement(HTMLElement):
    disabled        = False
    media           = attr_property("media")
    type            = attr_property("type")
