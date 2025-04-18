import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/joffre/ros2_tutorials_ws/src/install/pubsub_package'
