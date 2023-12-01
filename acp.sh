#!/bin/bash

pushitup(){

    git add .
    read -p "enter commit message" message
    git commit -m "$message"
    git push
    git status

}

pushitup