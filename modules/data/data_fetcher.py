import requests
import json


class data_fetcher:

    @staticmethod
    def get_data():
        # GlobalGiving API endpoint for projects
        api_url = "https://api.globalgiving.org/api/public/projectservice/all/projects/active"

        # Your GlobalGiving API key
        api_key = "f7a3ec25-cf95-4e66-bdcf-f31fbf8e1e9b"

        headers = {
            "Accept": "application/json",
        }

        # Define parameters for your API request, such as the number of results and the API key
        params = {
            "api_key": api_key,  
        }

        # Make the GET request to the API with custom headers
        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                data = json.loads(response.text)["projects"]["project"]  # Extract the project data
                # # Iterate through projects and print relevant data
                # project_data = []

                # for project in data:
                #     project_dict = {
                #         "Project Title": project.get("title", "N/A"),
                #         "Project ID": project.get("id", "N/A"),
                #         "Project Summary": project.get("summary", "N/A"),
                #         "Project Location": project.get("country", "N/A"),
                #         "Total Funding Received to Date": str(project.get("funding", "N/A")),
                #         "Remaining Goal to be Funded": str(project.get("remaining", "N/A")),
                #         "Total Funding Goal": str(project.get("goal", "N/A")),
                #         "Project URL": project.get("projectLink", "N/A"),
                #     }
                #     project_data.append(project_dict)

                # Save the data to a JSON file
                with open("modules/data/data.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)

                print("Data has been stored in 'project_data.json'")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON response: {e}")
        else:
            print(f"Error: Unable to retrieve data. Status code: {response.status_code}")