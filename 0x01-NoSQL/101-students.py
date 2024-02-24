#!/usr/bin/env python3
"""
Module to interact with mongo db
"""


def top_students(mongo_collection):
    """
    Print students in collection and sort
    by average score
    Args:
        mongo_collection: MongoDB Collection
    Return:
        MongoDB Collection
    """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score'
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
