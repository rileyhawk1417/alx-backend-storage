#!/usr/bin/python3

"""This module just demonstrates how to list docs for mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Find a collection, if none return empty array"""
    return mongo_collection.insertOne(kwargs)
