
"""
Automate Kubernetes resource deployment by
calling ansible playbooks
"""

import os
import sys
import logging
import subprocess

def main():
	"""Main Function
	"""
	cmd = ["ansible-playbook", "-i hosts",
	       "-e action=provision", "main.yml", "-v"]

	proc = subprocess.Popen(cmd,stdin=subprocess.PIPE,
		                    stdout=subprocess.PIPE,)

main()