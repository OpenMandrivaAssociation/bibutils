Summary:	The bibutils program set interconverts between various bibliography formats
Name:		bibutils
Version:	3.39
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://www.scripps.edu/~cdputnam/software/bibutils/bibutils.html
Source0:	http://www.scripps.edu/~cdputnam/software/bibutils/%{name}_%{version}_src.tar.bz2
Patch0:		%{name}-3.39-optflags.patch
Buildrequires:	tcsh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bibutils converts between bibliography formats
including BibTeX, RIS, Endnote (Refer), ISI,
COPAC, and Medline XML using a MODS v3.0 XML intermediate.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
./configure \
	--install-dir=%{_bindir}

%make

%check
pushd test
make
make test
popd

%install
rm -rf %{buildroot}
mkdir -p %buildroot%{_bindir}
%makeinstall_std INSTALLDIR=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

#%post

#%postun

%files
%defattr(-,root,root)
%doc ChangeLog readme.txt
%{_bindir}/*
