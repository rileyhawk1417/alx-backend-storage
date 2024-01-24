#!/usr/bin/env python3

"""This module is built on the previous files methods for mongodb"""

from pymongo import MongoClient


def dump_nginx_req_data(nginx_data):
    """Dump nginx request data to the output"""
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{nginx_data.count_documents()} logs')
    print('Methods:')
    for method in http_methods:
        method_counter = len(list(nginx_data.find({'method': method})))
        print(f'\tmethod {method}: {method_counter}')
    stat_count = len(list(nginx_data.find(
        {'method': 'GET', 'path': '/status'})))
    print(f'{stat_count} status check')


def runMain():
    """Run MongoClient then pass on the collection to next function"""
    mongodb = MongoClient('mongodb://127.0.0.1:27017')
    dump_nginx_req_data(mongodb)


if __name__ == '__main__':
    runMain()
