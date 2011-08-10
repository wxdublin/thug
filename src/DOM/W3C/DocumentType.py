#!/usr/bin/env python
from __future__ import with_statement

import sys, re, string

from DOMException import DOMException
from Node import Node
from Events import *


class DocumentType(Node):
    RE_DOCTYPE = re.compile("^DOCTYPE (\w+)", re.M + re.S)
    
    def __init__(self, doc, tag):
        Node.__init__(self, doc)
        
        self.parse(tag)
        
    def parse(self, text):
        m = self.RE_DOCTYPE.match(text)
        
        self._name = m.group(1) if m else ""
        
    @property
    def name(self):
        return self._name

    @property
    def nodeName(self):
        return self._name
    
    @property
    def entities(self):
        raise NotImplementedError()
    
    @property
    def notations(self):
        raise NotImplementedError()

    # Modified in DOM Level 2
    @property
    def ownerDocument(self):
        # FIXME
        return None

    # Introduced in DOM Level 2
    @property
    def publicId(self):
        pass

    # Introduced in DOM Level 2
    @property
    def systemId(self):
        pass

    # Introduced in DOM Level 2
    @property
    def internalSubset(self):
        pass

