def spotIntensity(intensity_values):
    spotIntensities = pd.DataFrame(intensity_values)
    spotIntensities.to_csv(f'{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}/data/graph_data/spotIntensities{img_name}.csv', index=False)
