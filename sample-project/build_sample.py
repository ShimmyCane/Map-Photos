#!/usr/bin/env python3
"""Build the self-contained Hollywood Bowl sample from the files in this folder.

Reads   project.src.json, hollywood_bowl_site_plan.jpg, photos/*.jpg
Writes  hollywood_bowl.sample.json   (open it with "Open JSON": plan + photos are embedded)
        hollywood_bowl.sample.js     (same data; index.html loads it so the start screen can offer
                                      the sample even when opened straight from disk)
Run:    python3 sample-project/build_sample.py
"""
import base64, json, os

here = os.path.dirname(os.path.abspath(__file__))

def data_uri(path, mime='image/jpeg'):
    with open(path, 'rb') as f:
        return f'data:{mime};base64,' + base64.b64encode(f.read()).decode()

with open(os.path.join(here, 'project.src.json')) as f:
    project = json.load(f)

plan_path = os.path.join(here, project['plan']['file_name'])
project['plan']['size_bytes'] = os.path.getsize(plan_path)
photos = []
for p in project['photos']:
    path = os.path.join(here, p['path'])
    p['size_bytes'] = os.path.getsize(path)
    photos.append(data_uri(path))
project['embedded'] = {'plan': data_uri(plan_path), 'photos': photos}

with open(os.path.join(here, 'hollywood_bowl.sample.json'), 'w') as f:
    json.dump(project, f, separators=(',', ':'))
with open(os.path.join(here, 'hollywood_bowl.sample.js'), 'w') as f:
    f.write('(window.MAPPHOTOS_SAMPLES = window.MAPPHOTOS_SAMPLES || []).push(')
    json.dump(project, f, separators=(',', ':'))
    f.write(');\n')
print('built', len(photos), 'photos')
