#!/usr/bin/env python

import os, re
import commands
import math

from runOMTFAnalyzer import *
########################################################
########################################################
def submitJob(aFile, dataPath, back):
    #Update the CMSSW configuration
    process.source.fileNames =  cms.untracked.vstring()
    process.source.fileNames.append('file:'+ dataPath + aFile)    
    process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
    ##Prepare working directory
    workdir = dataPath.split("Crab/")[1] + aFile.split(".root")[0]    
    command = "mkdir -p "+workdir
    os.system(command)
    command = "cp job.sh "+workdir
    os.system(command)
    out = open(workdir+'/'+'tmpConfig.py','w')
    out.write(process.dumpPython())
    out.close()
    command = "cd "+workdir+"; qsub -o logs -N "+aFile+" ./job.sh"
    command = "cd "+workdir+"; ./job.sh >& a.out"
    if back==True:
        command+=" &"
    os.system(command)
########################################################
########################################################


dataPaths = ["/cms/cms/akalinow/CMS/OverlapTrackFinder/Crab/Data/OMTFData/760_v2/WToMuNu_Tune4C_13TeV-pythia8/760_v2/151105_160955/0000/",
             "/cms/cms/akalinow/CMS/OverlapTrackFinder/Crab/Data/OMTFData/760_v2/DYToMuMu_M-50_Tune4C_13TeV-pythia8/760_v2/151105_160911/0000/",
             "/cms/cms/akalinow/CMS/OverlapTrackFinder/Crab/Data/OMTFData/760_v2/Neutrino_Pt-2to20_gun/760_v2/151105_161038/0000/"
            ]

########################################################
for path in dataPaths:
    command = "ls "+path 
    fileList = commands.getoutput(command).split("\n")
    index = 0
    for aFile in fileList:
        command = "ps aux | grep cmsRun"
        while commands.getoutput(command).count("cmsRun tmpConfig.py")>=3:
            time.sleep(150)
        submitJob(aFile,dataPath=path, back=True)
        index+=1
########################################################





