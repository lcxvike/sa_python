#!/bin/bash
current_dir=`pwd`
if [[ $(id -u) != "0" ]]; then
    echo "Error: You must be root to run this script, please use root to install ftp"
    exit 1
fi
function read_upd(){
while true
do
echo -n "Please enter the virtual users:"
read -a username
if [ -z $username ];then
        echo "Input is empty, please enter again"
else
        echo "username=$username"
        break
fi
done
while true
do
echo -n "Please enter a virtual user passwords:"
read -a password
if [ -z $password ];then
        echo "Input is empty, please enter again"
else
        echo "password=$password"
        break
fi
done
while true
do
echo -n "Please enter the FTP server directory:"
read -a  ftp_dir
if [ -z $ftp_dir ];then
        echo "Input is empty, please enter again"
else
        echo "ftp_dir=$ftp_dir"
        break
fi
done
}
read_upd
rpm -qa | grep vsftpd && rpm -qa | grep  ftp && rpm -qa | grep db4 && rpm -qa | grep db4-utils && rpm -qa | grep db4-devel && rpm -qa | grep db4-tcl 
if [[ $? -eq 0 ]];then
	echo "have"
else
	echo "no"
yum -y install vsftpd  ftp db4 db4-utils db4-devel db4-tcl >>/dev/null
fi
mv /etc/vsftpd/vsftpd.conf /etc/vsftpd/vsftpd.conf.bak
#egrep -v '^#|^$' /etc/vsftpd/vsftpd.conf.bak > /etc/vsftpd/vsftpd.conf
#cp $current_dir/ftp_configuration_files/vsftpd.conf /etc/vsftpd
cat >>/etc/vsftpd/vsftpd.conf<<EOF
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
message_file=.message
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen=YES
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
use_localtime=YES
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list
guest_enable=YES
guest_username=ftp
user_config_dir=/etc/vsftpd/vuser_conf	
EOF
echo "ftp" >> /etc/vsftpd/chroot_list
echo "$username" >>/etc/vsftpd/vftpuser.txtx
echo "$password" >>/etc/vsftpd/vftpuser.txtx
db_load -T -t hash -f  /etc/vsftpd/vftpuser.txtx /etc/vsftpd/vftpuser.db
#getconf LONG_BIT
if [[ `uname -m | sed -e 's/i.86/32/'` -eq 32 ]];then
        echo 32
echo "auth      required     pam_userdb.so db=/etc/vsftpd/vftpuser">>/etc/pam.d/vsftpd
echo "account   required     pam_userdb.so db=/etc/vsftpd/vftpuser">>/etc/pam.d/vsftpd
else
        echo 64
echo "auth   required    /lib64/security/pam_userdb.so db=/etc/vsftpd/vftpuser">>/etc/pam.d/vsftpd
echo "account required   /lib64/security/pam_userdb.so db=/etc/vsftpd/vftpuser">>/etc/pam.d/vsftpd
fi
if [ ! -d /etc/vsftpd/vuser_conf/ ];then
mkdir /etc/vsftpd/vuser_conf
fi
#cp $current_dir/ftp_configuration_files/xjq /etc/vsftpd/vuser_conf
cat >>/etc/vsftpd/vuser_conf/$username<<EOF
local_root=$ftp_dir
write_enable=YES
download_enable=YES
anon_world_readable_only=NO
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
local_umask=022
EOF
service vsftpd restart
modprobe ip_conntrack_ftp
modprobe ip_nat_ftp
