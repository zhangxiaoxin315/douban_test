import yaml

def get_test_data(test_data_pash):
    case = []
    http = []
    expected = []
    with open(test_data_pash,encoding="UTF-8") as f:
        # data = yaml.load(f.read(),Loader=yaml.SafeLoader)
        data = yaml.safe_load(f.read())
        test = list(data['tests'])
        for td in test:
            case.append(td.get('case'))
            http.append(td.get('http'))
            expected.append(td.get('expected'))
    parameters = zip(case,http,expected)
    return case,parameters


