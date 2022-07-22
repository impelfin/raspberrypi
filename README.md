# raspberrypi 

### rpi base raspbian/stretch

### Container execute 
docker run -d -it --name rpi -v /Users/lune/Documents/GitHub/raspberrypi:/app impelfin/rpi 

### Container shell connection 
docker exec -it rpi /bin/bash
