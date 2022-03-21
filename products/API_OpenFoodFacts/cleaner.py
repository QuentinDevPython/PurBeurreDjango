class Cleaner:
    """
    Class that takes in input all the data collected by the class Downloader.
    It cleans the data by conserving only data that has some specific
    characteristics (a product name in french, categories, a grade,
    an url and stores associated to it).

    Args:
        all_data (str dictionnary)
    """

    def __init__(self, all_data):

        self.data = all_data
        self.cleaned_data = list()

        for data_to_clean in self.data:
            if (
                data_to_clean.get("product_name_fr")
                and data_to_clean.get("countries")
                and data_to_clean.get("stores")
                and data_to_clean.get("nutriscore_grade")
                and data_to_clean.get("url")
                and data_to_clean.get("image_url")
                and data_to_clean.get("categories")
            ):
                self.cleaned_data.append(data_to_clean)

        for data in self.cleaned_data:
            data["product_name_fr"] = data.get("product_name_fr").lower().capitalize()
            data["countries"] = self.clean_strings(data.get("countries"))
            data["stores"] = data.get("stores").lower()
            data["nutriscore_grade"] = data.get("nutriscore_grade").upper()
            data["categories"] = self.clean_strings(data.get("categories").lower())
            print(data)


    def clean_strings(self, data):
        string_cleaned = ""
        counter = 0
        
        for item in data.split(','):
            string_cleaned += item.lstrip().capitalize()
            if counter != len(data.split(","))-1:
                string_cleaned += ','
            counter += 1

        return string_cleaned
        
    def get_cleaned_data(self):
        """
        Method that returns the data cleaned (it means only
        the data that has the characterics specified previously).
        """
        return self.cleaned_data