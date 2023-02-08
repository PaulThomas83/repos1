#!/bin/bash

# ops 301 challenge 5
# Author Paul Thomas
# Date 2-6-23

now=$(date "+%y-%m-%d-%h-%m-%s")

ls-l /var/log/syslog
ls-l /var/log/wtmp
zip /var/log/backup/wtmp_$now.zip/var/log/wtmp
zip /var/log/backup/syslog_$now.zip/var/syslog
> /var/log/syslog
> /var/log/wtmp
ls-l /var/log/backup
