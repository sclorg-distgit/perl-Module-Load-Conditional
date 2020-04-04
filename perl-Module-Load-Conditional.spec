%{?scl:%scl_package perl-Module-Load-Conditional}

Name:           %{?scl_prefix}perl-Module-Load-Conditional
Version:        0.70
Release:        2%{?dist}
Summary:        Looking up module information / loading at run-time
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Load-Conditional
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Load-Conditional-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
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
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\((Module::Load|Module::Metadata|version)\\)$

%description
This module provides simple ways to query and possibly load any of the modules
you have installed on your system during run-time.

%prep
%setup -q -n Module-Load-Conditional-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Load::Conditional.3*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-2
- SCL

* Mon Nov 11 2019 Paul Howarth <paul@city-fan.org> - 0.70-1
- Update to 0.70
  - Protect ourselves from Module::Metadata parsing problems (CPAN RT#130939)
- Use author-independent source URL
- Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Paul Howarth <paul@city-fan.org> - 0.68-1
- Update to 0.68
  - Fix unconditional @INC localization

* Wed Jul 27 2016 Paul Howarth <paul@city-fan.org> - 0.66-1
- Update to 0.66
  - Add FORCE_SAFE_INC option to address CVE-2016-1238
- BR: perl-generators
- Simplify find command using -delete
- Drop legacy Group: tag

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
