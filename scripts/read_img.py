#Function for reading image
# Author: Arthur Imbert <arthur.imbert.pro@gmail.com>
def read_img():
    root = tk.Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename()
    img_name = img_path.split("/")
    img_name = img_name[-1]
    img = stack.read_image(img_path)
    print("\r shape: {0}".format(img.shape))
    print("\r dtype: {0}".format(img.dtype))
    return (img, img_name)
