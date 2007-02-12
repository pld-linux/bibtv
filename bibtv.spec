# TODO:
# - fix it - seems to be broken
%include	/usr/lib/rpm/macros.perl
Summary:	Text based interactive searching
Summary(pl.UTF-8):   Interaktywne przeszukiwanie oparte na tekście
Name:		bibtv
Version:	0.2.7
Release:	0.9
License:	???
Group:		Applications
Source0:	http://www.ecst.csuchico.edu/~jacobsd/bib/archives/%{name}
# Source0-md5:	d86e2f751c83e1cf15317a1be45c2941
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text based interactive searching. Stores information in associative
arrays, so is extremely fast once the database is loaded, but it
requires a lot of memory for large databases.

%description -l pl.UTF-8
Interaktywne przeszukiwanie oparte na tekście. Program zapisuje
informacje w tablicach asocjacyjnych, więc po załadowaniu bazy jest
bardzo szybki, ale wymaga dużo pamięci dla dużych baz danych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
sed -i -e 's#/usr/local/bin/perl#/usr/bin/perl#' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
