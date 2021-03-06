#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright 2015 Google Inc. All Rights Reserved.
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

"""Wrapper around PyICU.

Assumes PyICU is installed somewhere in sys.path.
"""

import codecs
import sys

import icu  # Debian/Ubuntu: apt-get install python-pyicu


def LoadTransliterationRules(path, transform_name):
  rules = codecs.open(path, 'r', 'utf-8').read()
  transliterator = icu.Transliterator.createFromRules(
      transform_name, rules, icu.UTransDirection.FORWARD)
  return transliterator


def TestRulesInteractively(path):
  """Helper function for testing transliteration rules interactively.

  This is intended to be used in the edit-compile-test cycle when developing ICU
  transliteration rules. Note: This reloads the rules after every input line
  (input is unbuffered). This is useful for interactive development, but should
  not be used for batch processing, where the rules should be loaded exactly
  once, before the main loop.

  Args:
    path: Path to file containing transliteration rules.

  """
  stdout = codecs.lookup('utf-8').streamwriter(sys.stdout)
  while True:
    line = sys.stdin.readline()
    if not line:
      break
    line = line.decode('utf-8')
    transliterator = LoadTransliterationRules(path, 'foo-bar')
    result = transliterator.transliterate(line)
    stdout.write(result)
    stdout.flush()
  return


if __name__ == '__main__':
  TestRulesInteractively(sys.argv[1])
