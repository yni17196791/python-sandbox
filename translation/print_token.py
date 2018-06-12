import subprocess

f = open("printed_token.txt","w+")

def res_cmd(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].decode()

def main():
  cmd = ("gcloud auth activate-service-account --key-file=GCP-translate-d1c49e3c0c5c.json")
  print(res_cmd(cmd))
  cmd = ("gcloud auth print-access-token")
  print(res_cmd(cmd))
  f.write(res_cmd(cmd))
  f.close()

if __name__ == '__main__':
  main()

# gcloud auth print-access-token
#  f = open("C:\Users\Niwa Yoshiki\Desktop\translation\printed.txt","w+")
#  f.write()
#  f.close()
