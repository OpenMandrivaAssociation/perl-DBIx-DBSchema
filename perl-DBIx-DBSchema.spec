%define module	DBIx-DBSchema
%define name	perl-%{module}
%define version 0.34
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Database-independent schema objects
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/DBIx/%{module}-%{version}.tar.gz
BuildRequires:  perl-DBI
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*


