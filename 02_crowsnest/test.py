#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'

consonant_words = [
    'brigantine', 'clipper', 'Dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'Ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'Quay',
    'regatta', 'Submarine', 'tanker', 'vessel', 'whale', 'Xebec', 'yatch',
    'zebrafish'
]

vowel_words = ['aviso', 'Eel', 'iceberg', 'Octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_vowel():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        article = 'an' if word[0].islower() else 'An'
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format(article, word)


# --------------------------------------------------
def test_consonant():
    """Octopus -> An Octopus"""

    for word in consonant_words:
        article = 'a' if word[0].islower() else 'A'
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format(article, word)
