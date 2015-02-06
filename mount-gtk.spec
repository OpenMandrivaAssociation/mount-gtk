Summary:	Front end for udisks
Name:		mount-gtk
Version:	1.2.0
Release:	2
License: 	GPLv2
Group:  	Graphical desktop/GNOME
URL:		http://mount-gtk.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:		mount-gtk_format-not-a-string.patch
Patch1:		mount-gtk-1.2.0_desktop.patch

BuildRequires:	pkgconfig(c++-gtk-utils-3-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libnotify)

Requires:	udisks

%description
The program is a front end to udisks and mount. It provides a means of 
mounting devices with udisks and mount through an easy to use graphical 
interface.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README BUGS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop



%changelog
* Wed May 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801202
- imported package mount-gtk

