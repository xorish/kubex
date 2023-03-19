def settings(self):
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    self.process_settings.start('python3', ['-u', f'{path}/settings.py'])

def ssh_combo_add(self):
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    import json
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    ssh_combo_clear(self)
    for i in data.keys():
        self.ssh_combo.addItem(f"{i} {data[i][0]}")

def info(self):
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    self.process_info.start('python3', ['-u', f'{path}/about.py'])


def initiation():
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/flag", 'w')
    file.write('1')
    file.close()
    initiation_list = ['namespace_deployment_map.json', 'namespace_po_map.json', 'namespace_pvc.json',
                       'namespace_pvc_pv.json', 'namespace_svc_map.json', 'node_list.json', 'node_list.list',
                       'pod_con_map.json', 'pvc_pv.json', 'temp_buff_deployment', 'temp_buff_deployment_cmd',
                       'temp_buff_namespace_po', 'temp_buff_namespace_svc', 'temp_buff_node', 'temp_buff_node_desc',
                       'temp_buff_po_con', 'temp_buff_po_con_exec', 'temp_buff_po_delete', 'temp_buff_po_desc',
                       'temp_buff_po_logs', 'temp_buff_port_forward', 'temp_buff_pvc', 'temp_buff_pvc_desc',
                       'temp_buff_pvc_edit_cmd', 'temp_buff_pv_desc', 'temp_buff_pv_edit_cmd',
                       'temp_buff_roll_out_restart', 'temp_buff_roll_out_status', 'temp_buff_roll_out_undo',
                       'temp_buff_svc_desc', 'temp_buff_watch_cmd', 'temp_deployment.yaml', 'temp-file',
                       'temp_node_stat', 'temp_pod_stat', 'temp_pvc.json', 'temp_pvc.yaml', 'temp_pv.json',
                       'temp_pv.yaml','temp_buff_node_cordon','temp_buff_node_delete','temp_buff_node_drain']
    for i in initiation_list:
        os.system(f'rm {path}/temp/{i}')


