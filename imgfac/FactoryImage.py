# encoding: utf-8

#   Copyright 2012 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from props import prop
import uuid

class FactoryImage(object):
    """ TODO: Docstring for FactoryImage  """

    identifier = prop("_identifier")
    data = prop("_data")
    icicle = prop("_icicle")

    def __init__(self, template):
        """ TODO: Fill me in
        
        @param template TODO
        """
        super(FactoryImage, self).init()
        self.identifier = uuid.uuid4()
        self.data = None
        self.icicle = None