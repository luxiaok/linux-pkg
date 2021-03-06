# Makefile for rpmbuild

ALL =

define PrepareSource
	@cd SOURCES; rm -f $(1).tar.gz; tar zcf $(1).tar.gz $(1)
endef

define RpmBuild
	@echo -e "\033[32;49;1m[`date +"%F %T"`] Compiling for $(1)\033[39;49;0m"
	@rpmbuild -bb SPECS/$(1).spec
endef

help:
	# make help                Output this message for help
	# make test                Test RPM Package
	# make hello               GUN Hello RPM Package
	# make vde                 Virtual Distributed Ethernet
	# make pycurl              PycURL for Python
	# make qemu-kvm            QEMU-KVM
	# make qemu-guest-agent    QEMU Guest Agent
	# make libvirt             Libvirt
	# make libvirt-python      Libvirt API for Python2
	# make forcedeth           Forcedeth kernel module
	# make libiscsi            iSCSI client library
	# make ksmtuned            Kernel Samepage Merging (KSM) Tuning Daemo
	# make libzip              C library for zip
	# make autoconf            A GNU tool for automatically configuring source code
	# make hiredis             Minimalistic C client library for Redis
	# make yum                 Create YUM repodata
	# make all                 Compile all rpm packages
	# make update              Update for git repo
	# make clean               Clean cache files

# ALL += test
test:
	$(call PrepareSource,test-1.0.0)
	$(call RpmBuild,test)

ALL += hello
hello:
	$(call RpmBuild,hello)

ALL += vde
vde:
	$(call RpmBuild,vde)

ALL += pycurl
pycurl:
	$(call RpmBuild,python-pycurl)

ALL += qemu-kvm
qemu-kvm:
	$(call RpmBuild,qemu-kvm)

ALL += qemu-guest-agent
qemu-guest-agent:
	$(call PrepareSource,qemu-guest-agent-2.12.1)
	$(call RpmBuild,qemu-guest-agent)

ALL += libvirt
libvirt:
	$(call RpmBuild,libvirt)

ALL += libvirt-python
libvirt-python:
	$(call RpmBuild,libvirt-python)

ALL += forcedeth-kmod
forcedeth-kmod:
	$(call RpmBuild,forcedeth-kmod)

ALL += libiscsi
libiscsi:
	$(call RpmBuild,libiscsi)

ALL += ksmtuned
ksmtuned:
	$(call RpmBuild,ksmtuned)

ALL += libzip
libzip:
	$(call RpmBuild,libzip)

ALL += autoconf
autoconf:
	$(call RpmBuild,autoconf)

ALL += hiredis
hiredis:
	$(call RpmBuild,hiredis)

.PHONY: yum
yum:
	$(RM) -r RPMS/x86_64/repodata
	@createrepo RPMS/x86_64

.PHONY: update
update:
	git pull origin master

.PHONY: all
all: $(ALL)

.PHONY: install
install:
	# Hello installation!

.PHONY: clean
clean:
	$(RM) -r BUILD/*
	$(RM) -r BUILDROOT/*
	$(RM) -r RPMS/*
	$(RM) -r SRPMS/*

