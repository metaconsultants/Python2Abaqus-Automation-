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


s.Line(point1=(19, 1),point2=(19, 2))


s.Line(point1=(19, 2),point2=(19, 3))


s.Line(point1=(19, 3),point2=(19, 4))


s.Line(point1=(19, 4),point2=(18, 5))


s.Line(point1=(18, 5),point2=(17, 5))


s.Line(point1=(17, 5),point2=(16, 6))


s.Line(point1=(16, 6),point2=(15, 6))


s.Line(point1=(15, 6),point2=(15, 7))


s.Line(point1=(15, 7),point2=(15, 8))


s.Line(point1=(15, 8),point2=(15, 9))


s.Line(point1=(15, 9),point2=(15, 10))


s.Line(point1=(15, 10),point2=(15, 11))


s.Line(point1=(15, 11),point2=(14, 12))


s.Line(point1=(14, 12),point2=(13, 13))


s.Line(point1=(13, 13),point2=(12, 13))


s.Line(point1=(12, 13),point2=(11, 13))


s.Line(point1=(11, 13),point2=(10, 13))


s.Line(point1=(10, 13),point2=(9, 13))


s.Line(point1=(9, 13),point2=(8, 13))


s.Line(point1=(8, 13),point2=(7, 13))


s.Line(point1=(7, 13),point2=(6, 13))


s.Line(point1=(6, 13),point2=(5, 13))


s.Line(point1=(5, 13),point2=(4, 13))


s.Line(point1=(4, 13),point2=(3, 13))


s.Line(point1=(3, 13),point2=(2, 13))


s.Line(point1=(2, 13),point2=(1, 13))


s.Line(point1=(1, 13),point2=(1, 14))


s.Line(point1=(1, 14),point2=(1, 15))


s.Line(point1=(1, 15),point2=(1, 16))


s.Line(point1=(1, 16),point2=(1, 17))


s.Line(point1=(1, 17),point2=(1, 18))


s.Line(point1=(1, 18),point2=(1, 19))


s.Line(point1=(1, 19),point2=(1, 20))


s.Line(point1=(1, 20),point2=(1, 21))


s.Line(point1=(1, 21),point2=(1, 22))


s.Line(point1=(1, 22),point2=(1, 23))


s.Line(point1=(1, 23),point2=(1, 24))


s.Line(point1=(1, 24),point2=(1, 25))


s.Line(point1=(1, 25),point2=(1, 26))


s.Line(point1=(1, 26),point2=(1, 27))


s.Line(point1=(1, 27),point2=(1, 28))


s.Line(point1=(1, 28),point2=(1, 29))


s.Line(point1=(1, 29),point2=(1, 30))


s.Line(point1=(1, 30),point2=(1, 31))


s.Line(point1=(1, 31),point2=(1, 32))


s.Line(point1=(1, 32),point2=(1, 33))


s.Line(point1=(1, 33),point2=(1, 34))


s.Line(point1=(1, 34),point2=(1, 35))


s.Line(point1=(1, 35),point2=(1, 36))


s.Line(point1=(1, 36),point2=(1, 37))


s.Line(point1=(1, 37),point2=(1, 38))


s.Line(point1=(1, 38),point2=(2, 38))


s.Line(point1=(2, 38),point2=(3, 38))


s.Line(point1=(3, 38),point2=(4, 38))


s.Line(point1=(4, 38),point2=(5, 38))


s.Line(point1=(5, 38),point2=(6, 38))


s.Line(point1=(6, 38),point2=(7, 38))


s.Line(point1=(7, 38),point2=(8, 38))


s.Line(point1=(8, 38),point2=(9, 38))


s.Line(point1=(9, 38),point2=(10, 38))


s.Line(point1=(10, 38),point2=(11, 38))


s.Line(point1=(11, 38),point2=(12, 38))


s.Line(point1=(12, 38),point2=(13, 38))


s.Line(point1=(13, 38),point2=(14, 39))


