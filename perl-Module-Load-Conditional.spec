%{?scl:%scl_package perl-Module-Load-Conditional}

Name:           %{?scl_prefix}perl-Module-Load-Conditional
Version:        0.68
Release:        1%{?dist}
Summary:        Looking up module information and loading at run-time
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Load-Conditional/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-Conditional-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(Locale::Maketext::Simple)
BuildRequires:  %{?scl_prefix}perl(Module::CoreList) >= 2.22
BuildRequires:  %{?scl_prefix}perl(Module::Load) >= 0.28
BuildRequires:  %{?scl_prefix}perl(Module::Metadata) >= 1.000005
BuildRequires:  %{?scl_prefix}perl(Params::Check)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(version) >= 0.69
# Tests:
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(warnings)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Config)
Requires:       %{?scl_prefix}perl(Module::CoreList) >= 2.22
Requires:       %{?scl_prefix}perl(Module::Load) >= 0.28
Requires:       %{?scl_prefix}perl(Module::Metadata) >= 1.000005
Requires:       %{?scl_prefix}perl(version) >= 0.69

# Filter under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Module::Load)$/d
%filter_from_requires /^%{?scl_prefix}perl(Module::Metadata)$/d
%filter_from_requires /^%{?scl_prefix}perl(version)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\((Module::Load|Module::Metadata|version)\\)$
%endif

%description
This module provides simple ways to query and possibly load any of the modules
you have installed on your system during run-time.

%prep
%setup -q -n Module-Load-Conditional-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Load::Conditional.3*

%changelog
* Fri Jul 29 2016 Paul Howarth <paul@city-fan.org> - 0.68-1
- Update to 0.68
  - Fix unconditional @INC localization

* Wed Jul 27 2016 Paul Howarth <paul@city-fan.org> - 0.66-1
- Update to 0.66
  - Add FORCE_SAFE_INC option to address CVE-2016-1238
- BR: perl-generators
- Simplify find command using -delete

* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.64-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-2
- Perl 5.22 rebuild

* Mon Jan 19 2015 Paul Howarth <paul@city-fan.org> - 0.64-1
- Update to 0.64
  - Resolve an edge-case with DEPRECATED (CPAN RT#101555)
- Make %%files list more explicit

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 0.62-1
- 0.62 bump

* Mon Jan 20 2014 Petr Pisar <ppisar@redhat.com> - 0.60-1
- 0.60 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 0.58-1
- 0.58 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 0.54-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.54-2
- Perl 5.18 rebuild

* Fri Jan 25 2013 Petr Pisar <ppisar@redhat.com> 0.54-1
- Specfile autogenerated by cpanspec 1.78.
