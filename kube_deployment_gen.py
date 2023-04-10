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
        file = open(f"{path}/temp/temp_buff_deployment", "r")
        cmd_deployment = file.read()
        file.close()
        res_deployment = os.popen(cmd_deployment).readlines()
        length_deployment = len(res_deployment)
        namespace_deployment_map = {}
        for i in range(1, length_deployment):
            temp = res_deployment[i].replace("\n", "").split(" ")
            if temp[0] not in namespace_deployment_map.keys():

                namespace_deployment_map[temp[0]] = [temp[1]]
            else:
                namespace_deployment_map[temp[0]].append(temp[1])
        file = open(f"{path}/temp/namespace_deployment_map.json", "w")
        json.dump(namespace_deployment_map, file, indent=6)
        file.close()
        time.sleep(2)
    except Exception:
        pass