import json
from subprocess import PIPE
from subprocess import Popen

from loader import load_config
from pyqbit import Qbit

Auth = load_config("config.yaml")

q = Qbit(Auth.HOST, Auth.USER, Auth.PASSWORD)

process = Popen(["./port_forwarding.sh"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
stdout = stdout.decode("utf-8")
stderr = stderr.decode("utf-8")

if stdout == "" or stderr != "":
    raise Exception(f"Error opening port: {stderr}")

stdout = json.loads(stdout)
port = stdout["port"]

prefs = {"listen_port": port, "upnp": False, "random_port": False}

q.set_preference(prefs)
