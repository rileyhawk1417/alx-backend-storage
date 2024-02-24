#!/usr/bin/env python3

"""
Module interacts with MongoDB
"""

from pymongo import MongoClient


def dump_nginx_req_data(nginx_data):
    """Dump nginx request data to the output"""
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{nginx_data.estimated_document_count()} logs')
    print('Methods:')
    for method in http_methods:
        method_counter = nginx_data.count_documents({'method': method})
        print(f'\tmethod {method}: {method_counter}')
    stat_count = nginx_data.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{stat_count} status check')


def get_top_ip_group(ip_group):
    """
    Print statistics about the top 10 IP's in collection
    Args:
        ip_group: IP list to process
    """
    print('IPs:')
    fetch_logs = ip_group.aggregate(
        [
            {
                '$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10,
            },
        ]
    )
    for log in fetch_logs:
        ip = log['_id']
        ip_count = log['totalRequests']
        print(f'\t{ip}: {ip_count}')


def runMain():
    """Run MongoClient then pass on the collection to next function"""
    mongodb = MongoClient('mongodb://127.0.0.1:27017')
    dump_nginx_req_data(mongodb.logs.nginx)
    get_top_ip_group(mongodb.logs.nginx)


if __name__ == '__main__':
    runMain()
