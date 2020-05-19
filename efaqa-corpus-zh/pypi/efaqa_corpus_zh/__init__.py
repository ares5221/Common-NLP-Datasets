#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/efaqa-corpus-zh/app/sample.py
# Author: Hai Liang Wang
# Date: 2020-04-22:09:40:24
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 Chatopera Inc <https://chatopera.com>. All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2020-04-22:09:40:24"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

import json
import logging
import wget
import gzip

# Get ENV
CORPUS_URL = os.environ.get("EFA_CORPUS_URL", "https://github.com/chatopera/efaqa-corpus-zh/raw/master/data/efaqa-corpus-zh.utf8.gz")
CORPUS_DATA_PATH = os.path.join(curdir, "data", "efaqa-corpus-zh.utf8.gz")


try:
    from smart_open import smart_open
except ImportError:
    logging.debug("smart_open library not found; falling back to local-filesystem-only")

    def make_closing(base, **attrs):
        """
        Add support for `with Base(attrs) as fout:` to the base class if it's missing.
        The base class' `close()` method will be called on context exit, to always close the file properly.

        This is needed for gzip.GzipFile, bz2.BZ2File etc in older Pythons (<=2.6), which otherwise
        raise "AttributeError: GzipFile instance has no attribute '__exit__'".

        """
        if not hasattr(base, '__enter__'):
            attrs['__enter__'] = lambda self: self
        if not hasattr(base, '__exit__'):
            attrs['__exit__'] = lambda self, type, value, traceback: self.close()
        return type('Closing' + base.__name__, (base, object), attrs)


    def smart_open(fname, mode='rb'):
        _, ext = os.path.splitext(fname)
        if ext == '.bz2':
            from bz2 import BZ2File
            return make_closing(BZ2File)(fname, mode)
        if ext == '.gz':
            from gzip import GzipFile
            return make_closing(GzipFile)(fname, mode)
        return open(fname, mode)


def load(data_path=CORPUS_DATA_PATH):
    """
    加载数据集数据
    """
    if not os.path.exists(data_path):
        # download all pair data
        print("\n [efaqa-corpus-zh] downloading data %s ... \n" % CORPUS_URL)
        wget.download(CORPUS_URL, out = data_path)
    
    with smart_open(data_path) as f:
        for x in f:
            yield json.loads(x)