import requests


class PopDBFromJsonWithCategories:
    """
    This class allow to populate the application's database with data from Open Fact Foods. One function (
    json_from_api) call the API to get json file for one food. Another function (pop_db) populate the database with
    the json file. A third function (pop_db_with_categories) call the two precedent function to populate database
    with foods from 30 different categories of foods.
    """

    @staticmethod
    def json_from_api(name_category):
        """Call the API to get json file for one food."""
        pass
        payload = {
            'action': 'process', 'tagtype_0': 'categories',
            'tag_contains_0': 'contains', 'tag_0': "\'" + name_category + "\'",
            'sort_by': 'unique_scans_n', 'page_size': '100',
            'axis_x': 'energy', 'axis_y': 'products_n', 'json': '1'
        }
        req = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
        )
        data_category_json = req.json()
        return data_category_json, name_category

    @staticmethod
    def variables_from_foods_json(data_category_json, name_category):
        """Extract useful data from json and stock it in variables"""
        # Loop through data_category_json and stock useful data in dictionary_from_json
        dictionary_from_json = []
        for data in data_category_json['products']:
            try:
                if data['product_name_fr'] == '':
                    food_name = name_category
                else:
                    food_name = data['product_name_fr']
                food_url = data['url']
                score_nova_group = data['nova_group']
                nutri_score_grad = data['nutriscore_grade']
                image_src = data['image_url']
                allergen_list = data['allergens_tags']
            except:
                print("Loop through the data_category_json doesn't work")
            dictionary_from_json.append([{"food_name": food_name, "category": name_category,
                                            "score_nova_group": score_nova_group,
                                            "nutri_score_grad": nutri_score_grad,
                                            "food_url": food_url,
                                            "image_src": image_src,
                                            "allergen_list": [allergen for allergen in allergen_list]}])

        print(dictionary_from_json)
        return dictionary_from_json

    def pop_db(self):
        """Populate the database with the json file."""
        pass

    def pop_db_with_categories(self):
        """Use json_from_api and pop_db for 30 differents categories of foods. """
        pass
