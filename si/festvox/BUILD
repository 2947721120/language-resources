# si/festvox/BUILD
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
# Copyright 2016 Google, Inc.
# Author: pasindu@google.com (Pasindu De Silva)

package(default_visibility = ["//visibility:public"])

"""
Usage
    bazel test si/festvox:valid_phonology_file

"""
sh_test(
    name = "valid_phonology_file",
    timeout = "short",
    srcs = ["//utils:eval.sh"],
    args = [
        """
        $(location //utils:phonology_json_validator) $(location ipa_phonology.json)
        """,
    ],
    data = [
        "ipa_phonology.json",
        "//utils:phonology_json_validator",
    ],
)
