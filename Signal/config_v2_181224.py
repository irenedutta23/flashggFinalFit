# Config file: options for signal fitting

_year = '2022'

signalScriptCfg = {
  
  # Setup
  'inputWSDir': '/uscms_data/d3/idutta/HHbbgg_Run3_fits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/input_v2_181224/ws_GG2HH/',
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'v2_181224',#_%s_nGaus'%_year,
  'analysis':'v2_181224', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',
  'xvar':'Diphoton_Mass',
  'skipVertexSplit': '--skipVertexScenarioSplit', #For HH searches, skip this if you are forming single Hgg with split vertex
    #Photon shape systematics  
  'scales':'',#'Scale', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'',#'Smearing', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso',

}
