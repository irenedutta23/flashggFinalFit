# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'',
  #'listOfTreeNames' :['ntuple'],
  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["Diphoton_Mass","weight"],#"dZ","weight_*"], # Var for the nominal RooDataSets
  'dataVars':["Diphoton_Mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'systematicsVars':["Diphoton_Mass","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':'',#["Scale","Smearing"],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats': ['cat0','cat1','cat2']#'auto'

}
