from accesslink import AccessLink
from utils import load_config, save_config, pretty_print_json

CONFIG_FILENAME = "config.yml"

config = load_config(CONFIG_FILENAME)
if "access_token" not in config:
    print("Authorization is required. Run authorization_client.py first.")
    exit()

accesslink = AccessLink(client_id=config["client_id"],
                        client_secret=config["client_secret"])

# recuperation des infos utilisateur
user_info = accesslink.users.get_information(user_id= config["user_id"], access_token=config["access_token"])
# pretty_print_json(user_info)

# recuperation des infos d'entrainement
training_transaction = accesslink.training_data.create_transaction(user_id= config["user_id"], access_token=config["access_token"])
pretty_print_json(training_transaction.list_exercises())

training_details = []
for url in training_transaction.list_exercises()["exercises"]:
    exercise_summary = training_transaction.get_exercise_summary(url)
    training_details.append(exercise_summary)
    # pretty_print_json(exercise_summary)

# recuperation des infos d'entrainement
physical_info_transaction = accesslink.training_data.create_transaction(user_id= config["user_id"], access_token=config["access_token"])
pretty_print_json(physical_info_transaction.list_exercises())

physical_info_details = []
for url in physical_info_transaction.list_exercises()["exercises"]:
    exercise_summary = physical_info_transaction.get_exercise_summary(url)
    physical_info_details.append(exercise_summary)
    # pretty_print_json(exercise_summary)