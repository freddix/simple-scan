Summary:	Simple scanning utility
Name:		simple-scan
Version:	3.14.0
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://launchpad.net/simple-scan/3.14/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	d6355316444ecc1b2ab97864e145f71a
URL:		https://launchpad.net/simple-scan
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	colord-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vala
BuildRequires:	yelp-tools
Requires(post,postun):	glib-gio-gsettings
Requires:	gnome-icon-theme
Suggests:	colord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Scan is an easy-to-use application, designed to let users
connect their scanner and quickly have the image/document in an
appropriate format.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{mhr,sd}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md NEWS
%attr(755,root,root) %{_bindir}/simple-scan
%{_mandir}/man1/simple-scan.1*
%{_desktopdir}/simple-scan.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/simple-scan

