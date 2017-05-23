#!/usr/bin/env python

import os, re, time
import commands
import math

from runOMTFAnalyzer import *
########################################################
########################################################
def submitJob(iPt, sign,dataPath, back):
    signNames = ["m","","p"]
    iptString = str(iPt)+"_"+signNames[sign+1]+"_"
    command = "ls "+dataPath+"/SingleMu_"+iptString+"*"
    fileList = commands.getoutput(command).split("\n")
    #Update the CMSSW configuration
    process.source.fileNames =  cms.untracked.vstring()
    for aFile in fileList:
        process.source.fileNames.append('file:'+aFile)
    process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000))

    process.simOmtfDigis.dumpResultToXML = cms.bool(False)         
    process.simOmtfDigis.XMLDumpFileName = "Ipt_"+iptString+".xml" 
    process.omtfAnalyser.multiplyEvents = cms.uint32(1)

    ##Prepare working directory
    workdir = "SingleMu_"+str(iPt)+"_"+signNames[sign+1]    
    command = "mkdir -p "+workdir
    os.system(command)
    command = "cp job.sh "+workdir
    os.system(command)
    out = open(workdir+'/'+'tmpConfig.py','w')
    out.write(process.dumpPython())
    out.close()
    command = "cd "+workdir+"; qsub -o logs -N "+str(iPt)+"_"+signNames[sign+1]+" ./job.sh"
    command = "cd "+workdir+"; ./job.sh >& a.out"
    if back==True:
        command+=" &"
    os.system(command)
########################################################
########################################################
###Full eta ###
#dataPath = "/cms/cms/akalinow/CMS/OverlapTrackFinder/Crab/SingleMuFullEta/721_FullEta_v4/data/"
dataPath = "/cms/cms/akalinow/CMS/OverlapTrackFinder/Crab/SingleMuFullEtaTestSample/750_FullEta_v2/data/"

iPtMin = 1
iPtMax = 31
###Test settings
#iPtMin = 16
#iPtMax = 17
########################################################
for iPt in xrange(iPtMin,iPtMax+1):

    command = "ps aux | grep cmsRun"
    while commands.getoutput(command).count("cmsRun tmpConfig.py")>=10:
        time.sleep(150)
    submitJob(iPt=iPt,sign=-1,dataPath=dataPath,back=True)
    submitJob(iPt=iPt,sign=1,dataPath=dataPath,back=True)    
########################################################




