import ROOT

# Open the input ROOT file and get the input tree
input_file = ROOT.TFile("input_testV_231024/Signal_output_M125.root", "READ")
# Names of the trees in the input file
tree_names = ["gghh_125_13p6TeV_cat0", "gghh_125_13p6TeV_cat1", "gghh_125_13p6TeV_cat2"]  # Replace with the actual tree names
scale_factor = 34.43 * 0.0026 * 34.7

# Create the output ROOT file and clone the tree structure
output_file = ROOT.TFile("input_testV_231024/Signal_output_M125_new.root", "RECREATE")
for tree_name in tree_names:
    input_tree = input_file.Get(tree_name)  # Replace 'tree_name' with the actual tree name
    output_tree = input_tree.CloneTree(0)  # Clone only the structure, not the entries

    # Define the new branch

    new_branch_value = ROOT.std.vector('float')(1)  # Vector for the new branch
    new_branch = output_tree.Branch("new_event_weight", new_branch_value)

    # Loop over the entries, fill the new branch, and copy the old data
    for i in range(input_tree.GetEntries()):
        input_tree.GetEntry(i)
        event_weight = getattr(input_tree, "event_weight")
        new_branch_value[0] = event_weight / scale_factor
        output_tree.Fill()

    # Write the output tree to the file and close files
    output_tree.Write()
output_file.Close()
input_file.Close()