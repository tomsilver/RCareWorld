import os
import sys

# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from pyrcareworld.envs.base_env import RCareWorld
import pyrcareworld.utils.rfuniverse_utility as utility
from demo import urdf_path

# Initialize the environment
env = RCareWorld()

# Load the UR5 robot with native IK enabled
ur5 = env.LoadURDF(path=os.path.join(urdf_path, "UR5/ur5_robot.urdf"), native_ik=True)
ur5.SetTransform(position=[1, 0, 0])

# Load the Yumi robot with native IK disabled
yumi = env.LoadURDF(path=os.path.join(urdf_path, "yumi_description/urdf/yumi.urdf"), native_ik=False)
yumi.SetTransform(position=[2, 0, 0])

# Load the Kinova robot with native IK disabled
kinova = env.LoadURDF(path=os.path.join(urdf_path, "kinova_gen3/GEN3_URDF_V12.urdf"), native_ik=False)
kinova.SetTransform(position=[3, 0, 0])

# Perform an initial simulation step to update the environment
env.step()

# Perform a series of IK movements with the UR5 robot
ur5.IKTargetDoMove(position=[0, 0.5, 0], duration=0.1, relative=True)
ur5.WaitDo()

ur5.IKTargetDoMove(position=[0, 0, -0.5], duration=0.1, relative=True)
ur5.WaitDo()

ur5.IKTargetDoMove(position=[0, -0.2, 0.3], duration=0.1, relative=True)
ur5.IKTargetDoRotateQuaternion(
    quaternion=utility.UnityEulerToQuaternion([0, 90, 0]), duration=30, relative=True
)
ur5.WaitDo()

# End the environment session
env.Pend()
