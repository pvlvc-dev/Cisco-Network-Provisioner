# Cisco Network Provisioner README

## Software purpose
This software aims to speed up Cisco CLI input for network devices and reduce human error.

## The problem
Manual configuration for network rollouts can be an enormous task that can take hours. Deep into it a network engineer may make an error due to fatigue, potentially causing a network outage.

## The solution
A Python/Jinja2 templating engine that ingests CSV data to instantly generate standardized IOS configurations that can be input into network devices.

## Currently supported device configurations
**Access switch**
* VLANs
* Interfaces
* Access & Trunk ports
* Management Interface

## Future additions
* More configuration options
* Layer 3 switch support
* Router support
* Fault tolerance in code

## Usage
Format the CSV as per the example CSV file, one row per network device, then run 'py generate_bulk.py'