def start(self):
    import sys
    import os
    import json
    import time
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))

    prox=QtCore.QProcess()
    prox.start('python3', ['-u', f'{path}/loading.py'])
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    initiation()

    self.status.setText("Set Operation in Remote mode...")
    namespace_combo_clear(self)
    node_combo_clear(self)
    kube_cmd_svc = f"/home/{ssh[0]}/bin/kubectl get svc --all-namespaces --no-headers"
    cmd_svc = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_svc}' | pawk 'f[:2]'"
    file = open(f"{path}/temp/temp_buff_namespace_svc", "w")
    file.write(cmd_svc)
    file.close()

    kube_cmd_po = f"/home/{ssh[0]}/bin/kubectl get po --all-namespaces --no-headers"
    cmd_po = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_po}' | pawk 'f[:2]'"
    file = open(f"{path}/temp/temp_buff_namespace_po", "w")
    file.write(cmd_po)
    file.close()

    kube_cmd_con = f'''/home/{ssh[0]}/bin/kubectl get pod --all-namespaces --no-headers -o="custom-columns=NAME:.metadata.name,CONTAINERS:.spec.containers[*].name"'''
    cmd_con = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_con}' | pawk 'f[:2]'"
    file = open(f"{path}/temp/temp_buff_po_con", "w")
    file.write(cmd_con)
    file.close()

    kube_cmd_node = f"/home/{ssh[0]}/bin/kubectl get node --no-headers "
    cmd_node = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_node}' | pawk 'f[:2]'"
    file = open(f"{path}/temp/temp_buff_node", "w")
    file.write(cmd_node)
    file.close()

    kube_cmd_node = f"/home/{ssh[0]}/bin/kubectl get deployment  --no-headers --all-namespaces "
    cmd_node = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_node}' | pawk 'f[:2]'"
    file = open(f"{path}/temp/temp_buff_deployment", "w")
    file.write(cmd_node)
    file.close()

    kube_cmd_node = f"/home/{ssh[0]}/bin/kubectl get pvc  --no-headers --all-namespaces "
    cmd_node = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd_node}' | pawk 'f[:4]'"
    file = open(f"{path}/temp/temp_buff_pvc", "w")
    file.write(cmd_node)
    file.close()

    time.sleep(2)

    pro_ns_svc(self)
    pro_ns_po(self)
    pro_po_con(self)
    pro_node_list(self)
    pro_ns_deployment(self)
    pro_ns_pvc_pv(self)
    start = time.time()

    while True:
        count=time.time()
        file_count = len(os.popen(f"ls {path}/temp/").readlines())
        if (count-start)>=10:
            namespace_combo_clear(self)
            node_combo_clear(self)
            pod_combo_clear(self)
            deployment_combo_clear(self)
            container_combo_clear(self)
            pvc_combo_clear(self)
            pv_combo_clear(self)
            service_combo_clear(self)
            file = open(f"{path}/temp/flag", 'w')
            file.write('0')
            file.close()
            self.status.setText("Failed connecting to server...!!")
            break

        elif file_count != 15:
            time.sleep(1)

        elif file_count == 15:
            time.sleep(1)


            try:
                file = open(f"{path}/temp/namespace_svc_map.json", "r")
                namespace_svc_map = json.load(file)
                file.close()
                for i in namespace_svc_map.keys():
                    self.name_space_combo.addItem(i)

                file = open(f"{path}/temp/node_list.json", "r")
                node_list = json.load(file)
                self.node_number.display(str(len(node_list.keys())))
                ready_count = 0
                not_ready_count = 0
                for i in node_list.keys():
                    self.node_combo.addItem(i)
                    if node_list[i] == "Ready":
                        ready_count += 1
                    else:
                        not_ready_count += 1
                node_status_str = f"Ready : {ready_count} | Not-ready : {not_ready_count}"
                self.node_status_bar.setText(node_status_str)
                self.status.setText("Connected to server...")
            except Exception:
                self.status.setText("Failed connecting to server...!!")
            prox.kill()
            break


