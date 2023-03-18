

import json
import sys
import os

path = os.path.dirname(os.path.abspath(sys.argv[0]))
file = open('temp/ssh.json', 'r')
data = json.load(file)
file.close()
# kube_cmd = "/home/park/bin/kubectl get svc --all-namespaces"
# cmd = f"sshpass -p {data['park'][1]} ssh park@{data['park'][0]} '{kube_cmd}' | pawk 'f[:2]'"
#
# res_svc=os.popen(cmd).readlines()
# length_svc=len(res_svc)
# namespace_svc_map={}
# for i in range(1,length_svc):
#     temp=res_svc[i].replace("\n","").split(" ")
#     if temp[0] not in namespace_svc_map.keys():
#
#         namespace_svc_map[temp[0]]=[temp[1]]
#     else:
#         namespace_svc_map[temp[0]].append(temp[1])
# file=open("namespace_svc_map.json","w")
# json.dump(namespace_svc_map,file,indent=6)
#
# kube_cmd = "/home/park/bin/kubectl get po --all-namespaces"
# cmd = f"sshpass -p {data['park'][1]} ssh park@{data['park'][0]} '{kube_cmd}' | pawk 'f[:2]'"
# res_po=os.popen(cmd).readlines()
# length_po=len(res_po)
# namespace_po_map={}
# for i in range(1,length_po):
#     temp=res_po[i].replace("\n","").split(" ")
#     if temp[0] not in namespace_po_map.keys():
#
#         namespace_po_map[temp[0]]=[temp[1]]
#     else:
#         namespace_po_map[temp[0]].append(temp[1])
# file=open("namespace_po_map.json","w")
# json.dump(namespace_po_map,file,indent=6)

# kube_cmd = '''/home/park/bin/kubectl get pod --all-namespaces --no-headers -o="custom-columns=NAME:.metadata.name,CONTAINERS:.spec.containers[*].name"'''
# cmd = f"sshpass -p {data['park'][1]} ssh park@{data['park'][0]} '{kube_cmd}' | pawk 'f[:2]'"
# res_con=os.popen(cmd).readlines()
# print(res_con)


# length_con=len(res_con)
# pod_con_map={}
# for i in range(1,length_con):
#     temp=res_con[i].replace("\n","").split(" ")
#     pod_con_map[temp[0]]=temp[1].split(",")
# file=open("pod_con_map.json","w")
# json.dump(pod_con_map,file,indent=6)


kube_cmd="/home/park/bin/kubectl get pvc  --no-headers -A "
cmd = f"sshpass -p {data['park'][1]} ssh park@{data['park'][0]} '{kube_cmd}' | pawk 'f[:4]'"
print(cmd)
os.system(cmd)

# file=open('temp-file','r')
# data=file.readlines()
# temp_list=[]
# for i in data:
#     temp_list.append(i.replace("\n",""))
# print(temp_list)
cx=os.popen(f"ls {path}/temp/").readlines()
print(len(cx))








# for i in res:
#     test=i.replace("\n","")
#     tmp = "{.spec.containers[*].name}"
#     kube_cmdx = f"/home/park/kubectl get  -n {test} -o jsonpath='{tmp}'"
#     cmd = f"sshpass -p {data['park'][1]} ssh park@{data['park'][0]} '{kube_cmdx}'"
#     resx = os.popen(cmd).readlines()
#     print(resx)