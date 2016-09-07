%define __jar_repack 0

Name:		artik-plugin-artik5
Summary:	ARTIK5 plugin files for fedora
Version:	1.0.0
Release:	1
Group:		System Environment/Base
License:	none

Source0:	%{name}-%{version}.tar.gz

%description
ARTIK5 plugin files for fedora

%prep
%setup -q

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/modules-load.d
cp scripts/modules-load.d/* %{buildroot}/etc/modules-load.d

mkdir -p %{buildroot}/etc/modprobe.d
cp scripts/modprobe.d/dhd.conf %{buildroot}/etc/modprobe.d/

mkdir -p  %{buildroot}/etc/bluetooth
cp -r prebuilt/bluetooth/etc/bluetooth/* %{buildroot}/etc/bluetooth

mkdir -p %{buildroot}/usr/lib/systemd/system
cp scripts/units/brcm-firmware.service %{buildroot}/usr/lib/systemd/system

# fstab
mkdir -p %{buildroot}/etc
cp prebuilt/fstab/fstab %{buildroot}/etc/

# audio
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/alsa
cp -r prebuilt/audio/audio_setting.sh %{buildroot}/usr/bin

# wifi
mkdir -p %{buildroot}/etc/wifi
cp -r prebuilt/wifi/* %{buildroot}/etc/wifi

# adbd
mkdir -p %{buildroot}/usr/bin
cp -r prebuilt/adbd/* %{buildroot}/usr/bin
cp -r prebuilt/rndis/* %{buildroot}/usr/bin

%package bluetooth
Summary:    bluetooth
Group:		System
Requires:	bluez
Requires:	artik-plugin-bluetooth-common

%description bluetooth
Bluetooth

%post bluetooth
systemctl enable brcm-firmware.service

%files bluetooth
%attr(0644,root,root) /usr/lib/systemd/system/brcm-firmware.service
/etc/bluetooth/*

%package fstab
Summary:    fstab
Group:		System
Requires:	artik-plugin

%description fstab
fstab

%files fstab
%attr(0644,root,root) /etc/fstab

%package audio
Summary:    audio
Group:		System
Requires:       pulseaudio
Requires:	artik-plugin-audio-common

%description audio
audio

%files audio
%attr(0755,root,root) /usr/bin/audio_setting.sh

%package wifi
Summary:    wifi
Group:		System

%description wifi
wifi

%files wifi
%attr(0644,root,root) /etc/modules-load.d/dhd.conf
%attr(0644,root,root) /etc/modprobe.d/dhd.conf
/etc/wifi/*

%package usb
Summary:    artik5 usb package
Group:		System
Requires:	artik-plugin-usb-common

%description usb
artik5 usb package

%files usb
%attr(0755,root,root) /usr/bin/start_adbd.sh
%attr(0755,root,root) /usr/bin/start_rndis.sh
