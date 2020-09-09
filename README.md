# Schema Parser for Graph DBs 

This project aims to generate a JSON representation of the schema for graph databases like Janusgraph and Datastax Enterprise.

Both these graph databases provide commands to specify the schema, however, they do not have a proper export format.

Note: This project is still a Work in Progress

## Supported databases

1. Datastax Enterprise (incomplete)

## Usage

    >>> python parser.py dse_schema.txt

This returns a similar output:    
    
    {'name': {'type': 'text', 'cardinality': 'single'}, 'gender': {'type': 'text', 'cardinality': 'single'}}
