%define upstream_name    Data-Float

Name:       perl-%{upstream_name}
Version:    0.013
Release:    1

Summary:    Details of the floating point data type
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/Data-Float-%{version}.tar.gz

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
BuildRequires: make
BuildArch: noarch

%description
This module is about the native floating point numerical data type. A
floating point number is one of the types of datum that can appear in the
numeric part of a Perl scalar. This module supplies constants describing
the native floating point type, classification functions, and functions to
manipulate floating point values at a low level.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Build.PL prefix=%{_prefix} installdirs=vendor destdir=%{buildroot}

%build
./Build

%check
./Build test

%install
./Build install

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
