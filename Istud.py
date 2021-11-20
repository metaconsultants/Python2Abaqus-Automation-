# -*- coding: mbcs -*-
#
# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility 
# bending of I stud
# input data
depth =48
flange1 =34
flange2 =34
returnl = 6.5
H= 2500

from abaqus import *
from abaqusConstants import *

session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)

s.Line(point1=(flange1/2.0, 0.0), point2=(0.0, 0.0))
s.Line(point1=(flange1/2.0, 0.0), point2=(flange1/2.0, depth))
s.Line(point1=(0.0, depth), point2=(flange1/2.0, depth))
s.Line(point1=(flange1-returnl, depth), point2=(flange1/2.0, depth))
s.Line(point1=(flange1, depth), point2=(flange1-returnl, depth))
s.Line(point1=(flange1-returnl, 0.0), point2=(flange1/2.0, 0.0))
s.Line(point1=(flange1, 0.0), point2=(flange1-returnl, 0.0))


p = mdb.models['Model-1'].Part(name='Istud', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Istud']
p.BaseShellExtrude(sketch=s, depth=H)
s.unsetPrimaryObject()

#section
p1 = mdb.models['Model-1'].parts['Istud']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((170000.0, 0.3),    ))
mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM, 
    thickness=0.5, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['Istud']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1f ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['Istud']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0,offsetType=MIDDLE_SURFACE, offsetField='',thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Istud']
a.Instance(name='Istud-1', part=p, dependent=ON)

#step & BC
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', initialInc=0.01, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
e1 = a.instances['Istud-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#afb6d ]', ), )
region = a.Set(edges=edges1, name='Set-1')
mdb.models['Model-1'].PinnedBC(name='BC-1', createStepName='Step-1',   region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Istud-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region = a.Surface(side2Faces=side1Faces1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', region=region, distributionType=UNIFORM, field='', magnitude=0.005, 
    amplitude=UNSET)
	
#Mesh
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
pickedRegions = f.getSequenceFromMask(mask=('[#1f ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
p = mdb.models['Model-1'].parts['Istud']
p.generateMesh()

#Job
mdb.Job(name='Job-Istud', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
    numDomains=8, numGPUs=0)

mdb.jobs['Job-Istud'].submit(consistencyChecking=OFF)	