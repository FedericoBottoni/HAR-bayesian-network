from Config import Config

def range(snapshots):
    parsedData = list()
    test = list()
    print('LOG: Discretizing the dataset')
    config = Config()
    line = 0
    for row in snapshots:
        line += 1
        if line <= len(snapshots) * 0.75:
            parsedData.append(row.getDiscretizedInstance(config.getRangeSize()))
        else:
            test.append(row.getDiscretizedInstance(config.getRangeSize()))
            return  [parsedData, test]