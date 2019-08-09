#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-license-maven-plugin
Version  : 1.10
Release  : 4
URL      : https://github.com/mojohaus/license-maven-plugin/archive/license-maven-plugin-1.10.tar.gz
Source0  : https://github.com/mojohaus/license-maven-plugin/archive/license-maven-plugin-1.10.tar.gz
Source1  : https://repo1.maven.org/maven2/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.jar
Source2  : https://repo1.maven.org/maven2/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-2-Clause BSD-3-Clause CDDL-1.0 EPL-1.0 EUPL-1.0 GFDL-1.3 GPL-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: mvn-license-maven-plugin-data = %{version}-%{release}

%description
# license-maven-plugin
This is the [license-maven-plugin](http://www.mojohaus.org/license-maven-plugin/).
[![Build Status](https://travis-ci.org/mojohaus/license-maven-plugin.svg?branch=master)](https://travis-ci.org/mojohaus/license-maven-plugin)
[![Maven Central](https://img.shields.io/maven-central/v/org.codehaus.mojo/license-maven-plugin.svg?label=Maven%20Central)](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.codehaus.mojo%22%20a%3A%license-maven-plugin%22)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mojohaus/license-maven-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![The GNU Lesser General Public License, Version 3.0](https://img.shields.io/badge/license-LGPL3-blue.svg)](http://www.gnu.org/licenses/lgpl-3.0.txt)

%package data
Summary: data components for the mvn-license-maven-plugin package.
Group: Data

%description data
data components for the mvn-license-maven-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.jar
/usr/share/java/.m2/repository/org/codehaus/mojo/license-maven-plugin/1.10/license-maven-plugin-1.10.pom
