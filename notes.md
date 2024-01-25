<!--markdownlint-disable-next-line MD041 -->
```bash
# WSL 系统，/mnt下挂载移动硬盘
sudo mkdir /mnt/d
sudo mount -t drvfs D: /mnt/d
ls /mnt/d

# 卸载
sudo umount /mnt/d
```
