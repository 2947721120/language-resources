# zu/BUILD
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
# Author: mjansche@google.com (Martin Jansche)

package(default_visibility = ["//visibility:public"])

sh_test(
    name = "ipa_phonemes_are_uniquely_decodable",
    timeout = "short",
    srcs = ["//utils:eval.sh"],
    args = [
        """
        cut -f 2 $(location phonemes.txt) |
        $(location //utils:uniquely_decodable)
        """,
    ],
    data = [
        "phonemes.txt",
        "//utils:uniquely_decodable",
    ],
)

sh_test(
    name = "pronunciation_rules_match_nchlt_dictionary",
    timeout = "short",
    srcs = ["//utils:eval.sh"],
    args = [
        """
        $(location //utils:evaluate_pronunciation_rules) \
          $(location //third_party/cldr:zu-zu_FONIPA.txt) \
          $(location phonemes.txt) \
          $(location //third_party/nchlt_inlang:release/dictionaries/nchlt_zul.dict)
        """,
    ],
    data = [
        "phonemes.txt",
        "//third_party/cldr:zu-zu_FONIPA.txt",
        "//third_party/nchlt_inlang:release/dictionaries/nchlt_zul.dict",
        "//utils:evaluate_pronunciation_rules",
    ],
    tags = ["manual"],  # Test is not hermetic due to dependency on PyICU.
)
