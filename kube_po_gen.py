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
        file = open(f"{path}/temp/temp_buff_namespace_po", "r")
        cmd_po = file.read()
        file.close()
        res_po = os.popen(cmd_po).readlines()
        length_po = len(res_po)
        namespace_po_map = {}
        for i in range(1, length_po):
            temp = res_po[i].replace("\n", "").split(" ")
            if temp[0] not in namespace_po_map.keys():

                namespace_po_map[temp[0]] = [temp[1]]
            else:
                namespace_po_map[temp[0]].append(temp[1])
        file = open(f"{path}/temp/namespace_po_map.json", "w")
        json.dump(namespace_po_map, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass
