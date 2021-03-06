Summary: Shared MIME information database
Name: shared-mime-info
Version: 0.70
Release: 4%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://freedesktop.org/Software/shared-mime-info
Source0: http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.bz2
Source1: defaults.list
# Generated with:
# for i in `totem-video-indexer -m | grep -v real` ; do if grep MimeType /home/hadess/Projects/Cvs/rhythmbox/data/rhythmbox.desktop.in.in | grep -q $i ; then echo "$i=totem.desktop;rhythmbox.desktop;" >> totem-defaults.list ; else echo "$i=totem.desktop;" >> totem-defaults.list ; fi  ; done
Source2: totem-defaults.list

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libxml2-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext
# For intltool:
BuildRequires: perl(XML::Parser) intltool
Requires: pkgconfig

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types of
files. Frequently, it is necessary to work out the correct MIME type for
a file. This is generally done by examining the file's name or contents,
and looking up the correct MIME type in a database.

%prep
%setup -q

%build

%configure --disable-update-mimedb
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/%{_datadir}/applications/defaults.list
cat %SOURCE2 >> $RPM_BUILD_ROOT/%{_datadir}/applications/defaults.list

## remove bogus translation files
## translations are already in the xml file installed
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*

%post
# Should fail, as it would mean a problem in the mime database
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README NEWS HACKING COPYING shared-mime-info-spec.xml
%{_bindir}/*
%dir %{_datadir}/mime/
%{_datadir}/mime/packages
%{_datadir}/applications/defaults.list
%{_datadir}/pkgconfig/*
%{_mandir}/man*/*

%changelog
* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 0.70-4
- Update some OO.o defaults, patch from Caolan McNamara
Related: rhbz#580232

* Thu Oct 08 2009 Bastien Nocera <bnocera@redhat.com> 0.70-2
- Fix brasero desktop filenames

* Tue Oct 06 2009 Bastien Nocera <bnocera@redhat.com> 0.70-1
- Update to 0.70

* Thu Sep 24 2009 - Caolán McNamara <caolanm@redhat.com> - 0.60-5
- Resolves: rhbz#508559 openoffice.org desktop files changed name

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 - Bastien Nocera <bnocera@redhat.com> - 0.60-3
- Remove Totem as handling Blu-ray and HD-DVD
- Use brasero-ncb.desktop instead of nautilus-cd-burner for blank devices
- Update media mime-types for Rhythmbox/Totem

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 - Bastien Nocera <bnocera@redhat.com> - 0.60-1
- Update to 0.60

* Mon Dec 15 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-6
- Update with comments from Orcan Ogetbil <orcanbahri@yahoo.com>

* Wed Nov 26 2008 - Julian Sikorski <belegdol[at]gmail[dot]com> - 0.51-5
- Fix text/plain, gedit installs gedit.desktop and not gnome-gedit.desktop

