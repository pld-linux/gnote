Summary:	Note-taking application
Summary(pl.UTF-8):	Aplikacja do zbierania notatek
Name:		gnote
Version:	40.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnote/40/%{name}-%{version}.tar.xz
# Source0-md5:	bb2aadaa7febd8734fddab222343bce3
URL:		https://wiki.gnome.org/Apps/Gnote
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.11
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.62
BuildRequires:	gspell-devel >= 1.8.0
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	gtkmm3-devel >= 3.22.20
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel >= 0.8
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glibmm >= 2.62
Requires:	gspell >= 1.8.0
Requires:	gtk+3 >= 3.22.20
Requires:	gtkmm3 >= 3.22.20
Requires:	hicolor-icon-theme
Requires:	libsecret >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abi_ver		40

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
	--disable-silent-rules
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnote
%attr(755,root,root) %{_libdir}/libgnote-%{abi_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnote-%{abi_ver}.so.2
%dir %{_libdir}/gnote
%dir %{_libdir}/gnote/addins
%dir %{_libdir}/gnote/addins/%{version}
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libbacklinks.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libbugzilla.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libexporttogtg.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libexporttohtml.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libfilesystemsyncservice.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libfixedwidth.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libgvfssyncservice.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libinserttimestamp.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libnotedirectorywatcher.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libnoteoftheday.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libprintnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libreadonly.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libreplacetitle.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libspecialnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libstatistics.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libstickynoteimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libtableofcontents.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libtodo.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libtomboyimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libunderline.so
%attr(755,root,root) %{_libdir}/gnote/addins/%{version}/libwebdavsyncservice.so
%{_libdir}/gnote/addins/%{version}/backlinks.desktop
%{_libdir}/gnote/addins/%{version}/bugzilla.desktop
%{_libdir}/gnote/addins/%{version}/exporttogtg.desktop
%{_libdir}/gnote/addins/%{version}/exporttohtml.desktop
%{_libdir}/gnote/addins/%{version}/filesystemsyncservice.desktop
%{_libdir}/gnote/addins/%{version}/fixedwidth.desktop
%{_libdir}/gnote/addins/%{version}/gvfssyncservice.desktop
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
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Gnote.search-provider.ini
%{_datadir}/gnote
%{_datadir}/metainfo/org.gnome.Gnote.appdata.xml
%{_desktopdir}/org.gnome.Gnote.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Gnote.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Gnote.svg
%{_mandir}/man1/gnote.1*
