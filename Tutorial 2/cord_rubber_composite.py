# -*- coding: mbcs -*-
# copyright - metaengineeringconsultants@gmail.com

#import libraries
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

# -*- W-Width of matrix,rpu-radius of pulley,hwpu-half width of pulley,ac-position of aramid cord from top surface of matrix
# -*- acp- aramid cord position from reference, scp- steel cord position from reference
# define  parameters
w=15;Y1=4.5;R1=0.5;X1=2.5;R2=0.22;X2=1.5;Y2=2;rpu=25;hwpu=16;ac=1;acp=(Y1/2-ac);scp=acp-Y2

# parts generation 
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(w/2,Y1/2), point2=(-w/2, -Y1/2))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=170.0, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=mdb.models['Model-1'].parts['Part-1'].edges[3])
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=    mdb.models['Model-1'].parts['Part-1'].edges[10])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__', 
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=X1, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(-X1, -scp), point1=(-X1+R1, -scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(-3.5*X2, acp), point1=(-3.5*X2+R2, acp))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__',
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(-X1, scp), point1=(-X1+R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=34.143, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(-3.5*X2, acp), point1=(-3.5*X2+R2, acp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    ), number1=8, number2=1, spacing1=X2, spacing2=34.143, vertexList=())
mdb.models['Model-1'].parts['Part-1'].PartitionCellBySketch(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=TOP, sketchPlane=
    mdb.models['Model-1'].parts['Part-1'].faces[4], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-1'].datums[3])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[7], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[2], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[11], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[13], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[14], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[16], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[18], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[20], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
	
#material & section assignment	
mdb.models['Model-1'].Material(name='Rubber')
mdb.models['Model-1'].materials['Rubber'].Density(table=((1.4e-09, ), ))
mdb.models['Model-1'].materials['Rubber'].Hyperelastic(materialType=ISOTROPIC, 
    table=((0.736, 0.184, 0.0), ), testData=OFF, type=MOONEY_RIVLIN, 
    volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].Material(name='Aramid')
mdb.models['Model-1'].materials['Aramid'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Aramid'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Rubber', name='Rubber',   thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name='Steel',    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Aramid', name='Aramid',    thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#800 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Rubber', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), name='Set-2')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), name='Set-3')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), name='Set-4')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-4'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), name='Set-5')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-5'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), name='Set-6')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-6'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), name='Set-7')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-7'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), name='Set-8')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-8'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), name='Set-9')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-9'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), name='Set-10')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-10'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), name='Set-11')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-11'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-12')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Aramid', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

	
	
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(w/2, Y1/2), 
    point2=(-w/2, -Y1/2))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=170.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=
    mdb.models['Model-1'].parts['Part-1'].edges[3])
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=
    mdb.models['Model-1'].parts['Part-1'].edges[10])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__', 
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=X1, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -X1, scp), point1=(-X1+R1, scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -3.5*X2, acp), point1=(-3.5*X2+R2, acp))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__', 
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -X1, scp), point1=(-X1+R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=34.143, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -3.5*X2, acp), point1=(-3.5*X2+R2, acp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    ), number1=8, number2=1, spacing1=X2, spacing2=34.143, vertexList=())
mdb.models['Model-1'].parts['Part-1'].PartitionCellBySketch(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=TOP, sketchPlane=
    mdb.models['Model-1'].parts['Part-1'].faces[4], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-1'].datums[3])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[7], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[2], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[11], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[13], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[14], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[16], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[18], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[20], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].Material(name='Rubber')
mdb.models['Model-1'].materials['Rubber'].Density(table=((1.4e-09, ), ))
mdb.models['Model-1'].materials['Rubber'].Hyperelastic(materialType=ISOTROPIC, 
    table=((0.736, 0.184, 0.0), ), testData=OFF, type=MOONEY_RIVLIN, 
    volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].Material(name='Aramid')
mdb.models['Model-1'].materials['Aramid'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Aramid'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Rubber', name='Rubber', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name='Steel', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Aramid', name='Aramid', 
    thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#800 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Rubber', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), name='Set-2')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), name='Set-3')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), name='Set-4')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-4'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), name='Set-5')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-5'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), name='Set-6')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-6'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), name='Set-7')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-7'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), name='Set-8')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-8'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), name='Set-9')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-9'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), name='Set-10')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-10'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), name='Set-11')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-11'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-12')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-12'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(7, 2.25), 
    point2=(-8, -2.25))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=170.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=
    mdb.models['Model-1'].parts['Part-1'].edges[3])
