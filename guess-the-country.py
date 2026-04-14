import random
import streamlit as st




countries = {
    "Egypt": {"capital": "Cairo", "language": "Arabic", "currency": "EGP", "continent": "Africa", "famous_for": "Pyramids"},
    "France": {"capital": "Paris", "language": "French", "currency": "EUR", "continent": "Europe", "famous_for": "Eiffel Tower"},
    "Japan": {"capital": "Tokyo", "language": "Japanese", "currency": "JPY", "continent": "Asia", "famous_for": "Mount Fuji"},
    "Brazil": {"capital": "Brasilia", "language": "Portuguese", "currency": "BRL", "continent": "South America", "famous_for": "Christ the Redeemer"},
    "Australia": {"capital": "Canberra", "language": "English", "currency": "AUD", "continent": "Oceania", "famous_for": "Sydney Opera House"},
    "Canada": {"capital": "Ottawa", "language": "English", "currency": "CAD", "continent": "North America", "famous_for": "Niagara Falls"},
    "India": {"capital": "New Delhi", "language": "Hindi", "currency": "INR", "continent": "Asia", "famous_for": "Taj Mahal"},
    "China": {"capital": "Beijing", "language": "Chinese", "currency": "CNY", "continent": "Asia", "famous_for": "Great Wall"},
    "Germany": {"capital": "Berlin", "language": "German", "currency": "EUR", "continent": "Europe", "famous_for": "Brandenburg Gate"},
    "Italy": {"capital": "Rome", "language": "Italian", "currency": "EUR", "continent": "Europe", "famous_for": "Colosseum"},
    "Spain": {"capital": "Madrid", "language": "Spanish", "currency": "EUR", "continent": "Europe", "famous_for": "Sagrada Familia"},
    "Mexico": {"capital": "Mexico City", "language": "Spanish", "currency": "MXN", "continent": "North America", "famous_for": "Chichen Itza"},
    "Argentina": {"capital": "Buenos Aires", "language": "Spanish", "currency": "ARS", "continent": "South America", "famous_for": "Tango"},
    "Chile": {"capital": "Santiago", "language": "Spanish", "currency": "CLP", "continent": "South America", "famous_for": "Atacama Desert"},
    "Peru": {"capital": "Lima", "language": "Spanish", "currency": "PEN", "continent": "South America", "famous_for": "Machu Picchu"},
    "Colombia": {"capital": "Bogota", "language": "Spanish", "currency": "COP", "continent": "South America", "famous_for": "Coffee"},
    "Venezuela": {"capital": "Caracas", "language": "Spanish", "currency": "VES", "continent": "South America", "famous_for": "Angel Falls"},
    "Ecuador": {"capital": "Quito", "language": "Spanish", "currency": "USD", "continent": "South America", "famous_for": "Galapagos Islands"},
    "USA": {"capital": "Washington DC", "language": "English", "currency": "USD", "continent": "North America", "famous_for": "Statue of Liberty"},
    "UK": {"capital": "London", "language": "English", "currency": "GBP", "continent": "Europe", "famous_for": "Big Ben"},
    "Netherlands": {"capital": "Amsterdam", "language": "Dutch", "currency": "EUR", "continent": "Europe", "famous_for": "Windmills"},
    "Belgium": {"capital": "Brussels", "language": "Dutch", "currency": "EUR", "continent": "Europe", "famous_for": "Chocolate"},
    "Switzerland": {"capital": "Bern", "language": "German", "currency": "CHF", "continent": "Europe", "famous_for": "Alps"},
    "Austria": {"capital": "Vienna", "language": "German", "currency": "EUR", "continent": "Europe", "famous_for": "Mozart"},
    "Sweden": {"capital": "Stockholm", "language": "Swedish", "currency": "SEK", "continent": "Europe", "famous_for": "IKEA"},
    "Norway": {"capital": "Oslo", "language": "Norwegian", "currency": "NOK", "continent": "Europe", "famous_for": "Fjords"},
    "Denmark": {"capital": "Copenhagen", "language": "Danish", "currency": "DKK", "continent": "Europe", "famous_for": "Lego"},
    "Finland": {"capital": "Helsinki", "language": "Finnish", "currency": "EUR", "continent": "Europe", "famous_for": "Sauna"},
    "Poland": {"capital": "Warsaw", "language": "Polish", "currency": "PLN", "continent": "Europe", "famous_for": "Pierogi"},
    "Czech Republic": {"capital": "Prague", "language": "Czech", "currency": "CZK", "continent": "Europe", "famous_for": "Old Town"},
    "Hungary": {"capital": "Budapest", "language": "Hungarian", "currency": "HUF", "continent": "Europe", "famous_for": "Thermal baths"},
    "Greece": {"capital": "Athens", "language": "Greek", "currency": "EUR", "continent": "Europe", "famous_for": "Ancient ruins"},
    "Turkey": {"capital": "Ankara", "language": "Turkish", "currency": "TRY", "continent": "Asia", "famous_for": "Hagia Sophia"},
    "Russia": {"capital": "Moscow", "language": "Russian", "currency": "RUB", "continent": "Europe", "famous_for": "Kremlin"},
    "Ukraine": {"capital": "Kyiv", "language": "Ukrainian", "currency": "UAH", "continent": "Europe", "famous_for": "Sunflower fields"},
    "Portugal": {"capital": "Lisbon", "language": "Portuguese", "currency": "EUR", "continent": "Europe", "famous_for": "Seafood"},
    "Ireland": {"capital": "Dublin", "language": "English", "currency": "EUR", "continent": "Europe", "famous_for": "Green landscapes"},
    "Iceland": {"capital": "Reykjavik", "language": "Icelandic", "currency": "ISK", "continent": "Europe", "famous_for": "Volcanoes"},
    "South Africa": {"capital": "Pretoria", "language": "English", "currency": "ZAR", "continent": "Africa", "famous_for": "Table Mountain"},
    "Nigeria": {"capital": "Abuja", "language": "English", "currency": "NGN", "continent": "Africa", "famous_for": "Nollywood"},
    "Kenya": {"capital": "Nairobi", "language": "Swahili", "currency": "KES", "continent": "Africa", "famous_for": "Safari"},
    "Morocco": {"capital": "Rabat", "language": "Arabic", "currency": "MAD", "continent": "Africa", "famous_for": "Marrakesh"},
    "Algeria": {"capital": "Algiers", "language": "Arabic", "currency": "DZD", "continent": "Africa", "famous_for": "Sahara"},
    "Tunisia": {"capital": "Tunis", "language": "Arabic", "currency": "TND", "continent": "Africa", "famous_for": "Carthage"},
    "Ethiopia": {"capital": "Addis Ababa", "language": "Amharic", "currency": "ETB", "continent": "Africa", "famous_for": "Coffee origin"},
    "Ghana": {"capital": "Accra", "language": "English", "currency": "GHS", "continent": "Africa", "famous_for": "Gold Coast"},
    "Saudi Arabia": {"capital": "Riyadh", "language": "Arabic", "currency": "SAR", "continent": "Asia", "famous_for": "Mecca"},
    "UAE": {"capital": "Abu Dhabi", "language": "Arabic", "currency": "AED", "continent": "Asia", "famous_for": "Burj Khalifa"},
    "Qatar": {"capital": "Doha", "language": "Arabic", "currency": "QAR", "continent": "Asia", "famous_for": "Wealth"},
    "Kuwait": {"capital": "Kuwait City", "language": "Arabic", "currency": "KWD", "continent": "Asia", "famous_for": "Oil"},
    "Jordan": {"capital": "Amman", "language": "Arabic", "currency": "JOD", "continent": "Asia", "famous_for": "Petra"},
    "Lebanon": {"capital": "Beirut", "language": "Arabic", "currency": "LBP", "continent": "Asia", "famous_for": "Cuisine"},
    "Iran": {"capital": "Tehran", "language": "Persian", "currency": "IRR", "continent": "Asia", "famous_for": "Persian culture"},
    "Pakistan": {"capital": "Islamabad", "language": "Urdu", "currency": "PKR", "continent": "Asia", "famous_for": "Mountains"},
    "Bangladesh": {"capital": "Dhaka", "language": "Bengali", "currency": "BDT", "continent": "Asia", "famous_for": "Rivers"},
    "Vietnam": {"capital": "Hanoi", "language": "Vietnamese", "currency": "VND", "continent": "Asia", "famous_for": "Halong Bay"},
    "Thailand": {"capital": "Bangkok", "language": "Thai", "currency": "THB", "continent": "Asia", "famous_for": "Beaches"},
    "Malaysia": {"capital": "Kuala Lumpur", "language": "Malay", "currency": "MYR", "continent": "Asia", "famous_for": "Petronas Towers"},
    "Singapore": {"capital": "Singapore", "language": "English", "currency": "SGD", "continent": "Asia", "famous_for": "Marina Bay"},
    "Indonesia": {"capital": "Jakarta", "language": "Indonesian", "currency": "IDR", "continent": "Asia", "famous_for": "Bali"},
    "Philippines": {"capital": "Manila", "language": "Filipino", "currency": "PHP", "continent": "Asia", "famous_for": "Islands"},
    "South Korea": {"capital": "Seoul", "language": "Korean", "currency": "KRW", "continent": "Asia", "famous_for": "K-pop"},
    "North Korea": {"capital": "Pyongyang", "language": "Korean", "currency": "KPW", "continent": "Asia", "famous_for": "Isolation"},
    "New Zealand": {"capital": "Wellington", "language": "English", "currency": "NZD", "continent": "Oceania", "famous_for": "Hobbit"},
    "Fiji": {"capital": "Suva", "language": "English", "currency": "FJD", "continent": "Oceania", "famous_for": "Islands"},
    "Papua New Guinea": {"capital": "Port Moresby", "language": "English", "currency": "PGK", "continent": "Oceania", "famous_for": "Tribes"}
}


