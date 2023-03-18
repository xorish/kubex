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
        file = open(f"{path}/temp/temp_buff_pvc", "r")
        cmd_pvc = file.read()
        file.close()
        res_pvc = os.popen(cmd_pvc).readlines()
        length_pvc = len(res_pvc)
        namespace_pvc_map = {}
        pvc_pv_map = {}
        for i in range(1, length_pvc):
            temp = res_pvc[i].replace("\n", "").split(" ")
            if temp[0] not in namespace_pvc_map.keys():

                namespace_pvc_map[temp[0]] = [temp[1]]
            else:
                namespace_pvc_map[temp[0]].append(temp[1])
        file = open(f"{path}/temp/namespace_pvc.json", "w")
        json.dump(namespace_pvc_map, file, indent=6)
        file.close()
        for i in range(1, length_pvc):
            temp = res_pvc[i].replace("\n", "").split(" ")
            pvc_pv_map[temp[1]] = [temp[3]]
        file = open(f"{path}/temp/pvc_pv.json", "w")
        json.dump(pvc_pv_map, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass