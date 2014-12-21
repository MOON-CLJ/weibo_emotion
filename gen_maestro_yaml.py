#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

cluster_name = "weibo-emotion-cluster"
ships = ["219.224.135.93"]
base_image = "weibo_emotion:1.2"
base_port = 8000
num_instance_per_ship = 10


def gen_maestro_yaml():
    with open("maestro.yaml", "w") as conf:
        data = {
            "name": cluster_name,
            "ships": {},
            "services": {
                "weibo-emotion-app": {
                    "image": base_image,
                    "instances": {}
                },
            },
            "audit": [
                {"type": "log", "file": "/tmp/maestro.log"}
            ]
        }
        for ship in ships:
            data["ships"][ship] = {"ip": ship}

        for i in xrange(len(ships)):
            for j in xrange(num_instance_per_ship):
                container_no = i * num_instance_per_ship + j
                service_name = "weibo-emotion-app"
                container_name = "%s%s" % (service_name, container_no)
                container_port = base_port + container_no
                data["services"][service_name]["instances"][container_name] = {
                    "ship": ships[i],
                    "ports": {"client": {"external": container_port, "exposed": 8000}},
                }

        yaml.dump(data, conf, default_flow_style=False)

if __name__ == "__main__":
    gen_maestro_yaml()
