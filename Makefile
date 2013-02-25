default: buildout

buildout: bin/buildout
	bin/buildout -c buildout.cfg -t 1

clean:
	@rm -f bin/* .installed.cfg .mr.developer.cfg
#	@echo "To recompile PIL: remove all PIL* eggs from your eggs cache."
#	@find src -type d -name "Paste*" | xargs rm -rf
#	@echo "If you keep having problems, purge /var/tmp/dist/* and your eggs cache"

predepends: precise

precise: _check_apt
	sudo apt-get install -y make gcc python2.7-dev libjpeg-dev zlib1g-dev python-setuptools wget jed git-core openssh-client
	sudo easy_install virtualenv
#       # for python tests
#	sudo apt-get install python-profiler
#	# for cmmi compilation - soelim
#	apt-get install groff-base

start:
	bin/supervisord

stop:
	bin/supervisorctl shutdown


### helper targets ###

bin/buildout: bin/python2.7
	@bin/python2.7 bootstrap.py
##	bin/easy_install distribute==0.6.19
##	bin/easy_install zc.buildout==1.5.2

bin/python2.7:
	@virtualenv --clear -p python2.7 --distribute .

_check_apt:
	@grep 'restricted' /etc/apt/sources.list || ( echo 'Add to /etc/apt/sources.list: restricted universe multiverse'; exit 1 )
	@grep 'universe' /etc/apt/sources.list || ( echo 'Add to /etc/apt/sources.list: restricted universe multiverse'; exit 1 )
	@grep 'multiverse' /etc/apt/sources.list || ( echo 'Add to /etc/apt/sources.list: restricted universe multiverse'; exit 1 )

