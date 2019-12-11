import csv
import random
import codecs
from models.poll import PollObject


class PollMessageGeneratorService:
    """Grabs random entry from 'surfpooldataset.csv' and outputs it as a PoolObject

    :param dataset_filename: Filename for .csv dataset of all available poll messages
        (default is 'surfpooldavaset.csv', located in the project root folder)
    :type dataset_filename: string
    :returns: a PollObject with the selected "message" and corresponding "yes/no" options
    :rtype: PollObject
    """

    def __init__(self, dataset_filename="surfpooldata.csv"):
        self.dataset_filename = dataset_filename

    def call(self):
        with codecs.open(self.dataset_filename, "rb", "utf8") as f:
            reader = csv.reader(f, delimiter=";")
            messages = [row for row in reader]

        message, yes, no = random.choice(messages)
        return PollObject(message=message, yes=yes, no=no)
