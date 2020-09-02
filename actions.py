from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
#
#
class Actiongreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/greet.mp3")

        return []

class ActionPitchRealEstate(Action):

    def name(self) -> Text:
        return "action_pitch_real_estate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/pitch_real_estate.mp3")

        return []

class ActionRealEstateMoreOne(Action):

    def name(self) -> Text:
        return "action_real_estate_more_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/real_estate_more_1.mp3")

        return []

class ActionRealEstateMoreTwo(Action):

    def name(self) -> Text:
        return "action_real_estate_more_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/real_estate_more_2.mp3")

        return []

class ActionRealEstateMoreThree(Action):

    def name(self) -> Text:
        return "action_real_estate_more_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/real_estate_more_3.mp3")

        return []

class ActionRealEstateMoreFour(Action):

    def name(self) -> Text:
        return "action_real_estate_more_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/real_estate_more_4.mp3")

        return []

class ActionRealEstateMoreFive(Action):

    def name(self) -> Text:
        return "action_real_estate_more_5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/real_estate_more_5.mp3")

        return []

class ActionSelfStorage(Action):

    def name(self) -> Text:
        return "action_self_storage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/pitch_self_storage.mp3")

        return []

class ActionRebuttlesOne(Action):

    def name(self) -> Text:
        return "action_rebuttles_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/rebuttles_1.mp3")

        return []

class Action_no_self_storage_1(Action):

    def name(self) -> Text:
        return "action_no_self_storage_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/no_self_storage_1.mp3")

        return []

class Action_no_self_storage_2(Action):

    def name(self) -> Text:
        return "action_no_self_storage_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/no_self_storage_2.mp3")

        return []

class ActionTransferCall(Action):

    def name(self) -> Text:
        return "action_transfer_call"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("transfer")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/transfer_call.mp3")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)

        return []

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/bye.mp3")

        return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
       
        dispatcher.utter_message("transfer")
        dispatcher.utter_message("https://axlewebtech.com/kumar/Precision/transfer_call.mp3")
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        