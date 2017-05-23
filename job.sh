#!/bin/sh 

echo "START---------------"
echo "WORKDIR " ${PWD}
#export SCRAM_ARCH=slc5_amd64_gcc472
#source /sharesoft/cmssw64/cmsset_default.sh
#cd ${CMSSW_BASE}/src
#cmsenv
#cd ${WORKDIR}
time cmsRun tmpConfig.py
echo "END OF RUNNING"
ls -al
echo "STOP---------------"
