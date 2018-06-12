import subprocess

def res_cmd_lfeed(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).stdout.readlines()

def res_cmd_no_lfeed(cmd):
  return [str(x) for x in res_cmd_lfeed(cmd).decode()]

def main():
  cmd = ("ls -l")
  print(res_cmd_no_lfeed(cmd))

if __name__ == '__main__':
  main()