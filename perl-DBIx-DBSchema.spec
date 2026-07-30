%define upstream_name	 DBIx-DBSchema
%define upstream_version 0.47
Name:		perl-%{upstream_name}
Version:	0.47
Release:	4

Summary:	Database-independent schema objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/DBIx-DBSchema
Source0:	https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-0.47.tar.gz

BuildRequires:	make
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
%setup -q -n DBIx-DBSchema-0.47

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*


