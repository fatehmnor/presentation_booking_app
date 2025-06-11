import streamlit as st
import pandas as pd
import os

# File to store the bookings
DATA_FILE = "slots.csv"

# Load or create the CSV file
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Slot", "Group Number", "Team Members", "Slide Link"])

# Define presentation slots
available_slots = [
    "Slot1 (8:30–8:45am)",
    "Slot2 (8:50–9:05am)",
    "Slot3 (9:10–9:25am)",
    "Slot4 (9:30–9:45am)",
    "Slot5 (9:50–10:05am)",
    "Slot6 (10:10–10:25am)",
    "Slot7 (10:30–10:45am)"
]

# Remove taken slots
taken_slots = df["Slot"].tolist()
remaining_slots = [slot for slot in available_slots if slot not in taken_slots]

# Title
st.title("📅 PSA Presentation Slot Booking System 
Tuesday 17/6/2025")

if remaining_slots:
    selected_slot = st.selectbox("🕒 Choose a Slot", remaining_slots)
    group_number = st.text_input("🔢 Group Number (e.g. G1, G2, etc.)")
    team_members = st.text_area("👥 Team Members (list all names)")
    slide_link = st.text_input("🔗 Slide Link (Google Slides or PPT)")

    if st.button("✅ Submit Booking"):
        if group_number and team_members and slide_link:
            new_entry = pd.DataFrame([[selected_slot, group_number, team_members, slide_link]],
                                     columns=["Slot", "Group Number", "Team Members", "Slide Link"])
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Slot {selected_slot} booked by {group_number}!")
            st.experimental_rerun()
        else:
            st.warning("⚠️ Please fill in all fields before submitting.")
else:
    st.warning("⚠️ All slots have been booked.")

# Display the table of booked slots
st.markdown("---")
st.subheader("📋 Booked Slots Summary")
st.dataframe(df)