s.Line(point1=(14, 39),point2=(15, 40))


s.Line(point1=(15, 40),point2=(15, 41))


s.Line(point1=(15, 41),point2=(15, 42))


s.Line(point1=(15, 42),point2=(15, 43))


s.Line(point1=(15, 43),point2=(15, 44))


s.Line(point1=(15, 44),point2=(15, 45))


s.Line(point1=(15, 45),point2=(16, 45))


s.Line(point1=(16, 45),point2=(17, 46))


s.Line(point1=(17, 46),point2=(18, 46))


s.Line(point1=(18, 46),point2=(19, 47))


s.Line(point1=(19, 47),point2=(19, 48))


s.Line(point1=(19, 48),point2=(19, 49))


s.Line(point1=(19, 49),point2=(19, 50))


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


s.Line(point1=(32, 50),point2=(32, 49))


s.Line(point1=(32, 49),point2=(32, 48))


s.Line(point1=(32, 48),point2=(32, 47))


s.Line(point1=(32, 47),point2=(33, 46))


s.Line(point1=(33, 46),point2=(34, 46))


s.Line(point1=(34, 46),point2=(35, 45))


s.Line(point1=(35, 45),point2=(36, 45))


s.Line(point1=(36, 45),point2=(36, 44))


s.Line(point1=(36, 44),point2=(36, 43))


s.Line(point1=(36, 43),point2=(36, 42))


s.Line(point1=(36, 42),point2=(36, 41))


s.Line(point1=(36, 41),point2=(36, 40))


s.Line(point1=(36, 40),point2=(37, 39))


s.Line(point1=(37, 39),point2=(38, 38))


s.Line(point1=(38, 38),point2=(39, 38))


s.Line(point1=(39, 38),point2=(40, 38))


s.Line(point1=(40, 38),point2=(41, 38))


s.Line(point1=(41, 38),point2=(42, 38))


s.Line(point1=(42, 38),point2=(43, 38))


s.Line(point1=(43, 38),point2=(44, 38))


s.Line(point1=(44, 38),point2=(45, 38))


s.Line(point1=(45, 38),point2=(46, 38))


s.Line(point1=(46, 38),point2=(47, 38))


s.Line(point1=(47, 38),point2=(48, 38))


s.Line(point1=(48, 38),point2=(49, 38))


s.Line(point1=(49, 38),point2=(50, 38))


s.Line(point1=(50, 38),point2=(50, 37))


s.Line(point1=(50, 37),point2=(50, 36))


s.Line(point1=(50, 36),point2=(50, 35))


s.Line(point1=(50, 35),point2=(50, 34))


s.Line(point1=(50, 34),point2=(50, 33))


s.Line(point1=(50, 33),point2=(50, 32))


s.Line(point1=(50, 32),point2=(50, 31))


s.Line(point1=(50, 31),point2=(50, 30))


s.Line(point1=(50, 30),point2=(50, 29))


s.Line(point1=(50, 29),point2=(50, 28))


s.Line(point1=(50, 28),point2=(50, 27))


s.Line(point1=(50, 27),point2=(50, 26))


s.Line(point1=(50, 26),point2=(50, 25))


s.Line(point1=(50, 25),point2=(50, 24))


s.Line(point1=(50, 24),point2=(50, 23))


s.Line(point1=(50, 23),point2=(50, 22))


s.Line(point1=(50, 22),point2=(50, 21))


s.Line(point1=(50, 21),point2=(50, 20))


s.Line(point1=(50, 20),point2=(50, 19))


s.Line(point1=(50, 19),point2=(50, 18))


s.Line(point1=(50, 18),point2=(50, 17))


s.Line(point1=(50, 17),point2=(50, 16))


s.Line(point1=(50, 16),point2=(50, 15))


s.Line(point1=(50, 15),point2=(50, 14))


s.Line(point1=(50, 14),point2=(50, 13))


s.Line(point1=(50, 13),point2=(49, 13))


s.Line(point1=(49, 13),point2=(48, 13))


