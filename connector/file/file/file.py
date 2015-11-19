#   Copyright 2014-2015 PUNCH Cyber Analytics Group
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

"""
Overview
========

Retrieves and saves content to local disk

"""

import os

from stoq.scan import get_sha1
from stoq.plugins import StoqConnectorPlugin


class FileConnector(StoqConnectorPlugin):

    def __init__(self):
        super().__init__()

    def activate(self, stoq):
        self.stoq = stoq
        super().activate()

    # We are just going to be a wrapper for Stoq.get_file()
    def get_file(self, **kwargs):
        """
        Retrieve a file from disk

        :param **kwargs path: Path to the file to be retrieved
        :param **kwargs url: URL of file to be retrieved

        :returns: Content of file retrieved
        :rtype: bytes or None

        """

        valid_keys = ['path', 'url']
        for key in valid_keys:
            if key in kwargs:
                return self.stoq.get_file(source=kwargs[key])

        return None

    def save(self, payload, archive=False, **kwargs):
        """
        Save results to disk

        :param str payload: Content to be saved
        :param bool archive: Is this a file that is being archived?
        :param **kwargs sha1: SHA1 hash to use as a filename

        """

        if archive:
            if 'sha1' in kwargs:
                sha1 = kwargs['sha1']
            else:
                sha1 = get_sha1(payload)

            path = self.stoq.hashpath(sha1)
            self.stoq.write(payload, path=path, filename=sha1, binary=True)

            self.stoq.log.info("Saving file to disk: {}/{}".format(path, sha1))

        else:
            path = os.path.join(self.stoq.results_dir, self.parentname)
            self.stoq.write(path=path, payload=self.stoq.dumps(payload))

            self.stoq.log.info("Saving file to disk: {}".format(path))

        return True