#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023, Sergei Antipov <greendayonfire at gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: proxmox_vm_info
short_description: Retrieve information about one or more Proxmox VE virtual machines
version_added: 7.2.0
description:
  - Retrieve information about one or more Proxmox VE virtual machines.
author: 
  - 'Sergei Antipov (@UnderGreen) <greendayonfire at gmail dot com>'
  - Maryam Mayabi (@mmayabi) <mayabi.ahm at gmail dot com>
  - Orbsim (@orbsim) <orbsim at gmail dot com>
options:
  node:
    description:
      - Node where to get virtual machines info.
    type: str
  type:
    description:
      - Restrict results to a specific virtual machine(s) type.
    required: true
    type: str
    choices:
      - all
      - qemu
      - lxc
    default: all
  vmid:
    description:
      - Restrict results to a specific virtual machine by using its ID.
    type: int
  name:
    description:
      - Restrict results to a specific virtual machine by using its name.
      - If multiple virtual machines have the same name then vmid must be used instead.
    type: str
extends_documentation_fragment:
    - community.general.proxmox.documentation
    - community.general.attributes
    - community.general.attributes.info_module
"""

EXAMPLES = """
- name: List all existing QEMU virtual machines in proxmox cluster
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_token_id: '{{ token_id | default(omit) }}'
    api_token_secret: '{{ token_secret | default(omit) }}'
    type: qemu

- name: List all existing virtual machines on node01
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_token_id: '{{ token_id | default(omit) }}'
    api_token_secret: '{{ token_secret | default(omit) }}'
    node: node01

- name: List all QEMU virtual machines on node01
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    node: node01
    type: qemu

- name: Retrieve information about specific VM by ID
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    type: qemu
    vmid: 101

- name: Retrieve information about specific lxc by name
  community.general.proxmox_vm_info:
    api_host: proxmoxhost
    api_user: root@pam
    api_password: '{{ password | default(omit) }}'
    node: node01
    type: lxc
    name: lxc05.home.arpa
