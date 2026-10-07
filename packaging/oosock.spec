Name:           oosock
Version:        0.1.0
Release:        1%{?dist}
Summary:        Diagnostic tool connecting to and hosting UNIX domain sockets with permissions check.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosock
Source0:        oosock-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosock is a sovereign, capability-bounded UNIX DOMAIN SOCKET written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosock
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosock-uninstall

%files
/usr/bin/oosock
/usr/bin/oosock-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
