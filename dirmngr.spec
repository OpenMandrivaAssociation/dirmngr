%define name    dirmngr
%define version 1.1.0
%define release 4

Summary:	Client for Managing/Downloading CRLs
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libksba-devel >= 0.9.11
BuildRequires:	libassuan-devel >= 0.9.3
BuildRequires:	libpth-devel
# won't work with ldap1
BuildRequires:	openldap-devel
BuildRequires:	texinfo
BuildRequires:	tetex-latex

%description
Dirmngr is a client for managing and downloading certificate revocation
lists (CRLs) for X509 certificates and for downloading the certificates
themselves. Dirmngr is usually invoked by gpgsm and in general not used
directly.

%prep
%setup -q -n %{name}-%{version}

%build
export LDFLAGS="-llber"
%configure2_5x --localstatedir=%{_var}
%make

make -C doc pdf

%check
make check

%install
mkdir -p %{buildroot}%{_sysconfdir}/dirmngr
mkdir -p %{buildroot}%{_sysconfdir}/dirmngr/trusted-certs
mkdir -p %{buildroot}%{_var}/run/dirmngr
mkdir -p %{buildroot}%{_var}/cache/dirmngr/crls.d
mkdir -p %{buildroot}%{_var}/lib/dirmngr/extra-certs

%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README* ChangeLog NEWS doc/dirmngr.pdf
%dir %{_sysconfdir}/dirmngr
%dir %{_sysconfdir}/dirmngr/trusted-certs
%{_bindir}/*
%{_infodir}/*.info*
%{_libexecdir}/dirmngr_ldap
%{_mandir}/man1/dirmngr-client.*
%{_mandir}/man1/dirmngr.*
%{_var}/run/dirmngr
%{_var}/cache/dirmngr
%{_var}/lib/dirmngr


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 663780
- mass rebuild

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 611876
- new version 1.1.0 final

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-0.rc1.2mdv2011.0
+ Revision: 604793
- rebuild

* Tue Mar 09 2010 Lonyai Gergely <aleph@mandriva.org> 1.1.0-0.rc1.1mdv2010.1
+ Revision: 516973
- 1.1.0-rc1

* Wed Jun 17 2009 Lonyai Gergely <aleph@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 386691
- update to 1.0.3

* Sun Jan 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2009.1
+ Revision: 331042
- update to new version 1.0.2

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2009.1
+ Revision: 316555
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 220627
- rebuild

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 173704
- new version
- add %%check section

* Mon Dec 24 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.1
+ Revision: 137460
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-4mdv2008.0
+ Revision: 85799
- rebuild for 2008
- Fedora license policy

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed Nov 29 2006 Andreas Hasenack <andreas@mandriva.com> 1.0.0-3mdv2007.0
+ Revision: 88665
- added manpages
- updated to version 1.0.0
- updated libassuan buildrequires

* Sat Sep 02 2006 Andreas Hasenack <andreas@mandriva.com> 0.9.5-3mdv2007.0
+ Revision: 59352
- bump release
- added tetex-latex to buildrequires, needed for doc build

* Fri Sep 01 2006 Andreas Hasenack <andreas@mandriva.com> 0.9.5-2mdv2007.0
+ Revision: 59241
- added lots of missing directories
- Import dirmngr

* Mon Jul 24 2006 Emmanuel Andry <eandry@mandriva.org> 0.9.5-1mdv2007.0
- 0.9.5
- drop patch0

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 0.9.3-2mdk
- rebuild for sparc

* Mon Jan 09 2006 Andreas Hasenack <andreas@mandriva.com> 0.9.3-1mdk
- updated to version 0.9.3

* Fri Sep 02 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.9.2-3mdk
- add BuildRequires: libpth-devel

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.9.2-2mdk
- Rebuild for libldap2.3

* Thu Aug 25 2005 Abel Cheung <deaddog@mandriva.org> 0.9.2-1mdk
- New release 0.9.2
- Sync patch0
- Drop patch1, ldap is searched in standard lib path now

* Thu Jun 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.5-4mdk 
- fix lib64 build

* Mon Feb 07 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.5.5-3mdk
- rebuild for ldap2.2_7

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5.5-2mdk
- rebuilt against new openldap libs

* Fri May 21 2004 Abel Cheung <deaddog@deaddog.org> 0.5.5-1mdk
- New version
- Regenerate patch0
- Include lang file

* Thu Apr 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.1-2mdk
- rebuild for new libgcrypt

* Sat Jan 24 2004 Abel Cheung <deaddog@deaddog.org> 0.5.1-1mdk
- New version
- Drop patch1 (dropped db4 support)

* Wed Dec 10 2003 Abel Cheung <deaddog@deaddog.org> 0.5.0-1mdk
- 0.5.0

