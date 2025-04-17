import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    if len(password) < 8:
        return strength

    # Regex checks
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    checks_passed = sum([bool(has_upper), bool(has_lower), bool(has_digit), bool(has_special)])

    if checks_passed == 4:
        strength = "Strong"
    elif checks_passed >= 2:
        strength = "Medium"

    return strength

def main():
    st.title("🔒 Password Strength Checker")
    password = st.text_input("Enter your password:", type="password")

    if password:
        strength = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")

        if strength == "Weak":
            st.error("⚠️ Your password is weak. Try adding uppercase letters, numbers, or special characters.")
        elif strength == "Medium":
            st.warning("💬 Your password is medium. You can still improve it!")
        else:
            st.success("✅ Your password is strong!")

if __name__ == "__main__":
    main()
