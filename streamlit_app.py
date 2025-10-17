import random
import streamlit as st

st.set_page_config(page_title="Scamazon: Is it a Scam or Not?", page_icon="🛡️", layout="centered")

SCENARIOS = [
    {"text": "Email from principal linking to the exact school domain on the poster.", "is_scam": False,
     "why": "Known sender + matching domain + no extra info requests."},
    {"text": "Pop-up: 'You won a phone! Pay shipping with a card to claim.'", "is_scam": True,
     "why": "Prizes that ask for payment info are scams."},
    {"text": "Game DM: 'Support here. Share your password to avoid a ban.'", "is_scam": True,
     "why": "Legit support never asks for passwords."},
    {"text": "School newsletter: donate via official website or bring cash to the office.", "is_scam": False,
     "why": "Trusted channel and official site options."},
     {"text": "An adult asks you for help.", "is_scam": True,
     "why": "Adults should not need help from a kid. They should get help from other adults. Tell them you can't help and then you should go get help yourself"},
     {"text": "An adult asks you to come play with their puppy", "is_scam": True,
     "why": "It could be a lure. Adults you don't know should NOT ask you go anywhere with you."},
#    {"text": "INSERT SCENARIO HERE", "is_scam": False/True,
#     "why": "INSERT REASON HERE"},
]

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
    st.caption("Tips: Match URLs with known sources, never share passwords, be wary of 'free prizes'.")
    if st.button("Play again"):
        for k in ["deck","idx","score","locked","feedback"]:
            st.session_state.pop(k, None)
        st.rerun()
