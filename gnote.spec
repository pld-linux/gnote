Summary:	Note-taking application
Name:		gnote
Version:	0.7.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnote/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	c4e1a93896cb8610d2e08c72d41f1777
Patch0:		%{name}-gtk_deprecated.patch
Patch1:		%{name}-unicode.patch
URL:		http://live.gnome.org/Gnote
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2.20.0
BuildRequires:	gtkmm-devel >= 2.14.0
BuildRequires:	gtkspell-devel >= 2.0.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libpanelappletmm-devel >= 2.26.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnote is a desktop note-taking application which is simple and easy to
use. It lets you organize your notes intelligently by allowing you to
easily link ideas together with Wiki style interconnects. It is a port
of Tomboy to C++ and consumes fewer resources.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnote/addins/*/*.{a,la}

%find_lang gnote --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnote.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnote.schemas

%postun
%update_icon_cache hicolor

%files -f gnote.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnote
%attr(755,root,root) %{_libdir}/gnote-applet
%dir %{_libdir}/gnote
%dir %{_libdir}/gnote/addins
%dir %{_libdir}/gnote/addins/%{version}
%attr(755,root,root) %{_libdir}/gnote/addins/*/backlinks.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/bugzilla.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/exporttohtml.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/fixedwidth.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/inserttimestamp.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/libnoteoftheday.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/printnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/stickynoteimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/tomboyimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/underline.so
%{_libdir}/bonobo/servers/GNOME_GnoteApplet.server
%{_datadir}/gnote
%{_desktopdir}/gnote.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gnote.1*
%{_sysconfdir}/gconf/schemas/gnote.schemas
