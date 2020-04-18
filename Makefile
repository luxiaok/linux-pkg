all:
	@echo "make test | qemu-guest-agent | clean"

test:
	@rpmbuild --target noarch -bb SPECS/test.spec

qemu-guest-agent:
	@rpmbuild -bb SPECS/qemu-guest-agent.spec

clean:
	rm -rf BUILD/*
	rm -rf BUILDROOT/*
	rm -rf RPMS/*

