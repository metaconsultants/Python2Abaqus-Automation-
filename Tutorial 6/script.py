###########################################################################
#   Author:           # copyright - metaengineeringconsultants@gmail.com  #
# abaqus 2017 compatibility                                               #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
#   By:               NKJ                                                 #
#   Version:          1.1.1                                               #
#                                                                         #
#       		                                                          #
#                                                                         #
#                                                                         #
#                                                                         #                     
#                               		                                  #
#                     													  #
#                                                                         #
#                                                                         #
###########################################################################
"""
Abaqus 2017
------------------

This program opens an Abaqus output file and computes the maximum equivalent or component stress/strain
Note: This script requires an Abaqus Python installation! 
Replacement keyword LE --> S for stress measures
Parameters
~~~~~~~~~~
"""
import odbAccess
from abaqus import *
from abaqusConstants import *
from caeModules import *
import copy
import operator
import os
import visualization
import math
import string
import displayGroupOdbToolset
import displayGroupOdbToolset as dgo

#Input parameters GUI -- Read odb

odbfile = 'Y:/run_NKJ/dogbone/dogbone.odb'
o2 = session.openOdb(name=odbfile, readOnly=True) 
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
odb = session.odbs[odbfile]

#stepTimes for step tension
stepTimes = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
frames = len(odb.steps['tension'].frames)
autoComputeLimits = TRUE

strainComponents = [ 'LE11', 'LE22', 'LE33', 'LE12', 'LE13', 'LE23' ]


    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
def getmaxEquiStrain(odb, stepTimes):
     
	INSTANCE =  'DOGBONE-1'
	maxPrincStrains = []
	maxPrincElements = []
	
	for stepTime in stepTimes:
	
		InternalSet = odb.rootAssembly.instances[INSTANCE].elementSets['SET-1']
		strainField = odb.steps['tension'].getFrame(frameValue=stepTime, match=CLOSEST).fieldOutputs['LE'].getSubset(region=InternalSet)
		fieldValues = strainField.values
		Principals = []
		PrincElements = []
			
		for j in fieldValues:
			
			Principals += [j.maxPrincipal]
			PrincElements += [j.elementLabel]
				
						
		maxPrincStrains.append(max(Principals))
		idx1 = Principals.index(max(Principals))
		maxPrincElements.append(PrincElements[idx1])
			
	return ('Principal strains:', maxPrincStrains, maxPrincElements)      

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getmaxStrain(odb, stepTimes):
     
    INSTANCE =  'DOGBONE-1'
    LE11 = []
    LE22 = []
    LE33 = []
    LE12 = []
    LE13 = []
    LE23 = []    
	
    for stepTime in stepTimes:
	
		InternalSet = odb.rootAssembly.instances[INSTANCE].elementSets['SET-1']
		strainField = odb.steps['tension'].getFrame(frameValue=stepTime, match=CLOSEST).fieldOutputs['LE'].getSubset(region=InternalSet)
		fieldValues = strainField.values
		STRAIN11 = []
		STRAIN22 = []
		STRAIN33 = []
		STRAIN12 = []
		STRAIN13 = []
		STRAIN23 = []
			
		for i in range(0,len(fieldValues)):
			
			STRAIN11 += [fieldValues[i].data[0]]
			STRAIN22 += [fieldValues[i].data[1]] 
			STRAIN33 += [fieldValues[i].data[2]] 
			STRAIN12 += [fieldValues[i].data[3]] 
			STRAIN13 += [fieldValues[i].data[4]] 
			STRAIN23 += [fieldValues[i].data[5]] 
				
						
		LE11.append(max(STRAIN11))
		LE22.append(max(STRAIN22))
		LE33.append(max(STRAIN33))
		LE12.append(max(STRAIN12))
		LE13.append(max(STRAIN13))
		LE23.append(max(STRAIN23))        
        
    return ('Component strains:', LE11, LE22, LE33, LE12, LE13, LE23)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    
