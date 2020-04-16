import os
import datetime
import json
import notion

from notion.client import NotionClient
from dotenv import load_dotenv
from pathlib import Path  # python3 only
# timer
print( datetime.datetime.utcnow().isoformat() )

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
notion_token = os.getenv('NOTION_TOKEN')
# add a try catch
client = NotionClient(token_v2=notion_token) 
root_page = client.get_block('https://www.notion.so/duylam/DLCC-89d296a0590643a68cc60acac1d486b2')
shadow_root = {}

for p in root_page.children.filter('page'):
    shadow_root[p.title] = p

dispatch = shadow_root['Dispatch']
dispatch = dispatch.children.filter('collection_view')[0]
dispatch_collection = dispatch.collection.get_rows()
dispatch_meta = dispatch.collection.get_schema_properties()
flat_dispatch_collection = []
for row in dispatch_collection:
    result = {}
    result = row.get_all_properties()
    # storing date as ISOFORMAT 
    result['creation_date'] = row.creation_date.start.isoformat()
    result['_id'] = "{}-{}".format(result['creation_date'],row.id)
    result['content'] = []
    for child in row.children:
        if child.type == 'image':
            result['content'].append(child.source)
        if child.type == 'text':
            result['content'].append(child.title)
    flat_dispatch_collection.append(result)
shadow_root['Dispatch'] = flat_dispatch_collection

projects = shadow_root['Projects']
projects = projects.children.filter('collection_view')[0]
projects_collection = projects.collection.get_rows()
projects_meta = projects.collection.get_schema_properties()
flat_projects_collection = []
for row in projects_collection:
    result = {}
    result = row.get_all_properties()
    # storing date as ISOFORMAT 
    result['creation_date'] = row.creation_date.start.isoformat()
    result['_id'] = "{}-{}".format(result['creation_date'],row.id)
    result['content'] = []
    for child in row.children:
        if child.type == 'image':
            result['content'].append({'type':child.type,'src':child.source})
        if child.type != 'image':
            result['content'].append({'type':child.type, 'title':child.title})
    flat_projects_collection.append(result)
shadow_root['Projects'] = flat_projects_collection

notes = shadow_root['Notes']
notes = notes.children.filter('collection_view')[0]
notes_collection = notes.collection.get_rows()
notes_meta = notes.collection.get_schema_properties()
flat_notes_collection = []
for row in notes_collection:
    result = {}
    result = row.get_all_properties()
    # storing date as ISOFORMAT 
    result['posted_date'] = row.posted_date.isoformat()
    result['_id'] = "{}-{}".format(result['posted_date'],row.id)
    result['content'] = []
    for child in row.children:
        if child.type == 'image':
            result['content'].append({'type':child.type,'src':child.source})
        if child.type != 'image':
            result['content'].append({'type':child.type, 'title':child.title})
    flat_notes_collection.append(result)
shadow_root['Notes'] = flat_notes_collection


about = shadow_root['About']
flat_about_collection = []
for row in about.children:
    result = {}
    result['content'] = []
    if row.type == 'image':
        result['content'].append({'type':row.type,'src':row.source})
    if row.type != 'image':
        result['content'].append({'type':row.type, 'title':row.title})
    flat_about_collection.append(result)
shadow_root['About'] = flat_about_collection

with open('db001.json', 'w') as outfile:
    json.dump(shadow_root, outfile, indent=4)
    # timer
    print( datetime.datetime.utcnow().isoformat() )