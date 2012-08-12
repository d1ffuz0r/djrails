#!/bin/sh

PROJECT_NAME=$1
PATH_TO_TEMPLATE=https://github.com/d1ffuz0r/djrails/zipball/master

if [ ! -d $PROJECT_NAME ]; then
    django-admin.py startproject --template $PATH_TO_TEMPLATE --extension py,md,txt $PROJECT_NAME -v 2
    echo "project $PROJECT_NAME was created"
    pip install -r $PROJECT_NAME/pipfile.txt
else
    echo "project $PROJECT_NAME already exists"
fi;
