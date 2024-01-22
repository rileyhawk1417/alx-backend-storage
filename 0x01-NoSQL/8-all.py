#!/usr/bin/python3

"""This module just demonstrates how to list docs for mongodb"""


def list_all(mongo_collection):
    """Find a collection, if none return empty array"""
    if mongo_collection.find() is None:
        return []
    return mongo_collection.find()
