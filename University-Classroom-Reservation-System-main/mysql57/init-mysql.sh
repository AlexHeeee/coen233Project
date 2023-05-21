#!/bin/bash
mkdir -p $PWD/mysql57/{conf,data,log}


tee $PWD/mysql57/conf/my.cnf<<-'EOF'
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
lower_case_table_names=1 
# By default we only accept connections from localhost
#bind-address   = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
default-time_zone = '-6:00'

symbolic-links=0
character-set-server=utf8mb4
[client]
default-character-set=utf8mb4
[mysql]
default-character-set=utf8mb4

EOF

