import sys

def print_help():
    print("Usage: app.py --train <file-path> --ideal <file-path> --test <filepath>")
    print()
    print("--train  file-path to training dataset")
    print("--ideal  file-path to ideal dataset")
    print("--test   file-path to test dataset")


def run():
    training_dataset_found = False
    training_dataset_path = ""

    ideal_dataset_found = False
    ideal_dataset_path = ""

    test_dataset_found = False
    test_dataset_path = ""

    try:
        for i in range(len(sys.argv)):
            match sys.argv[i]:
                case "--train":
                    i = i + 1
                    training_dataset_path = sys.argv[i]
                    training_dataset_found = True
                case "--ideal":
                    i = i + 1
                    ideal_dataset_path = sys.argv[i]
                    ideal_dataset_found = True
                case "--test":
                    i = i + 1
                    test_dataset_path = sys.argv[i]
                    test_dataset_found = True
    except IndexError:
        pass

    if not (training_dataset_found and ideal_dataset_found and test_dataset_found):
        print_help()
    else:
        print("*********************************************")
        print("*               Hello, World!               *")
        print("*********************************************")

        print("Training dataset: {}".format(training_dataset_path))
        print("Ideal dataset: {}".format(ideal_dataset_path))
        print("Test dataset: {}".format(test_dataset_path))

        # Create the train, ideal an test objects
        # using the objects create the tables in the SQLite database

run()
