## Start `pytardo` at boot

* Edit the `pytardo.service` file and set the right paths to pytardo and its config file
* Copy the file in the `/etc/systemd/system/` folder. 
* Give it the right permissions: `chmod 774 /etc/systemd/system/pytardo.service`
* `systemctl daemon-reload`
* `systemctl enable pytardo.service`
* Test the script: `systemctl start pytardo.service`
* Reboot

