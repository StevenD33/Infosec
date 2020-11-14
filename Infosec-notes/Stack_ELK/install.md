https://techexpert.tips/elasticsearch/elasticsearch-enable-tls-https/

https://www.elastic.co/guide/en/elasticsearch/reference/7.9/deb.html

output.elasticsearch:    
  hosts: ["192.168.0.41:9200"]
  protocol: "https"
  ssl.certificate_authorities: /home/vpnhugo/elasticsearch-ca.pem
  username: "elastic"
  password: "Soc123!"
setup.kibana:
  host: "http://192.168.0.41:5601"
