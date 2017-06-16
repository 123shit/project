# ! /bin/sh

basepath=$(cd `dirname $0`; pwd)

while true
do
    procnum=`ps -ef|grep "RunServer.py"|grep -v grep|wc -l`
    if [ $procnum -eq 0 ]
    then
        cd $basepath ; nohup python3 RunServer.py  > /dev/null &
        echo `date +%Y-%m-%d` `date +%H:%M:%S`  "restart RunServer" >>$basepath/shell.log
    fi
    sleep 10
done
