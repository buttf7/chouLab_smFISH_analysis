#Function for creating seperate image channels
def seperate_channels(img, img_name):    
    #Sorted shape
    sorted_shape = sorted([i for i in img.shape])
    n_channels = sorted_shape[0]
    print('This image has {} channels'.format(n_channels))
    z_slices = sorted_shape[1]
    print('This image has {} z-slices'.format(z_slices))
    pixels_x = sorted_shape[2]
    print('This image has {} pixels on the x-axis'.format(pixels_x))
    pixels_y = sorted_shape[3]
    print('This image has {} pixels on the y-axis'.format(pixels_y))
    
    #channel segmentation
    n_channels = sorted_shape[0]
    parentDirectory = "./data/separated_channels"
    directory = os.path.join(parentDirectory, 'FISH_SEARCH', 'data')
    for i in range(n_channels):
        save_name = f"/channel{i}_{img_name}"
        if n_channels == 3:
            channel = img[:,:,:,i]
            stack.save_image(channel,parentDirectory + save_name)
        if n_channels == 2:
            channel = img[:,i,:,:] # 2 channel
            stack.save_image(channel,parentDirectory + save_name)
