#! /usr/bin/env python

import requests

def inputvars():
	#clusterVIP = raw_input("Enter Cluster VIP: ")
	#userName = raw_input("Enter Username: ")
	#passWord = raw_input("Enter password: ")
	clusterVIP = "10.21.232.57"
	userName = "conrad.corbett@nutanixsp.com"
	passWord = "nutanix/4u"
	return clusterVIP, userName, passWord

def selection():
	print "1) List VM's"
	print "2) Get Powerstate of a VM"
	print "9) Quit"
	print "\n"
	menuSelection = input("Please enter a selection: ")
	print "\n"
	return menuSelection

def clusterauth(userName, passWord):
	requests.packages.urllib3.disable_warnings()
	global s
	s = requests.Session()
	s.auth = (userName,passWord)
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})

def baseurl(clusterVIP):
	baseurl = "https://" + clusterVIP + ":9440/PrismGateway/services/rest/v2.0/"
	return baseurl

def getVMjsondata(baseUrl):
	VMdata = s.get(baseUrl + 'vms', verify=False).json()
	return VMdata

def getVSTOREjsondata(baseUrl):
	VSTOREdata = s.get(baseUrl + 'vstores', verify=False).json()
	return VSTOREdata

def listvms(jsonData):
	i = 0
	for e in jsonData["entities"]:
		i = i +1
		print i,") ",e["name"]
		#print(e["name"])
	print "\n"

def getpowerstate(jsonData):
	VMselection = input("Enter VM number: ") - 1
	print "\n" + jsonData["entities"][VMselection]["name"] + ' is ' + jsonData["entities"][VMselection]["power_state"]
