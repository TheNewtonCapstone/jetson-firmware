#!/bin/bash
# shellcheck disable=SC1090,SC1091
set -e

# setup ros2 environment
source /opt/ros/"$ROS_DISTRO"/setup.bash --

# add sourcing to .bashrc
echo "source '/opt/ros/$ROS_DISTRO/setup.bash'" >> ~/.bashrc
echo "source '/home/newton/projects/newton-jetson-software/setup.bash'" >> ~/.bashrc

exec "$@"
