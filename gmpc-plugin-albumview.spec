%define		source_name gmpc-albumview
Summary:	Album view plugin for Gnome Music Player Client
Name:		gmpc-plugin-albumview
Version:	0.20.0
Release:	2
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
%attr(755,root,root) %{_libdir}/gmpc/plugins/albumviewplugin.so
%{_datadir}/gmpc-albumview
