#!/usr/bin/python

import subprocess

def res_cmd_lfeed(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).stdout.readlines()

def main():
  cmd = ("ls -l")
  for i in res_cmd_lfeed(cmd):
    print(i.decode())

if __name__ == '__main__':
  main()