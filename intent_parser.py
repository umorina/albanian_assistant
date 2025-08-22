from skills import time_skill, date_skill, weather_skill, search_skill

def handle_intent(text):
    text = text.lower()
    if "ora" in text:
        return time_skill.get_time()
    elif "data" in text:
        return date_skill.get_date()
    elif "mot" in text:
        return weather_skill.get_weather()
    else:
        return search_skill.search(text)
