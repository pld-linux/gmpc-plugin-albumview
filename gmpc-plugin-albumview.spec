%define		source_name gmpc-albumview
Summary:	Album view plugin for Gnome Music Player Client
Name:		gmpc-plugin-albumview
Version:	11.8.16
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	e7a587729561dceab4596adf7ed835e1
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_ALBUMVIEW
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.10
BuildRequires:	gmpc-devel >= 0.19.2
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libmpd-devel >= 0.18.100
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GMPC plugin shows your music collection in albums, it's showing
album covers with the artist and album name under it.

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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/albumviewplugin.so
%{_datadir}/gmpc-albumview
