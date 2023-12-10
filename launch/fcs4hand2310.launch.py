import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
#from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
#from launch_ros.substitutions import FindPackageShare
import xacro

def generate_launch_description():
    
    package_dir = get_package_share_directory("fcs4hand2310")
    xacro_file = os.path.join(package_dir, "urdf", "fcs4hand2310ctrl.xacro")
    conf_path = os.path.join(package_dir, "config", "ros2_controllers_fcs4hand2310.yaml")
    
    urdf_content = xacro.process_file(xacro_file).toprettyxml()

    ros2_control_params = {"robot_description": urdf_content,
                           "update_rate" : 20,
                           "joint_state_broadcaster_fcs4hand2310" : {  "type": "joint_state_broadcaster/JointStateBroadcaster" },
                           "joint_trajectory_controller_fcs4hand2310" : { "type": "joint_trajectory_controller/JointTrajectoryController"},
                           }

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{"robot_description": urdf_content}]),
        
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[ros2_control_params, conf_path ],
            output="both"),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster_fcs4hand2310"],),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_trajectory_controller_fcs4hand2310"],),

        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2"),
    ])