def service_pod_deployment_pvc(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    try:
        file = open(f"{path}/temp/namespace_svc_map.json", "r")
        namespace_svc_map = json.load(file)
        file.close()
        file = open(f"{path}/temp/namespace_po_map.json", "r")
        namespace_po_map = json.load(file)
        file.close()
        file = open(f"{path}/temp/namespace_deployment_map.json", "r")
        namespace_deployment_map = json.load(file)
        file.close()
        file = open(f"{path}/temp/namespace_pvc.json", "r")
        namespace_pvc_map = json.load(file)
        file.close()

        service_combo_clear(self)
        namespace = self.name_space_combo.currentText()
        self.svc_combo.addItems(namespace_svc_map[namespace])
        pod_combo_clear(self)
        self.pod_combo.addItems(namespace_po_map[namespace])
        self.pod_count.display(str(len(namespace_po_map[namespace])))
        deployment_combo_clear(self)
        self.deployment_combo.addItems(namespace_deployment_map[namespace])
        pvc_combo_clear(self)

        self.pvc_combo.addItems(namespace_pvc_map[namespace])
        self.pvc_number.display(str(len(namespace_pvc_map[namespace])))

    except Exception as e:
        print(e)


def container(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/pod_con_map.json", "r")
    pod_con_map = json.load(file)
    file.close()
    container_combo_clear(self)
    try:
        pod = self.pod_combo.currentText()
        self.container_combo.addItems(pod_con_map[pod])
    except Exception as e:
        pass


def pv(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/pvc_pv.json", "r")
    pvc_pv_map = json.load(file)
    file.close()
    pv_combo_clear(self)
    try:
        pvc = self.pvc_combo.currentText()
        self.pv_combo.addItems(pvc_pv_map[pvc])
    except Exception as e:
        pass


# PROCESSES

def pro_ns_svc(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_svc_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


def pro_ns_po(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_po_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


def pro_po_con(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_con_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


def pro_node_list(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_node_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


def pro_ns_deployment(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_deployment_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


def pro_ns_pvc_pv(self):
    import sys
    import os
    from subprocess import Popen, PIPE
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    pro_cmd = f'python3 -u  {path}/kube_pvc_gen.py'
    Popen("exec " + pro_cmd, stdout=PIPE, stderr=None, shell=True)


# COMBO CLEAR
def ssh_combo_clear(self):
    self.ssh_combo.clear()

def namespace_combo_clear(self):
    self.name_space_combo.clear()


def service_combo_clear(self):
    self.svc_combo.clear()


def pod_combo_clear(self):
    self.pod_combo.clear()


def container_combo_clear(self):
    self.container_combo.clear()


def node_combo_clear(self):
    self.node_combo.clear()


def deployment_combo_clear(self):
    self.deployment_combo.clear()


def pv_combo_clear(self):
    self.pv_combo.clear()


def pvc_combo_clear(self):
    self.pvc_combo.clear()


def namespace_filter(self):
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.namespace_filter.text()
    import json
    file = open(f"{path}/temp/namespace_svc_map.json", "r")
    namespace_svc_map = json.load(file)
    file.close()
    namespace_combo_clear(self)
    if search:
        for i in namespace_svc_map.keys():
            if search in i:
                self.name_space_combo.addItem(i)
    else:
        self.name_space_combo.addItems(namespace_svc_map.keys())


# POD

def po_filter(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.pod_filter.text()
    file = open(f"{path}/temp/namespace_po_map.json", "r")
    namespace_po_map = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod_combo_clear(self)
    if search:
        for i in namespace_po_map[namespace]:
            if search in i:
                self.pod_combo.addItem(i)
    else:
        self.pod_combo.addItems(namespace_po_map[namespace])


def watch_po(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore, QtGui, QtWidgets
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod_filter = self.pod_filter.text()
    if pod_filter:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl get pods -n {namespace} --watch | grep {pod_filter}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'"
    else:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl get pods -n {namespace} --watch "
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'"
    file = open(f"{path}/temp/temp_buff_watch_cmd", "w")
    file.write(cmd)
    file.close()
    self.process_watch = QtCore.QProcess()
    self.process_watch.start('python3', ['-u', f'{path}/watch_disp.py'])


def pod_describe(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod = self.pod_combo.currentText()
    if pod:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl describe po {pod} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pod
        file = open(f"{path}/temp/temp_buff_po_desc", "w")
        file.write(cmd)
        file.close()
        self.process_po_desc = QtCore.QProcess()
        self.process_po_desc.start('python3', ['-u', f'{path}/po_describe.py'])
    else:
        self.status.setText("No pod Found !!")


def po_logs(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod = self.pod_combo.currentText()
    containerx = self.container_combo.currentText()

    if containerx:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl logs {pod} -c {containerx} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + containerx
        file = open(f"{path}/temp/temp_buff_po_logs", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/po_logs.py'])
    elif pod and not containerx:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl logs {pod}  -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + containerx
        file = open(f"{path}/temp/temp_buff_po_logs", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/po_logs.py'])
    else:
        self.status.setText("No pod or container Found !!")


def po_delete(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod = self.pod_combo.currentText()

    if pod:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl delete pod {pod} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pod
        file = open(f"{path}/temp/temp_buff_po_delete", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/delete_pod_consent.py'])

    else:
        self.status.setText("No pod Found !!")


def excute_po_con(self):
    import json
    import sys
    from subprocess import Popen, PIPE
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod = self.pod_combo.currentText()
    containerx = self.container_combo.currentText()

    if containerx:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl exec -it {pod} -c {containerx} -n {namespace} bash"
        cmd = f'''sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} "{kube_cmd}"'''
        cmdx = f"dbus-launch gnome-terminal -e '{cmd}'"
        Popen(cmdx, stdout=PIPE, stderr=None, shell=True)
    elif pod and not containerx:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl exec -it {pod}  -n {namespace} bash"
        cmd = f'''sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} "{kube_cmd}"'''
        cmdx = f"dbus-launch gnome-terminal -e '{cmd}'"
        Popen(cmdx, stdout=PIPE, stderr=None, shell=True)
    else:
        self.status.setText("No pod Found !!")


def pod_top(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pod = self.pod_combo.currentText()
    if pod:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl top pod {pod} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pod
        file = open(f"{path}/temp/temp_pod_stat", "w")
        file.write(cmd)
        file.close()
        self.process_po_top = QtCore.QProcess()
        self.process_po_top.start('python3', ['-u', f'{path}/cpu_mem_stat.py'])
    else:
        self.status.setText("No pod Found !!")


##NODE

def node_cordon(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    node = self.node_combo.currentText()

    if node:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl cordon {node}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + node
        file = open(f"{path}/temp/temp_buff_node_cordon", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/cordon_node_consent.py'])

    else:
        self.status.setText("No node Found !!")

def node_delete(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    node = self.node_combo.currentText()

    if node:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl delete  {node} --force"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + node
        file = open(f"{path}/temp/temp_buff_node_delete", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/delete_node_consent.py'])

    else:
        self.status.setText("No node Found !!")
def node_drain(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    node = self.node_combo.currentText()

    if node:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl drain  {node} "
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + node
        file = open(f"{path}/temp/temp_buff_node_drain", "w")
        file.write(cmd)
        file.close()
        self.process_po_logs = QtCore.QProcess()
        self.process_po_logs.start('python3', ['-u', f'{path}/drain_node_consent.py'])

    else:
        self.status.setText("No node Found !!")
def node_ready_filter(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/node_list.json", "r")
    node_list = json.load(file)

    count = 0
    temp = []
    for i in node_list.keys():
        if node_list[i] == "Ready":
            temp.append(i)
            count += 1
    if len(temp) > 0:
        node_combo_clear(self)
        self.node_combo.addItems(temp)
        self.node_status_bar.setText("All Ready Node/s Filtered!!")
        self.node_number.display(str(count))
    else:
        self.node_status_bar.setText("No Ready Node/s Found!!")


def node_not_ready_filter(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/node_list.json", "r")
    node_list = json.load(file)

    count = 0
    temp = []
    for i in node_list.keys():
        if node_list[i] != "Ready":
            temp.append(i)
            count += 1
    if len(temp) > 0:
        node_combo_clear(self)
        self.node_combo.addItems(temp)
        self.node_number.display(str(count))
        self.node_status_bar.setText("All Not-Ready Node/s Filtered!!")
    else:
        self.node_status_bar.setText("No Not-Ready Node/s Found!!")


def node_describe(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    node = self.node_combo.currentText()
    if node:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl describe node {node}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + node
        file = open(f"{path}/temp/temp_buff_node_desc", "w")
        file.write(cmd)
        file.close()
        self.process_node_desc = QtCore.QProcess()
        self.process_node_desc.start('python3', ['-u', f'{path}/node_describe.py'])
    else:
        self.status.setText("No Node Found !!")


def node_top(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    node = self.node_combo.currentText()
    if node:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl top node {node} "
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + node
        file = open(f"{path}/temp/temp_node_stat", "w")
        file.write(cmd)
        file.close()
        self.process_node_top = QtCore.QProcess()
        self.process_node_top.start('python3', ['-u', f'{path}/cpu_mem_stat_node.py'])
    else:
        self.status.setText("No node Found !!")


def node_search_filter(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.node_filter.text()
    file = open(f"{path}/temp/node_list.json", "r")
    node_list = json.load(file)
    file.close()
    node_combo_clear(self)
    if search:
        for i in node_list.keys():
            if search in i:
                self.node_combo.addItem(i)
    else:
        self.node_combo.addItems(node_list.keys())


# SERVICE

def svc_filter(self):
    search = self.svc_filter.text()
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file = open(f"{path}/temp/namespace_svc_map.json", "r")
    namespace_svc_map = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    service_combo_clear(self)
    if search:
        for i in namespace_svc_map[namespace]:
            if search in i:
                self.svc_combo.addItem(i)
    else:
        self.svc_combo.addItems(namespace_svc_map[namespace])


def svc_describe(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    svc = self.svc_combo.currentText()
    if svc:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl describe service {svc} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + svc
        file = open(f"{path}/temp/temp_buff_svc_desc", "w")
        file.write(cmd)
        file.close()
        self.process_svc_desc = QtCore.QProcess()
        self.process_svc_desc.start('python3', ['-u', f'{path}/svc_describe.py'])
    else:
        self.status.setText("No Service Found !!")


def svc_port_forward(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    port = self.svc_port.text()
    portx = port.split(":")
    svc = self.svc_combo.currentText()
    x = False
    for i in portx:
        if i.isnumeric():
            x = True

    pod = self.pod_combo.currentText()
    if port and x:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl port-forward  {pod} {port} -n {namespace} "
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -L :{portx[0]}:127.0.0.1:{portx[0]} -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + svc
        file = open(f"{path}/temp/temp_buff_port_forward", "w")
        file.write(cmd)
        file.close()
        self.process_svc_port_forward = QtCore.QProcess()
        self.process_svc_port_forward.start('python3', ['-u', f'{path}/port_forward.py'])
        self.status.setText(f"Port forwarded to local port : {port}")
    else:
        self.status.setText("No Service Found !!")


def clear_port(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()

    kube_cmd = f"pkill kubectl -9"
    cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'"
    try:
        os.system(cmd)
        self.status.setText("Clearing all associated ports in remote server...")
    except Exception:
        pass


# Deployment


def deployment_filetr(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.deployment_filter.text()
    file = open(f"{path}/temp/namespace_deployment_map.json", "r")
    namespace_deployment_map = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    deployment_combo_clear(self)
    if search:
        for i in namespace_deployment_map[namespace]:
            if search in i:
                self.deployment_combo.addItem(i)
    else:
        self.deployment_combo.addItems(namespace_deployment_map[namespace])


def deployment_edit(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    deployment = self.deployment_combo.currentText()
    if deployment:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl get deployment {deployment} -n {namespace} -o yaml"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + deployment + "#" + \
              data[ssh[0]][1] + "#" + ssh[0] + "#" + ssh[1]

        file = open(f"{path}/temp/temp_buff_deployment_cmd", "w")
        file.write(cmd)
        file.close()
        self.process_edit_deployment = QtCore.QProcess()
        self.process_edit_deployment.start('python3', ['-u', f'{path}/edit_deployment_disp.py'])
    else:
        self.status.setText("No Deployment Found !!")


def rollout_status(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    deployment = self.deployment_combo.currentText()
    if deployment:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl rollout status deployment {deployment} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + deployment
        file = open(f"{path}/temp/temp_buff_roll_out_status", "w")
        file.write(cmd)
        file.close()
        self.process_rollout_status = QtCore.QProcess()
        self.process_rollout_status.start('python3', ['-u', f'{path}/watch_disp_rollout_status.py'])
    else:
        self.status.setText("No Deployment Found !!")


def rollout_restart(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    deployment = self.deployment_combo.currentText()
    if deployment:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl rollout restart deployment {deployment} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + deployment
        file = open(f"{path}/temp/temp_buff_roll_out_restart", "w")
        file.write(cmd)
        file.close()
        self.process_rollout_restart = QtCore.QProcess()
        self.process_rollout_restart.start('python3', ['-u', f'{path}/roll_out_restart_consent.py'])
    else:
        self.status.setText("No Deployment Found !!")


def rollout_undo(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    deployment = self.deployment_combo.currentText()
    if deployment:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl rollout undo deployment {deployment} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + deployment
        file = open(f"{path}/temp/temp_buff_roll_out_undo", "w")
        file.write(cmd)
        file.close()
        self.process_rollout_undo = QtCore.QProcess()
        self.process_rollout_undo.start('python3', ['-u', f'{path}/roll_out_undo_consent.py'])
    else:
        self.status.setText("No Deployment Found !!")


# PVC

def pvc_describe(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pvc = self.pvc_combo.currentText()
    if pvc:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl describe pvc {pvc} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pvc
        file = open(f"{path}/temp/temp_buff_pvc_desc", "w")
        file.write(cmd)
        file.close()
        self.process_pvc_desc = QtCore.QProcess()
        self.process_pvc_desc.start('python3', ['-u', f'{path}/pvc_describe.py'])
    else:
        self.status.setText("No PVC Found !!")


def pvc_edit(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pvc = self.pvc_combo.currentText()
    if pvc:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl get pvc {pvc} -n {namespace} -o yaml"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pvc + "#" + \
              data[ssh[0]][1] + "#" + ssh[0] + "#" + ssh[1]

        file = open(f"{path}/temp/temp_buff_pvc_edit_cmd", "w")
        file.write(cmd)
        file.close()
        self.process_edit_pvc = QtCore.QProcess()
        self.process_edit_pvc.start('python3', ['-u', f'{path}/edit_pvc_disp.py'])
    else:
        self.status.setText("No PVC Found !!")


def pvc_filetr(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.pvc_filter.text()
    file = open(f"{path}/temp/namespace_pvc.json", "r")
    namespace_pvc_map = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pvc_combo_clear(self)
    if search:
        for i in namespace_pvc_map[namespace]:
            if search in i:
                self.pvc_combo.addItem(i)
    else:
        self.pvc_combo.addItems(namespace_pvc_map[namespace])


# PV

def pv_describe(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pv = self.pv_combo.currentText()
    if pv:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl describe pv {pv} -n {namespace}"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pv
        file = open(f"{path}/temp/temp_buff_pv_desc", "w")
        file.write(cmd)
        file.close()
        self.process_pv_desc = QtCore.QProcess()
        self.process_pv_desc.start('python3', ['-u', f'{path}/pv_describe.py'])
    else:
        self.status.setText("No PV Found !!")


def pv_filetr(self):
    import json
    import sys
    import os
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    search = self.pv_filter.text()
    file = open(f"{path}/temp/pvc_pv.json", "r")
    pvc_pv_map = json.load(file)
    file.close()
    pvc = self.pvc_combo.currentText()
    pv_combo_clear(self)
    if search:
        for i in pvc_pv_map[pvc]:
            if search in i:
                self.pv_combo.addItem(i)
    else:
        self.pv_combo.addItems(pvc_pv_map[pvc])


def pv_edit(self):
    import json
    import sys
    import os
    from PyQt5 import QtCore
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    ssh = self.ssh_combo.currentText().split(" ")
    file = open(f'{path}/temp/ssh.json', 'r')
    data = json.load(file)
    file.close()
    namespace = self.name_space_combo.currentText()
    pv = self.pv_combo.currentText()
    if pv:
        kube_cmd = f"/home/{ssh[0]}/bin/kubectl get pv {pv} -n {namespace} -o yaml"
        cmd = f"sshpass -p {data[ssh[0]][1]} ssh -o StrictHostKeyChecking=no {ssh[0]}@{ssh[1]} '{kube_cmd}'" + "#" + pv + "#" + \
              data[ssh[0]][1] + "#" + ssh[0] + "#" + ssh[1]

        file = open(f"{path}/temp/temp_buff_pv_edit_cmd", "w")
        file.write(cmd)
        file.close()
        self.process_edit_pv = QtCore.QProcess()
        self.process_edit_pv.start('python3', ['-u', f'{path}/edit_pv_disp.py'])
    else:
        self.status.setText("No PV Found !!")
