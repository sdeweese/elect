# Elect
## Requirements
* python3

	**Note** This command is for mac with homebrew installed
```
$ brew install python3
```
* pip3

	**Note** This command is for mac with homebrew installed
```
$ brew install python3-pip
```
## Installing Python3 Virtual Environment
1) Install virtualenv
```
$ pip3 install virtualenv
```
2) Enter project directory
```
$ cd <project>
```
3) Create Python3 virtual Environment for Project
```
$ virtualenv -p python3 venv
```
## Activate Virtual Environment
* Activate from project directory
```
$ source venv/bin/activate
```
## Deactivate Virtual Environment
```
$ (venv) deactivate
```
## Requirements for Virutal Environment
* Add requirements for application

	**Note** requirements.txt contains all packages needed for application
1) Install requirements.txt
```
$ (venv) pip3 install -r requirements.txt
```
* Add requirements to requirements.txt
```
$ (venv) pip3 freeze > requirements.txt
```
## Run server
* Start Web App

	**Note** need to be in `project` directory and within virtual env
```
$ python3 manage.py runserver <port number>
```
