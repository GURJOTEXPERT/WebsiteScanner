#!/bin/bash


clear
sleep 3
figlet Website Scanner
sleep 1

echo -n  "ENTER THE DOMAIN :"
read a
sleep 3
echo -n  "ENTER THE FILE NAME TO SAVE THE SCANNING :"
read b

sleep 3
nmap $a -oN $b.txt
sleep 3
nslookup $a
sleep 7
echo "____________"
echo "PLEASE WAIT "
echo "____________"
sleep 2
clear
cowsay "THANK FOR USING"
figlet Website Scanner
