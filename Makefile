mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


install:
	ln -sf $(mkfile_path)bin/kgit.py ~/bin/kgit

uninstall:
	rm -i ~/bin/kgit
