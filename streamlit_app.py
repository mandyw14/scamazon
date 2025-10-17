import random
import streamlit as st

st.set_page_config(page_title="Scamazon: Is it a Scam or Not?", page_icon="🛡️", layout="centered")

SCENARIOS = [
    {"text": "You get an email from the principal linking to the exact school domain on the poster.", "is_scam": False,
     "why": "Known sender + matching domain + no extra info requests."},
    {"text": "A Pop-up appears on your screen: 'You won a phone! Pay shipping with a card to claim.'", "is_scam": True,
     "why": "Prizes that ask for payment info are scams."},
    {"text": "You get a DM (a direct message) that says:'Support here. Share your password to avoid a ban.'", "is_scam": True,
     "why": "Legit support never asks for passwords."},
    {"text": "A School newsletter says: Donate via official website or bring cash to the office.", "is_scam": False,
     "why": "Trusted channel and official site options."},
     {"text": "You're walking home and an adult stops you and asks for your help.", "is_scam": True,
     "why": "Adults should not need help from a kid. They should get help from other adults. You can say I'm sorry, I can't help. Then walk away and go tell someone."},
     {"text": "An adult you don't know asks you to come see their puppy", "is_scam": True,
     "why": "It could be a lure. Adults you don't know should never ask you go anywhere with them. Do not go."},
     {"text": "You're home alone and someone comes to the door saying there is an emergency. They want you to open the door.", "is_scam": True,
     "why": "It may or may not be a scam. It's hard to know. The best thing to do is NOT open the door. You can call 911 for the person while staying safely inside."},
     {"text": "Your friend is in trouble and asks for your help", "is_scam": False,
     "why": "We should help a friend in need, if it's safe to do so. As a kid, you will probably also need to get an adult's help too"},
     {"text": "A new window pops up on the computer while you are searching for information. You don't know what it is.", "is_scam": True,
     "why": "Scams can get unleashed by going onto a scamming website. Sounds like this is what happens. Gt help from an adult to learn how to fix it. "},
     {"text": "Someone online says they are going to share a naked photo of you unless you pay them money", "is_scam": True,
     "why": "This is called sextortion. It won't end when you send money so don't do it. You need to get help from your adult."},
     {"text": "Your bank card starting with (45064**) has been locked, visit https://cibcsecurelogin.com to resolve. Note: Any attempt to unlock access after 11:59PM will necessit a visit at your nearest CIBC branch.", "is_scam": True,
     "why": "Messages that invoke a sense of urgency, i.e., that you have to act fast, are typically scams. Also, the first 4 digits of cards are somewhat standard and generic."},
    {"text": "You get a text that says: Thank you for your recent purchase... and then references a purchase you just made", "is_scam": False,
     "why": "The message included personal, not generic information and also didn't ask you to click on anything."},
    {"text": "You see a poster that says: 'Free Kittens.' And you see a QR code.", "is_scam": True,
     "why": "It may or may not be a scam. If you want a kitten, talk to your adult and then do some investigating into whether the poster is legit or a scam."},

]
# {"text": "INSERT", "is_scam": False/True,
#     "why": "INSERT THE RATIONALE HERE"},

if "deck" not in st.session_state:
    st.session_state.deck = random.sample(SCENARIOS, k=len(SCENARIOS))
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.locked = False
    st.session_state.feedback = ""

st.title("🛡️ Scamazon: Is it a Scam or Not?")
st.caption("Read each scenario. Decide if it’s likely a *scam* or *not a scam*.")

i = st.session_state.idx
deck = st.session_state.deck

if i < len(deck):
    s = deck[i]
    st.markdown(f"### Question {i+1} of {len(deck)}")
    st.write(s["text"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Scam", disabled=st.session_state.locked):
            st.session_state.locked = True
            correct = True == s["is_scam"]
            if correct: st.session_state.score += 1
            st.session_state.feedback = ("✅ Correct! " if correct else "❌ Not quite. ") + s["why"]
    with col2:
        if st.button("Not a Scam", disabled=st.session_state.locked):
            st.session_state.locked = True
            correct = False == s["is_scam"]
            if correct: st.session_state.score += 1
            st.session_state.feedback = ("✅ Correct! " if correct else "❌ Not quite. ") + s["why"]

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    if st.session_state.locked and st.button("Next"):
        st.session_state.idx += 1
        st.session_state.locked = False
        st.session_state.feedback = ""
        st.rerun()
else:
    percent = round((st.session_state.score/len(deck))*100)
    st.success(f"Finished! Score: {st.session_state.score}/{len(deck)} ({percent}%).")
    st.caption("Tips: Match URLs with known sources, never share passwords, be wary of 'free prizes'. Parents: for more information go to https://protectkidsonline.ca/app/en/")
    if st.button("Play again"):
        for k in ["deck","idx","score","locked","feedback"]:
            st.session_state.pop(k, None)
        st.rerun()
