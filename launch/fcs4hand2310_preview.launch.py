import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
#from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
#from launch_ros.substitutions import FindPackageShare
#import xacro

def generate_launch_description():
    
    package_dir = get_package_share_directory("fcs4hand2310")
    urdf_file = os.path.join(package_dir, "urdf", "fcs4hand2310.urdf")
    
    urdf_content = "\n".join(open(urdf_file).readlines())

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{"robot_description": urdf_content}]),
        
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'),

        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2"),
    ])
