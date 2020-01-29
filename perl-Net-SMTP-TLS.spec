#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Net
%define	pnam	SMTP-TLS
Summary:	Net::SMTP::TLS - An SMTP client supporting TLS and AUTH
Summary(pl.UTF-8):	Net::SMTP::TLS - klient SMTP obsługujący TLS i AUTH
Name:		perl-Net-SMTP-TLS
Version:	0.12
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a845eba3670e56a197ecd37f571d153a
Patch0:		io-socket-ssl.patch
Patch1:		multiple-attachments.patch
URL:		http://search.cpan.org/dist/Net-SMTP-TLS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-Net-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SMTP::TLS is a TLS and AUTH capable SMTP client which offers an
interface that users will find familiar from Net::SMTP. Net::SMTP::TLS
implements a subset of the methods provided by that module, but
certainly not (yet) a complete mirror image of that API.

%description -l pl.UTF-8
Net::SMTP::TLS to klient SMTP obsługujący TLS i AUTH, oferujący
użytkownikom interfejs zbliżony do Net::SMTP. Net::SMTP::TLS
implementuje podzbiór metod udostępnianych przez tamten moduł, ale
(jeszcze) nie pełne odzwierciedlenie tamtego API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/SMTP/*.pm
%{_mandir}/man3/*
