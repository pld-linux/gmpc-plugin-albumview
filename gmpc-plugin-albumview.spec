%define		source_name gmpc-albumview
Summary:	Album view plugin for Gnome Music Player Client
Name:		gmpc-plugin-albumview
Version:	0.20.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	8e2b0f3e0084fcf4844bef43de217a9e
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_ALBUMVIEW
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.10
BuildRequires:	gmpc-devel >= 0.19.2
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	libmpd-devel >= 0.18.100
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GMPC plugin shows your music collection in albums, it's showing album
covers with the artist and album name under it.

You can also filter out specific artists or albums and set the amount
of albums per row.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so

%dir %{_datadir}/gmpc-albumview
%dir %{_datadir}/gmpc-albumview/icons/Humanity/16x16/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/22x22/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/24x24/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/32x32/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/48x48/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/64x64/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/72x72/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/96x96/apps
%dir %{_datadir}/gmpc-albumview/icons/Humanity/scalable/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/128x128/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/16x16/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/22x22/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/24x24/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/32x32/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/48x48/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/64x64/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/72x72/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/96x96/apps
%dir %{_datadir}/gmpc-albumview/icons/hicolor/scalable/apps

%{_datadir}/gmpc-albumview/icons/Humanity/16x16/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/22x22/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/24x24/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/32x32/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/48x48/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/64x64/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/72x72/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/96x96/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/Humanity/scalable/apps/albumview.svg
%{_datadir}/gmpc-albumview/icons/hicolor/128x128/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/16x16/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/22x22/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/24x24/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/32x32/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/48x48/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/64x64/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/72x72/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/96x96/apps/albumview.png
%{_datadir}/gmpc-albumview/icons/hicolor/scalable/apps/albumview.svg
