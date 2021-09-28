#!/bin/bash
set -e
echo 
echo 
echo 
echo "##############################################################"
echo " This script is to clear system  and install softwares needed."
echo " You must know what is going on before running this script."
echo "               Good luck for your life !"
echo "##############################################################"
echo 
echo
echo


echo "Disable Selinux..............."

if [ `getenforce` != "Disabled" ];then
	setenforce 0
	sed -i "s/^SELINUX=/SELINUX=Disabled/g" /etc/selinux/config
fi


echo "Install softwares needed......."

yum -y install git nmap iftop $>/dev/null

