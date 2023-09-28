streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_reponse=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
