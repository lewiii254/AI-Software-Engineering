
# CryptoBuddy - Your First AI-Powered Financial Sidekick! 🌟

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def chatbot():
    print("👋 Hey there! I'm *CryptoBuddy*, your AI-powered crypto sidekick! Ask me anything about crypto profitability or sustainability. 💸🌱\n")

    while True:
        user_query = input("You: ").lower()

        if "exit" in user_query or "bye" in user_query:
            print("CryptoBuddy: 🚀 Stay safe out there, crypto explorer! Remember: always do your own research! 🛡️")
            break

        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: I recommend {recommend}! 🌱 It's eco-friendly with a strong sustainability score of {crypto_db[recommend]['sustainability_score']*10}/10!")

        elif "trending" in user_query or "rising" in user_query:
            rising_cryptos = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print(f"CryptoBuddy: 🚀 These cryptos are trending up: {', '.join(rising_cryptos)}.")

        elif "growth" in user_query or "long-term" in user_query:
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                    print(f"CryptoBuddy: I suggest looking at {coin}! 📈 It's on the rise and has promising long-term growth potential.")
                    break

        elif "energy" in user_query:
            low_energy = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
            print(f"CryptoBuddy: ⚡️ These cryptos use low energy: {', '.join(low_energy)}.")

        else:
            print("CryptoBuddy: 🤖 Hmm, I didn’t catch that. Try asking about trending, sustainable, or growth-focused cryptos!")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
