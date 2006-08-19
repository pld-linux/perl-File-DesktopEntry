#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	DesktopEntry
Summary:	File::DesktopEntry - desktop files module
Summary(pl):	File::DesktopEntry - modu³ do plików .desktop
Name:		perl-File-DesktopEntry
Version:	0.02
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c97efa062c04bcb86a0a6a3707355d1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is used to work with .desktop files. The format of these
files is specified by the freedesktop "Desktop Entry" specification.

%description -l pl
Ten modu³ s³u¿y do pracy z plikami .desktop. Format tych plików jest
opisany w specyfikacji freedesktop "Desktop Entry".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/DesktopEntry.pm
%{_mandir}/man3/*
