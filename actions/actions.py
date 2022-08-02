# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from matplotlib import image

import requests
import arrow 
import dateparser
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGPT(Action):

    def name(self) -> Text:
        return "action_gpt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # txt=tracker.latest_message.text
        # print("text : ",txt)

        current_state = tracker.current_state()
        latest_message = current_state["latest_message"]["text"]
        print("text : ", latest_message)

        return[]