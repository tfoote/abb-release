Name:           ros-hydro-abb-driver
Version:        1.1.6
Release:        0%{?dist}
Summary:        ROS abb_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/abb_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-industrial-robot-client
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-industrial-robot-client
BuildRequires:  ros-hydro-simple-message

%description
ROS-Industrial nodes for interfacing with ABB robot controllers. This package
is part of the ROS-Industrial program and contains nodes for interfacing with
ABB industrial robot controllers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Mar 17 2015 Shaun Edwards <sedwards@swri.org> - 1.1.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Shaun Edwards <sedwards@swri.org> - 1.1.5-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Shaun Edwards <sedwards@swri.org> - 1.1.4-0
- Autogenerated by Bloom

