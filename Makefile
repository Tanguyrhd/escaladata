#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y escaladata || :
	@pip install -e .
