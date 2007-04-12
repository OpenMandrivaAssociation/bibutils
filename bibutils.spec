%define		name bibutils
%define		version 3.24
%define		release %mkrel 3

Summary:	The bibutils program set interconverts between various bibliography formats

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.scripps.edu/~cdputnam/software/bibutils/%{name}_%{version}_src.tar.bz2

License:	GPL
Group:		Sciences/Computer science
Url:		http://www.scripps.edu/~cdputnam/software/bibutils/bibutils.html

Buildrequires:	tcsh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bibutils converts between bibliography formats
including BibTeX, RIS, Endnote (Refer), ISI,
COPAC, and Medline XML using a MODS v3.0 XML intermediate.

%prep
%setup -q -n %{name}_%{version}
./configure 

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
%make install INSTALLDIR=%{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

#%post

#%postun

%files
%defattr(-,root,root,0755)
%{_bindir}/*
%doc ChangeLog COPYING readme.txt

