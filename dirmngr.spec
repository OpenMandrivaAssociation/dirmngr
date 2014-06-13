Summary:	Client for Managing/Downloading CRLs
Name:		dirmngr
Version:	1.1.0
Release:	14
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
BuildRequires:	libassuan-devel >= 0.9.3
BuildRequires:	libksba-devel >= 0.9.11
BuildRequires:	openldap-devel
BuildRequires:	pth-devel
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	pkgconfig(libgcrypt)

%description
Dirmngr is a client for managing and downloading certificate revocation
lists (CRLs) for X509 certificates and for downloading the certificates
themselves. Dirmngr is usually invoked by gpgsm and in general not used
directly.

%prep
%setup -q
autoreconf -fiv

%build
export LDFLAGS="-llber"
%configure2_5x --localstatedir=%{_var}
%make


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
%doc README* ChangeLog NEWS
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

