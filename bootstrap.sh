#!/bin/sh

PROJECT_NAME=$1
REPO=git://github.com/d1ffuz0r/djrails.git

if [ ! -d djrails ]; then
    git clone git://github.com/d1ffuz0r/djrails.git
fi;

if [ ! -d $PROJECT_NAME ]; then
    django-admin.py startproject --template ./djrails/project_name $PROJECT_NAME -v 2
    echo "project $PROJECT_NAME was created"
    pip install -r $PROJECT_NAME/pipfile.txt
else
    echo "project $PROJECT_NAME already exists"
fi;

if [ -d djrails ]; then
    rm -rf djrails
fi;
