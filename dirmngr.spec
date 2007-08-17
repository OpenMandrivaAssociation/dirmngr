%define version 1.0.0
%define rel 3
%define release %mkrel %rel

Name:		dirmngr
Version:	%{version}
Release:	%{release}
Summary:	Client for Managing/Downloading CRLs
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://www.gnupg.org/

Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libksba-devel >= 0.9.11
BuildRequires:	libassuan-devel >= 0.9.3
BuildRequires:	libpth-devel
# won't work with ldap1
Buildrequires:	openldap2-devel
# patch0
BuildRequires:	texinfo
BuildRequires:	tetex-latex

%description
Dirmngr is a client for managing and downloading certificate revocation
lists (CRLs) for X509 certificates and for downloading the certificates
themselves. Dirmngr is usually invoked by gpgsm and in general not used
directly.

%prep
%setup -q

%build
%configure2_5x --localstatedir=%{_var}
%make
make check

make -C doc pdf

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/dirmngr
mkdir -p %{buildroot}%{_sysconfdir}/dirmngr/trusted-certs
mkdir -p %{buildroot}%{_var}/run/dirmngr
mkdir -p %{buildroot}%{_var}/cache/dirmngr/crls.d
mkdir -p %{buildroot}%{_var}/lib/dirmngr/extra-certs

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

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



