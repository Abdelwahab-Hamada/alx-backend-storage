#!/usr/bin/env python3
""":
mongo_collection will be the pymongo collection object
Returns the new _id
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    return mongo_collection.insert(kwargs)
