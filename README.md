## To Run Project 
### 1. Install Docker
### 2. create development environment
### 3. activate development environment

<!-- ```
$ docker-compose build
$ docker-compose up
```      -->

### 4. make migrations first
```
docker-compose run web python manage.py migrate
```
### 5. then you can directly run docker image
```
docker-compose up
```
OR

### 6. build docker image
```
docker-compose build
```
### 7. run docker image
```
docker-compose run
```