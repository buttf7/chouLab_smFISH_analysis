import bigfish.multistack as multistack
def cell_extraction(nuc_label, rs_spots, RNA_2D):
    spots_in, spots_out = multistack.identify_objects_in_region(nuc_label, rs_spots, ndim=2)
    fov_results = multistack.extract_cell(
    cell_label=cell_label, 
    ndim=2, 
    nuc_label=nuc_label, 
    rna_coord=rs_spots, 
    image=RNA_2D)
    
    print("detected spots (inside nuclei)")
    print("\r shape: {0}".format(spots_in.shape))
    print("\r dtype: {0}".format(spots_in.dtype), "\n")
    print("detected spots (outside nuclei)")
    print("\r shape: {0}".format(spots_out.shape))
    print("\r dtype: {0}".format(spots_out.dtype))
    print("number of cells identified: {0}".format(len(fov_results)))
    return fov_results
