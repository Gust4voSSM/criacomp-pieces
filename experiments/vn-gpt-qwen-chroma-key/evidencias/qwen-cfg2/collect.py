"""Read existing jobs and download completed archives; never submits generation."""
import json
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parent
WORKSPACE=ROOT.parents[3]
auth=json.loads((WORKSPACE.parent/'flux-klein-modal/.api-auth.json').read_text(encoding='utf-8'))
headers={key:auth[key] for key in ('Modal-Key','Modal-Secret')}
base='https://gssm--vn-sprites-qwen-reference-views-web.us-east.modal.run'
for label in ('control','negative'):
    folder=ROOT/label
    ident=json.loads((folder/'job.json').read_text())['job_id']
    with urllib.request.urlopen(urllib.request.Request(base+'/jobs/'+ident,headers=headers),timeout=90) as response:
        status=json.load(response)
    (folder/'last-status.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
    print(label,status['status'],flush=True)
    if status['status']=='completed' and not (folder/'results.zip').exists():
        with urllib.request.urlopen(urllib.request.Request(base+'/jobs/'+ident+'/download',headers=headers),timeout=90) as response:
            (folder/'results.zip').write_bytes(response.read())
        print(label,'downloaded',flush=True)
