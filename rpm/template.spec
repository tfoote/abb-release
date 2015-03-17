Name:           ros-hydro-abb-irb5400-support
Version:        1.1.5
Release:        0%{?dist}
Summary:        ROS abb_irb5400_support package

Group:          Development/Libraries
License:        Apache2
URL:            http://ros.org/wiki/abb_irb5400_support
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-abb-driver
Requires:       ros-hydro-joint-state-publisher
Requires:       ros-hydro-robot-state-publisher
Requires:       ros-hydro-rviz
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roslaunch

%description
ROS-Industrial support for the ABB IRB 5400 (and variants). This package
contains configuration data, 3D models and launch files for ABB IRB 5400
manipulators. This currently includes the base model. Joint limits and max joint
velocities are based on the information in the ABB data sheets. All URDFs /
XACROs are based on the default motion and joint velocity limits, unless noted
otherwise (ie: no support for high speed joints, extended / limited motion
ranges or other options). Before using any of the configuration files and / or
meshes included in this package, be sure to check they are correct for the
particular robot model and configuration you intend to use them with.

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
* Tue Mar 17 2015 Shaun Edwards (Southwest Research Institute) <sedewards@swri.org> - 1.1.5-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Shaun Edwards (Southwest Research Institute) <sedewards@swri.org> - 1.1.4-0
- Autogenerated by Bloom

