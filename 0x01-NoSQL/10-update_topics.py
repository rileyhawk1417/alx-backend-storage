#!/usr/bin/python3

"""This module just demonstrates how to update docs for mongodb"""


def update_topics(mongo_collection, name, topics):
    """Find a collection then update it"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