* Wed Oct 29 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-4
- Add patch to avoid picture CD being anything with a pictures directory
  (#459365)

* Thu Oct 02 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-3
- Use evince, not tetex-xdvi.desktop for DVI files (#465242)

* Mon Sep 01 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-2
- Use Firefox and not redhat-web as the default app for HTML files (#452184)

* Wed Jul 23 2008 - Bastien Nocera <bnocera@redhat.com> - 0.51-1
- Update to 0.51

* Tue Jul 22 2008 - Bastien Nocera <bnocera@redhat.com> - 0.50-1
- Update to 0.50

* Sat Jun 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.40-2
- update license tag

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.40-1
- Update to 0.40

* Mon May 12 2008 - Bastien Nocera <bnocera@redhat.com> - 0.30-1
- Update to 0.30

* Fri May  2 2008 David Zeuthen <davidz@redhat.com> - 0.23-9
- Fix defaults for x-content/image-dcf (#445032)

* Thu Apr 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.23-8
- Make mount-archive.desktop the default for iso images (#442960)

* Tue Apr 15 2008 Matthias Clasen <mclasen@redhat.com> - 0.23-7
- Update the desktop file name for Gimp, too

* Tue Apr 15 2008 Matthias Clasen <mclasen@redhat.com> - 0.23-6
- Change default for rpm to gpk-install-file (#442485)

* Thu Mar 27 2008 - Bastien Nocera <bnocera@redhat.com> - 0.23-5
- Make Totem the default for the mime-types it handles (#366101)
- And make sure Rhythmbox is the second default only for the mime-types
  it handles

* Thu Mar 20 2008 Matthias Clasen <mclasen@redhat.com> - 0.23-4
- Change default for rpm to pk-install-file

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.23-3
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Matthias Clasen <mclasen@redhat.com> - 0.23-2
- Add defaults for content types

* Tue Dec 18 2007 - Bastien Nocera <bnocera@redhat.com> - 0.23-1
- Update to 0.23

* Tue Nov 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.22-5
- Remove Totem as the default music/movie player, it will be the
  default for movies, as only it handles them, and Rhythmbox can
  handle missing plugins now

* Mon Nov 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.22-4
- Make Totem the default for the mime-types it handles (#366101)

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 0.22-3
- Rebuild for PPC toolchain bug
- BuildRequires: gawk

* Tue Aug 21 2007 - Bastien Nocera <bnocera@redhat.com> - 0.22-2
- Don't say that webcal files are handled by evolution-2.0, it can't
- Disable vCard mapping as well, as evolution doesn't handle it
  (See http://bugzilla.gnome.org/show_bug.cgi?id=309073)

* Mon Jul 30 2007 - Bastien Nocera <bnocera@redhat.com> - 0.22-1
- Update to 0.22

* Tue Apr 17 2007 - Bastien Nocera <bnocera@redhat.com> - 0.20-2
- Fix the dia association (#194313)

* Tue Feb 06 2007 - Bastien Nocera <bnocera@redhat.com> - 0.20-1
- Update to 0.20, and remove outdated patches

* Fri Nov 10 2006 Christopher Aillon <caillon@redhat.com> - 0.19-2
- Alias image/pdf to application/pdf

* Fri Aug 25 2006 Christopher Aillon <caillon@redhat.com> - 0.19-1
- Update to 0.19

* Wed Jul 26 2006 Matthias Clasen <mclasen@redhat.com> - 0.18-2
- add an inode/directory entry to defaults.list (#187021)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.18-1.1
- rebuild

* Wed Jul  5 2006 Kristian Høgsberg <krh@redhat.com> - 0.18-1
- Update to 0.18 and drop backported patches.

* Thu Jun 29 2006 Kristian Høgsberg <krh@redhat.com> - 0.17-3
- Adding PDF fix backported from CVS.

* Wed Mar 22 2006 Matthias Clasen <mclasen@redhat.com> - 0.17-2
- Backport upstream change to fix postscript vs. matlab confusion

* Thu Mar 16 2006 Matthias Clasen <mclasen@redhat.com> - 0.17-1
- Update to 0.17

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 0.16.cvs20060212-3
- add gthumb as fallback

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 0.16.cvs20060212-2
- make eog the default image viewer

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 0.16.cvs20060212-1
- Newer CVS snapshot

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.16.cvs20051219-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Caolan McNamara <caolanm@redhat.com> - 0.16.cvs20051219-2
- rh#179138# add openoffice.org as preferred app for oasis formats 

* Mon Dec 19 2005 Matthias Clasen <mclasen@redhat.com> - 0.16.cvs20051219-1
- Newer cvs snapshot

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Matthias Clasen <mclasen@redhat.com> - 0.16.cvs20051201-1
- Incorporate upstream changes

* Wed Nov 02 2005 John (J5) Palmieri <johnp@redhat.com> - 0.16.cvs20051018-2
- Change all refs of eog to gthumb in defaults.list

* Tue Oct 18 2005 Matthias Clasen <mclasen@redhat.com> - 0.16.cvs20051018-1
- Incorporate upstream changes

* Wed Oct 12 2005 Matthias Clasen <mclasen@redhat.com> - 0.16-6
- Add glade to defaults.list

* Mon Oct  3 2005 Matthias Clasen <mclasen@redhat.com> - 0.16-5
- Make sure Type1 fonts are recognized as such (#160909)

* Fri Jun 17 2005 David Zeuthen <davidz@redhat.com> - 0.16-4
- Add MIME-types for .pcf Cisco VPN settings files (fdo #3560)

* Fri May 20 2005 Dan Williams <dcbw@redhat.com> - 0.16-3
- Update OpenOffice.org desktop file names. #155353
- WordPerfect default now OOo Writer, since Abiword is in Extras

* Sun Apr  3 2005 David Zeuthen <davidz@redhat.com> - 0.16-2
- Make Evince the default for application/pdf and application/postscript
- Remove remaining references to gnome-ggv (application/x-gzpostscript and
  image/x-eps) as this is no longer in the distribution

* Fri Apr  1 2005 David Zeuthen <davidz@redhat.com> - 0.16-1
- Update to upstream release 0.16
- Drop all patches as they are in the new upstream release

* Wed Mar  9 2005 David Zeuthen <davidz@redhat.com> - 0.15-11
- Add mimetypes for OOo2 (#150546)

* Mon Oct 18 2004 Alexander Larsson <alexl@redhat.com> - 0.15-10
- Fix for mime sniffing on big-endian

* Thu Oct 14 2004 Colin Walters <walters@redhat.com> - 0.15-9
- Handle renaming of hxplay.desktop to realplay.desktop

* Wed Oct 13 2004 Matthias Clasen <mclasen@redhat.com> - 0.15-8
- Handle XUL files. #134122

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> - 0.15-7
- Make helix default for ogg and mp3, will switch wav/flac too 
  when support is added

* Wed Oct  6 2004 Alexander Larsson <alexl@redhat.com> - 0.15-6
- Change default pdf viewer to ggv

* Tue Sep  7 2004 Alexander Larsson <alexl@redhat.com> - 0.15-4
- Fixed evo desktop file reference in defaults.list

* Mon Sep  6 2004 Caolan McNamara <caolanm@redhat.com> - 0.15-3
- wpd can be opened in abiword, but not in openoffice.org (#114907)

* Fri Sep  3 2004 Alexander Larsson <alexl@redhat.com> - 0.15-2
- Add list of default apps (#131643)

* Mon Aug 30 2004 Jonathan Blandford <jrb@redhat.com> 0.15-1
- bump version

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 22 2004 Alex Larsson <alexl@redhat.com> 0.14-1
- update to 0.14

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Alexander Larsson <alexl@redhat.com> 0.13-1
- 0.13

* Fri Jan 16 2004 Alexander Larsson <alexl@redhat.com> mime-info
- Initial build.
