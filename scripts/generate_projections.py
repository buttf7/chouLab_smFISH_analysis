import bigfish.plot as plot

def generate_projections(img):
    # Define DAPI Channel
    DAPI_3D = img[:,0,:,:]
    DAPI_2D = stack.maximum_projection(DAPI_3D)

    # Probe Channel
    RNA_3D = img[:,1,:,:]
    RNA_2D = stack.maximum_projection(RNA_3D)
    
    images = [DAPI_2D, RNA_2D]
    bigfish.plot.plot_images(images,rescale=True, contrast=True)
    
    return [DAPI_3D, DAPI_2D, RNA_3D, RNA_2D]
