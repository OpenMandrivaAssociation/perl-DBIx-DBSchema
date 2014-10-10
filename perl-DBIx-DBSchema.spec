%define upstream_name	 DBIx-DBSchema
%define upstream_version 0.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Database-independent schema objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
DBIx::DBSchema objects are collections of DBIx::DBSchema::Table objects and 
represent a database schema.
This module implements an OO-interface to database schemas. Using this module, 
you can create a database schema with an OO Perl interface. You can read the 
schema from an existing database. You can save the schema to disk and restore 
it a different process. Most importantly, DBIx::DBSchema can write SQL CREATE 
statements statements for different databases from a single source.

Currently supported databases are MySQL and PostgreSQL. Sybase support 
is partially implemented. DBIx::DBSchema will attempt to use generic SQL 
syntax for other databases. Assistance adding support for other databases 
is welcomed. See DBIx::DBSchema::DBD, "Driver Writer's Guide and Base Class".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.390.0-3mdv2011.0
+ Revision: 681360
- mass rebuild

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-2mdv2011.0
+ Revision: 528109
- rebuild
- update to 0.39

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 491626
- update to 0.38

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 405960
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.36-3mdv2009.0
+ Revision: 256586
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.1
+ Revision: 132043
- update to new version 0.36

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2008.1
+ Revision: 105893
- update to new version 0.35
- update to new version 0.35

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2008.0
+ Revision: 81170
- new schema

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2008.0
+ Revision: 46620
- update to new version 0.33


* Thu Nov 02 2006 Michael Scherer <misc@mandriva.org> 0.31-2mdv2007.0
+ Revision: 75496
- Rebuild
- Import perl-DBIx-DBSchema