if "secret_country" not in st.session_state:
    st.session_state.secret_country = random.choice(list(countries.keys()))
    st.session_state.info = countries[st.session_state.secret_country]
    st.session_state.history = []
    st.session_state.game_over = False

info = st.session_state.info

st.title("🎮 Guess The Country Game")

question = st.text_input("Ask a question")

if st.button("Send") and not st.session_state.game_over:
    q = question.lower()

    if "capital" in q:
        response = f"The capital is {info['capital']}"

    elif "language" in q:
        response = f"The language is {info['language']}"

    elif "currency" in q:
        response = f"The currency is {info['currency']}"

    elif "continent" in q:
        response = f"It is in {info['continent']}"

    elif "famous" in q:
        response = f"It is famous for {info['famous_for']}"

    elif q in ["give up", "i give up"]:
        response = f"You gave up 😢 The country was {st.session_state.secret_country}"
        st.session_state.game_over = True

    else:
        response = "I don't understand 🤔"

    st.session_state.history.append(("You", question))
    st.session_state.history.append(("Game", response))

guess = st.text_input("Guess the country")

if st.button("Guess") and not st.session_state.game_over:
    if guess.title() == st.session_state.secret_country:
        st.success("🎉 Correct! You won!")
        st.session_state.game_over = True
    else:
        st.error("❌ Wrong! Try again")

st.subheader("💬 Chat")

for sender, msg in st.session_state.history:
    st.write(f"{sender}: {msg}")

if st.button("🔄 Restart Game"):
    st.session_state.secret_country = random.choice(list(countries.keys()))
    st.session_state.info = countries[st.session_state.secret_country]
    st.session_state.history = []
    st.session_state.game_over = False


