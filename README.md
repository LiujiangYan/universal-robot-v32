# universal-robot-v32

The existing ros industrial ur5 package is out-of-date and some files in ur_driver folder should be refined for the up-to-date controller verision 3.2.  
One could make it work by firstly cloning the officical package like following  
```
$ git clone --branch indigo-devel https://github.com/ros-industrial/universal_robot /[your-space-name]
```
and replace /[your-space-name]/src/universal_robot/ur_driver/src/ur_driver to this refined folder.
