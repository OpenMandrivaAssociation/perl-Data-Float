%define upstream_name    Data-Float
%define upstream_version 0.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Details of the floating point data type
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/Data-Float-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(integer)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
This module is about the native floating point numerical data type. A
floating point number is one of the types of datum that can appear in the
numeric part of a Perl scalar. This module supplies constants describing
the native floating point type, classification functions, and functions to
manipulate floating point values at a low level.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.11.0-3mdv2011.0
+ Revision: 657773
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 612361
- new version

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 573832
- import perl-Data-Float


