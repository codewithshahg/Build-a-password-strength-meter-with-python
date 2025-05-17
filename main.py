# main.py

import streamlit as st
import re
import random
import string

# ✅ Function 1: Check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Add lowercase letters (a-z).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔸 Add uppercase letters (A-Z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔸 Add special characters (!@#$%^&*).")

    common_passwords = ['password', '123456', 'qwerty', 'password123', 'admin']
    if password.lower() in common_passwords:
        feedback.append("❌ This password is too common. Please choose another.")
        score = min(score, 2)

    return score, feedback

# ✅ Function 2: Generate strong password
def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_chars) for _ in range(length))

# ✅ Streamlit App
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Checker & Generator")

option = st.radio("Choose an option:", ["Check a password", "Generate a strong password"])

if option == "Check a password":
    password = st.text_input("Enter your password:", type="password")
    if password:
        score, feedback = check_password_strength(password)

        st.markdown(f"### 🔍 Your Password Score: **{score}/5**")

        if score <= 2:
            st.error("❌ Strength: Weak")
        elif score <= 4:
            st.warning("⚠️ Strength: Moderate")
        else:
            st.success("✅ Strength: Strong\n🎉 Great job! Your password is secure.")

        if feedback:
            st.markdown("#### 💡 Suggestions to improve:")
            for f in feedback:
                st.markdown(f"- {f}")

elif option == "Generate a strong password":
    length = st.slider("Select password length:", 8, 20, 12)
    if st.button("🔄 Generate Password"):
        new_pass = generate_strong_password(length)
        st.success(f"🔐 Your New Password:\n`{new_pass}`")
