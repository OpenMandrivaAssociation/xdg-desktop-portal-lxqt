Name:          xdg-desktop-portal-lxqt
Version:       1.0.1
Release:       1
Summary:       A backend implementation for xdg-desktop-portal
License:       LGPLv2.1
Group:         Graphical desktop/KDE
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/xdg-desktop-portal-lxqt/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: pkgconfig(libfm-qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6WindowSystem)

Requires:  kwindowsystem
Requires:  xdg-desktop-portal
Requires:  libfm-qt

%description
A backend implementation for xdg-desktop-portal that is using
Qt/KF5/libfm-qt.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_libexecdir}/xdg-desktop-portal-lxqt
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
