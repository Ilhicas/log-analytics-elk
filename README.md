# Mei Course 2017 / 2018 - University of Coimbra
### Analysis of Log using BI tools in this particular case using ELK from Elastic.co

#

## Requirements
docker version >= 1.12
docker-compose >= 1.9
## How to use
docker-compose up -d elasticsearch kibana logstash


Navigate to http://localhost:5601 and you will be presented with kibana dashboard, refresh until status red disappears from elasticsearch status presented on kibana

then 

docker-compose up -d parser

