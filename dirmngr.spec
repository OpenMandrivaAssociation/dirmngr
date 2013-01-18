Summary:	Client for Managing/Downloading CRLs
Name:		dirmngr
Version:	1.1.0
Release:	5
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libksba-devel >= 0.9.11
BuildRequires:	libassuan-devel >= 0.9.3
BuildRequires:	pth-devel
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

