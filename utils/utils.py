import os

# read all txt files inside test, train, and valid folders
def read_files(path):
    print(path)
    files = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(root, filename))
    return files

folders = ["test", "train", "valid"]

if __name__ == "__main__":
    # for folder in folders:
    #     files = read_files(folder)
    #     for file in files:
    #         with open(file, 'r') as f:
    #             lines = f.readlines()
    #         with open(file, 'w') as f:
    #             for line in lines:
    #                 f.write(line.replace('\n', ' '))

    for folder in folders:
        files = read_files("./stage1-processing/{}".format(folder))
        for file in files:
            print(file, type(file))
