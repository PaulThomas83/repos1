#!/bin/bash

# script: Ops challenge class 3
# author: Paul Thomas
# date: 1-25-2023
# purpose: File permissions

echo "Please input a directory path"

ls
read file
echo "Please input a directory number"
read permissions
chmod $Permissions $file
echo "you have successfully granted permissions to $file"
ls -l $file
