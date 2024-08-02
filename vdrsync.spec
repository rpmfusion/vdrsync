Name:           vdrsync
Version:        0.1.3
Release:        36.PRE1.050322%{?dist}
Summary:        Recording demultiplexer for VDR

License:        GPLv2
URL:            http://vdrsync.vdr-portal.de/
Source0:        %url/releases/%{name}-%{version}PRE1.tgz
Source1:        %url/releases/%{name}-050322.tgz
Patch0:         %{name}-recpath.patch
Patch1:         %{name}-panteltje.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
Requires:       dejavu-lgc-sans-fonts
Requires:       dvdauthor
Requires:       ffmpeg
Requires:       m2vrequantiser
Requires:       mjpegtools
Requires:       genisoimage

%description
vdrsync is a script that demultiplexes VDR recordings and tries to
synchronize the video and audio streams by addition or deletion of
audio data. It can also start some other tools at the end of a run to
generate a video DVD Directory structure that can be burned on a DVD.


%prep
%setup -q -n %{name}-%{version}PRE1 -a1
mv vdrsync-050322/*.pl vdrsync-050322/CHANGES . ; rm -rf  vdrsync-050322
%patch0
%patch1
for f in README.dvd-menu MANUAL-DE ; do
  iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done
rename .pl "" *.pl
mv dvd-menu vdrsync-dvd-menu
%{__perl} -pi -e "s/tcmplex_panteltje/'tcmplex-panteltje'/g" vdrsync
%{__perl} -pi -e 's/(vdrsync(_buffer)?)\.pl/$1/g' *
%{__perl} -pi -e 's/dvd-menu\.pl/vdrsync-dvd-menu/g' *
%{__perl} -pi -e 's|vdrsync_buffer|%{_datadir}/vdrsync/vdrsync_buffer|' \
  vdrsync
%{__perl} -pi -e 's|/usr/X11R6/lib/X11/fonts/truetype/arial.ttf|%{_datadir}/fonts/dejavu/DejaVuLGCSans.ttf| ; s/arial.ttf/DejaVuLGCSans.ttf/' *dvd-menu*


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 vdrsync vdrsync-dvd-menu $RPM_BUILD_ROOT%{_bindir}
install -Dpm 755 vdrsync_buffer \
  $RPM_BUILD_ROOT%{_datadir}/vdrsync/vdrsync_buffer


%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%doc BUGS CHANGES MANUAL README* TODO
%lang(de) %doc MANUAL-DE
%{_bindir}/vdrsync
%{_bindir}/vdrsync-dvd-menu
%{_datadir}/vdrsync/


%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.3-36.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.3-35.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.3-34.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.3-33.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.3-32.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-31.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-30.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-29.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-28.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-27.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-26.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.3-25.PRE1.050322
- Require genisoimage as mkisofs virtual provides was removed
- Remove Group tag and clean up

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.3-24.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.3-23.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.3-22.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Paul Howarth <paul@city-fan.org> - 0.1.3-21.PRE1.050322
- Perl 5.26 rebuild
- BR: perl-interpreter rather than just perl
  (https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules)

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.3-20.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Paul Howarth <paul@city-fan.org> - 0.1.3-19.PRE1.050322
- BR: perl and perl-generators
  (https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl)
- Use %%license where possible
- Drop %%defattr, redundant since rpm 4.4

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.1.3-18.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-17.PRE1.050322
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-16.PRE1.050322
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-15.PRE1.050322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Felix Kaechele <felix at fetzig dot org> - 0.1.3-14.PRE1.050322
- fixed fonts again

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.1.3-13.PRE1.050322
- rebuild for new F11 features

* Sat Jan 03 2009 Felix Kaechele <felix at fetzig dot org> - 0.1.3-12.PRE1.050322
- fixed font deps (once again)

* Mon Dec 15 2008 Felix Kaechele <felix at fetzig dot org> - 0.1.3-11.PRE1.050322
- fixed dependencies for new dejavu subpackages

* Fri Nov 28 2008 Felix Kaechele <felix at fetzig dot org> - 0.1.3-10.PRE1.050322
- renamed dvd-menu to vdrsync-dvd-menu due to conflict with dvd-slideshow

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.1.3-9.PRE1.050322
- rebuild

* Sun Nov 18 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-8.PRE1.050322
- Adjust font paths for dejavu-lgc-fonts 2.21+.

* Wed Aug 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-7.PRE1.050322
- Use DejaVu LGC fonts instead of Bitstream Vera.
- Fix some tcmplex-panteltje detection bugs.
- License: GPLv2

* Fri Oct 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-6.PRE1.050322
- Use m2vrequantiser instead of transcode.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.1.3-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-4.PRE1.050322
- Rebuild.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.1.3-3.PRE1.050322
- drop 1.lvn from release

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.3.PRE1.050322
- Fix missing dir separator in recording paths.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.2.PRE1.050322
- 050322 snapshot, cleanup patch applied upstream.

* Fri Aug 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.1.PRE1
- Convert docs to UTF-8.

* Sat Jun 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-0.2.PRE1
- Rebuild for FC4.

* Mon Jan 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-0.1.PRE1
- Update to 0.1.3PRE1.

* Sun Dec 26 2004 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2.2-0.2
- Remove unnecessary Epochs.

* Sun Nov 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.2.2-0.scop.1
- First build.
