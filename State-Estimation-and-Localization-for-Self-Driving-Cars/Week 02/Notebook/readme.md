## Implementation an Extended Kalman filter, which will estimate the trajectory of a vehicle using odometry, range and bearing measurements

In this assignment you will recursively estimate the position of a vehicle along a trajectory using available measurements and a motion model.

The vehicle is equipped with a very simple type of LIDAR sensor, which returns range and bearing measurements corresponding to individual landmarks in the environment. The global positions of the landmarks are assumed to be known beforehand. We will also assume known data association, that is, which measurment belong to which landmark.

