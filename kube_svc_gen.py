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
        file = open(f"{path}/temp/temp_buff_namespace_svc", "r")
        cmd_svc = file.read()
        file.close()
        res_svc = os.popen(cmd_svc).readlines()
        length_svc = len(res_svc)
        namespace_svc_map = {}
        for i in range(1, length_svc):
            temp = res_svc[i].replace("\n", "").split(" ")
            if temp[0] not in namespace_svc_map.keys():

                namespace_svc_map[temp[0]] = [temp[1]]
            else:
                namespace_svc_map[temp[0]].append(temp[1])
        file = open(f"{path}/temp/namespace_svc_map.json", "w")
        json.dump(namespace_svc_map, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass
