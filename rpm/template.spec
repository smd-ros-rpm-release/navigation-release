Name:           ros-indigo-amcl
Version:        1.11.14
Release:        0%{?dist}
Summary:        ROS amcl package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/amcl
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-map-server
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf

%description
amcl is a probabilistic localization system for a robot moving in 2D. It
implements the adaptive (or KLD-sampling) Monte Carlo localization approach (as
described by Dieter Fox), which uses a particle filter to track the pose of a
robot against a known map. This node is derived, with thanks, from Andrew
Howard's excellent 'amcl' Player driver.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

