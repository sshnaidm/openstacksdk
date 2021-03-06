# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack import resource


class Type(resource.Resource):
    resource_key = "volume_type"
    resources_key = "volume_types"
    base_path = "/types"

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_commit = True

    _query_mapping = resource.QueryParameters("is_public")

    # Properties
    #: A ID representing this type.
    id = resource.Body("id")
    #: Name of the type.
    name = resource.Body("name")
    #: Description of the type.
    description = resource.Body("description")
    #: A dict of extra specifications. "capabilities" is a usual key.
    extra_specs = resource.Body("extra_specs", type=dict)
    #: a private volume-type. *Type: bool*
    is_public = resource.Body('os-volume-type-access:is_public', type=bool)


class TypeEncryption(resource.Resource):
    resource_key = "encryption"
    resources_key = "encryption"
    base_path = "/types/%(volume_type_id)s/encryption"

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_list = False
    allow_commit = True

    # Properties
    #: A ID representing this type.
    encryption_id = resource.Body("encryption_id", alternate_id=True)
    #: The ID of the Volume Type.
    volume_type_id = resource.URI("volume_type_id")
    #: The Size of encryption key.
    key_size = resource.Body("key_size")
    #: The class that provides encryption support.
    provider = resource.Body("provider")
    #: Notional service where encryption is performed.
    control_location = resource.Body("control_location")
    #: The encryption algorithm or mode.
    cipher = resource.Body("cipher")
    #: The resource is deleted or not.
    deleted = resource.Body("deleted")
    #: The date and time when the resource was created.
    created_at = resource.Body("created_at")
    #: The date and time when the resource was updated.
    updated_at = resource.Body("updated_at")
    #: The date and time when the resource was deleted.
    deleted_at = resource.Body("deleted_at")
