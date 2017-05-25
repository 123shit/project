#/bin/sh
ps -ef | grep "RunServer.py" |  grep -v "grep" | awk '{print $2}' | xargs kill -s 9
nohup python3 /mnt/EASProxy/RunServer.py &