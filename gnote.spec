Summary:	Note-taking application
Name:		gnote
Version:	3.6.1
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnote/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	ea4fea28aa7ed52bc918193678c6524b
URL:		http://live.gnome.org/Gnote
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtkmm3-devel
BuildRequires:	gtkspell-devel >= 2.0.9
BuildRequires:	itstool
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnote is a desktop note-taking application which is simple and easy to
use. It lets you organize your notes intelligently by allowing you to
easily link ideas together with Wiki style interconnects. It is a port
of Tomboy to C++ and consumes fewer resources.

%prep
%setup -q

%build
%configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} V=1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnote/addins/*/*.la

%find_lang gnote --with-gnome --with-omf

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
%attr(755,root,root) %{_libdir}/libgnote-3.6.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnote-3.6.so.0
%dir %{_libdir}/gnote
%dir %{_libdir}/gnote/addins
%dir %{_libdir}/gnote/addins/%{version}
%attr(755,root,root) %{_libdir}/gnote/addins/*/backlinks.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/bugzilla.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/exporttohtml.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/filesystemsyncservice.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/fixedwidth.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/inserttimestamp.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/notedirectorywatcher.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/noteoftheday.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/printnotes.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/replacetitle.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/stickynoteimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/tomboyimport.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/underline.so
%attr(755,root,root) %{_libdir}/gnote/addins/*/webdavsyncservice.so
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%{_datadir}/gnote
%{_desktopdir}/gnote.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gnote.1*
