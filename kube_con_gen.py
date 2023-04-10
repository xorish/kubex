import os
import sys
import json
import time

path = os.path.dirname(os.path.abspath(sys.argv[0]))

# Author: Sourish Datta
# Email: sourishonax@gmail.com
# Phone: (+91) 8343003660


while True:
    try:
        file = open(f"{path}/temp/flag", 'r')
        flag = file.read()
        file.close()
        if flag == '0':
            break
        file = open(f"{path}/temp/temp_buff_po_con", "r")
        cmd_con=file.read()
        file.close()
        res_con = os.popen(cmd_con).readlines()
        length_con = len(res_con)
        pod_con_map = {}
        for i in range(1, length_con):
            temp = res_con[i].replace("\n", "").split(" ")
            pod_con_map[temp[0]] = temp[1].split(",")
        file = open(f"{path}/temp/pod_con_map.json", "w")
        json.dump(pod_con_map, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass
