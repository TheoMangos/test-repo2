from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='asccas',
            executable='Node1.py',
            name='node1'
        ),
        Node(
            package='asccas',
            executable='Node2.py',
            name='node2'
        ),

        # customize launch file below
        # asdsd
        # end launch file customization
    ])
