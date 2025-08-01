# Copyright 2025 Google LLC
#
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
#
# SPDX-License-Identifier: Apache-2.0

"""Stub type annotations for native Handlebars."""

from collections.abc import Callable
from typing import Any

def html_escape(text: str) -> str: ...
def no_escape(text: str) -> str: ...

class HandlebarrzHelperOptions:
    """Stub type annotations for native Handlebars helper options."""

    def __init__(self) -> None: ...
    def context_json(self) -> str: ...
    def hash_value_json(self, key: str) -> str: ...
    def template(self) -> str: ...
    def inverse(self) -> str: ...

class HandlebarrzTemplate:
    """Stub type annotations for native Handlebars."""

    def __init__(self) -> None: ...

    # Strict mode.
    def get_strict_mode(self) -> bool: ...
    def set_strict_mode(self, enabled: bool) -> None: ...

    # Dev mode.
    def get_dev_mode(self) -> bool: ...
    def set_dev_mode(self, enabled: bool) -> None: ...

    # Escape function.
    def set_escape_fn(self, escape_fn: str) -> None: ...

    # Template registration.
    def register_template(self, name: str, template_string: str) -> None: ...
    def register_partial(self, name: str, template_string: str) -> None: ...
    def register_template_file(self, name: str, file_path_str: str) -> None: ...
    def register_templates_directory(self, dir_path_str: str, extension: str) -> None: ...

    # Helper registration.
    def register_helper(self, name: str, helper_fn: Callable[[str], str]) -> None: ...

    # Template management.
    def has_template(self, name: str) -> bool: ...
    def unregister_template(self, name: str) -> None: ...

    # Rendering.
    def render(self, name: str, data_json: str) -> str: ...
    def render_template(self, template_str: str, data_json: str) -> str: ...

    # Extra helper registration.
    def register_extra_helpers(self) -> None: ...
