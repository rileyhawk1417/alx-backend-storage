#!/usr/bin/env python3

"""This module just demonstrates how to list docs for mongodb"""


def list_all(mongo_collection):
    """Find a collection, if none return empty array"""
    return [docs for docs in mongo_collection.find()]
