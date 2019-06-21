#! /bin/bash
sudo yum -y install httpd
sudo sh -c "echo '<html><h1>Hello from Amazon EC2, Version 2.0</h1></html>' > /var/www/html/index.html"
sudo systemctl enable httpd.service
sudo systemctl start httpd.service