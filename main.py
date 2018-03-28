#! /usr/bin/env python

import requests
import ntnx

def main():
	cluster_VIP, username, password = ntnx.inputvars()
	ntnx.clusterauth(username, password)
	base_url = ntnx.baseurl(cluster_VIP)
	menuitem = ntnx.selection()

	data = ntnx.getVMjsondata(base_url)

	if menuitem == 1:
		ntnx.listvms(data)
	elif menuitem == 2:
		ntnx.listvms(data)
		ntnx.getpowerstate(data)
	else:
		print "nothing selected"

#	datavstores = ntnx.getVSTOREjsondata(base_url)

if __name__ == "__main__":
    main()