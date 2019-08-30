
import os
import datetime
import asana
import json
import shutil
import tempfile
import webbrowser

PERSONAL_ACCESS_TOKEN = os.environ['ASANA_TOKEN']

def showcalendar():
    client = asana.Client.access_token(PERSONAL_ACCESS_TOKEN)
    me = client.users.me()

    tasks = []
    for workspace in me['workspaces']:
        tasks.extend(list(client.tasks.find_all(params={
            'workspace':workspace['gid'],
            'assignee':me['gid'],
            'completed_since':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        })))

    full_tasks = [client.tasks.find_by_id(task['gid']) for task in tasks]

    n = len(me['workspaces'])
    colors = ['DarkGreen','Tomato','GoldenRod','DodgerBlue','DimGray',
            'BlueViolet','DarkCyan','DarkTurquoise','Khaki','Orchid']
    color = dict(zip([w['gid'] for w in me['workspaces']],colors[:n]))

    events_json = json.dumps([{'title': task['name'], 
                            'start': task['due_on'], 
                            'color': color[task['workspace']['gid']],
                            'link_to_url': f"https://app.asana.com/0/0/{task['gid']}"}
                                for task in full_tasks])

    tmpdir = new_html_temp('fullcalendar')
    with open(os.path.join(tmpdir,"fullcalendar", "asanaview.html"),'r') as f:
        filedata = f.read()
        filedata = filedata.replace("EVENTS",events_json)
        filedata = filedata.replace("TODAY",datetime.datetime.now().strftime("%Y-%m-%d"))
    with open(os.path.join(tmpdir,"fullcalendar", "asanaview.html"),'w') as f:
        f.write(filedata)

    return html_open(os.path.join(tmpdir,"fullcalendar"),"asanaview.html")

def new_html_temp(src):
    """
    Create a tmp directory, copy `src` into it, and return the tmp directory
    """
    tmpdir = tempfile.mkdtemp()
    parentdir =  os.path.dirname(__file__)
    shutil.copytree(os.path.join(parentdir,src), os.path.join(tmpdir,src))
    return tmpdir
   
def html_open(tmpdir,file):
    """
    Try to open an html file in the OS asanaview web browser. If that fails, 
    provide a link to open it in Jupyter.
    """
    opened = webbrowser.open_new_tab('file://' + os.path.join(tmpdir,file))
    if not opened:
        from IPython.display import FileLink
        localdir = 'tmp-asana-' + ''.join(random.choice(string.ascii_letters) for _ in range(6))
        shutil.copytree(tmpdir,localdir)
        return FileLink(os.path.join(localdir,file))
