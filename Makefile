all:
	@echo "make test | qemu-guest-agent | clean"

define PrepareSource
	@cd SOURCES; rm -f $(1).tar.gz; tar zcf $(1).tar.gz $(1)
endef

test:
	$(call PrepareSource, test-1.0.0)
	@rpmbuild --target noarch -bb SPECS/test.spec

hello:
	@rpmbuild -bb SPECS/hello.spec

qemu-guest-agent:
	$(call PrepareSource, qemu-guest-agent-2.12.1)
	@rpmbuild -bb SPECS/qemu-guest-agent.spec

vde:
	@rpmbuild -bb SPECS/vde.spec

clean:
	rm -rf BUILD/*
	rm -rf BUILDROOT/*
	rm -rf RPMS/*

