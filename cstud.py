# -*- coding: mbcs -*-
#
# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility 
# bending of stud
# input data
depth =48
flange1 =34
flange2 =34
returnl = 6.5
H= 2500

from abaqus import *
from abaqusConstants import *

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
#s.setPrimaryObject(option=STANDALONE)
s.Spot(point=(0.0, 0.0))
s.Spot(point=(flange1, 0.0))
s.Spot(point=(flange1, returnl))
s.Spot(point=(0.0, depth))
s.Spot(point=(flange2, depth))
s.Spot(point=(flange2,depth-returnl ))
s.Line(point1=(flange1, returnl), point2=(flange1, 0.0))
s.VerticalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(flange1, 0.0), point2=(0.0, 0.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(0.0, depth))
s.VerticalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0, depth), point2=(flange2, depth))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(flange2, depth), point2=(flange2, depth-returnl))
s.VerticalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
p = mdb.models['Model-1'].Part( dimensionality=THREE_D, name='CStud', type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['CStud']
p.BaseShellExtrude(sketch=s, depth=H)
s.unsetPrimaryObject()

#section
p1 = mdb.models['Model-1'].parts['CStud']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((170000.0, 0.3),    ))
mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM, 
    thickness=0.5, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['CStud']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1f ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['CStud']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,offsetType=MIDDLE_SURFACE, offsetField='',thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['CStud']
a.Instance(name='CStud-1', part=p, dependent=ON)

#step & BC
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', initialInc=0.01, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
e1 = a.instances['CStud-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#b6d5 ]', ), )
region = a.Set(edges=edges1, name='Set-1')
mdb.models['Model-1'].PinnedBC(name='BC-1', createStepName='Step-1',   region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['CStud-1'].faces
side2Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Surface(side2Faces=side2Faces1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', region=region, distributionType=UNIFORM, field='', magnitude=0.005, 
    amplitude=UNSET)
	
#Mesh
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
pickedRegions = f.getSequenceFromMask(mask=('[#1f ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
p = mdb.models['Model-1'].parts['CStud']
p.generateMesh()

#Job
mdb.Job(name='Job-CStud', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
    numDomains=8, numGPUs=0)

mdb.jobs['Job-CStud'].submit(consistencyChecking=OFF)	