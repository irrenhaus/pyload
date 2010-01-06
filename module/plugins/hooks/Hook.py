# -*- coding: utf-8 -*-

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.
    
    @author: mkaay
    @interface-version: 0.1
"""

import logging

class Hook():
    def __init__(self, core):
        self.logger = logging.getLogger("log")
        props = {}
        props['name'] = "Hook"
        props['version'] = "0.1"
        props['description'] = """interface for hook"""
        props['author_name'] = ("mkaay")
        props['author_mail'] = ("mkaay@mkaay.de")
        self.props = props
        self.core = core
    
    def downloadStarts(self, pyfile):
        pass
    
    def downloadFinished(self, pyfile):
        pass
    
    def packageFinished(self, pypack):
        """
            not implemented!
        """
        pass
    
    def beforeReconnecting(self, ip):
        pass
    
    def afterReconnecting(self, ip):
        pass