%define _disable_ld_no_undefined 1

Summary:	Inter-convert between various bibliography formats
Name:		bibutils
Version:	4.12
Release:	2
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://www.scripps.edu/~cdputnam/software/bibutils/bibutils.html
Source0:	http://www.scripps.edu/~cdputnam/software/bibutils/%{name}_%{version}_src.tgz
Patch0:		add_missing_library.patch
Buildrequires:	tcsh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Bibutils converts between bibliography formats
including BibTeX, RIS, Endnote (Refer), ISI,
COPAC, and Medline XML using a MODS v3.0 XML intermediate.

%prep
%setup -q -n %{name}_%{version}
# sed -i.orig "s|/usr/local/bin|%{_bindir}|" configure
%patch0 -p1 -b .missinglib

%build
export CFLAGS="%{optflags}"
./configure --install-dir %_bindir --install-lib %_libdir

%make

%check
cd test
make
make test
cd ..

%install
rm -rf %{buildroot}
mkdir -p %buildroot%{_bindir}
%makeinstall_std INSTALLDIR=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog readme.txt
%{_bindir}/*


%changelog
* Wed Sep 28 2011 Stéphane Téletchéa <steletch@mandriva.org> 4.12-1mdv2012.0
+ Revision: 701653
- Use the corret flag for patch ...
- Update to 4.12
- Remove bashism
- Add missing libraries for the Makefile test

* Wed Sep 15 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.11-1mdv2011.0
+ Revision: 578715
- Update to 4.11

* Mon Sep 13 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.10-1mdv2011.0
+ Revision: 577888
- Update to 4.10
- Cosmetic English correction

* Mon Feb 15 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.8-1mdv2010.1
+ Revision: 506178
- Update output directory to workaround bogus configure file
- Update to 4.8

  + Thierry Vignaud <tv@mandriva.org>
    - better summary for rpmdrake

* Fri Jan 08 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.7-1mdv2010.1
+ Revision: 487578
- New version
- Removed obsolete patch references

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 4.6-1mdv2010.1
+ Revision: 463064
- update to new version 4.6

* Wed Sep 02 2009 Stéphane Téletchéa <steletch@mandriva.org> 4.3-1mdv2010.0
+ Revision: 424072
- Update to revision 4.3

* Sun Aug 10 2008 Emmanuel Andry <eandry@mandriva.org> 3.41-1mdv2009.0
+ Revision: 270349
- New version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.39-3mdv2009.0
+ Revision: 243257
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.39-1mdv2008.1
+ Revision: 105044
- compile with optflags (patch 0)
- add check and run tests
- spec file clean

* Fri Sep 07 2007 Stéphane Téletchéa <steletch@mandriva.org> 3.24-4mdv2008.0
+ Revision: 81844
- Rebuild


* Wed Aug 23 2006 St�phane T�letch�a <steletch@mandriva.org> 3.24-3
- bzip the archive, remove unused macros

* Tue May 16 2006 St�phane T�letch�a <steletch@mandriva.org> 3.24-2mdk
- add (t)csh buildrequires

* Tue May 09 2006 St�phane T�letch�a <steletch@free.fr> 3.24-1mdk
- Initial release

