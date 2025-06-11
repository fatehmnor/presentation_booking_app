import streamlit as st
import pandas as pd
import os

# Set CSV filename
DATA_FILE = "slots.csv"

# Load or create DataFrame
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Slot", "Group", "Team Members", "Slide Link"])

# Define all available slots
available_slots = [
    "Slot 1: 8:30 AM – 8:45 AM",
    "Slot 2: 8:50 AM – 9:05 AM",
    "Slot 3: 9:10 AM – 9:25 AM",
    "Slot 4: 9:30 AM – 9:45 AM",
    "Slot 5: 9:50 AM – 10:05 AM",
    "Slot 6: 10:10 AM – 10:25 AM",
    "Slot 7: 10:30 AM – 10:45 AM"
]

# Remove taken slots
taken_slots = df["Slot"].tolist()
remaining_slots = [slot for slot in available_slots if slot not in taken_slots]

# Streamlit UI
st.set_page_config(page_title="PSA Presentation Slot Booking", layout="centered")
st.title("📅 PSA Presentation Slot Booking — Tuesday 17/6/2025")

# Input form
if remaining_slots:
    selected_slot = st.selectbox("🕒 Select Your Presentation Slot", remaining_slots)
    group = st.text_input("🔢 Group (e.g., G1, G2)")
    team_members = st.text_area("👥 Team Members (list all names)")
    slide_link = st.text_input("🔗 Slide Link (Google Slides or PPT)")

    if st.button("✅ Submit Booking"):
        if group.strip() and team_members.strip() and slide_link.strip():
            new_entry = pd.DataFrame([[selected_slot, group.strip(), team_members.strip(), slide_link.strip()]],
                                     columns=["Slot", "Group", "Team Members", "Slide Link"])
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Slot booked successfully for {group.strip()}!")
            st.balloons()
            st.stop()
        else:
            st.warning("⚠️ Please fill in all fields before submitting.")
else:
    st.warning("⚠️ All slots have been booked.")

# Display current bookings
st.markdown("---")
st.subheader("📋 Current Bookings")
st.dataframe(df)
#admin
# Admin reset button (for development use only)
#if st.checkbox("🛠️ Admin: Clear all bookings"):
    #if st.button("🚨 Confirm Reset"):
       # df = pd.DataFrame(columns=["Slot", "Group", "Team Members", "Slide Link"])
       # df.to_csv(DATA_FILE, index=False)
       # st.success("✅ All bookings have been cleared.")
       # st.stop()
