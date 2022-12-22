
def convert_units(names, heights, weights):
    
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    name_data = {}

    for idx, name in enumerate(names):
        name_data[name] = (new_hts[idx], new_wts[idx])

    return name_data