
rm -rf orange.service
cat <<EOT >> orange.service
[Unit]
Description=systemd auto orange service
After=weston.target

[Service]
PAMName=login
Type=simple
User=mendel
WorkingDirectory=/home/mendel/ReefVision
Environment=DISPLAY=:0
ExecStart=/bin/bash /usr/bin/orange_service.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOT

sudo mv orange.service /lib/systemd/system/orange.service


echo "python3 -m Orange_Vision.detect_server" >> orange_service.sh
sudo chmod u+x orange_service.sh
sudo mv orange_service.sh /usr/bin
sudo systemctl enable orange.service
sudo systemctl start orange.service
