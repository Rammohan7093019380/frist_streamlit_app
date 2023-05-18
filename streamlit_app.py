import streamlit
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

# Streamlit < 0.65
from streamlit.ReportThread import get_report_ctx
try:
    # Streamlit < 0.65
    from streamlit.ReportThread import get_report_ctx

except ModuleNotFoundError:
    try:
        # Streamlit > 0.65
        from streamlit.report_thread import get_report_ctx

    except ModuleNotFoundError:
        try:
            # Streamlit > ~1.3
            from streamlit.script_run_context import get_script_run_ctx as get_report_ctx

        except ModuleNotFoundError:
            try:
                # Streamlit > ~1.8
                from streamlit.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx

            except ModuleNotFoundError:
                # Streamlit > ~1.12
                from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx

# Streamlit > 0.65
from streamlit.report_thread import get_report_ctx

# Streamlit > ~1.3
from streamlit.script_run_context import get_script_run_ctx as get_report_ctx

# Streamlit > ~1.8
from streamlit.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx

# Streamlit > ~1.12
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx
