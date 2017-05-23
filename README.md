This repository holds utility scripts for running OMTF tests.
It requires setup CMSSW workspace with UserCode/L1RpcTriggerAnalysis/
and DataFormats/L1RpcTriggerAnalysis/ packages.

To run OMTF on single muon samples use:

----
./submitJobs.py
----

By default the scriupt run over all pt codes.
Modify pt ranges

----
iPtMin = 1
iPtMax = 31
----

for running on smaller ammount of events. By default four jobs are run in
parallel.


To run OMTF on official DY, WJets and Neutrino samples use:

----
submitJobsDataset.py
----

The results are saved into separate directories foe each job. Merge thos into a single file with ROOT hadd:

----
hadd EfficiencyTree.root SingleMu_*/EfficiencyTree.root
----

If you are processing datasets, save events frome eahc process (W, DY, Neutrino) into separate file.
