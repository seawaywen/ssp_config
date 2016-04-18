#!/bin/sh

#set -e 

#SS_SERVER='/home/kelvin/DevTools/ss/shadowsocks-local-linux64-1.1.4'
SS_SERVER='sslocal'
CONFIG_PATH='/home/kelvin/DevTools/ss'
error=0
#PS_KEYWORD='shado'
PS_KEYWORD='sslocal'

ps -ef | grep $PS_KEYWORD | grep -v "grep"

SS_PROCESS_NUM=`ps -ef | grep $PS_KEYWORD | grep -v "grep" | wc | awk '{print $1}'`
echo $SS_PROCESS_NUM

if [ $SS_PROCESS_NUM -ge 1 ]; then
    echo "kill existing ss service"
    kill `ps -ef | grep $PS_KEYWORD | grep -v 'grep' |  awk '{print $2}'`
fi

CONFIG_FILE="$CONFIG_PATH/config.json"
if [ -n "$1" ];then
    CONFIG_FILE="$CONFIG_PATH/config_$1.json"
fi

echo $CONFIG_FILE
$SS_SERVER -c $CONFIG_FILE


