# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes

# TODO(kt):  Not implemented yet
class FlumeSyslogRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:syslog}-relation-joined')
    def joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.connected')

    @hook('{requires:syslog}-relation-changed')
    def changed(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.available')

    @hook('{requires:syslog}-relation-{departed,broken}')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.connected')
        conv.remove_state('{relation_name}.available')

    def get_flume_ip(self):
        conv = self.conversation()
        conv.get_remote('private-address')

    def get_flume_port(self):
        conv = self.conversation()
        conv.get_remote('port')
