#!/usr/bin/python3

from queue import PriorityQueue
import yaml
import os

# with open('/home/li/workspaces/SmallWashingRobotSDK/config/cloud/error_maps.yaml') as f:
#     docs = yaml.load_all(f, Loader=yaml.dump)
#     print(docs)


# 将字典写入到yaml
alist = []
adict = {'ec': '0x05130033','iec': '0x2E26'}
alist.append(adict)
rdict = {'maps':alist}

yamlpath =  "/home/li/caps.yaml"

# 写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(rdict, f)
