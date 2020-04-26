all:
	@echo "make test | qemu-guest-agent | clean"

define PrepareSource
	@cd SOURCES; rm -f $(1).tar.gz; tar zcf $(1).tar.gz $(1)
endef

define RpmBuild
	@rpmbuild -bb SPECS/$(1).spec
endef

test:
	$(call PrepareSource, test-1.0.0)
	@rpmbuild --target noarch -bb SPECS/test.spec

hello:
	$(call RpmBuild, hello)

qemu-guest-agent:
	$(call PrepareSource, qemu-guest-agent-2.12.1)
	$(call RpmBuild, qemu-guest-agent)

vde:
	$(call RpmBuild, vde)

clean:
	rm -rf BUILD/*
	rm -rf BUILDROOT/*
	rm -rf RPMS/*

