# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'',
  #'listOfTreeNames' :['ntuple'],
  # Variables to be added to dataframe: use wildcard * for common strings
  
  #new_event_weight is event_weight/(xs*br*lumi)-> extra branch added by hand for FlashggFinalFit datacards
  'mainVars':["Diphoton_Mass","new_event_weight"],#"dZ","weight_*"], # Var for the nominal RooDataSets
  
  ### ^^^^ IF YOU CHANGE THE EVENT WEIGHT VAR NAME HERE, ALSO CHANGE IN TREE2WS.PY ^^^^^
  
  'dataVars':["Diphoton_Mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'systematicsVars':["Diphoton_Mass","new_event_weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':'',#["Scale","Smearing"],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats': ['cat0','cat1','cat2']#'auto'

}
