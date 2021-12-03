# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility 
# bending of stud
# input data

from abaqus import *
from abaqusConstants import *

# CALL UNIT CELL FROM LIBRARY 
execfile("C:/temp/FEMML/S20/S20_003.py"), __main__.__dict__
execfile("C:/temp/FEMML/S20/S20_013.py"), __main__.__dict__
execfile("C:/temp/FEMML/S20/S20_017.py"), __main__.__dict__
execfile("C:/temp/FEMML/S20/S20_004.py"), __main__.__dict__

# CREATE INSTANCES
a = mdb.models["Model-1"].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-1", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-2", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-3", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-4", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-1", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-2", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-1", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-2", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-3", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-4", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-5", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-3", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-4", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-1", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-5", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-6", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-7", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-8", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-9", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-10", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-11", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-12", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-13", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-14", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-15", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-16", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-2", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-5", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-6", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-6", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-17", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-18", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-19", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-20", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-21", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-3", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-7", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-8", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-9", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-10", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-11", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-4", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-22", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-23", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-24", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-25", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-26", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-27", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-28", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-29", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-30", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-31", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-32", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-33", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-34", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-35", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-36", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-37", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-12", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-7", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-8", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-13", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-38", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-39", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-40", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-41", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-42", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-43", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-44", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-45", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-46", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-47", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-48", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-49", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-50", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-51", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-52", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-53", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-5", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-14", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-15", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-16", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-17", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-18", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-6", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-54", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-55", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-56", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-57", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-58", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-9", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-19", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-10", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-7", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-59", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-60", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-61", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-62", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-63", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-64", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-65", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-66", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-67", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-68", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-69", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-70", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_003"]
a.Instance(name="S20_003-8", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-11", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-12", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-20", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-21", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-22", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-23", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_004"]
a.Instance(name="S20_004-24", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-13", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_013"]
a.Instance(name="S20_013-14", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-71", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-72", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-73", part=p, dependent=ON)
p = mdb.models["Model-1"].parts["S20_017"]
a.Instance(name="S20_017-74", part=p, dependent=ON)

# TRABSLATE INSTANCES 
a.translate(instanceList=("S20_017-1", ), vector=(49.0, 0.0, 0))
a.translate(instanceList=("S20_017-2", ), vector=(98.0, 0.0, 0))
a.translate(instanceList=("S20_017-3", ), vector=(147.0, 0.0, 0))
a.translate(instanceList=("S20_017-4", ), vector=(196.0, 0.0, 0))
a.translate(instanceList=("S20_013-1", ), vector=(245.0, 0.0, 0))
a.translate(instanceList=("S20_013-2", ), vector=(294.0, 0.0, 0))
a.translate(instanceList=("S20_004-1", ), vector=(343.0, 0.0, 0))
a.translate(instanceList=("S20_004-2", ), vector=(392.0, 0.0, 0))
a.translate(instanceList=("S20_004-3", ), vector=(441.0, 0.0, 0))
a.translate(instanceList=("S20_004-4", ), vector=(490.0, 0.0, 0))
a.translate(instanceList=("S20_004-5", ), vector=(539.0, 0.0, 0))
a.translate(instanceList=("S20_013-3", ), vector=(588.0, 0.0, 0))
a.translate(instanceList=("S20_013-4", ), vector=(637.0, 0.0, 0))
a.translate(instanceList=("S20_003-1", ), vector=(686.0, 0.0, 0))
a.translate(instanceList=("S20_017-5", ), vector=(735.0, 0.0, 0))
a.translate(instanceList=("S20_017-6", ), vector=(784.0, 0.0, 0))
a.translate(instanceList=("S20_017-7", ), vector=(833.0, 0.0, 0))
a.translate(instanceList=("S20_017-8", ), vector=(882.0, 0.0, 0))
a.translate(instanceList=("S20_017-9", ), vector=(931.0, 0.0, 0))
a.translate(instanceList=("S20_017-10", ), vector=(980.0, 0.0, 0))
a.translate(instanceList=("S20_017-11", ), vector=(1029.0, 0.0, 0))
a.translate(instanceList=("S20_017-12", ), vector=(1078.0, 0.0, 0))
a.translate(instanceList=("S20_017-13", ), vector=(1127.0, 0.0, 0))
a.translate(instanceList=("S20_017-14", ), vector=(1176.0, 0.0, 0))
a.translate(instanceList=("S20_017-15", ), vector=(1225.0, 0.0, 0))
a.translate(instanceList=("S20_017-16", ), vector=(1274.0, 0.0, 0))
a.translate(instanceList=("S20_003-2", ), vector=(1323.0, 0.0, 0))
a.translate(instanceList=("S20_013-5", ), vector=(1372.0, 0.0, 0))
a.translate(instanceList=("S20_004-6", ), vector=(1421.0, 0.0, 0))
a.translate(instanceList=("S20_013-6", ), vector=(1470.0, 0.0, 0))
a.translate(instanceList=("S20_017-17", ), vector=(49.0, -49.0, 0))
a.translate(instanceList=("S20_017-18", ), vector=(98.0, -49.0, 0))
a.translate(instanceList=("S20_017-19", ), vector=(147.0, -49.0, 0))
a.translate(instanceList=("S20_017-20", ), vector=(196.0, -49.0, 0))
a.translate(instanceList=("S20_017-21", ), vector=(245.0, -49.0, 0))
a.translate(instanceList=("S20_003-3", ), vector=(294.0, -49.0, 0))
a.translate(instanceList=("S20_004-7", ), vector=(343.0, -49.0, 0))
a.translate(instanceList=("S20_004-8", ), vector=(392.0, -49.0, 0))
a.translate(instanceList=("S20_004-9", ), vector=(441.0, -49.0, 0))
a.translate(instanceList=("S20_004-10", ), vector=(490.0, -49.0, 0))
a.translate(instanceList=("S20_004-11", ), vector=(539.0, -49.0, 0))
a.translate(instanceList=("S20_003-4", ), vector=(588.0, -49.0, 0))
a.translate(instanceList=("S20_017-22", ), vector=(637.0, -49.0, 0))
a.translate(instanceList=("S20_017-23", ), vector=(686.0, -49.0, 0))
a.translate(instanceList=("S20_017-24", ), vector=(735.0, -49.0, 0))
a.translate(instanceList=("S20_017-25", ), vector=(784.0, -49.0, 0))
a.translate(instanceList=("S20_017-26", ), vector=(833.0, -49.0, 0))
a.translate(instanceList=("S20_017-27", ), vector=(882.0, -49.0, 0))
a.translate(instanceList=("S20_017-28", ), vector=(931.0, -49.0, 0))
a.translate(instanceList=("S20_017-29", ), vector=(980.0, -49.0, 0))
a.translate(instanceList=("S20_017-30", ), vector=(1029.0, -49.0, 0))
a.translate(instanceList=("S20_017-31", ), vector=(1078.0, -49.0, 0))
a.translate(instanceList=("S20_017-32", ), vector=(1127.0, -49.0, 0))
a.translate(instanceList=("S20_017-33", ), vector=(1176.0, -49.0, 0))
a.translate(instanceList=("S20_017-34", ), vector=(1225.0, -49.0, 0))
a.translate(instanceList=("S20_017-35", ), vector=(1274.0, -49.0, 0))
a.translate(instanceList=("S20_017-36", ), vector=(1323.0, -49.0, 0))
a.translate(instanceList=("S20_017-37", ), vector=(1372.0, -49.0, 0))
a.translate(instanceList=("S20_004-12", ), vector=(1421.0, -49.0, 0))
a.translate(instanceList=("S20_013-7", ), vector=(1470.0, -49.0, 0))
a.translate(instanceList=("S20_013-8", ), vector=(49.0, -98.0, 0))
a.translate(instanceList=("S20_004-13", ), vector=(98.0, -98.0, 0))
a.translate(instanceList=("S20_017-38", ), vector=(147.0, -98.0, 0))
a.translate(instanceList=("S20_017-39", ), vector=(196.0, -98.0, 0))
a.translate(instanceList=("S20_017-40", ), vector=(245.0, -98.0, 0))
a.translate(instanceList=("S20_017-41", ), vector=(294.0, -98.0, 0))
a.translate(instanceList=("S20_017-42", ), vector=(343.0, -98.0, 0))
a.translate(instanceList=("S20_017-43", ), vector=(392.0, -98.0, 0))
a.translate(instanceList=("S20_017-44", ), vector=(441.0, -98.0, 0))
a.translate(instanceList=("S20_017-45", ), vector=(490.0, -98.0, 0))
a.translate(instanceList=("S20_017-46", ), vector=(539.0, -98.0, 0))
a.translate(instanceList=("S20_017-47", ), vector=(588.0, -98.0, 0))
a.translate(instanceList=("S20_017-48", ), vector=(637.0, -98.0, 0))
a.translate(instanceList=("S20_017-49", ), vector=(686.0, -98.0, 0))
a.translate(instanceList=("S20_017-50", ), vector=(735.0, -98.0, 0))
a.translate(instanceList=("S20_017-51", ), vector=(784.0, -98.0, 0))
a.translate(instanceList=("S20_017-52", ), vector=(833.0, -98.0, 0))
a.translate(instanceList=("S20_017-53", ), vector=(882.0, -98.0, 0))
a.translate(instanceList=("S20_003-5", ), vector=(931.0, -98.0, 0))
a.translate(instanceList=("S20_004-14", ), vector=(980.0, -98.0, 0))
a.translate(instanceList=("S20_004-15", ), vector=(1029.0, -98.0, 0))
a.translate(instanceList=("S20_004-16", ), vector=(1078.0, -98.0, 0))
a.translate(instanceList=("S20_004-17", ), vector=(1127.0, -98.0, 0))
a.translate(instanceList=("S20_004-18", ), vector=(1176.0, -98.0, 0))
a.translate(instanceList=("S20_003-6", ), vector=(1225.0, -98.0, 0))
a.translate(instanceList=("S20_017-54", ), vector=(1274.0, -98.0, 0))
a.translate(instanceList=("S20_017-55", ), vector=(1323.0, -98.0, 0))
a.translate(instanceList=("S20_017-56", ), vector=(1372.0, -98.0, 0))
a.translate(instanceList=("S20_017-57", ), vector=(1421.0, -98.0, 0))
a.translate(instanceList=("S20_017-58", ), vector=(1470.0, -98.0, 0))
a.translate(instanceList=("S20_013-9", ), vector=(49.0, -147.0, 0))
a.translate(instanceList=("S20_004-19", ), vector=(98.0, -147.0, 0))
a.translate(instanceList=("S20_013-10", ), vector=(147.0, -147.0, 0))
a.translate(instanceList=("S20_003-7", ), vector=(196.0, -147.0, 0))
a.translate(instanceList=("S20_017-59", ), vector=(245.0, -147.0, 0))
a.translate(instanceList=("S20_017-60", ), vector=(294.0, -147.0, 0))
a.translate(instanceList=("S20_017-61", ), vector=(343.0, -147.0, 0))
a.translate(instanceList=("S20_017-62", ), vector=(392.0, -147.0, 0))
a.translate(instanceList=("S20_017-63", ), vector=(441.0, -147.0, 0))
a.translate(instanceList=("S20_017-64", ), vector=(490.0, -147.0, 0))
a.translate(instanceList=("S20_017-65", ), vector=(539.0, -147.0, 0))
a.translate(instanceList=("S20_017-66", ), vector=(588.0, -147.0, 0))
a.translate(instanceList=("S20_017-67", ), vector=(637.0, -147.0, 0))
a.translate(instanceList=("S20_017-68", ), vector=(686.0, -147.0, 0))
a.translate(instanceList=("S20_017-69", ), vector=(735.0, -147.0, 0))
a.translate(instanceList=("S20_017-70", ), vector=(784.0, -147.0, 0))
a.translate(instanceList=("S20_003-8", ), vector=(833.0, -147.0, 0))
a.translate(instanceList=("S20_013-11", ), vector=(882.0, -147.0, 0))
a.translate(instanceList=("S20_013-12", ), vector=(931.0, -147.0, 0))
a.translate(instanceList=("S20_004-20", ), vector=(980.0, -147.0, 0))
a.translate(instanceList=("S20_004-21", ), vector=(1029.0, -147.0, 0))
a.translate(instanceList=("S20_004-22", ), vector=(1078.0, -147.0, 0))
a.translate(instanceList=("S20_004-23", ), vector=(1127.0, -147.0, 0))
a.translate(instanceList=("S20_004-24", ), vector=(1176.0, -147.0, 0))
a.translate(instanceList=("S20_013-13", ), vector=(1225.0, -147.0, 0))
a.translate(instanceList=("S20_013-14", ), vector=(1274.0, -147.0, 0))
a.translate(instanceList=("S20_017-71", ), vector=(1323.0, -147.0, 0))
a.translate(instanceList=("S20_017-72", ), vector=(1372.0, -147.0, 0))
a.translate(instanceList=("S20_017-73", ), vector=(1421.0, -147.0, 0))
a.translate(instanceList=("S20_017-74", ), vector=(1470.0, -147.0, 0))

# CREATE STATIC STEP 
mdb.models["Model-1"].StaticStep(name="Step-1", previous="Initial", initialInc=0.01)

# CONSTRAINT THE NEIGHBOUR CELLS
# MAKE SURE THE NUMBER OF CONSTRAINTS ARE RIGHT  (29*4 + 56*2 = ??  CHECK)
region1=a.instances["S20_017-1"].surfaces["right"]
region2=a.instances["S20_017-2"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-1", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-2"].surfaces["right"]
region2=a.instances["S20_017-3"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-2", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-3"].surfaces["right"]
region2=a.instances["S20_017-4"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-3", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-4"].surfaces["right"]
region2=a.instances["S20_013-1"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-4", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-1"].surfaces["right"]
region2=a.instances["S20_013-2"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-5", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-2"].surfaces["right"]
region2=a.instances["S20_004-1"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-6", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-1"].surfaces["right"]
region2=a.instances["S20_004-2"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-7", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-2"].surfaces["right"]
region2=a.instances["S20_004-3"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-8", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-3"].surfaces["right"]
region2=a.instances["S20_004-4"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-9", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-4"].surfaces["right"]
region2=a.instances["S20_004-5"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-10", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-5"].surfaces["right"]
region2=a.instances["S20_013-3"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-11", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-3"].surfaces["right"]
region2=a.instances["S20_013-4"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-12", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-4"].surfaces["right"]
region2=a.instances["S20_003-1"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-13", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-1"].surfaces["right"]
region2=a.instances["S20_017-5"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-14", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-5"].surfaces["right"]
region2=a.instances["S20_017-6"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-15", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-6"].surfaces["right"]
region2=a.instances["S20_017-7"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-16", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-7"].surfaces["right"]
region2=a.instances["S20_017-8"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-17", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-8"].surfaces["right"]
region2=a.instances["S20_017-9"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-18", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-9"].surfaces["right"]
region2=a.instances["S20_017-10"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-19", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-10"].surfaces["right"]
region2=a.instances["S20_017-11"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-20", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-11"].surfaces["right"]
region2=a.instances["S20_017-12"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-21", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-12"].surfaces["right"]
region2=a.instances["S20_017-13"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-22", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-13"].surfaces["right"]
region2=a.instances["S20_017-14"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-23", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-14"].surfaces["right"]
region2=a.instances["S20_017-15"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-24", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-15"].surfaces["right"]
region2=a.instances["S20_017-16"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-25", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-16"].surfaces["right"]
region2=a.instances["S20_003-2"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-26", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-2"].surfaces["right"]
region2=a.instances["S20_013-5"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-27", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-5"].surfaces["right"]
region2=a.instances["S20_004-6"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-28", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-6"].surfaces["right"]
region2=a.instances["S20_013-6"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-29", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-17"].surfaces["right"]
region2=a.instances["S20_017-18"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-30", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-18"].surfaces["right"]
region2=a.instances["S20_017-19"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-31", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-19"].surfaces["right"]
region2=a.instances["S20_017-20"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-32", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-20"].surfaces["right"]
region2=a.instances["S20_017-21"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-33", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-21"].surfaces["right"]
region2=a.instances["S20_003-3"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-34", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-3"].surfaces["right"]
region2=a.instances["S20_004-7"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-35", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-7"].surfaces["right"]
region2=a.instances["S20_004-8"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-36", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-8"].surfaces["right"]
region2=a.instances["S20_004-9"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-37", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-9"].surfaces["right"]
region2=a.instances["S20_004-10"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-38", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-10"].surfaces["right"]
region2=a.instances["S20_004-11"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-39", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-11"].surfaces["right"]
region2=a.instances["S20_003-4"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-40", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-4"].surfaces["right"]
region2=a.instances["S20_017-22"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-41", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-22"].surfaces["right"]
region2=a.instances["S20_017-23"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-42", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-23"].surfaces["right"]
region2=a.instances["S20_017-24"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-43", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-24"].surfaces["right"]
region2=a.instances["S20_017-25"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-44", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-25"].surfaces["right"]
region2=a.instances["S20_017-26"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-45", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-26"].surfaces["right"]
region2=a.instances["S20_017-27"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-46", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-27"].surfaces["right"]
region2=a.instances["S20_017-28"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-47", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-28"].surfaces["right"]
region2=a.instances["S20_017-29"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-48", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-29"].surfaces["right"]
region2=a.instances["S20_017-30"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-49", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-30"].surfaces["right"]
region2=a.instances["S20_017-31"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-50", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-31"].surfaces["right"]
region2=a.instances["S20_017-32"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-51", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-32"].surfaces["right"]
region2=a.instances["S20_017-33"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-52", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-33"].surfaces["right"]
region2=a.instances["S20_017-34"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-53", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-34"].surfaces["right"]
region2=a.instances["S20_017-35"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-54", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-35"].surfaces["right"]
region2=a.instances["S20_017-36"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-55", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-36"].surfaces["right"]
region2=a.instances["S20_017-37"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-56", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-37"].surfaces["right"]
region2=a.instances["S20_004-12"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-57", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-12"].surfaces["right"]
region2=a.instances["S20_013-7"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-58", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-8"].surfaces["right"]
region2=a.instances["S20_004-13"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-59", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

region1=a.instances["S20_004-13"].surfaces["right"]
region2=a.instances["S20_017-38"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-60", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

region1=a.instances["S20_017-38"].surfaces["right"]
region2=a.instances["S20_017-39"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-61", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-39"].surfaces["right"]
region2=a.instances["S20_017-40"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-62", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-40"].surfaces["right"]
region2=a.instances["S20_017-41"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-63", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-41"].surfaces["right"]
region2=a.instances["S20_017-42"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-64", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-42"].surfaces["right"]
region2=a.instances["S20_017-43"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-65", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-43"].surfaces["right"]
region2=a.instances["S20_017-44"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-66", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-44"].surfaces["right"]
region2=a.instances["S20_017-45"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-67", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-45"].surfaces["right"]
region2=a.instances["S20_017-46"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-68", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-46"].surfaces["right"]
region2=a.instances["S20_017-47"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-69", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-47"].surfaces["right"]
region2=a.instances["S20_017-48"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-70", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-48"].surfaces["right"]
region2=a.instances["S20_017-49"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-71", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-49"].surfaces["right"]
region2=a.instances["S20_017-50"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-72", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-50"].surfaces["right"]
region2=a.instances["S20_017-51"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-73", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-51"].surfaces["right"]
region2=a.instances["S20_017-52"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-74", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-52"].surfaces["right"]
region2=a.instances["S20_017-53"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-75", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-53"].surfaces["right"]
region2=a.instances["S20_003-5"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-76", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-5"].surfaces["right"]
region2=a.instances["S20_004-14"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-77", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-14"].surfaces["right"]
region2=a.instances["S20_004-15"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-78", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-15"].surfaces["right"]
region2=a.instances["S20_004-16"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-79", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-16"].surfaces["right"]
region2=a.instances["S20_004-17"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-80", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-17"].surfaces["right"]
region2=a.instances["S20_004-18"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-81", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-18"].surfaces["right"]
region2=a.instances["S20_003-6"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-82", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-6"].surfaces["right"]
region2=a.instances["S20_017-54"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-83", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-54"].surfaces["right"]
region2=a.instances["S20_017-55"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-84", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-55"].surfaces["right"]
region2=a.instances["S20_017-56"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-85", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-56"].surfaces["right"]
region2=a.instances["S20_017-57"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-86", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-57"].surfaces["right"]
region2=a.instances["S20_017-58"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-87", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-9"].surfaces["right"]
region2=a.instances["S20_004-19"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-88", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-19"].surfaces["right"]
region2=a.instances["S20_013-10"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-89", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-10"].surfaces["right"]
region2=a.instances["S20_003-7"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-90", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-7"].surfaces["right"]
region2=a.instances["S20_017-59"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-91", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-59"].surfaces["right"]
region2=a.instances["S20_017-60"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-92", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-60"].surfaces["right"]
region2=a.instances["S20_017-61"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-93", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-61"].surfaces["right"]
region2=a.instances["S20_017-62"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-94", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-62"].surfaces["right"]
region2=a.instances["S20_017-63"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-95", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-63"].surfaces["right"]
region2=a.instances["S20_017-64"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-96", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-64"].surfaces["right"]
region2=a.instances["S20_017-65"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-97", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-65"].surfaces["right"]
region2=a.instances["S20_017-66"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-98", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-66"].surfaces["right"]
region2=a.instances["S20_017-67"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-99", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-67"].surfaces["right"]
region2=a.instances["S20_017-68"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-100", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-68"].surfaces["right"]
region2=a.instances["S20_017-69"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-101", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-69"].surfaces["right"]
region2=a.instances["S20_017-70"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-102", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-70"].surfaces["right"]
region2=a.instances["S20_003-8"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-103", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-8"].surfaces["right"]
region2=a.instances["S20_013-11"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-104", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-11"].surfaces["right"]
region2=a.instances["S20_013-12"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-105", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-12"].surfaces["right"]
region2=a.instances["S20_004-20"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-106", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-20"].surfaces["right"]
region2=a.instances["S20_004-21"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-107", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-21"].surfaces["right"]
region2=a.instances["S20_004-22"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-108", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-22"].surfaces["right"]
region2=a.instances["S20_004-23"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-109", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-23"].surfaces["right"]
region2=a.instances["S20_004-24"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-110", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-24"].surfaces["right"]
region2=a.instances["S20_013-13"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-111", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-13"].surfaces["right"]
region2=a.instances["S20_013-14"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-112", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-14"].surfaces["right"]
region2=a.instances["S20_017-71"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-113", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-71"].surfaces["right"]
region2=a.instances["S20_017-72"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-114", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-72"].surfaces["right"]
region2=a.instances["S20_017-73"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-115", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-73"].surfaces["right"]
region2=a.instances["S20_017-74"].surfaces["left"]
mdb.models["Model-1"].Tie(name= "Constraint-116", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-1"].surfaces["bottom"]
region2=a.instances["S20_017-17"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-117", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

region1=a.instances["S20_017-17"].surfaces["bottom"]
region2=a.instances["S20_013-8"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-1170", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)

region1=a.instances["S20_017-2"].surfaces["bottom"]
region2=a.instances["S20_017-18"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-118", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-3"].surfaces["bottom"]
region2=a.instances["S20_017-19"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-119", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-4"].surfaces["bottom"]
region2=a.instances["S20_017-20"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-120", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-1"].surfaces["bottom"]
region2=a.instances["S20_017-21"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-121", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-2"].surfaces["bottom"]
region2=a.instances["S20_003-3"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-122", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-1"].surfaces["bottom"]
region2=a.instances["S20_004-7"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-123", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-2"].surfaces["bottom"]
region2=a.instances["S20_004-8"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-124", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-3"].surfaces["bottom"]
region2=a.instances["S20_004-9"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-125", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-4"].surfaces["bottom"]
region2=a.instances["S20_004-10"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-126", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-5"].surfaces["bottom"]
region2=a.instances["S20_004-11"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-127", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-3"].surfaces["bottom"]
region2=a.instances["S20_003-4"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-128", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-4"].surfaces["bottom"]
region2=a.instances["S20_017-22"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-129", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-1"].surfaces["bottom"]
region2=a.instances["S20_017-23"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-130", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-5"].surfaces["bottom"]
region2=a.instances["S20_017-24"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-131", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-6"].surfaces["bottom"]
region2=a.instances["S20_017-25"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-132", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-7"].surfaces["bottom"]
region2=a.instances["S20_017-26"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-133", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-8"].surfaces["bottom"]
region2=a.instances["S20_017-27"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-134", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-9"].surfaces["bottom"]
region2=a.instances["S20_017-28"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-135", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-10"].surfaces["bottom"]
region2=a.instances["S20_017-29"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-136", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-11"].surfaces["bottom"]
region2=a.instances["S20_017-30"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-137", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-12"].surfaces["bottom"]
region2=a.instances["S20_017-31"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-138", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-13"].surfaces["bottom"]
region2=a.instances["S20_017-32"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-139", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-14"].surfaces["bottom"]
region2=a.instances["S20_017-33"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-140", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-15"].surfaces["bottom"]
region2=a.instances["S20_017-34"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-141", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-16"].surfaces["bottom"]
region2=a.instances["S20_017-35"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-142", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-2"].surfaces["bottom"]
region2=a.instances["S20_017-36"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-143", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-5"].surfaces["bottom"]
region2=a.instances["S20_017-37"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-144", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-6"].surfaces["bottom"]
region2=a.instances["S20_004-12"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-145", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-6"].surfaces["bottom"]
region2=a.instances["S20_013-7"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-1460", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-7"].surfaces["bottom"]
region2=a.instances["S20_017-58"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-1461", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-18"].surfaces["bottom"]
region2=a.instances["S20_004-13"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-147", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-19"].surfaces["bottom"]
region2=a.instances["S20_017-38"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-148", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-20"].surfaces["bottom"]
region2=a.instances["S20_017-39"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-149", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-21"].surfaces["bottom"]
region2=a.instances["S20_017-40"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-150", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-3"].surfaces["bottom"]
region2=a.instances["S20_017-41"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-151", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-7"].surfaces["bottom"]
region2=a.instances["S20_017-42"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-152", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-8"].surfaces["bottom"]
region2=a.instances["S20_017-43"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-153", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-9"].surfaces["bottom"]
region2=a.instances["S20_017-44"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-154", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-10"].surfaces["bottom"]
region2=a.instances["S20_017-45"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-155", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-11"].surfaces["bottom"]
region2=a.instances["S20_017-46"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-156", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-4"].surfaces["bottom"]
region2=a.instances["S20_017-47"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-157", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-22"].surfaces["bottom"]
region2=a.instances["S20_017-48"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-158", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-23"].surfaces["bottom"]
region2=a.instances["S20_017-49"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-159", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-24"].surfaces["bottom"]
region2=a.instances["S20_017-50"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-160", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-25"].surfaces["bottom"]
region2=a.instances["S20_017-51"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-161", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-26"].surfaces["bottom"]
region2=a.instances["S20_017-52"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-162", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-27"].surfaces["bottom"]
region2=a.instances["S20_017-53"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-163", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-28"].surfaces["bottom"]
region2=a.instances["S20_003-5"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-164", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-29"].surfaces["bottom"]
region2=a.instances["S20_004-14"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-165", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-30"].surfaces["bottom"]
region2=a.instances["S20_004-15"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-166", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-31"].surfaces["bottom"]
region2=a.instances["S20_004-16"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-167", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-32"].surfaces["bottom"]
region2=a.instances["S20_004-17"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-168", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-33"].surfaces["bottom"]
region2=a.instances["S20_004-18"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-169", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-34"].surfaces["bottom"]
region2=a.instances["S20_003-6"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-170", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-35"].surfaces["bottom"]
region2=a.instances["S20_017-54"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-171", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-36"].surfaces["bottom"]
region2=a.instances["S20_017-55"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-172", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-37"].surfaces["bottom"]
region2=a.instances["S20_017-56"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-173", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-12"].surfaces["bottom"]
region2=a.instances["S20_017-57"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-174", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-7"].surfaces["bottom"]
region2=a.instances["S20_017-58"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-175", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_013-8"].surfaces["bottom"]
region2=a.instances["S20_013-9"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-175", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-13"].surfaces["bottom"]
region2=a.instances["S20_004-19"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-176", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-38"].surfaces["bottom"]
region2=a.instances["S20_013-10"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-177", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-39"].surfaces["bottom"]
region2=a.instances["S20_003-7"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-178", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-40"].surfaces["bottom"]
region2=a.instances["S20_017-59"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-179", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-41"].surfaces["bottom"]
region2=a.instances["S20_017-60"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-180", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-42"].surfaces["bottom"]
region2=a.instances["S20_017-61"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-181", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-43"].surfaces["bottom"]
region2=a.instances["S20_017-62"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-182", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-44"].surfaces["bottom"]
region2=a.instances["S20_017-63"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-183", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-45"].surfaces["bottom"]
region2=a.instances["S20_017-64"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-184", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-46"].surfaces["bottom"]
region2=a.instances["S20_017-65"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-185", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-47"].surfaces["bottom"]
region2=a.instances["S20_017-66"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-186", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-48"].surfaces["bottom"]
region2=a.instances["S20_017-67"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-187", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-49"].surfaces["bottom"]
region2=a.instances["S20_017-68"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-188", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-50"].surfaces["bottom"]
region2=a.instances["S20_017-69"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-189", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-51"].surfaces["bottom"]
region2=a.instances["S20_017-70"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-190", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-52"].surfaces["bottom"]
region2=a.instances["S20_003-8"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-191", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-53"].surfaces["bottom"]
region2=a.instances["S20_013-11"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-192", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-5"].surfaces["bottom"]
region2=a.instances["S20_013-12"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-193", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-14"].surfaces["bottom"]
region2=a.instances["S20_004-20"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-194", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-15"].surfaces["bottom"]
region2=a.instances["S20_004-21"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-195", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-16"].surfaces["bottom"]
region2=a.instances["S20_004-22"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-196", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-17"].surfaces["bottom"]
region2=a.instances["S20_004-23"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-197", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_004-18"].surfaces["bottom"]
region2=a.instances["S20_004-24"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-198", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_003-6"].surfaces["bottom"]
region2=a.instances["S20_013-13"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-199", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-54"].surfaces["bottom"]
region2=a.instances["S20_013-14"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-200", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-55"].surfaces["bottom"]
region2=a.instances["S20_017-71"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-201", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-56"].surfaces["bottom"]
region2=a.instances["S20_017-72"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-202", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-57"].surfaces["bottom"]
region2=a.instances["S20_017-73"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-203", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
region1=a.instances["S20_017-58"].surfaces["bottom"]
region2=a.instances["S20_017-74"].surfaces["top"]
mdb.models["Model-1"].Tie(name= "Constraint-204", master=region1, slave=region2,
positionToleranceMethod=COMPUTED, adjust=OFF, tieRotations=ON, thickness=ON)
rp1 = mdb.models["Model-1"].rootAssembly.ReferencePoint(point=(-50.0, -25.0, 0.0))
rp1 = mdb.models["Model-1"].rootAssembly.ReferencePoint(point=(1550.0, -25.0, 0.0))

# BOUNDARY CONDITIONS
mdb.models['Model-1'].rootAssembly.Set(name='LEFT', nodes=
    mdb.models['Model-1'].rootAssembly.instances['S20_013-9'].nodes.getSequenceFromMask(
    mask=('[#0:4 #2 #0:3 #fff80000 #ffffffff #f ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_013-8'].nodes.getSequenceFromMask(
    mask=('[#0:4 #2 #0:3 #fff80000 #ffffffff #f ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_017-17'].nodes.getSequenceFromMask(
    mask=('[#0:4 #2 #0:4 #ff800000 #ffffffff #ff ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_017-1'].nodes.getSequenceFromMask(
    mask=('[#0:4 #2 #0:4 #ff800000 #ffffffff #ff ]', ), ))

mdb.models['Model-1'].rootAssembly.Set(name='RIGHT', nodes=
    mdb.models['Model-1'].rootAssembly.instances['S20_017-74'].nodes.getSequenceFromMask(
    mask=('[#0:6 #fffffff8 #1fffff ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_017-58'].nodes.getSequenceFromMask(
    mask=('[#0:6 #fffffff8 #1fffff ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_013-7'].nodes.getSequenceFromMask(
    mask=('[#0:5 #fffe0000 #ffffffff #7 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['S20_013-6'].nodes.getSequenceFromMask(
    mask=('[#0:5 #fffe0000 #ffffffff #7 ]', ), ))
	
	
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-1', region=mdb.models['Model-1'].rootAssembly.sets['LEFT'])
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['RIGHT'], u1=-5.0, 
    u2=UNSET, ur3=UNSET)
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-10', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-10'].submit(consistencyChecking=OFF)
