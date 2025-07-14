import random
import re
import time

class RuleBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", "not interested", "no thank you", "not today", "never", "negative", "decline", "pass", "no way", "naur", "no thanks", "not really", "not at all", "nope, not happening", "not for me", "not interested in that", "not my thing")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "see you", "stop", "end", "terminate", "close", "cya", "farewell", "adios", "peace out", "take care", "catch you later", "i'm done", "i'm out", "exit chat", "leave chat", "stop chatting", "end conversation", "close chat", "sign off", "log off", "end session", "stop talking", "i'm finished", "i'm leaving", "i'm gone", "i'm off", "i'm outta here", "i'm signing off", "i'm clocking out", "i'm done here", "i'm taking my leave", "i'm exiting", "i'm bowing out", "i'm checking out", "i'm logging out", "i'm saying goodbye", "i'm parting ways", "i'm bidding farewell")

    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?"
    )

    def __init__(self):
        self.intent_patterns = {
            'describe_planet': r'.*\b(your|alien|planet)\b.*',
            'reason_for_visit': r'.*\bwhy\sare.*|purpose|mission.*',
            'about_intellipaat': r'.*\bintellipaat\b.*'
        }

    def delay_print(self, text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def greet(self):
        self.name = input("What is your name, kind human?\n")
        will_help = input(f"Hello {self.name}, I'm an alien bot learning about Earth. Will you help me?\n").lower()

        if will_help in self.negative_responses:
            self.delay_print("Understood. Have a pleasant Earth day! 🚀")
            return

        self.chat()

    def make_exit(self, reply):
        return any(command in reply for command in self.exit_commands)

    def chat(self):
        self.delay_print("Great! Let's begin...\n")
        while True:
            reply = input(random.choice(self.random_questions) + "\n").lower()

            if self.make_exit(reply):
                self.delay_print("Goodbye, Earthling! Stay curious ")
                break

            response = self.match_intent(reply)
            if self.make_exit(response): 
                self.delay_print("Goodbye, Earthling! Stay curious ")
                break

            reply = input(response).lower()
            if self.make_exit(reply):
                self.delay_print("Goodbye, Earthling! Stay curious")
                break

    def negative_emotion_intent(self):
        responses = (
        "I understand. Everyone needs rest sometimes. ☕",
        "No problem! We can chat whenever you're ready.",
        "Take it easy. I’ll be here if you change your mind!"
    )
        return random.choice(responses) + "\n"

    def match_intent(self, reply):
        for intent, pattern in self.intent_patterns.items():
            if re.search(pattern, reply, re.IGNORECASE):
                return getattr(self, f"{intent}_intent")()
            elif intent == 'negative_emotion':
                return self.negative_emotion_intent()

        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a harmonious blend of technology and nature.",
            "We have floating cities and forests that glow at night. It's quite beautiful.",
            "We value peace, knowledge, and great coffee — like some of you do!"
        )
        return random.choice(responses) + "\n"

    def reason_for_visit(self):
        responses = (
            "I'm here out of curiosity and wonder — and to study your fascinating world.",
            "I come in peace, with a quest for knowledge and coffee recommendations!",
            "My mission is to understand your species and build interplanetary friendships."
        )
        return random.choice(responses) + "\n"

    def about_intellipaat(self):
        responses = (
            "Intellipaat is a global learning platform that helps people grow in tech careers.",
            "It's a great place to learn data science, AI, and many futuristic skills.",
            "They teach in a way that's practical, engaging, and career-oriented."
        )
        return random.choice(responses) + "\n"

    def no_match_intent(self):
        responses = (
            "Hmm, could you elaborate on that?",
            "Interesting! Tell me more about it.",
            "That sounds curious. Please explain further.",
            "I'm still learning... Can you clarify what you mean?",
            "Why do you say that?",
            "That’s fascinating. Let’s talk more about it."
        )
        return random.choice(responses) + "\n"

if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
