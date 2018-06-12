import subprocess

auth = 'gcloud auth activate-service-account --key-file=GCP-translate-d1c49e3c0c5c.json'
subprocess.call(auth, shell=True)