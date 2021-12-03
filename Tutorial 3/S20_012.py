
# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility 
# bending of stud
# input datafrom abaqus import *
from abaqusConstants import *
import __main__

def Macro5():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=100.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(1, 1),point2=(1, 2))
s.Line(point1=(1, 2),point2=(1, 3))
s.Line(point1=(1, 3),point2=(1, 4))
s.Line(point1=(1, 4),point2=(1, 5))
s.Line(point1=(1, 5),point2=(1, 6))
s.Line(point1=(1, 6),point2=(1, 7))
s.Line(point1=(1, 7),point2=(1, 8))
s.Line(point1=(1, 8),point2=(1, 9))
s.Line(point1=(1, 9),point2=(1, 10))
s.Line(point1=(1, 10),point2=(1, 11))
s.Line(point1=(1, 11),point2=(1, 12))
s.Line(point1=(1, 12),point2=(1, 13))
s.Line(point1=(1, 13),point2=(1, 14))
s.Line(point1=(1, 14),point2=(1, 15))
s.Line(point1=(1, 15),point2=(1, 16))
s.Line(point1=(1, 16),point2=(2, 16))
s.Line(point1=(2, 16),point2=(3, 16))
s.Line(point1=(3, 16),point2=(4, 17))
s.Line(point1=(4, 17),point2=(4, 18))
s.Line(point1=(4, 18),point2=(5, 19))
s.Line(point1=(5, 19),point2=(5, 20))
s.Line(point1=(5, 20),point2=(5, 21))
s.Line(point1=(5, 21),point2=(5, 22))
s.Line(point1=(5, 22),point2=(5, 23))
s.Line(point1=(5, 23),point2=(5, 24))
s.Line(point1=(5, 24),point2=(5, 25))
s.Line(point1=(5, 25),point2=(5, 26))
s.Line(point1=(5, 26),point2=(5, 27))
s.Line(point1=(5, 27),point2=(5, 28))
s.Line(point1=(5, 28),point2=(5, 29))
s.Line(point1=(5, 29),point2=(5, 30))
s.Line(point1=(5, 30),point2=(5, 31))
s.Line(point1=(5, 31),point2=(5, 32))
s.Line(point1=(5, 32),point2=(4, 33))
s.Line(point1=(4, 33),point2=(4, 34))
s.Line(point1=(4, 34),point2=(3, 35))
s.Line(point1=(3, 35),point2=(2, 35))
s.Line(point1=(2, 35),point2=(1, 35))
s.Line(point1=(1, 35),point2=(1, 36))
s.Line(point1=(1, 36),point2=(1, 37))
s.Line(point1=(1, 37),point2=(1, 38))
s.Line(point1=(1, 38),point2=(1, 39))
s.Line(point1=(1, 39),point2=(1, 40))
s.Line(point1=(1, 40),point2=(1, 41))
s.Line(point1=(1, 41),point2=(1, 42))
s.Line(point1=(1, 42),point2=(1, 43))
s.Line(point1=(1, 43),point2=(1, 44))
s.Line(point1=(1, 44),point2=(1, 45))
s.Line(point1=(1, 45),point2=(1, 46))
s.Line(point1=(1, 46),point2=(1, 47))
s.Line(point1=(1, 47),point2=(1, 48))
s.Line(point1=(1, 48),point2=(1, 49))
s.Line(point1=(1, 49),point2=(1, 50))
s.Line(point1=(1, 50),point2=(2, 50))
s.Line(point1=(2, 50),point2=(3, 50))
s.Line(point1=(3, 50),point2=(4, 50))
s.Line(point1=(4, 50),point2=(5, 50))
s.Line(point1=(5, 50),point2=(5, 49))
s.Line(point1=(5, 49),point2=(5, 48))
s.Line(point1=(5, 48),point2=(5, 47))
s.Line(point1=(5, 47),point2=(5, 46))
s.Line(point1=(5, 46),point2=(5, 45))
s.Line(point1=(5, 45),point2=(5, 44))
s.Line(point1=(5, 44),point2=(5, 43))
s.Line(point1=(5, 43),point2=(5, 42))
s.Line(point1=(5, 42),point2=(5, 41))
s.Line(point1=(5, 41),point2=(5, 40))
s.Line(point1=(5, 40),point2=(6, 39))
s.Line(point1=(6, 39),point2=(6, 38))
s.Line(point1=(6, 38),point2=(6, 37))
s.Line(point1=(6, 37),point2=(7, 36))
s.Line(point1=(7, 36),point2=(8, 36))
s.Line(point1=(8, 36),point2=(9, 37))
s.Line(point1=(9, 37),point2=(9, 36))
s.Line(point1=(9, 36),point2=(9, 35))
s.Line(point1=(9, 35),point2=(9, 34))
s.Line(point1=(9, 34),point2=(9, 33))
s.Line(point1=(9, 33),point2=(9, 32))
s.Line(point1=(9, 32),point2=(9, 31))
s.Line(point1=(9, 31),point2=(9, 30))
s.Line(point1=(9, 30),point2=(9, 29))
s.Line(point1=(9, 29),point2=(9, 28))
s.Line(point1=(9, 28),point2=(10, 27))
s.Line(point1=(10, 27),point2=(11, 27))
s.Line(point1=(11, 27),point2=(12, 28))
s.Line(point1=(12, 28),point2=(12, 29))
s.Line(point1=(12, 29),point2=(13, 30))
s.Line(point1=(13, 30),point2=(13, 31))
s.Line(point1=(13, 31),point2=(13, 32))
s.Line(point1=(13, 32),point2=(13, 33))
s.Line(point1=(13, 33),point2=(13, 34))
s.Line(point1=(13, 34),point2=(13, 35))
s.Line(point1=(13, 35),point2=(13, 36))
s.Line(point1=(13, 36),point2=(13, 37))
s.Line(point1=(13, 37),point2=(14, 37))
s.Line(point1=(14, 37),point2=(15, 38))
s.Line(point1=(15, 38),point2=(15, 39))
s.Line(point1=(15, 39),point2=(15, 40))
s.Line(point1=(15, 40),point2=(15, 41))
s.Line(point1=(15, 41),point2=(15, 42))
s.Line(point1=(15, 42),point2=(15, 43))
s.Line(point1=(15, 43),point2=(15, 44))
s.Line(point1=(15, 44),point2=(15, 45))
s.Line(point1=(15, 45),point2=(15, 46))
s.Line(point1=(15, 46),point2=(15, 47))
s.Line(point1=(15, 47),point2=(15, 48))
s.Line(point1=(15, 48),point2=(15, 49))
s.Line(point1=(15, 49),point2=(15, 50))
s.Line(point1=(15, 50),point2=(16, 50))
s.Line(point1=(16, 50),point2=(17, 50))
s.Line(point1=(17, 50),point2=(18, 50))
s.Line(point1=(18, 50),point2=(19, 50))
s.Line(point1=(19, 50),point2=(20, 50))
s.Line(point1=(20, 50),point2=(21, 50))
s.Line(point1=(21, 50),point2=(22, 50))
s.Line(point1=(22, 50),point2=(23, 50))
s.Line(point1=(23, 50),point2=(24, 50))
s.Line(point1=(24, 50),point2=(25, 50))
s.Line(point1=(25, 50),point2=(26, 50))
s.Line(point1=(26, 50),point2=(27, 50))
s.Line(point1=(27, 50),point2=(28, 50))
s.Line(point1=(28, 50),point2=(29, 50))
s.Line(point1=(29, 50),point2=(30, 50))
s.Line(point1=(30, 50),point2=(31, 50))
s.Line(point1=(31, 50),point2=(32, 50))
s.Line(point1=(32, 50),point2=(33, 50))
s.Line(point1=(33, 50),point2=(34, 50))
s.Line(point1=(34, 50),point2=(35, 50))
s.Line(point1=(35, 50),point2=(36, 50))
s.Line(point1=(36, 50),point2=(36, 49))
s.Line(point1=(36, 49),point2=(36, 48))
s.Line(point1=(36, 48),point2=(36, 47))
s.Line(point1=(36, 47),point2=(36, 46))
s.Line(point1=(36, 46),point2=(36, 45))
s.Line(point1=(36, 45),point2=(36, 44))
s.Line(point1=(36, 44),point2=(36, 43))
s.Line(point1=(36, 43),point2=(36, 42))
s.Line(point1=(36, 42),point2=(36, 41))
s.Line(point1=(36, 41),point2=(36, 40))
s.Line(point1=(36, 40),point2=(36, 39))
s.Line(point1=(36, 39),point2=(36, 38))
s.Line(point1=(36, 38),point2=(37, 37))
s.Line(point1=(37, 37),point2=(38, 37))
s.Line(point1=(38, 37),point2=(38, 36))
s.Line(point1=(38, 36),point2=(38, 35))
s.Line(point1=(38, 35),point2=(38, 34))
s.Line(point1=(38, 34),point2=(38, 33))
s.Line(point1=(38, 33),point2=(38, 32))
s.Line(point1=(38, 32),point2=(38, 31))
s.Line(point1=(38, 31),point2=(38, 30))
s.Line(point1=(38, 30),point2=(39, 29))
s.Line(point1=(39, 29),point2=(39, 28))
s.Line(point1=(39, 28),point2=(40, 27))
s.Line(point1=(40, 27),point2=(41, 27))
s.Line(point1=(41, 27),point2=(42, 28))
s.Line(point1=(42, 28),point2=(42, 29))
s.Line(point1=(42, 29),point2=(42, 30))
s.Line(point1=(42, 30),point2=(42, 31))
s.Line(point1=(42, 31),point2=(42, 32))
s.Line(point1=(42, 32),point2=(42, 33))
s.Line(point1=(42, 33),point2=(42, 34))
s.Line(point1=(42, 34),point2=(42, 35))
s.Line(point1=(42, 35),point2=(42, 36))
s.Line(point1=(42, 36),point2=(42, 37))
s.Line(point1=(42, 37),point2=(43, 36))
s.Line(point1=(43, 36),point2=(44, 36))
s.Line(point1=(44, 36),point2=(45, 37))
s.Line(point1=(45, 37),point2=(45, 38))
s.Line(point1=(45, 38),point2=(45, 39))
s.Line(point1=(45, 39),point2=(46, 40))
s.Line(point1=(46, 40),point2=(46, 41))
s.Line(point1=(46, 41),point2=(46, 42))
s.Line(point1=(46, 42),point2=(46, 43))
s.Line(point1=(46, 43),point2=(46, 44))
s.Line(point1=(46, 44),point2=(46, 45))
s.Line(point1=(46, 45),point2=(46, 46))
s.Line(point1=(46, 46),point2=(46, 47))
s.Line(point1=(46, 47),point2=(46, 48))
s.Line(point1=(46, 48),point2=(46, 49))
s.Line(point1=(46, 49),point2=(46, 50))
s.Line(point1=(46, 50),point2=(47, 50))
s.Line(point1=(47, 50),point2=(48, 50))
s.Line(point1=(48, 50),point2=(49, 50))
s.Line(point1=(49, 50),point2=(50, 50))
s.Line(point1=(50, 50),point2=(50, 49))
s.Line(point1=(50, 49),point2=(50, 48))
s.Line(point1=(50, 48),point2=(50, 47))
s.Line(point1=(50, 47),point2=(50, 46))
s.Line(point1=(50, 46),point2=(50, 45))
s.Line(point1=(50, 45),point2=(50, 44))
s.Line(point1=(50, 44),point2=(50, 43))
s.Line(point1=(50, 43),point2=(50, 42))
s.Line(point1=(50, 42),point2=(50, 41))
s.Line(point1=(50, 41),point2=(50, 40))
s.Line(point1=(50, 40),point2=(50, 39))
s.Line(point1=(50, 39),point2=(50, 38))
s.Line(point1=(50, 38),point2=(50, 37))
s.Line(point1=(50, 37),point2=(50, 36))
s.Line(point1=(50, 36),point2=(50, 35))
s.Line(point1=(50, 35),point2=(49, 35))
s.Line(point1=(49, 35),point2=(48, 35))
s.Line(point1=(48, 35),point2=(47, 34))
s.Line(point1=(47, 34),point2=(47, 33))
s.Line(point1=(47, 33),point2=(46, 32))
s.Line(point1=(46, 32),point2=(46, 31))
s.Line(point1=(46, 31),point2=(46, 30))
s.Line(point1=(46, 30),point2=(46, 29))
s.Line(point1=(46, 29),point2=(46, 28))
s.Line(point1=(46, 28),point2=(46, 27))
s.Line(point1=(46, 27),point2=(46, 26))
s.Line(point1=(46, 26),point2=(46, 25))
s.Line(point1=(46, 25),point2=(46, 24))
s.Line(point1=(46, 24),point2=(46, 23))
s.Line(point1=(46, 23),point2=(46, 22))
s.Line(point1=(46, 22),point2=(46, 21))
s.Line(point1=(46, 21),point2=(46, 20))
s.Line(point1=(46, 20),point2=(46, 19))
s.Line(point1=(46, 19),point2=(47, 18))
s.Line(point1=(47, 18),point2=(47, 17))
s.Line(point1=(47, 17),point2=(48, 16))
s.Line(point1=(48, 16),point2=(49, 16))
s.Line(point1=(49, 16),point2=(50, 16))
s.Line(point1=(50, 16),point2=(50, 15))
s.Line(point1=(50, 15),point2=(50, 14))
s.Line(point1=(50, 14),point2=(50, 13))
s.Line(point1=(50, 13),point2=(50, 12))
s.Line(point1=(50, 12),point2=(50, 11))
s.Line(point1=(50, 11),point2=(50, 10))
s.Line(point1=(50, 10),point2=(50, 9))
s.Line(point1=(50, 9),point2=(50, 8))
s.Line(point1=(50, 8),point2=(50, 7))
s.Line(point1=(50, 7),point2=(50, 6))
s.Line(point1=(50, 6),point2=(50, 5))
s.Line(point1=(50, 5),point2=(50, 4))
s.Line(point1=(50, 4),point2=(50, 3))
s.Line(point1=(50, 3),point2=(50, 2))
s.Line(point1=(50, 2),point2=(50, 1))
s.Line(point1=(50, 1),point2=(49, 1))
s.Line(point1=(49, 1),point2=(48, 1))
s.Line(point1=(48, 1),point2=(47, 1))
s.Line(point1=(47, 1),point2=(46, 1))
s.Line(point1=(46, 1),point2=(46, 2))
s.Line(point1=(46, 2),point2=(46, 3))
s.Line(point1=(46, 3),point2=(46, 4))
s.Line(point1=(46, 4),point2=(46, 5))
s.Line(point1=(46, 5),point2=(46, 6))
s.Line(point1=(46, 6),point2=(46, 7))
s.Line(point1=(46, 7),point2=(46, 8))
s.Line(point1=(46, 8),point2=(46, 9))
s.Line(point1=(46, 9),point2=(46, 10))
s.Line(point1=(46, 10),point2=(46, 11))
s.Line(point1=(46, 11),point2=(45, 12))
s.Line(point1=(45, 12),point2=(45, 13))
s.Line(point1=(45, 13),point2=(45, 14))
s.Line(point1=(45, 14),point2=(44, 15))
s.Line(point1=(44, 15),point2=(43, 15))
s.Line(point1=(43, 15),point2=(42, 14))
s.Line(point1=(42, 14),point2=(42, 15))
s.Line(point1=(42, 15),point2=(42, 16))
s.Line(point1=(42, 16),point2=(42, 17))
s.Line(point1=(42, 17),point2=(42, 18))
s.Line(point1=(42, 18),point2=(42, 19))
s.Line(point1=(42, 19),point2=(42, 20))
s.Line(point1=(42, 20),point2=(42, 21))
s.Line(point1=(42, 21),point2=(42, 22))
s.Line(point1=(42, 22),point2=(42, 23))
s.Line(point1=(42, 23),point2=(41, 24))
s.Line(point1=(41, 24),point2=(40, 24))
s.Line(point1=(40, 24),point2=(39, 23))
s.Line(point1=(39, 23),point2=(39, 22))
s.Line(point1=(39, 22),point2=(38, 21))
s.Line(point1=(38, 21),point2=(38, 20))
s.Line(point1=(38, 20),point2=(38, 19))
s.Line(point1=(38, 19),point2=(38, 18))
s.Line(point1=(38, 18),point2=(38, 17))
s.Line(point1=(38, 17),point2=(38, 16))
s.Line(point1=(38, 16),point2=(38, 15))
s.Line(point1=(38, 15),point2=(38, 14))
s.Line(point1=(38, 14),point2=(37, 14))
s.Line(point1=(37, 14),point2=(36, 13))
s.Line(point1=(36, 13),point2=(36, 12))
s.Line(point1=(36, 12),point2=(36, 11))
s.Line(point1=(36, 11),point2=(36, 10))
s.Line(point1=(36, 10),point2=(36, 9))
s.Line(point1=(36, 9),point2=(36, 8))
s.Line(point1=(36, 8),point2=(36, 7))
s.Line(point1=(36, 7),point2=(36, 6))
s.Line(point1=(36, 6),point2=(36, 5))
s.Line(point1=(36, 5),point2=(36, 4))
s.Line(point1=(36, 4),point2=(36, 3))
s.Line(point1=(36, 3),point2=(36, 2))
s.Line(point1=(36, 2),point2=(36, 1))
s.Line(point1=(36, 1),point2=(35, 1))
s.Line(point1=(35, 1),point2=(34, 1))
s.Line(point1=(34, 1),point2=(33, 1))
s.Line(point1=(33, 1),point2=(32, 1))
s.Line(point1=(32, 1),point2=(31, 1))
s.Line(point1=(31, 1),point2=(30, 1))
s.Line(point1=(30, 1),point2=(29, 1))
s.Line(point1=(29, 1),point2=(28, 1))
s.Line(point1=(28, 1),point2=(27, 1))
s.Line(point1=(27, 1),point2=(26, 1))
s.Line(point1=(26, 1),point2=(25, 1))
s.Line(point1=(25, 1),point2=(24, 1))
s.Line(point1=(24, 1),point2=(23, 1))
s.Line(point1=(23, 1),point2=(22, 1))
s.Line(point1=(22, 1),point2=(21, 1))
s.Line(point1=(21, 1),point2=(20, 1))
s.Line(point1=(20, 1),point2=(19, 1))
s.Line(point1=(19, 1),point2=(18, 1))
s.Line(point1=(18, 1),point2=(17, 1))
s.Line(point1=(17, 1),point2=(16, 1))
s.Line(point1=(16, 1),point2=(15, 1))
s.Line(point1=(15, 1),point2=(15, 2))
s.Line(point1=(15, 2),point2=(15, 3))
s.Line(point1=(15, 3),point2=(15, 4))
s.Line(point1=(15, 4),point2=(15, 5))
s.Line(point1=(15, 5),point2=(15, 6))
s.Line(point1=(15, 6),point2=(15, 7))
s.Line(point1=(15, 7),point2=(15, 8))
s.Line(point1=(15, 8),point2=(15, 9))
s.Line(point1=(15, 9),point2=(15, 10))
s.Line(point1=(15, 10),point2=(15, 11))
s.Line(point1=(15, 11),point2=(15, 12))
s.Line(point1=(15, 12),point2=(15, 13))
s.Line(point1=(15, 13),point2=(14, 14))
s.Line(point1=(14, 14),point2=(13, 14))
s.Line(point1=(13, 14),point2=(13, 15))
s.Line(point1=(13, 15),point2=(13, 16))
s.Line(point1=(13, 16),point2=(13, 17))
s.Line(point1=(13, 17),point2=(13, 18))
s.Line(point1=(13, 18),point2=(13, 19))
s.Line(point1=(13, 19),point2=(13, 20))
s.Line(point1=(13, 20),point2=(13, 21))
s.Line(point1=(13, 21),point2=(12, 22))
s.Line(point1=(12, 22),point2=(12, 23))
s.Line(point1=(12, 23),point2=(11, 24))
s.Line(point1=(11, 24),point2=(10, 24))
s.Line(point1=(10, 24),point2=(9, 23))
s.Line(point1=(9, 23),point2=(9, 22))
s.Line(point1=(9, 22),point2=(9, 21))
s.Line(point1=(9, 21),point2=(9, 20))
s.Line(point1=(9, 20),point2=(9, 19))
s.Line(point1=(9, 19),point2=(9, 18))
s.Line(point1=(9, 18),point2=(9, 17))
s.Line(point1=(9, 17),point2=(9, 16))
s.Line(point1=(9, 16),point2=(9, 15))
s.Line(point1=(9, 15),point2=(9, 14))
s.Line(point1=(9, 14),point2=(8, 15))
s.Line(point1=(8, 15),point2=(7, 15))
s.Line(point1=(7, 15),point2=(6, 14))
s.Line(point1=(6, 14),point2=(6, 13))
s.Line(point1=(6, 13),point2=(6, 12))
s.Line(point1=(6, 12),point2=(5, 11))
s.Line(point1=(5, 11),point2=(5, 10))
s.Line(point1=(5, 10),point2=(5, 9))
s.Line(point1=(5, 9),point2=(5, 8))
s.Line(point1=(5, 8),point2=(5, 7))
s.Line(point1=(5, 7),point2=(5, 6))
s.Line(point1=(5, 6),point2=(5, 5))
s.Line(point1=(5, 5),point2=(5, 4))
s.Line(point1=(5, 4),point2=(5, 3))
s.Line(point1=(5, 3),point2=(5, 2))
s.Line(point1=(5, 2),point2=(5, 1))
s.Line(point1=(5, 1),point2=(4, 1))
s.Line(point1=(4, 1),point2=(3, 1))
s.Line(point1=(3, 1),point2=(2, 1))
s.Line(point1=(2, 1),point2=(1, 1))
p = mdb.models["Model-1"].Part(name="S20_012", dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
p = mdb.models["Model-1"].parts["S20_012"]
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models["Model-1"].parts["S20_012"]
session.viewports["Viewport: 1"].setValues(displayedObject=p)
del mdb.models["Model-1"].sketches["__profile__"]
session.viewports["Viewport: 1"].partDisplay.setValues(mesh=ON)
session.viewports["Viewport: 1"].partDisplay.meshOptions.setValues(meshTechnique=ON)
session.viewports["Viewport: 1"].partDisplay.geometryOptions.setValues(
referenceRepresentation=OFF)
p = mdb.models["Model-1"].parts["S20_012"]
p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models["Model-1"].parts["S20_012"]
p.generateMesh()
s=p.edges
edges=s.findAt(((1, 1, 0),),((1, 2, 0),),((1, 3, 0),),((1, 4, 0),),((1, 5, 0),),((1, 6, 0),),((1, 7, 0),),((1, 8, 0),),((1, 9, 0),),((1, 10, 0),),((1, 11, 0),),((1, 12, 0),),((1, 13, 0),),((1, 14, 0),),((1, 15, 0),),((1, 16, 0),),((2, 16, 0),),((3, 16, 0),),((4, 17, 0),),((4, 18, 0),),((5, 19, 0),),((5, 20, 0),),((5, 21, 0),),((5, 22, 0),),((5, 23, 0),),((5, 24, 0),),((5, 25, 0),),((5, 26, 0),),((5, 27, 0),),((5, 28, 0),),((5, 29, 0),),((5, 30, 0),),((5, 31, 0),),((5, 32, 0),),((4, 33, 0),),((4, 34, 0),),((3, 35, 0),),((2, 35, 0),),((1, 35, 0),),((1, 36, 0),),((1, 37, 0),),((1, 38, 0),),((1, 39, 0),),((1, 40, 0),),((1, 41, 0),),((1, 42, 0),),((1, 43, 0),),((1, 44, 0),),((1, 45, 0),),((1, 46, 0),),((1, 47, 0),),((1, 48, 0),),((1, 49, 0),),((1, 50, 0),),)
p.Surface(side1Edges=edges, name="left")
edges=s.findAt(((49, 1, 0),),((48, 1, 0),),((47, 1, 0),),((46, 1, 0),),((46, 2, 0),),((46, 3, 0),),((46, 4, 0),),((46, 5, 0),),((46, 6, 0),),((46, 7, 0),),((46, 8, 0),),((46, 9, 0),),((46, 10, 0),),((46, 11, 0),),((45, 12, 0),),((45, 13, 0),),((45, 14, 0),),((44, 15, 0),),((43, 15, 0),),((42, 14, 0),),((42, 15, 0),),((42, 16, 0),),((42, 17, 0),),((42, 18, 0),),((42, 19, 0),),((42, 20, 0),),((42, 21, 0),),((42, 22, 0),),((42, 23, 0),),((41, 24, 0),),((40, 24, 0),),((39, 23, 0),),((39, 22, 0),),((38, 21, 0),),((38, 20, 0),),((38, 19, 0),),((38, 18, 0),),((38, 17, 0),),((38, 16, 0),),((38, 15, 0),),((38, 14, 0),),((37, 14, 0),),((36, 13, 0),),((36, 12, 0),),((36, 11, 0),),((36, 10, 0),),((36, 9, 0),),((36, 8, 0),),((36, 7, 0),),((36, 6, 0),),((36, 5, 0),),((36, 4, 0),),((36, 3, 0),),((36, 2, 0),),((36, 1, 0),),((35, 1, 0),),((34, 1, 0),),((33, 1, 0),),((32, 1, 0),),((31, 1, 0),),((30, 1, 0),),((29, 1, 0),),((28, 1, 0),),((27, 1, 0),),((26, 1, 0),),((25, 1, 0),),((24, 1, 0),),((23, 1, 0),),((22, 1, 0),),((21, 1, 0),),((20, 1, 0),),((19, 1, 0),),((18, 1, 0),),((17, 1, 0),),((16, 1, 0),),((15, 1, 0),),((15, 2, 0),),((15, 3, 0),),((15, 4, 0),),((15, 5, 0),),((15, 6, 0),),((15, 7, 0),),((15, 8, 0),),((15, 9, 0),),((15, 10, 0),),((15, 11, 0),),((15, 12, 0),),((15, 13, 0),),((14, 14, 0),),((13, 14, 0),),((13, 15, 0),),((13, 16, 0),),((13, 17, 0),),((13, 18, 0),),((13, 19, 0),),((13, 20, 0),),((13, 21, 0),),((12, 22, 0),),((12, 23, 0),),((11, 24, 0),),((10, 24, 0),),((9, 23, 0),),((9, 22, 0),),((9, 21, 0),),((9, 20, 0),),((9, 19, 0),),((9, 18, 0),),((9, 17, 0),),((9, 16, 0),),((9, 15, 0),),((9, 14, 0),),((8, 15, 0),),((7, 15, 0),),((6, 14, 0),),((6, 13, 0),),((6, 12, 0),),((5, 11, 0),),((5, 10, 0),),((5, 9, 0),),((5, 8, 0),),((5, 7, 0),),((5, 6, 0),),((5, 5, 0),),((5, 4, 0),),((5, 3, 0),),((5, 2, 0),),((5, 1, 0),),((4, 1, 0),),((3, 1, 0),),((2, 1, 0),),((1.5, 1, 0),),)
p.Surface(side1Edges=edges, name="bottom")
edges=s.findAt(((2, 50, 0),),((3, 50, 0),),((4, 50, 0),),((5, 50, 0),),((5, 49, 0),),((5, 48, 0),),((5, 47, 0),),((5, 46, 0),),((5, 45, 0),),((5, 44, 0),),((5, 43, 0),),((5, 42, 0),),((5, 41, 0),),((5, 40, 0),),((6, 39, 0),),((6, 38, 0),),((6, 37, 0),),((7, 36, 0),),((8, 36, 0),),((9, 37, 0),),((9, 36, 0),),((9, 35, 0),),((9, 34, 0),),((9, 33, 0),),((9, 32, 0),),((9, 31, 0),),((9, 30, 0),),((9, 29, 0),),((9, 28, 0),),((10, 27, 0),),((11, 27, 0),),((12, 28, 0),),((12, 29, 0),),((13, 30, 0),),((13, 31, 0),),((13, 32, 0),),((13, 33, 0),),((13, 34, 0),),((13, 35, 0),),((13, 36, 0),),((13, 37, 0),),((14, 37, 0),),((15, 38, 0),),((15, 39, 0),),((15, 40, 0),),((15, 41, 0),),((15, 42, 0),),((15, 43, 0),),((15, 44, 0),),((15, 45, 0),),((15, 46, 0),),((15, 47, 0),),((15, 48, 0),),((15, 49, 0),),((15, 50, 0),),((16, 50, 0),),((17, 50, 0),),((18, 50, 0),),((19, 50, 0),),((20, 50, 0),),((21, 50, 0),),((22, 50, 0),),((23, 50, 0),),((24, 50, 0),),((25, 50, 0),),((26, 50, 0),),((27, 50, 0),),((28, 50, 0),),((29, 50, 0),),((30, 50, 0),),((31, 50, 0),),((32, 50, 0),),((33, 50, 0),),((34, 50, 0),),((35, 50, 0),),((36, 50, 0),),((36, 49, 0),),((36, 48, 0),),((36, 47, 0),),((36, 46, 0),),((36, 45, 0),),((36, 44, 0),),((36, 43, 0),),((36, 42, 0),),((36, 41, 0),),((36, 40, 0),),((36, 39, 0),),((36, 38, 0),),((37, 37, 0),),((38, 37, 0),),((38, 36, 0),),((38, 35, 0),),((38, 34, 0),),((38, 33, 0),),((38, 32, 0),),((38, 31, 0),),((38, 30, 0),),((39, 29, 0),),((39, 28, 0),),((40, 27, 0),),((41, 27, 0),),((42, 28, 0),),((42, 29, 0),),((42, 30, 0),),((42, 31, 0),),((42, 32, 0),),((42, 33, 0),),((42, 34, 0),),((42, 35, 0),),((42, 36, 0),),((42, 37, 0),),((43, 36, 0),),((44, 36, 0),),((45, 37, 0),),((45, 38, 0),),((45, 39, 0),),((46, 40, 0),),((46, 41, 0),),((46, 42, 0),),((46, 43, 0),),((46, 44, 0),),((46, 45, 0),),((46, 46, 0),),((46, 47, 0),),((46, 48, 0),),((46, 49, 0),),((46, 50, 0),),((47, 50, 0),),((48, 50, 0),),((49, 50, 0),),((50, 50, 0),),)
p.Surface(side1Edges=edges, name="top")
edges=s.findAt(((50, 49, 0),),((50, 48, 0),),((50, 47, 0),),((50, 46, 0),),((50, 45, 0),),((50, 44, 0),),((50, 43, 0),),((50, 42, 0),),((50, 41, 0),),((50, 40, 0),),((50, 39, 0),),((50, 38, 0),),((50, 37, 0),),((50, 36, 0),),((50, 35, 0),),((49, 35, 0),),((48, 35, 0),),((47, 34, 0),),((47, 33, 0),),((46, 32, 0),),((46, 31, 0),),((46, 30, 0),),((46, 29, 0),),((46, 28, 0),),((46, 27, 0),),((46, 26, 0),),((46, 25, 0),),((46, 24, 0),),((46, 23, 0),),((46, 22, 0),),((46, 21, 0),),((46, 20, 0),),((46, 19, 0),),((47, 18, 0),),((47, 17, 0),),((48, 16, 0),),((49, 16, 0),),((50, 16, 0),),((50, 15, 0),),((50, 14, 0),),((50, 13, 0),),((50, 12, 0),),((50, 11, 0),),((50, 10, 0),),((50, 9, 0),),((50, 8, 0),),((50, 7, 0),),((50, 6, 0),),((50, 5, 0),),((50, 4, 0),),((50, 3, 0),),((50, 2, 0),),((50, 1, 0),),)
p.Surface(side1Edges=edges, name="right")
mdb.models["Model-1"].Material(name="Material-1")
mdb.models["Model-1"].materials["Material-1"].Elastic(table=((1E6, 0.3), ))
mdb.models["Model-1"].HomogeneousSolidSection(name="S20_012",
material="Material-1", thickness=None)
f = p.faces
faces= p.faces.findAt(((1,1,0), (50,50,0)), )
region = p.Set(faces=faces, name="S20_012")
p = mdb.models["Model-1"].parts["S20_012"]
p.SectionAssignment(region=region, sectionName="S20_012", offset=0.0,
offsetType=MIDDLE_SURFACE, offsetField="",
thicknessAssignment=FROM_SECTION)