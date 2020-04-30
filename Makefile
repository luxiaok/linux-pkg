# Makefile for rpmbuild

define PrepareSource
	@cd SOURCES; rm -f $(1).tar.gz; tar zcf $(1).tar.gz $(1)
endef

define RpmBuild
	@rpmbuild -bb SPECS/$(1).spec
endef

help:
	@echo "make test                # For Test RPM Package"
	@echo "make hello               # For GUN Hello RPM Package"
	@echo "make qemu-guest-agent    # For QEMU Guest Agent RPM Package"
	@echo "make vde                 # For Virtual Distributed Ethernet RPM Package"
	@echo "make pycurl              # For python-pycurl RPM Package"
	@echo "make libvirt             # For libvirt RPM Package"
	@echo "make libvirt-python      # For libvirt-python RPM Package"
	@echo "make qemu-kvm            # For QEMU-KVM RPM Package"
	@echo "make clean               # Clean cache files"

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

