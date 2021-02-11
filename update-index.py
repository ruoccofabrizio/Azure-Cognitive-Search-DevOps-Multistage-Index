import json
import logging
import sys
import os
os.system("pip install requests")
os.system("pip install argparse")
import requests
import argparse

def update_index_definition(endpoint, headers, api_version, index_name, index_file_path=".\index.json"):
    with open(index_file_path) as index_file:
        index_data = json.load(index_file)
    index_data['name'] = index_name
    logging.info(index_data)
    response = requests.put(f"{endpoint}indexes/{index_name}{api_version}", headers=headers, json=index_data)
    return f"{index_name} result_code: {response.status_code} text: {response.text}"


# MAIN
if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )
    parser = argparse.ArgumentParser(description='Input parameter for azure-search-copy-index')
    parser.add_argument('--service', dest="service", required=True,
                        help='Azure Cognitive Search Service')
    parser.add_argument('--service_key', dest="service_key", required=True,
                        help='Azure Cognitive Search Service KEY')
    parser.add_argument('--include', dest="include",
                        help='Azure Cognitive Search Indexes to update. If not specified mod applies to ALL')
    parser.add_argument('--exclude', dest="exclude",
                        help='Azure Cognitive Search Indexes to skip in updating')
    parser.add_argument('--index_file_path', dest="index_file_path", required=True,
                        help='Azure Cognitive Search Indexes file path')
                        
    
    args = parser.parse_args()
    service = args.service
    service_key = args.service_key 
    include = args.include.split(',') if args.include != None else []
    exclude = args.exclude.split(',') if args.exclude != None else []  
    index_file_path = args.index_file_path if args.index_file_path != None else None
    
    logging.info(f"\n\tservice name: {service}\n\tecluded indexes:{exclude}\n\tincluded indexes: {include if include != [] else 'All not excluded'}")

    endpoint = 'https://' + service + '.search.windows.net/'
    api_version = '?api-version=2020-06-30'
    headers = {'Content-Type': 'application/json',
            'api-key': service_key } 

    response = requests.get(f"{endpoint}indexes{api_version}&$select=name", headers=headers)
    indexes = list(filter(None,map(lambda x: x['name'] if x['name'] not in exclude else None, response.json()['value']))) if include == [] else include

    result = list(map(lambda x: update_index_definition(endpoint, headers, api_version, x, index_file_path), indexes))
    logging.info(result)


