# 00 Prerequisite
先理解数字证书，数字证书和CA的概念：
http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html

# Use openssl to make certificate of CA(sekf-signed)，key and certifecate of server&client
## Server
> ```
> openssl genrsa -des3 -out server.key 1024
> openssl req -new -key server.key -out server.csr
> ```

## Client
> ```
> openssl genrsa -des3 -out client.key 1024
> openssl req -new -key client.key -out client.csr
> ```

## CA
> ```
> mkdir ca
> cd ca
> openssl genrsa -des3 -out ca.key 1024
> openssl req -new -x509 -key ca.key -out ca.crt 
> ```

## 利用CA证书进行签名
> ```
> openssl ca -in ../server.csr -out ../server.crt -cert ca.crt -keyfile ca.key 
> openssl ca -in ../client.csr -out ../client.crt -cert ca.crt -keyfile ca.key 
> ```

注意: 此时会出错：Using configuration from /usr/share/ssl/openssl.cfg I am unable to access the ./demoCA/newcerts directory ./demoCA/newcerts: No such file or directory 
### 解决方法：
> 1. mkdir -p ./demoCA/newcerts 
> 2. touch demoCA/index.txt 
> 3. touch demoCA/serial 
> 4. echo 01 > demoCA/serial
