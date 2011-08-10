#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property


class HTMLHRElement(HTMLElement):
    align           = attr_property("align")
    noShade         = attr_property("noshade", bool)
    size            = attr_property("size")
    width           = attr_property("width")