mdb.models['Model-1'].parts['Part-1'].DatumAxisByThruEdge(edge=
    mdb.models['Model-1'].parts['Part-1'].edges[10])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__', 
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=X1, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -X1, scp), point1=(-X1+R1, scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -3.5*X2, acp), point1=(-3.5*X2+R2, acp))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=8.53, name='__profile__', 
    sheetSize=341.43, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].datums[3], 
    sketchOrientation=TOP, origin=(0.0, 0.0, 170.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, scp), point1=(R1, scp))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -X1, scp), point1=(-X1+R1, scp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=2, number2=1, spacing1=X1, spacing2=34.143, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -3.5*X2, acp), point1=(-3.5*X2+R2, acp))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    ), number1=8, number2=1, spacing1=X2, spacing2=34.143, vertexList=())
mdb.models['Model-1'].parts['Part-1'].PartitionCellBySketch(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=TOP, sketchPlane=
    mdb.models['Model-1'].parts['Part-1'].faces[4], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-1'].datums[3])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[7], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[2], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[11], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[13], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[14], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[15], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[16], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[18], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].parts['Part-1'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-1'].edges[20], ), line=
    mdb.models['Model-1'].parts['Part-1'].datums[2], sense=REVERSE)
mdb.models['Model-1'].Material(name='Rubber')
mdb.models['Model-1'].materials['Rubber'].Density(table=((1.4e-09, ), ))
mdb.models['Model-1'].materials['Rubber'].Hyperelastic(materialType=ISOTROPIC, 
    table=((0.736, 0.184, 0.0), ), testData=OFF, type=MOONEY_RIVLIN, 
    volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].Material(name='Aramid')
mdb.models['Model-1'].materials['Aramid'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Aramid'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((1e-09, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((49000.0, 0.35), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Rubber', name='Rubber', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name='Steel', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Aramid', name='Aramid', 
    thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#800 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Rubber', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), name='Set-2')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#200 ]', 
    ), ), name='Set-3')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), name='Set-4')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-4'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), name='Set-5')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-5'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#40 ]', 
    ), ), name='Set-6')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-6'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), name='Set-7')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-7'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), name='Set-8')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-8'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), name='Set-9')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-9'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), name='Set-10')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-10'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), name='Set-11')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-11'], sectionName='Aramid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(rpu, 0.0), point2=(
    rpu, hwpu))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(rpu, 0.0), point2=(
    rpu, -hwpu))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[3], 
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-2', type=
    ANALYTIC_RIGID_SURFACE)
mdb.models['Model-1'].parts['Part-2'].AnalyticRigidSurfRevolve(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-2'].DatumAxisByCylFace(face=
    mdb.models['Model-1'].parts['Part-2'].faces[0])
mdb.models['Model-1'].parts['Part-2'].ReferencePoint(point=(0.0, 0.0, 0.0))
mdb.models['Model-1'].parts['Part-2'].features.changeKey(fromName='RP', toName=
    'RP_pulley')
mdb.models['Model-1'].parts['Part-2'].features.changeKey(fromName=
    '3D Analytic rigid shell-1', toName='Pulley')
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-2-1', 
    part=mdb.models['Model-1'].parts['Part-2'])
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices[23])
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
    mdb.models['Model-1'].rootAssembly.referencePoints[6])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Part-2-1', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 10.0, 
    0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Part-2-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Part-1-1', ), 
    vector=(w/2, rpu+Y1, -170.0))
mdb.models['Model-1'].ContactProperty('friction_04')
mdb.models['Model-1'].interactionProperties['friction_04'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.4, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['friction_04'].NormalBehavior(
    allowSeparation=ON, clearanceAtZeroContactPressure=0.0, 
    constraintEnforcementMethod=PENALTY, contactStiffness=DEFAULT, 
    contactStiffnessScaleFactor=1.0, pressureOverclosure=HARD, 
    stiffnessBehavior=LINEAR)
mdb.models['Model-1'].interactionProperties['friction_04'].GeometricProperties(
    contactArea=1.0, padThickness=None)
mdb.models['Model-1'].rootAssembly.Surface(name='m_Surf-1', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-1', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#0 #4 ]', ), ))
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='friction_04', master=
    mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-1'], name='friction', 
    slave=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-1'], sliding=
    FINITE, thickness=ON)
#mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName='m_Surf-1',toName='pulley_top_surface')
#mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName='s_Surf-1',toName='Belt_surface')
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices[27])
mdb.models['Model-1'].rootAssembly.Set(name='Set-1', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='disp_BC-1', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=SET, u2=UNSET, 
    u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-2', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='disp_BC-2', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=UNSET, u2=UNSET
    , u3=UNSET, ur1=SET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-3', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='disp_BC-3', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=UNSET, u2=UNSET
    , u3=UNSET, ur1=UNSET, ur2=SET, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-4', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='disp_BC-4', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], u1=UNSET, u2=UNSET
    , u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=SET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-5', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_1', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-5'], v1=0.0, v2=UNSET, 
    v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-6', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_6', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-6'], v1=UNSET, v2=0.0, 
    v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-7', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_3', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-7'], v1=UNSET, v2=UNSET
    , v3=0.0, vr1=0.0, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].boundaryConditions['Vel_BC_3'].setValues(vr1=UNSET)
mdb.models['Model-1'].boundaryConditions['Vel_BC_6'].setValues(v2=UNSET, vr3=
    0.0)
mdb.models['Model-1'].rootAssembly.Set(name='Set-8', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_2', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-8'], v1=UNSET, v2=0.0, 
    v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-9', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_4', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-9'], v1=UNSET, v2=UNSET
    , v3=UNSET, vr1=0.0, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-10', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_5', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-10'], v1=UNSET, v2=
    UNSET, v3=UNSET, vr1=UNSET, vr2=0.0, vr3=UNSET)
mdb.models['Model-1'].StaticStep(name='preload', previous='Initial')
mdb.models['Model-1'].steps['preload'].setValues(nlgeom=ON)
mdb.models['Model-1'].rootAssembly.Set(name='Set-11', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].ConcentratedForce(cf3=-375.0, createStepName='preload', 
    distributionType=UNIFORM, field='', localCsys=None, name='Point_Load', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-11'])
mdb.models['Model-1'].ImplicitDynamicsStep(initialInc=0.001, maxNumInc=1000, 
    minInc=1e-12, name='install', previous='preload')
mdb.models['Model-1'].FieldOutputRequest(createStepName='install', name=
    'F-Output-2', variables=PRESELECT)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].deactivate('install')
mdb.models['Model-1'].HistoryOutputRequest(createStepName='install', name=
    'H-Output-2', variables=PRESELECT)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].deactivate('install')
mdb.models['Model-1'].boundaryConditions['Vel_BC_4'].deactivate('install')
mdb.models['Model-1'].rootAssembly.Set(name='Set-12', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='install', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_7', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-12'], v1=UNSET, v2=
    UNSET, v3=UNSET, vr1=1.308, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].StaticStep(name='equlibriate', previous='install')
mdb.models['Model-1'].FieldOutputRequest(createStepName='equlibriate', name=
    'F-Output-3', variables=PRESELECT)
mdb.models['Model-1'].fieldOutputRequests['F-Output-2'].deactivate(
    'equlibriate')
mdb.models['Model-1'].HistoryOutputRequest(createStepName='equlibriate', name=
    'H-Output-3', variables=PRESELECT)
mdb.models['Model-1'].boundaryConditions['Vel_BC_7'].deactivate('equlibriate')
mdb.models['Model-1'].rootAssembly.Set(name='Set-13', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].VelocityBC(amplitude=UNSET, createStepName='equlibriate', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Vel_BC_8', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-13'], v1=UNSET, v2=
    UNSET, v3=UNSET, vr1=0.0, vr2=UNSET, vr3=UNSET)
mdb.models['Model-1'].boundaryConditions['Vel_BC_7'].reset('equlibriate')
mdb.models['Model-1'].boundaryConditions['Vel_BC_7'].deactivate('equlibriate')
mdb.models['Model-1'].historyOutputRequests['H-Output-2'].deactivate(
    'equlibriate')
