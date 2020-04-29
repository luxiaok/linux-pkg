# Makefile for rpmbuild

define PrepareSource
	@cd SOURCES; rm -f $(1).tar.gz; tar zcf $(1).tar.gz $(1)
endef

define RpmBuild
	@rpmbuild -bb SPECS/$(1).spec
endef

all:
	@echo "make test | qemu-guest-agent | vde | pycurl | clean"

test:
	$(call PrepareSource,test-1.0.0)
	$(call RpmBuild,test)

hello:
	$(call RpmBuild,hello)

qemu-guest-agent:
	$(call PrepareSource,qemu-guest-agent-2.12.1)
	$(call RpmBuild,qemu-guest-agent)

vde:
	$(call RpmBuild,vde)

pycurl:
	$(call RpmBuild,python-pycurl)

libvirt:
	$(call RpmBuild,libvirt)

libvirt-python:
	$(call RpmBuild,libvirt-python)

qemu-kvm:
	$(call RpmBuild,qemu-kvm)

clean:
	rm -rf BUILD/*
	rm -rf BUILDROOT/*
	rm -rf RPMS/*