s.Line(point1=(48, 13),point2=(47, 13))


s.Line(point1=(47, 13),point2=(46, 13))


s.Line(point1=(46, 13),point2=(45, 13))


s.Line(point1=(45, 13),point2=(44, 13))


s.Line(point1=(44, 13),point2=(43, 13))


s.Line(point1=(43, 13),point2=(42, 13))


s.Line(point1=(42, 13),point2=(41, 13))


s.Line(point1=(41, 13),point2=(40, 13))


s.Line(point1=(40, 13),point2=(39, 13))


s.Line(point1=(39, 13),point2=(38, 13))


s.Line(point1=(38, 13),point2=(37, 12))


s.Line(point1=(37, 12),point2=(36, 11))


s.Line(point1=(36, 11),point2=(36, 10))


s.Line(point1=(36, 10),point2=(36, 9))


s.Line(point1=(36, 9),point2=(36, 8))


s.Line(point1=(36, 8),point2=(36, 7))


s.Line(point1=(36, 7),point2=(36, 6))


s.Line(point1=(36, 6),point2=(35, 6))


s.Line(point1=(35, 6),point2=(34, 5))


s.Line(point1=(34, 5),point2=(33, 5))


s.Line(point1=(33, 5),point2=(32, 4))


s.Line(point1=(32, 4),point2=(32, 3))


s.Line(point1=(32, 3),point2=(32, 2))


s.Line(point1=(32, 2),point2=(32, 1))


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


p = mdb.models["Model-1"].Part(name="S20_005", dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)


p = mdb.models["Model-1"].parts["S20_005"]


p.BaseShell(sketch=s)


s.unsetPrimaryObject()


p = mdb.models["Model-1"].parts["S20_005"]


session.viewports["Viewport: 1"].setValues(displayedObject=p)


del mdb.models["Model-1"].sketches["__profile__"]


session.viewports["Viewport: 1"].partDisplay.setValues(mesh=ON)


session.viewports["Viewport: 1"].partDisplay.meshOptions.setValues(meshTechnique=ON)


session.viewports["Viewport: 1"].partDisplay.geometryOptions.setValues(


referenceRepresentation=OFF)


p = mdb.models["Model-1"].parts["S20_005"]


p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)


p = mdb.models["Model-1"].parts["S20_005"]


p.generateMesh()


s=p.edges


edges=s.findAt(((19, 1, 0),),((19, 2, 0),),((19, 3, 0),),((19, 4, 0),),((18, 5, 0),),((17, 5, 0),),((16, 6, 0),),((15, 6, 0),),((15, 7, 0),),((15, 8, 0),),((15, 9, 0),),((15, 10, 0),),((15, 11, 0),),((14, 12, 0),),((13, 13, 0),),((12, 13, 0),),((11, 13, 0),),((10, 13, 0),),((9, 13, 0),),((8, 13, 0),),((7, 13, 0),),((6, 13, 0),),((5, 13, 0),),((4, 13, 0),),((3, 13, 0),),((2, 13, 0),),((1, 13, 0),),((1, 14, 0),),((1, 15, 0),),((1, 16, 0),),((1, 17, 0),),((1, 18, 0),),((1, 19, 0),),((1, 20, 0),),((1, 21, 0),),((1, 22, 0),),((1, 23, 0),),((1, 24, 0),),((1, 25, 0),),((1, 26, 0),),((1, 27, 0),),((1, 28, 0),),((1, 29, 0),),((1, 30, 0),),((1, 31, 0),),((1, 32, 0),),((1, 33, 0),),((1, 34, 0),),((1, 35, 0),),((1, 36, 0),),((1, 37, 0),),((1, 38, 0),),((2, 38, 0),),((3, 38, 0),),((4, 38, 0),),((5, 38, 0),),((6, 38, 0),),((7, 38, 0),),((8, 38, 0),),((9, 38, 0),),((10, 38, 0),),((11, 38, 0),),((12, 38, 0),),((13, 38, 0),),((14, 39, 0),),((15, 40, 0),),((15, 41, 0),),((15, 42, 0),),((15, 43, 0),),((15, 44, 0),),((15, 45, 0),),((16, 45, 0),),((17, 46, 0),),((18, 46, 0),),((19, 47, 0),),((19, 48, 0),),((19, 49, 0),),((19, 50, 0),),)


