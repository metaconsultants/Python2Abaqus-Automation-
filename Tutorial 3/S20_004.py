# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility 
# bending of stud
# input data
from abaqus import *
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
s.Line(point1=(1, 10),point2=(2, 10))
s.Line(point1=(2, 10),point2=(3, 10))
s.Line(point1=(3, 10),point2=(4, 10))
s.Line(point1=(4, 10),point2=(5, 10))
s.Line(point1=(5, 10),point2=(6, 10))
s.Line(point1=(6, 10),point2=(7, 10))
s.Line(point1=(7, 10),point2=(8, 10))
s.Line(point1=(8, 10),point2=(9, 11))
s.Line(point1=(9, 11),point2=(10, 12))
s.Line(point1=(10, 12),point2=(10, 13))
s.Line(point1=(10, 13),point2=(10, 14))
s.Line(point1=(10, 14),point2=(10, 15))
s.Line(point1=(10, 15),point2=(10, 16))
s.Line(point1=(10, 16),point2=(11, 17))
s.Line(point1=(11, 17),point2=(12, 17))
s.Line(point1=(12, 17),point2=(13, 17))
s.Line(point1=(13, 17),point2=(14, 17))
s.Line(point1=(14, 17),point2=(15, 18))
s.Line(point1=(15, 18),point2=(16, 19))
s.Line(point1=(16, 19),point2=(16, 20))
s.Line(point1=(16, 20),point2=(16, 21))
s.Line(point1=(16, 21),point2=(16, 22))
s.Line(point1=(16, 22),point2=(16, 23))
s.Line(point1=(16, 23),point2=(16, 24))
s.Line(point1=(16, 24),point2=(16, 25))
s.Line(point1=(16, 25),point2=(16, 26))
s.Line(point1=(16, 26),point2=(16, 27))
s.Line(point1=(16, 27),point2=(16, 28))
s.Line(point1=(16, 28),point2=(16, 29))
s.Line(point1=(16, 29),point2=(16, 30))
s.Line(point1=(16, 30),point2=(16, 31))
s.Line(point1=(16, 31),point2=(16, 32))
s.Line(point1=(16, 32),point2=(15, 33))
s.Line(point1=(15, 33),point2=(14, 34))
s.Line(point1=(14, 34),point2=(13, 34))
s.Line(point1=(13, 34),point2=(12, 34))
s.Line(point1=(12, 34),point2=(11, 34))
s.Line(point1=(11, 34),point2=(10, 35))
s.Line(point1=(10, 35),point2=(10, 36))
s.Line(point1=(10, 36),point2=(10, 37))
s.Line(point1=(10, 37),point2=(10, 38))
s.Line(point1=(10, 38),point2=(10, 39))
s.Line(point1=(10, 39),point2=(9, 40))
s.Line(point1=(9, 40),point2=(8, 41))
s.Line(point1=(8, 41),point2=(7, 41))
s.Line(point1=(7, 41),point2=(6, 41))
s.Line(point1=(6, 41),point2=(5, 41))
s.Line(point1=(5, 41),point2=(4, 41))
s.Line(point1=(4, 41),point2=(3, 41))
s.Line(point1=(3, 41),point2=(2, 41))
s.Line(point1=(2, 41),point2=(1, 41))
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
s.Line(point1=(5, 50),point2=(6, 50))
s.Line(point1=(6, 50),point2=(7, 50))
s.Line(point1=(7, 50),point2=(8, 50))
s.Line(point1=(8, 50),point2=(9, 50))
s.Line(point1=(9, 50),point2=(10, 50))
s.Line(point1=(10, 50),point2=(11, 50))
s.Line(point1=(11, 50),point2=(12, 50))
s.Line(point1=(12, 50),point2=(13, 50))
s.Line(point1=(13, 50),point2=(14, 50))
s.Line(point1=(14, 50),point2=(15, 50))
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
s.Line(point1=(36, 50),point2=(37, 50))
s.Line(point1=(37, 50),point2=(38, 50))
s.Line(point1=(38, 50),point2=(39, 50))
s.Line(point1=(39, 50),point2=(40, 50))
s.Line(point1=(40, 50),point2=(41, 50))
s.Line(point1=(41, 50),point2=(42, 50))
s.Line(point1=(42, 50),point2=(43, 50))
s.Line(point1=(43, 50),point2=(44, 50))
s.Line(point1=(44, 50),point2=(45, 50))
s.Line(point1=(45, 50),point2=(46, 50))
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
s.Line(point1=(50, 41),point2=(49, 41))
s.Line(point1=(49, 41),point2=(48, 41))
s.Line(point1=(48, 41),point2=(47, 41))
s.Line(point1=(47, 41),point2=(46, 41))
s.Line(point1=(46, 41),point2=(45, 41))
s.Line(point1=(45, 41),point2=(44, 41))
s.Line(point1=(44, 41),point2=(43, 41))
s.Line(point1=(43, 41),point2=(42, 40))
s.Line(point1=(42, 40),point2=(41, 39))
s.Line(point1=(41, 39),point2=(41, 38))
s.Line(point1=(41, 38),point2=(41, 37))
s.Line(point1=(41, 37),point2=(41, 36))
s.Line(point1=(41, 36),point2=(41, 35))
s.Line(point1=(41, 35),point2=(40, 34))
s.Line(point1=(40, 34),point2=(39, 34))
s.Line(point1=(39, 34),point2=(38, 34))
s.Line(point1=(38, 34),point2=(37, 34))
s.Line(point1=(37, 34),point2=(36, 33))
s.Line(point1=(36, 33),point2=(35, 32))
s.Line(point1=(35, 32),point2=(35, 31))
s.Line(point1=(35, 31),point2=(35, 30))
s.Line(point1=(35, 30),point2=(35, 29))
s.Line(point1=(35, 29),point2=(35, 28))
s.Line(point1=(35, 28),point2=(35, 27))
s.Line(point1=(35, 27),point2=(35, 26))
s.Line(point1=(35, 26),point2=(35, 25))
s.Line(point1=(35, 25),point2=(35, 24))
s.Line(point1=(35, 24),point2=(35, 23))
s.Line(point1=(35, 23),point2=(35, 22))
s.Line(point1=(35, 22),point2=(35, 21))
s.Line(point1=(35, 21),point2=(35, 20))
s.Line(point1=(35, 20),point2=(35, 19))
s.Line(point1=(35, 19),point2=(36, 18))
s.Line(point1=(36, 18),point2=(37, 17))
s.Line(point1=(37, 17),point2=(38, 17))
s.Line(point1=(38, 17),point2=(39, 17))
s.Line(point1=(39, 17),point2=(40, 17))
s.Line(point1=(40, 17),point2=(41, 16))
s.Line(point1=(41, 16),point2=(41, 15))
s.Line(point1=(41, 15),point2=(41, 14))
s.Line(point1=(41, 14),point2=(41, 13))
s.Line(point1=(41, 13),point2=(41, 12))
s.Line(point1=(41, 12),point2=(42, 11))
s.Line(point1=(42, 11),point2=(43, 10))
s.Line(point1=(43, 10),point2=(44, 10))
s.Line(point1=(44, 10),point2=(45, 10))
s.Line(point1=(45, 10),point2=(46, 10))
s.Line(point1=(46, 10),point2=(47, 10))
s.Line(point1=(47, 10),point2=(48, 10))
s.Line(point1=(48, 10),point2=(49, 10))
s.Line(point1=(49, 10),point2=(50, 10))
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
s.Line(point1=(46, 1),point2=(45, 1))
s.Line(point1=(45, 1),point2=(44, 1))
s.Line(point1=(44, 1),point2=(43, 1))
s.Line(point1=(43, 1),point2=(42, 1))
s.Line(point1=(42, 1),point2=(41, 1))
s.Line(point1=(41, 1),point2=(40, 1))
s.Line(point1=(40, 1),point2=(39, 1))
s.Line(point1=(39, 1),point2=(38, 1))
s.Line(point1=(38, 1),point2=(37, 1))
s.Line(point1=(37, 1),point2=(36, 1))
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
s.Line(point1=(15, 1),point2=(14, 1))
s.Line(point1=(14, 1),point2=(13, 1))
s.Line(point1=(13, 1),point2=(12, 1))
s.Line(point1=(12, 1),point2=(11, 1))
s.Line(point1=(11, 1),point2=(10, 1))
s.Line(point1=(10, 1),point2=(9, 1))
s.Line(point1=(9, 1),point2=(8, 1))
s.Line(point1=(8, 1),point2=(7, 1))
s.Line(point1=(7, 1),point2=(6, 1))
s.Line(point1=(6, 1),point2=(5, 1))
s.Line(point1=(5, 1),point2=(4, 1))
s.Line(point1=(4, 1),point2=(3, 1))
s.Line(point1=(3, 1),point2=(2, 1))
s.Line(point1=(2, 1),point2=(1, 1))
p = mdb.models["Model-1"].Part(name="S20_004", dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
p = mdb.models["Model-1"].parts["S20_004"]
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models["Model-1"].parts["S20_004"]
session.viewports["Viewport: 1"].setValues(displayedObject=p)
del mdb.models["Model-1"].sketches["__profile__"]
session.viewports["Viewport: 1"].partDisplay.setValues(mesh=ON)
session.viewports["Viewport: 1"].partDisplay.meshOptions.setValues(meshTechnique=ON)
session.viewports["Viewport: 1"].partDisplay.geometryOptions.setValues(
referenceRepresentation=OFF)
p = mdb.models["Model-1"].parts["S20_004"]
p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models["Model-1"].parts["S20_004"]
p.generateMesh()
s=p.edges
edges=s.findAt(((1, 1, 0),),((1, 2, 0),),((1, 3, 0),),((1, 4, 0),),((1, 5, 0),),((1, 6, 0),),((1, 7, 0),),((1, 8, 0),),((1, 9, 0),),((1, 10, 0),),((2, 10, 0),),((3, 10, 0),),((4, 10, 0),),((5, 10, 0),),((6, 10, 0),),((7, 10, 0),),((8, 10, 0),),((9, 11, 0),),((10, 12, 0),),((10, 13, 0),),((10, 14, 0),),((10, 15, 0),),((10, 16, 0),),((11, 17, 0),),((12, 17, 0),),((13, 17, 0),),((14, 17, 0),),((15, 18, 0),),((16, 19, 0),),((16, 20, 0),),((16, 21, 0),),((16, 22, 0),),((16, 23, 0),),((16, 24, 0),),((16, 25, 0),),((16, 26, 0),),((16, 27, 0),),((16, 28, 0),),((16, 29, 0),),((16, 30, 0),),((16, 31, 0),),((16, 32, 0),),((15, 33, 0),),((14, 34, 0),),((13, 34, 0),),((12, 34, 0),),((11, 34, 0),),((10, 35, 0),),((10, 36, 0),),((10, 37, 0),),((10, 38, 0),),((10, 39, 0),),((9, 40, 0),),((8, 41, 0),),((7, 41, 0),),((6, 41, 0),),((5, 41, 0),),((4, 41, 0),),((3, 41, 0),),((2, 41, 0),),((1, 41, 0),),((1, 42, 0),),((1, 43, 0),),((1, 44, 0),),((1, 45, 0),),((1, 46, 0),),((1, 47, 0),),((1, 48, 0),),((1, 49, 0),),((1, 50, 0),),)
p.Surface(side1Edges=edges, name="left")
edges=s.findAt(((49, 1, 0),),((48, 1, 0),),((47, 1, 0),),((46, 1, 0),),((45, 1, 0),),((44, 1, 0),),((43, 1, 0),),((42, 1, 0),),((41, 1, 0),),((40, 1, 0),),((39, 1, 0),),((38, 1, 0),),((37, 1, 0),),((36, 1, 0),),((35, 1, 0),),((34, 1, 0),),((33, 1, 0),),((32, 1, 0),),((31, 1, 0),),((30, 1, 0),),((29, 1, 0),),((28, 1, 0),),((27, 1, 0),),((26, 1, 0),),((25, 1, 0),),((24, 1, 0),),((23, 1, 0),),((22, 1, 0),),((21, 1, 0),),((20, 1, 0),),((19, 1, 0),),((18, 1, 0),),((17, 1, 0),),((16, 1, 0),),((15, 1, 0),),((14, 1, 0),),((13, 1, 0),),((12, 1, 0),),((11, 1, 0),),((10, 1, 0),),((9, 1, 0),),((8, 1, 0),),((7, 1, 0),),((6, 1, 0),),((5, 1, 0),),((4, 1, 0),),((3, 1, 0),),((2, 1, 0),),((1.5, 1, 0),),)
p.Surface(side1Edges=edges, name="bottom")
edges=s.findAt(((2, 50, 0),),((3, 50, 0),),((4, 50, 0),),((5, 50, 0),),((6, 50, 0),),((7, 50, 0),),((8, 50, 0),),((9, 50, 0),),((10, 50, 0),),((11, 50, 0),),((12, 50, 0),),((13, 50, 0),),((14, 50, 0),),((15, 50, 0),),((16, 50, 0),),((17, 50, 0),),((18, 50, 0),),((19, 50, 0),),((20, 50, 0),),((21, 50, 0),),((22, 50, 0),),((23, 50, 0),),((24, 50, 0),),((25, 50, 0),),((26, 50, 0),),((27, 50, 0),),((28, 50, 0),),((29, 50, 0),),((30, 50, 0),),((31, 50, 0),),((32, 50, 0),),((33, 50, 0),),((34, 50, 0),),((35, 50, 0),),((36, 50, 0),),((37, 50, 0),),((38, 50, 0),),((39, 50, 0),),((40, 50, 0),),((41, 50, 0),),((42, 50, 0),),((43, 50, 0),),((44, 50, 0),),((45, 50, 0),),((46, 50, 0),),((47, 50, 0),),((48, 50, 0),),((49, 50, 0),),((50, 50, 0),),)
p.Surface(side1Edges=edges, name="top")
edges=s.findAt(((50, 49, 0),),((50, 48, 0),),((50, 47, 0),),((50, 46, 0),),((50, 45, 0),),((50, 44, 0),),((50, 43, 0),),((50, 42, 0),),((50, 41, 0),),((49, 41, 0),),((48, 41, 0),),((47, 41, 0),),((46, 41, 0),),((45, 41, 0),),((44, 41, 0),),((43, 41, 0),),((42, 40, 0),),((41, 39, 0),),((41, 38, 0),),((41, 37, 0),),((41, 36, 0),),((41, 35, 0),),((40, 34, 0),),((39, 34, 0),),((38, 34, 0),),((37, 34, 0),),((36, 33, 0),),((35, 32, 0),),((35, 31, 0),),((35, 30, 0),),((35, 29, 0),),((35, 28, 0),),((35, 27, 0),),((35, 26, 0),),((35, 25, 0),),((35, 24, 0),),((35, 23, 0),),((35, 22, 0),),((35, 21, 0),),((35, 20, 0),),((35, 19, 0),),((36, 18, 0),),((37, 17, 0),),((38, 17, 0),),((39, 17, 0),),((40, 17, 0),),((41, 16, 0),),((41, 15, 0),),((41, 14, 0),),((41, 13, 0),),((41, 12, 0),),((42, 11, 0),),((43, 10, 0),),((44, 10, 0),),((45, 10, 0),),((46, 10, 0),),((47, 10, 0),),((48, 10, 0),),((49, 10, 0),),((50, 10, 0),),((50, 9, 0),),((50, 8, 0),),((50, 7, 0),),((50, 6, 0),),((50, 5, 0),),((50, 4, 0),),((50, 3, 0),),((50, 2, 0),),((50, 1, 0),),)
p.Surface(side1Edges=edges, name="right")
mdb.models["Model-1"].Material(name="Material-1")
mdb.models["Model-1"].materials["Material-1"].Elastic(table=((1E6, 0.3), ))
mdb.models["Model-1"].HomogeneousSolidSection(name="S20_004",
material="Material-1", thickness=None)
f = p.faces
faces= p.faces.findAt(((1,1,0), (50,50,0)), )
region = p.Set(faces=faces, name="S20_004")
p = mdb.models["Model-1"].parts["S20_004"]
p.SectionAssignment(region=region, sectionName="S20_004", offset=0.0,
offsetType=MIDDLE_SURFACE, offsetField="",
thicknessAssignment=FROM_SECTION)