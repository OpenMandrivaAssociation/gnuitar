%define	name	gnuitar
%define	version	0.3.2
%define	release	%mkrel 10

Name:		%{name}
Summary:	Real-time guitar effects
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
URL:		http://sourceforge.net/projects/gnuitar/files/
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