p.Surface(side1Edges=edges, name="left")


edges=s.findAt(((31, 1, 0),),((30, 1, 0),),((29, 1, 0),),((28, 1, 0),),((27, 1, 0),),((26, 1, 0),),((25, 1, 0),),((24, 1, 0),),((23, 1, 0),),((22, 1, 0),),((21, 1, 0),),((20, 1, 0),),((19.5, 1, 0),),)


p.Surface(side1Edges=edges, name="bottom")


edges=s.findAt(((20, 50, 0),),((21, 50, 0),),((22, 50, 0),),((23, 50, 0),),((24, 50, 0),),((25, 50, 0),),((26, 50, 0),),((27, 50, 0),),((28, 50, 0),),((29, 50, 0),),((30, 50, 0),),((31, 50, 0),),((32, 50, 0),),)


p.Surface(side1Edges=edges, name="top")


edges=s.findAt(((32, 49, 0),),((32, 48, 0),),((32, 47, 0),),((33, 46, 0),),((34, 46, 0),),((35, 45, 0),),((36, 45, 0),),((36, 44, 0),),((36, 43, 0),),((36, 42, 0),),((36, 41, 0),),((36, 40, 0),),((37, 39, 0),),((38, 38, 0),),((39, 38, 0),),((40, 38, 0),),((41, 38, 0),),((42, 38, 0),),((43, 38, 0),),((44, 38, 0),),((45, 38, 0),),((46, 38, 0),),((47, 38, 0),),((48, 38, 0),),((49, 38, 0),),((50, 38, 0),),((50, 37, 0),),((50, 36, 0),),((50, 35, 0),),((50, 34, 0),),((50, 33, 0),),((50, 32, 0),),((50, 31, 0),),((50, 30, 0),),((50, 29, 0),),((50, 28, 0),),((50, 27, 0),),((50, 26, 0),),((50, 25, 0),),((50, 24, 0),),((50, 23, 0),),((50, 22, 0),),((50, 21, 0),),((50, 20, 0),),((50, 19, 0),),((50, 18, 0),),((50, 17, 0),),((50, 16, 0),),((50, 15, 0),),((50, 14, 0),),((50, 13, 0),),((49, 13, 0),),((48, 13, 0),),((47, 13, 0),),((46, 13, 0),),((45, 13, 0),),((44, 13, 0),),((43, 13, 0),),((42, 13, 0),),((41, 13, 0),),((40, 13, 0),),((39, 13, 0),),((38, 13, 0),),((37, 12, 0),),((36, 11, 0),),((36, 10, 0),),((36, 9, 0),),((36, 8, 0),),((36, 7, 0),),((36, 6, 0),),((35, 6, 0),),((34, 5, 0),),((33, 5, 0),),((32, 4, 0),),((32, 3, 0),),((32, 2, 0),),((32, 1, 0),),)


p.Surface(side1Edges=edges, name="right")


mdb.models["Model-1"].Material(name="Material-1")


mdb.models["Model-1"].materials["Material-1"].Elastic(table=((1E6, 0.3), ))


mdb.models["Model-1"].HomogeneousSolidSection(name="S20_005",


material="Material-1", thickness=None)


f = p.faces


faces= p.faces.findAt(((19,1,0), (32,50,0)), )


region = p.Set(faces=faces, name="S20_005")


p = mdb.models["Model-1"].parts["S20_005"]


p.SectionAssignment(region=region, sectionName="S20_005", offset=0.0,


offsetType=MIDDLE_SURFACE, offsetField="",


thicknessAssignment=FROM_SECTION)