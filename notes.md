# WSL 系统，/mnt下挂载移动硬盘

sudo mkdir /mnt/d
sudo mount -t drvfs D: /mnt/d
ls /mnt/d

sudo umount /mnt/d
