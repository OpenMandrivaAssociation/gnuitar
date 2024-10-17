%define	name	gnuitar
%define	version	0.3.2
%define release	11

Name:		%{name}
Summary:	Real-time guitar effects
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
URL:		https://sourceforge.net/projects/gnuitar/files/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk2-devel

%description
This is a program for real-time sound effect processing. Probably could be
used not only for guitar. It has GTK interface and uses OSS sound driver.

Includes effects:
	o wah-wah
	o sustain
	o two flavours of distortion
	o reverberator, echo, delay
	o tremolo
	o vibrato
	o chorus/flanger
	o phasor
	o noise gate

%prep
%setup -q

%build
%configure2_5x --with-gtk2
%make
										
%install
rm -rf %{buildroot}
%makeinstall

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_bindir}/pasuspender %{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;AudioVideo;Audio;AudioVideoEditing;
EOF

#icons
mkdir -p %{buildroot}/%_liconsdir
cp %SOURCE1  %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
cp %SOURCE2  %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
cp %SOURCE3  %{buildroot}/%_miconsdir/%name.png

# house cleaning
rm -rf %{buildroot}%{_datadir}/doc
rm -rf %{buildroot}%{_datadir}/%name/win32

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING docs/*.html FAQ NEWS TODO
%attr(4755,root,root) %{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(0644,root,root,755)
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-10mdv2011.0
+ Revision: 610954
- rebuild

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.2-9mdv2010.1
+ Revision: 502945
- Fix url and clean spec file

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 06 2009 Emmanuel Andry <eandry@mandriva.org> 0.3.2-7mdv2009.1
+ Revision: 350228
- launch gnuitar through pasuspender, needs exclusive hardware access throug OSS

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-6mdv2009.0
+ Revision: 246494
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 14 2007 Funda Wang <fwang@mandriva.org> 0.3.2-4mdv2008.1
+ Revision: 119617
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - import gnuitar


* Sun Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.2-3mdv2007.0
- add forgotten xdg tag

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.2-2mdv2007.0
- xdg menu
- %%mkrel

* Wed May 11 2005 Austin Acton <austin@mandriva.org> 0.3.2-1mdk
- 0.3.2
- URL
- remove patch
- gtk2

* Tue Aug 5 2003 Austin Acton <aacton@yorku.ca> 0.3.1-2mdk
- DIRM

* Sun Jul 20 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3.1-1mdk
- 0.3.1
- added P0
- misc spec file fixes

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-1mdk
- 0.3.0

* Tue Mar 25 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2.1-1mdk
- 0.2.1

* Mon Feb 17 2003 Austin Acton <aacton@yorku.ca> 0.2.0-1mdk
- initial package
