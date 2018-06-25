#! /usr/bin/env python

import sys
import requests
import ntnx

def main():
	print(sys.executable)
	print(sys.version)

	cluster_VIP, username, password = ntnx.inputvars()
	ntnx.clusterauth(username, password)
	base_url = ntnx.baseurl(cluster_VIP)
	menuitem = ntnx.selection()

	data = ntnx.getVMjsondata(base_url)

	while (menuitem != 9):
		if menuitem == 1:
			ntnx.listvms(data)
			menuitem = ntnx.selection()
		elif menuitem == 2:
			ntnx.listvms(data)
			ntnx.getpowerstate(data)
			menuitem = ntnx.selection()

		else:
			print "nothing selected"
			menuitem = ntnx.selection()
#	datavstores = ntnx.getVSTOREjsondata(base_url)

if __name__ == "__main__":
    main()
