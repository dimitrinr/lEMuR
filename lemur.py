import subprocess
from tkinter import Tk, Button, Entry, filedialog, StringVar, Label
import threading

def setup_storage():
    directory = storage_entry.get()
    command = f"aws s3 cp autoloader.sh {directory}"
    subprocess.run(command, shell=True)

def connect_cluster():
    cluster_id = cluster_entry.get()
    directory = storage_entry.get()
    command = f"aws emr add-steps --cluster-id {cluster_id} --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://mybucket/mytest.jar,Args=[arg1,arg2,arg3]"
    subprocess.run(command, shell=True)

def source():
    folder = filedialog.askdirectory()
    source_entry.delete(0, 'end')
    source_entry.insert(0, folder)

def fswatch():
    source_dir = source_entry.get()
    target_dir = storage_entry.get()
    command = f"fswatch {source_dir} | xargs -n1 -I{} aws s3 sync {source_dir} {target_dir}"
    if toggle_btn_var.get() == "On":
        toggle_btn_var.set("Off")
        threading.Thread(target=lambda: subprocess.run(command, shell=True)).start()
    else:
        toggle_btn_var.set("On")
        # Here you need a way to stop the fswatch process

def ssh():
    ip_address = cluster_entry.get()
    command = f"ssh --root {ip_address}"
    subprocess.run(command, shell=True)

root = Tk()

storage_entry = Entry(root)
storage_entry.pack()
Button(root, text="Setup Temp Storage", command=setup_storage).pack()

cluster_entry = Entry(root)
cluster_entry.pack()
Button(root, text="Connect to EMR Cluster", command=connect_cluster).pack()

source_entry = Entry(root)
source_entry.pack()
Button(root, text="Source", command=source).pack()

toggle_btn_var = StringVar()
toggle_btn_var.set("Off")
Button(root, textvariable=toggle_btn_var, command=fswatch).pack()

Button(root, text="SSH", command=ssh).pack()

root.mainloop()
