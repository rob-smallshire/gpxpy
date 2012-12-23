# -*- coding: utf-8 -*-

# Copyright 2011 Tomo Krajina
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .gpx import GPXException

def parse(xml_or_file, parser='lxml'):
    """ Parse xml (string) or file object. This is just an wrapper for GPXParser.parse() function """

    from . import gpx as mod_gpx
    from . import parser as mod_parser

    parser = mod_parser.GPXParser(xml_or_file, parser=parser)

    gpx = parser.parse()

    if not parser.is_valid():
        NUM_EXCERPT_CHARS = 100
        try:
            xml_or_file.seek(0)
            excerpt = xml_or_file.read(NUM_EXCERPT_CHARS)
        except AttributeError:
            excerpt = xml_or_file[:NUM_EXCERPT_CHARS]
        raise mod_gpx.GPXException('Error parsing {0}: {1}'.format(excerpt, parser.get_error()))

    return gpx

