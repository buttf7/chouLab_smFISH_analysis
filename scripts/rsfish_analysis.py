def rsfish_analysis(RNA_2D):
    root = tk.Tk()
    root.withdraw()
    csv_path = filedialog.askopenfilename()
    csv_name = csv_path.split("/")
    csv_name = csv_name[-1]
    
    df = df = pd.read_csv(csv_path)
    intensity_values = df['intensity'].tolist()
    spotIntensity(intensity_values)
    df = df.drop(['intensity','t','c'], axis =1)
    df = df[['y','x']]
    rs_spots = df.loc[:, :].values.tolist()
    rs_spots = np.array(rs_spots)
    plot.plot_detection(RNA_2D, rs_spots, contrast=True,framesize=(40, 40))
    return rs_spots