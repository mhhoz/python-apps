import random
from datetime import datetime

class Chatbot:
    def __init__(self):
        self.name = "WeatherBot"
        self.greetings = [
            "Hello! Hope you're having a great day!", 
            "Hi there! Wonderful to see you!",
            f"Greetings! It's {datetime.now().strftime('%A')}, a perfect day to chat!",
            "Hey! I'm excited to talk with you!"
        ]
        self.farewells = [
            "Goodbye! Have a wonderful rest of your day!",
            "Bye! Looking forward to our next chat!",
            "See you later! Stay amazing!",
            "Take care! Come back soon!"
        ]
        self.responses = {
            "how are you": [
                "I'm doing fantastic, thanks for asking! How about you?",
                "I'm great and excited to help! How are you feeling today?",
                "All good here! I hope your day is going well too!"
            ],
            "what's your name": [
                f"I'm {self.name}, your friendly chat companion!",
                f"You can call me {self.name}! I'm here to chat and help!",
                f"I'm {self.name}! Nice to properly meet you!"
            ],
            "help": [
                "I'm here to help! I can chat about various topics, answer questions about myself, or just have a friendly conversation!",
                "I can assist you in many ways! Try asking how I am, what my name is, or just chat with me!",
                "Let's chat! I'm knowledgeable about various topics and always happy to help!"
            ]
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if not user_input:
            return "I didn't catch that. Could you please say something?"
        
        if any(greeting in user_input for greeting in ["hello", "hi", "hey", "morning", "afternoon", "evening"]):
            return random.choice(self.greetings)
        
        if any(farewell in user_input for farewell in ["bye", "goodbye", "see you", "later"]):
            return random.choice(self.farewells)

        for key, responses in self.responses.items():
            if key in user_input:
                return random.choice(responses)
        
        return random.choice([
            "I'm not quite sure about that. Could you rephrase it?",
            "Interesting! Could you tell me more about what you mean?",
            "I'm still learning! Could you try asking something else?",
            "Hmm, that's a bit tricky for me. Let's try a different topic!"
        ])

def main():
    bot = Chatbot()
    print(f"{bot.name}: Welcome! I'm here to chat with you. Type 'bye' to exit.")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                print(f"{bot.name}:", bot.get_response('bye'))
                break
                
            response = bot.get_response(user_input)
            print(f"{bot.name}:", response)
            
        except KeyboardInterrupt:
            print(f"\n{bot.name}: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"{bot.name}: Oops! Something went wrong. Let's start over.")

if __name__ == "__main__":
    main()
