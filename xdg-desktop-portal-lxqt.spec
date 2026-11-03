Name:          xdg-desktop-portal-lxqt
Version:       1.4.0
Release:       4
Summary:       A backend implementation for xdg-desktop-portal
License:       LGPLv2.1
Group:         Graphical desktop/KDE
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/xdg-desktop-portal-lxqt/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildSystem:   cmake
BuildRequires: cmake(fm-qt6) >= 2.5.0
BuildRequires: cmake(Qt6GuiPrivate)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6WindowSystem)

Requires: kf6-kwindowsystem
Suggests: kf6-kwindowsystem-backend-x11
Requires: xdg-desktop-portal
Requires: libfm-qt
Provides: xdg-desktop-portal-implementation

%description
A backend implementation for xdg-desktop-portal that is using
Qt/KF6/libfm-qt.

%files
%{_libexecdir}/xdg-desktop-portal-lxqt
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/xdg-desktop-portal/lxqt-portals.conf
%{_prefix}/lib/systemd/user/xdg-desktop-portal-lxqt.service
