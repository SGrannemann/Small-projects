"""Quick script to add the contents of a csv file to my todoist via Todoists REST API."""

import csv
import sys
from pathlib import Path
from todoist.api import TodoistAPI


tasks = {}

# get the data from the csv
file_path = Path('MigrationNotionTodoist') / Path('MediaList.csv')

with open(file_path, 'r', encoding='cp1252') as media_file:
    
    dict_reader = csv.DictReader(media_file, fieldnames=['Name','Tags','Type','URL','Finished'])
    for row in dict_reader:
        
        if 'Dev' in [tag.strip() for tag in row['Type'].split(',')] and 'Data' in [tag.strip() for tag in row['Type'].split(',')]:
            tasks[row['Name']] = row['URL']



# add the data to the todoist account, section depending on the existing tags from notion

api = TodoistAPI('{}'.format(sys.argv[1]))
api.sync()
#print(api.state['sections'])
 #find the id of the project where we want to add the task
for project in api.state['projects']:
    if project.data['name'] == 'Media List':
        id_of_project = project.data['id']
    
for section in api.state['sections']:
    if section.data['project_id'] == id_of_project:
        if section.data['name'] == 'Software Dev':
            tasks_section_id = section.data['id']

for task, url in tasks.items():
    book1 = api.items.add('[{}]({})'.format(task, url), project_id=id_of_project, section_id=tasks_section_id)
api.commit()