mdb.models['Model-1'].rootAssembly.Set(name='m_Set-14', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[10], ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-3', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#0 #40 ]', ), ))
mdb.models['Model-1'].Coupling(controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-14'], couplingType=KINEMATIC
    , influenceRadius=WHOLE_SURFACE, localCsys=None, name='Constraint-1', 
    surface=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-3'], u1=OFF, 
    u2=OFF, u3=ON, ur1=OFF, ur2=OFF, ur3=OFF)
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-1', toName=
    'load')
mdb.models['Model-1'].rootAssembly.Surface(name='Surf-4', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].RigidBody(name='rigid_pulley', refPointRegion=Region(
    referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    )), surfaceRegion=mdb.models['Model-1'].rootAssembly.surfaces['Surf-4'])
mdb.models['Model-1'].rootAssembly.Set(name='m_Set-16', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-5', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#400000 ]', ), ))
mdb.models['Model-1'].Coupling(controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-16'], couplingType=KINEMATIC
    , influenceRadius=WHOLE_SURFACE, localCsys=None, name='Symmetry', surface=
    mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-5'], u1=OFF, u2=OFF, 
    u3=ON, ur1=ON, ur2=ON, ur3=OFF)
mdb.models['Model-1'].rootAssembly.Set(name='m_Set-17', referencePoints=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].referencePoints[3], 
    ))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-6', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#400000 ]', ), ))
mdb.models['Model-1'].Coupling(controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-17'], couplingType=KINEMATIC
    , influenceRadius=WHOLE_SURFACE, localCsys=None, name='Symmetry23', 
    surface=mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-6'], u1=OFF, 
    u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=OFF)
mdb.models['Model-1'].rootAssembly.makeIndependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ))
mdb.models['Model-1'].rootAssembly.makeIndependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'], ))
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ), size=1)
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ))
elemType1 = mesh.ElemType(elemCode=C3D8RH, elemLibrary=STANDARD, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#fff ]', ), )
pickedRegions =(cells1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)
	

#node set creation & re creation of ineractions 
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#24000000 #0:27 #ffc00000 #f ]', ), )
a.Set(nodes=nodes1, name='Set-17')
#: The set 'Set-17' has been created (16 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=352.773, 
    farPlane=595.246, width=31.3657, height=15.2116, viewOffsetX=-20.9874, 
    viewOffsetY=6.74925)
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#d8199999 #fff8001f #1fff8001 #1fff800 #1fff80 #1fff8 #0:22', 
    ' #3fffff #10 #0:41 #8000 #0:41 #1000000 #0:42', 
    ' #8 #0:41 #1000 #0:41 #800000 #0:42 #1', 
    ' #0:41 #800 #0:41 #100000 #0:41 #80000000 #0:42', 
    ' #100 #0:59 #fffffff8 #ffffffff:16 #fffff ]', ), )
a.Set(nodes=nodes1, name='Set-18')

a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Set-17']
mdb.models['Model-1'].constraints['Symmetry'].setValues(surface=region2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=351.154, 
    farPlane=596.865, width=42.5421, height=20.6319, viewOffsetX=-21.8237, 
    viewOffsetY=5.8586)
session.viewports['Viewport: 1'].view.setValues(nearPlane=350.787, 
    farPlane=595.998, width=42.4976, height=20.6103, cameraPosition=(196.55, 
    45.1945, 356.216), cameraUpVector=(0.0901256, 0.988991, -0.117363), 
    cameraTarget=(-6.02996, 11.1703, -86.0602), viewOffsetX=-21.8009, 
    viewOffsetY=5.85247)
session.viewports['Viewport: 1'].view.setValues(nearPlane=346.048, 
    farPlane=600.737, width=77.8358, height=37.7484, viewOffsetX=-23.77, 
    viewOffsetY=3.35152)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Set-18']
mdb.models['Model-1'].constraints['Symmetry23'].setValues(surface=region2)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)

#translate the instance to make the parts close to  each other 
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('Part-2-1', ), vector=(0.0, 2.25, 0.0))
	
# some leftout stuff
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-12')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Aramid', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