"""

RETURN = """
proxmox_vms:
    description: List of virtual machines.
    returned: on success
    type: list
    elements: dict
    sample:
      [
        {
            "balloon": 0,
            "boot": "cd",
            "bootdisk": "virtio0",
            "cores": 8,
            "cpu": "host",
            "cpus": 8,
            "description": "test vm",
            "digest": "cf607ea96a24673100a1ab66a500e7adb421adea",
            "disk": 0,
            "diskread": 0,
            "disks": [
                {
                    "media": "cdrom",
                    "name": "ide2"
                },
                {
                    "name": "virtio0",
                    "path": "vm-102-disk-0.raw",
                    "size": "10G",
                    "storage": "local"
                }
            ],
            "diskwrite": 0,
            "maxdisk": 10737418240,
            "maxmem": 8589934592,
            "mem": 0,
            "memory": 8192,
            "meta": "creation-qemu=6.2.0,ctime=1669614540",
            "name": "test1",
            "netin": 0,
            "netout": 0,
            "nets": [
                {
                    "bridge": "vmbr0",
                    "mac": "6E:72:FF:28:E0:5A",
                    "model": "virtio",
                    "name": "net0",
                    "tag": "8"
                }
            ],
            "node": "node02",
            "numa": 1,
            "ostype": "l26",
            "scsihw": "virtio-scsi-pci",
            "smbios1": "uuid=d72b666e-0765-4218-aee6-bbee16ba6a75",
            "sockets": 1,
            "status": "stopped",
            "type": "qemu",
            "uptime": 0,
            "vcpus": 8,
            "vmgenid": "308acf0b-2cdc-45bc-825b-7bc6c1f30d7b",
            "vmid": 101
        },
        {
            "balloon": 0,
            "bios": "seabios",
            "boot": "cdn",
            "bootdisk": "scsi0",
            "cipassword": "**********",
            "ciuser": "root",
            "cores": 16,
            "cpu": "host",
            "cpus": 16,
            "cpuunits": 1024,
            "description": "this server created for test",
            "digest": "a5bb492225c13d5fb3ea2e12ba1fb73aeaa80c3d",
            "disk": 0,
            "diskread": 0,
            "disks": [
                {
                    "media": "cdrom",
                    "name": "ide2",
                    "path": "vm-100-cloudinit.qcow2",
                    "storage": "cloud"
                },
                {
                    "name": "scsi0",
                    "path": "vm-100-disk-0.qcow2",
                    "size": "30G",
                    "storage": "local"
                }
            ],
            "diskwrite": 0,
            "ipconfig0": "ip=10.0.0.2/24,gw=10.1.1.1",
            "keyboard": "en-us",
            "kvm": 1,
            "maxdisk": 32212254720,
            "maxmem": 17179869184,
            "mem": 1200450749,
            "memory": 16384,
            "meta": "creation-qemu=6.2.0,ctime=1689583658",
            "name": "test2",
            "nameserver": "8.8.8.8 4.4.4.4",
            "netin": 79600081,
            "netout": 15525264,
            "nets": [
                {
                    "bridge": "br0",
                    "firewall": "0",
                    "mac": "28:08:FE:80:DE:A3",
                    "model": "virtio",
                    "name": "net0",
                    "tag": "100"
                }
            ],
            "node": "node01",
            "numa": 1,
            "onboot": 1,
            "pid": 1969629,
            "scsihw": "virtio-scsi-pci",
            "smbios1": "uuid=8204a99c-d4e7-4a7e-afb8-5f1fecc750a8",
            "sockets": 1,
            "sshkeys": "ssh-rsa%20AAAAB3Nz",
            "status": "running",
            "type": "qemu",
            "uptime": 23972,
            "vmgenid": "54c2917c-c1ae-9468-8934-db249f73aa36",
            "vmid": 100
        }
      ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.general.plugins.module_utils.proxmox import (
    proxmox_auth_argument_spec,
    ProxmoxAnsible,
)
import re

class ProxmoxVmInfoAnsible(ProxmoxAnsible):
    disks = []
    nets = []
    def add_to_disks(self, name, value):
        regex = "^.+:[0-9].+/.+\..+"
        item = {}
        item['name'] = name
        try:
            for data in value.split(','):
                if not re.search(regex, data) and '=' not in data:
                    continue #e.g data is "none"  (  "ide2": "none:media=cdrom" )
                if re.search(regex, data):
                    item['storage'] = data.split(':')[0]
                    item['path'] = data.split('/')[1]
                else:
                    k = data.split('=')[0]
                    v = data.split('=')[1]
                    item[k] = v
            self.disks.append(item)
        except Exception:
            return False
        return True

    def add_to_nets(self, name, value):
        item = {}
        item['name'] = name
        try:
            for data in value.split(','):
                if '=' in data:
                    k, v = data.split('=')
                    if k in ['e1000','virtio','rtl8139','vmxnet3']:
                        item['model'] = k
                        item['mac'] = v
                    else:
                        item[k] = v
            self.nets.append(item)
        except Exception:
            return False
        return True

    def vm_in_node(self, vmid, node):
        try:
          for vm in self.proxmox_api.nodes(node).qemu.get():
            if int(vm['vmid']) == vmid:
               return True
        except Exception as e:
          self.module.fail_json(msg="Failed to retrieve QEMU VMs information: %s" % e)
        return False

    def get_vm_node(self, vmid):
        try:
          for node in self.proxmox_api.nodes.get():
            node = node['node'] #node becomes a string
            if self.vm_in_node(vmid, node):
                return node
        except Exception as e:
          self.module.fail_json(msg="Failed to retrieve QEMU VMs Node Name: %s" % e)

    def get_vm_configs(self, node, vm):
        disk_regex = "^ide[0-3]{1}$|^scsi(30|[12][0-9]|[0-9])$|^virtio(1[0-5]|[0-9])$|^sata[0-5]{1}$|^efidisk0$|^tpmstate0$|^unused(25[0-5]|[12][0-4][0-9]|[1-9]?[0-9])$"
        net_regex = "^net(0[1-9]?|[1-9]?[0-9]*)$"
        try:
            vmcnf = self.proxmox_api.nodes(node).qemu(vm['vmid']).config.get()
            vm.update(vmcnf)
            vm['node'] = node #add node name to vm dict
            dsw = nsw = False
            #for key, val in vm.items():
            for key in list(vm):
                val = vm[key]
                if (re.search(disk_regex, key)):
                    self.add_to_disks(key, val)
                    del vm[key]
                    dsw = True
                elif (re.search(net_regex, key)):
                    self.add_to_nets(key, val)
                    del vm[key]
                    nsw = True
                elif key == "cpu" and isinstance(val, (int, float)):
                   vm['cpu'] = 'default'
            if dsw:
                vm['disks'] = self.disks #add disks list to vm dict
                self.disks = []
            if nsw:
                vm['nets'] = self.nets #add nets list to vm dict
                self.nets = []
            return vm
        except Exception as e:
            self.module.fail_json(msg="Failed to retrieve QEMU VMs information: %s" % e)

    def get_qemu_vms(self, node, vmid=None):
        vms = []
        try:
            vmlist = self.proxmox_api.nodes(node).qemu().get()
            for vm in vmlist:
                vm["vmid"] = int(vm["vmid"])
                vm["type"] = "qemu"
                vms.append(self.get_vm_configs(node,vm))
            if vmid is None:
                return vms
            return [vm for vm in vms if vm["vmid"] == vmid]
        except Exception as e:
            self.module.fail_json(msg="Failed to retrieve QEMU VMs information: %s" % e)

    def get_lxc_vms(self, node, vmid=None):
        try:
            vms = self.proxmox_api.nodes(node).lxc().get()
            for vm in vms:
                vm["vmid"] = int(vm["vmid"])
            if vmid is None:
                return vms
            return [vm for vm in vms if vm["vmid"] == vmid]
        except Exception as e:
            self.module.fail_json(msg="Failed to retrieve LXC VMs information: %s" % e)


def main():
    module_args = proxmox_auth_argument_spec()
    vm_info_args = dict(
        node=dict(type="str", required=False),
        type=dict(
            type="str", choices=["lxc", "qemu", "all"], default="all", required=False
        ),
        vmid=dict(type="int", required=False),
        name=dict(type="str", required=False),
    )
    module_args.update(vm_info_args)

    module = AnsibleModule(
        argument_spec=module_args,
        required_together=[("api_token_id", "api_token_secret")],
        required_one_of=[("api_password", "api_token_id")],
        mutually_exclusive=[('node', 'vmid', 'vmname')],
        supports_check_mode=True,
    )

    proxmox = ProxmoxVmInfoAnsible(module)
    node = module.params["node"]
    type = module.params["type"]
    vmid = module.params["vmid"]
    name = module.params["name"]

    result = dict(changed=False)

    if node and (proxmox.get_node(node) is None):
        module.fail_json(msg="Node %s doesn't exist in PVE cluster" % node)

    if not vmid and name:
        vmid = int(proxmox.get_vmid(name, ignore_missing=False))

    vms = []
    if type == "lxc":
        vms = proxmox.get_lxc_vms(node, vmid=vmid)
    elif type == "qemu":
        if node:
            vms = proxmox.get_qemu_vms(node=node)
        elif vmid or name:
            vms = proxmox.get_qemu_vms(node=proxmox.get_vm_node(vmid),vmid=vmid)  
        else:
            for node in proxmox.proxmox_api.nodes.get(): 
                node = node['node']
                nodevms = proxmox.get_qemu_vms(node=node)
                if nodevms:
                    vms = vms + nodevms     

    if vms or vmid is None:
        result["proxmox_vms"] = vms
        module.exit_json(**result)
    else:
        result["msg"] = "VM with vmid %s doesn't exist on node %s" % (vmid, node)
        module.fail_json(**result)


if __name__ == "__main__":
    main()
