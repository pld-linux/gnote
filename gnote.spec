# TODO: build version without x11 support (plain GTK+) to use on Wayland or Broadway
#
Summary:	Note-taking application
Summary(pl.UTF-8):	Aplikacja do zbierania notatek
Name:		gnote
Version:	3.18.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnote/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	cc985a9ab0614ee2ed831a57cf260231
URL:		http://live.gnome.org/Gnote
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.11
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.32
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	gtkmm3-devel >= 3.10
BuildRequires:	gtkspell3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel >= 0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glibmm >= 2.32
Requires:	gtk+3 >= 3.10
Requires:	gtkmm3 >= 3.10
Requires:	hicolor-icon-theme
Requires:	libsecret >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnote is a desktop note-taking application which is simple and easy to
use. It lets you organize your notes intelligently by allowing you to
easily link ideas together with Wiki style interconnects. It is a port
of Tomboy to C++ and consumes fewer resources.

%description -l pl.UTF-8
Gnote to graficzna aplikacja do zbierania notatek. Jest prosta i łatwa
w użyciu; umożliwia organizowanie notatek w sposób inteligentny,
pozwalając łatwo łączyć pomysły przy użyciu połączeń w stylu Wiki.
Jest to port aplikacji Tomboy do C++, pochłaniający mniej zasobów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-x11-support
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnote/addins/%{version}/*.la

# remove -devel files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgnote.{la,so}

%find_lang gnote --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%files -f gnote.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnote
%attr(755,root,root) %{_libdir}/libgnote-3.18.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnote-3.18.so.0
%dir %{_libdir}/gnote
%dir %{_libdir}/gnote/addins
%dir %{_libdir}/gnote/addins/%{version}
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/backlinks.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/bugzilla.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/exporttogtg.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/exporttohtml.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/filesystemsyncservice.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/fixedwidth.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/inserttimestamp.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/notedirectorywatcher.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/noteoftheday.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/printnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/readonly.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/replacetitle.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/specialnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/statistics.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/stickynoteimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/tableofcontents.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/todo.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/tomboyimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/underline.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/webdavsyncservice.so
%{_libdir}/gnote/addins/%{version}/backlinks.desktop
%{_libdir}/gnote/addins/%{version}/bugzilla.desktop
%{_libdir}/gnote/addins/%{version}/exporttogtg.desktop
%{_libdir}/gnote/addins/%{version}/exporttohtml.desktop
%{_libdir}/gnote/addins/%{version}/filesystemsyncservice.desktop
%{_libdir}/gnote/addins/%{version}/fixedwidth.desktop
%{_libdir}/gnote/addins/%{version}/inserttimestamp.desktop
%{_libdir}/gnote/addins/%{version}/notedirectorywatcher.desktop
%{_libdir}/gnote/addins/%{version}/noteoftheday.desktop
%{_libdir}/gnote/addins/%{version}/printnotes.desktop
%{_libdir}/gnote/addins/%{version}/readonly.desktop
%{_libdir}/gnote/addins/%{version}/replacetitle.desktop
%{_libdir}/gnote/addins/%{version}/specialnotes.desktop
%{_libdir}/gnote/addins/%{version}/statistics.desktop
%{_libdir}/gnote/addins/%{version}/stickynoteimport.desktop
%{_libdir}/gnote/addins/%{version}/tableofcontents.desktop
%{_libdir}/gnote/addins/%{version}/todo.desktop
%{_libdir}/gnote/addins/%{version}/tomboyimport.desktop
%{_libdir}/gnote/addins/%{version}/underline.desktop
%{_libdir}/gnote/addins/%{version}/webdavsyncservice.desktop
%{_datadir}/appdata/gnote.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnote-search-provider.ini
%{_datadir}/gnote
%{_desktopdir}/gnote.desktop
%{_iconsdir}/hicolor/*x*/apps/gnote.png
%{_iconsdir}/hicolor/scalable/apps/gnote.svg
%{_mandir}/man1/gnote.1*
