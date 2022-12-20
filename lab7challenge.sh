#!/bin/bash
echo CPU info
sudo lshw -c cpu | grep "description:\|physical id:\|size"
echo ram INFO
 sudo lshw -c memory | grep "product:\|vendor:\|physical:\|bus info:\|width"
echo netowrk info
 sudo lshw -c network | grep "description:\|product:\|vendor:\|physical id:\|bus info:\|logical name:\|version:\| serial:\| size:\| capacity:\|width;\|clock;\|capabilities;\|configuration;\|resources"
 echo display adapter info
sudo lshw -c display adapter | grep "description:\|product:\|vendor:\|physical id:\|bus info:\|logical name:\|capacity:\|width;\|clock;\|capabilities;\|configuration;\|resources"