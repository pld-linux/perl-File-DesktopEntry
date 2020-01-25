#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	DesktopEntry
Summary:	File::DesktopEntry - desktop files module
Summary(pl.UTF-8):	File::DesktopEntry - moduł do plików .desktop
Name:		perl-File-DesktopEntry
Version:	0.04
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc196bc1a4d6ca84953fee5a9cdaa629
URL:		http://search.cpan.org/dist/File-DesktopEntry/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-File-BaseDir >= 0.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is used to work with .desktop files. The format of these
files is specified by the freedesktop "Desktop Entry" specification.

%description -l pl.UTF-8
Ten moduł służy do pracy z plikami .desktop. Format tych plików jest
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
