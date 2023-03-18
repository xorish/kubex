import os
import sys
import json
import time

path = os.path.dirname(os.path.abspath(sys.argv[0]))
while True:
    try:


        file=open(f"{path}/temp/flag",'r')
        flag=file.read()
        file.close()
        if flag=='0':
            break
        file = open(f"{path}/temp/temp_buff_node", "r")
        cmd_svc = file.read()
        file.close()
        res_svc = os.popen(cmd_svc).readlines()
        temp = {}
        for i in res_svc:
            x = i.replace("\n", "").split(" ")
            temp[x[0]] = x[1]

        file = open(f"{path}/temp/node_list.json", "w")
        json.dump(temp, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass