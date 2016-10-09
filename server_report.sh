#!/bin/bash

#Purpose : Gerenerate Server Report
#Author  : Pradip More

line="============================="
dash="-----------------------------"

echo ""
echo "System Report for $(hostname)"

total_cpu_core=$(grep -c processor /proc/cpuinfo)
total_memory=$( free -m | awk '/Mem/{print$2,"MB"}' )
free_memory=$( free -m | awk '/Mem/{print$4,"MB"}')

echo ""
echo "CPU Cores: $total_cpu_core"
echo $line

echo "Memory"
echo $dash

echo "Total Memory : $total_memory"
echo "Free Memory  : $free_memory"
echo $line

echo "Disk Space"
echo $dash
df -hTP
echo $line

load_avg=$( uptime | awk '/load/{print$9,$10,$11,$12,$13}')
echo $load_avg
echo $line

echo "Log Messages"
echo $dash
tail /var/log/messages
echo ""
echo $line


echo "Failed Cron Jobs"
echo $dash
cat /var/log/cron | grep ! | tail
echo $line
