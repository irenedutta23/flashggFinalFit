# Config file: options for bkg fitting
_year ='2022'
backgroundScriptCfg = {
  
  # Setup
  'inputWS': '/uscms_data/d3/idutta/HHbbgg_Run3_fits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/input_testV_231024/ws_data/Data_output_M125_GG2HH.root',
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'testV_231024_%s'%_year,
  'catOffset':0,
  'year':'2022',   # Use 'combined' if merging all years: not recommended    
  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso',

}
