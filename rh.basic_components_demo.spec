###############################################################################
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
# 
# This file is part of REDHAWK basic_components_demo.
# 
# REDHAWK basic_components_demo is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# REDHAWK basic_components_demo is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
# 
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see http://www.gnu.org/licenses/.
###############################################################################

# RPM package for rh.basic_components_demo

%global _sdrroot /var/redhawk/sdr
%global _prefix %{_sdrroot}

Name: rh.basic_components_demo
Summary: Waveform rh.basic_components_demo
Version: 1.0.2
Release: 2%{?dist}
License: LGPLv3+
Group: REDHAWK/Waveforms
Source: %{name}-%{version}.tar.gz

# Require the controller whose SPD is referenced
Requires: rh.SigGen

# Require each referenced component
Requires: rh.SigGen rh.HardLimit rh.agc rh.fcalc rh.autocorrelate

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description

%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dom/waveforms/rh/basic_components_demo"
%__install -m 644 basic_components_demo.sad.xml $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/rh/basic_components_demo/basic_components_demo.sad.xml
%__install -m 644 basic_components_demo.sad_GDiagram $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/rh/basic_components_demo/basic_components_demo.sad_GDiagram

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/waveforms/rh
%dir %{_prefix}/dom/waveforms/rh/basic_components_demo
%{_prefix}/dom/waveforms/rh/basic_components_demo/basic_components_demo.sad.xml
%{_prefix}/dom/waveforms/rh/basic_components_demo/basic_components_demo.sad_GDiagram
