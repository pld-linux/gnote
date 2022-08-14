Summary:	Note-taking application
Summary(pl.UTF-8):	Aplikacja do zbierania notatek
Name:		gnote
Version:	42.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnote/42/%{name}-%{version}.tar.xz
# Source0-md5:	0f9ca46d947fcbf37c3eacb8ca40a37f
URL:		https://wiki.gnome.org/Apps/Gnote
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.62
BuildRequires:	gspell-devel >= 1.8.0
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	gtkmm3-devel >= 3.22.20
BuildRequires:	libsecret-devel >= 0.8
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.62
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glibmm >= 2.62
Requires:	gspell >= 1.8.0
Requires:	gtk+3 >= 3.22.20
Requires:	gtkmm3 >= 3.22.20
Requires:	hicolor-icon-theme
Requires:	libsecret >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abi_ver		42

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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgnote-%{abi_ver}.so

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
%attr(755,root,root) %ghost %{_libdir}/libgnote-%{abi_ver}.so.0
%dir %{_libdir}/gnote
%dir %{_libdir}/gnote/plugins
%dir %{_libdir}/gnote/plugins/%{abi_ver}
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libbacklinks.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libbugzilla.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libexporttogtg.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libexporttohtml.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libfilesystemsyncservice.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libfixedwidth.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libgvfssyncservice.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libinserttimestamp.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libnotedirectorywatcher.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libnoteoftheday.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libprintnotes.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libreadonly.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libreplacetitle.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libspecialnotes.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libstatistics.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libstickynoteimport.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libtableofcontents.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libtodo.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libtomboyimport.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libunderline.so
%attr(755,root,root) %{_libdir}/gnote/plugins/%{abi_ver}/libwebdavsyncservice.so
%{_libdir}/gnote/plugins/%{abi_ver}/backlinks.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/bugzilla.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/exporttogtg.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/exporttohtml.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/filesystemsyncservice.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/fixedwidth.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/gvfssyncservice.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/inserttimestamp.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/notedirectorywatcher.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/noteoftheday.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/printnotes.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/readonly.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/replacetitle.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/specialnotes.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/statistics.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/stickynoteimport.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/tableofcontents.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/todo.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/tomboyimport.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/underline.desktop
%{_libdir}/gnote/plugins/%{abi_ver}/webdavsyncservice.desktop
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Gnote.search-provider.ini
%{_datadir}/gnote
%{_datadir}/metainfo/org.gnome.Gnote.appdata.xml
%{_desktopdir}/org.gnome.Gnote.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Gnote.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Gnote.svg
%{_mandir}/man1/gnote.1*
