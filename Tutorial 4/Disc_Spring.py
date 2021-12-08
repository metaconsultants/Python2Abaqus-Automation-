# copyright - metaengineeringconsultants@gmail.com
# abaqus 2017 compatibility

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
 

executeOnCaeStartup()

#Design parameters
De = 4           #Outer diameter
Di = 3.2         #Inner diameter
t =  0.3         #Thickness
l0 = 0.75        #Spring height 
alpha= -0.2    #shift

#sketch
# spring
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -25.0), point2=(0.0, 25.0))
s.FixedConstraint(entity=g[2])
s.Line(point1=(0.5*De, 0), point2=(0.5*De, t))
s.VerticalConstraint(entity=g[3], addUndoState=False)
s.Line(point1=(0.5*De, t), point2=(0.5*Di, l0))
s.Line(point1=(0.5*Di, l0), point2=(0.5*Di, l0-t))
s.VerticalConstraint(entity=g[5], addUndoState=False)
s.Line(point1=(0.5*Di, l0-t), point2=(0.5*De, 0))
p = mdb.models['Model-1'].Part(name='Spring', dimensionality=AXISYMMETRIC,  type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Spring']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Density(table=((7e-09, ), ))
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((170000.0, 0.3),     ))
#mdb.models['Model-1'].materials['Material-1'].Plastic(table=((710.0, 0.0), (804, 0.0008)))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Material-1', thickness=None)
p = mdb.models['Model-1'].parts['Spring']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['Spring']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
    

# rigid bodies
#rb1
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -25.0), point2=(0.0, 25.0))
s.FixedConstraint(entity=g[2])
s.Line(point1=(0.0, l0), point2=(De, l0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = mdb.models['Model-1'].Part(name='upper', dimensionality=AXISYMMETRIC, type=DISCRETE_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['upper']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['upper']
v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[0], rule=MIDDLE))
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#rb2
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -25.0), point2=(0.0, 25.0))
s.FixedConstraint(entity=g[2])
s.Line(point1=(0.0, 0.0), point2=(De, 0.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = mdb.models['Model-1'].Part(name='lower', dimensionality=AXISYMMETRIC, type=DISCRETE_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['lower']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['lower']
v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[0], rule=MIDDLE))
session.viewports['Viewport: 1'].setValues(displayedObject=p)


#Assemblies
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0),    point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
p = mdb.models['Model-1'].parts['Spring']
a.Instance(name='Spring-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['lower']
a.Instance(name='lower-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['upper']
a.Instance(name='upper-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)

# Interactions
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
    
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['upper-1'].edges
side2Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region1=a.Surface(side2Edges=side2Edges1, name='m_Surf-1')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Spring-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-1')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', 
    createStepName='Initial', master=region1, slave=region2, sliding=FINITE, 
    enforcement=NODE_TO_SURFACE, thickness=OFF, 
    interactionProperty='IntProp-1', surfaceSmoothing=NONE, adjustMethod=NONE, 
    smooth=0.2, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "Int-1" has been created.
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['lower-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region1=a.Surface(side1Edges=side1Edges1, name='m_Surf-2')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Spring-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-2')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-2', 
    createStepName='Initial', master=region1, slave=region2, sliding=FINITE, 
    enforcement=NODE_TO_SURFACE, thickness=OFF, 
    interactionProperty='IntProp-1', surfaceSmoothing=NONE, adjustMethod=NONE, 
    smooth=0.2, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)    
    
# step & BC
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    timeIncrementationMethod=FIXED, initialInc=0.01, noStop=OFF, nlgeom=ON)
mdb.models['Model-1'].steps['Step-1'].setValues(
    timeIncrementationMethod=AUTOMATIC)     
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['lower-1'].referencePoints
refPoints1=(r1[2], )
region = a.Set(referencePoints=refPoints1, name='Set-3')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['upper-1'].referencePoints
refPoints1=(r1[2], )
region = a.Set(referencePoints=refPoints1, name='Set-4')
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
    region=region, u1=0.0, u2=-l0-alpha, ur3=0.0, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)    
    
# Mesh
p = mdb.models['Model-1'].parts['Spring']
p.seedPart(size=0.01, deviationFactor=0.4, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Spring']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)
p = mdb.models['Model-1'].parts['Spring']
p.generateMesh()

p = mdb.models['Model-1'].parts['lower']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['lower']
p.generateMesh()

p = mdb.models['Model-1'].parts['upper']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['upper']
p.generateMesh()

#job submit
mdb.Job(name='Disc_Spring', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Disc_Spring'].submit(consistencyChecking=OFF)

 