# valumodel.com

[![Build Status](https://travis-ci.org/willmarkley/valumodel.com.svg?branch=master)](https://travis-ci.org/willmarkley/valumodel.com)  

A Linux Apache MySQL Python web application that generates discounted cash flow valuations

[valumodel.com](https://valumodel.willmarkley.com)

![valumodel1](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel1.png)  
![valumodel2](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel2.png)  
![valumodel3](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel3.png)  
![valumodel4](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel4.png)  
![valumodel5](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel5.png)  
![valumodel6](https://raw.githubusercontent.com/willmarkley/willmarkley.com/master/img/valumodel6.png)  


## Setup

Assuming Apache and MySQL are already installed:

* Clone the repository to the `/var/www/html` directory
* Download `font-awesome-4.7.0` and `font-mfizz-2.3.0` to the `/var/www/html` directory
* Copy `conf/httpd.conf` to the `/etc/httpd/conf` directory
* Create symbolic link: `ln -s valumodel.com/html/index.html index.html` in the `/var/www/html` directory
* Setup Databases and Password in MySQL:
```
mysql -u root -e "CREATE DATABASE valumodel; USE valumodel; CREATE TABLE avg (ticker VARCHAR(10), enterprise_value DOUBLE);"
mysqladmin -u root password '$Dcfr$ck1'
```

* Restart the Apache and MySQL:
```
#!/bin/bash

sudo service httpd restart
sudo service mysql restart

```

#### Maintenance

###### SSL Renewal with Let's Encrypt

```
#!/bin/bash

sudo service httpd stop
sudo opt/certbot-auto --apache renew
sudo service httpd restart
```

###### Cron to reset Apache everyday

```
# sudo crontab -e

53 4 * * * service httpd restart
```


## Technology Stack

#### Back End

[Linux](https://en.wikipedia.org/wiki/LAMP_(software_bundle))  
[Apache HTTP Server](https://httpd.apache.org)  
[MySQL](https://www.mysql.com)  
[Python](https://www.python.org)  

#### Front End

[HTML](http://www.w3.org/html/)  
[CSS](http://www.w3.org/Style/CSS/)  
[Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  
[Font Awesome](http://fontawesome.io)  
[Font Mfizz](http://fizzed.com/oss/font-mfizz)

#### Hosting

[Amazon Web Services](https://aws.amazon.com)  
[Let's Encrypt](https://letsencrypt.org/)  
[Certbot](https://certbot.eff.org)

#### Libraries

[Quandl](https://www.quandl.com)  
[Jinja](http://jinja.pocoo.org)  

## Reference

[Installing LAMP on AWS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)  
[Python in the Web](https://docs.python.org/3/howto/webservers.html)  
[mod_python Documentation](http://modpython.org/live/current/doc-html/contents.html)  
[MySQL Connector Python Documentation](http://dev.mysql.com/doc/connector-python/en/)  
  
