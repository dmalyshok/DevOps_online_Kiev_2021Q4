#!/bin/bash

yum update -y
yum install git nano wget net-tools unzip wget epel-release -y
timedatectl set-timezone Europe/Kiev