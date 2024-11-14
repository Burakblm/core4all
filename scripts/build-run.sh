
cd /home/burak/core4all

git pull
          
sudo docker-compose -f /home/burak/core4all/docker-compose-prod.yml down

sudo docker pull burakblm/core4all:latest

sudo docker-compose -f /home/burak/core4all/docker-compose-prod.yml up -d