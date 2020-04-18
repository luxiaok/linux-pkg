all:
	@echo Hello world

test:
	@rpmbuild -bb SPECS/test.spec
# rpmbuild --target noarch -bb SPECS/test.spec

qemu-guest-agent:
	@rpmbuild -bb SPECS/qemu-guest-agent.spec

clean:
	rm -rf BUILD/* BUILDROOT/*

