import streamlit as st
import pandas as pd
import os

# CSV file name
DATA_FILE = "slots.csv"

# Load or create data
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Slot", "Group", "Team Members", "Slide Link"])

# Define available slots
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

# App title
st.set_page_config(page_title="PSA Presentation Slot Booking", layout="centered")
st.title("📅 PSA Presentation Slot Booking — Tuesday 17/6/2025")

# Booking form
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

# Admin delete panel
st.markdown("---")
st.subheader("🔐 Admin Panel – Delete a Booking")

admin_password = st.text_input("Enter admin password", type="password")

if admin_password == "delete123":  # You can change this password
    group_to_delete = st.text_input("Enter Group name to delete (e.g., G5)")
    
    if st.button("❌ Delete Booking"):
        if group_to_delete.strip() in df["Group"].values:
            df = df[df["Group"] != group_to_delete.strip()]
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Booking for {group_to_delete.strip()} has been deleted.")
            st.experimental_rerun()
        else:
            st.warning("⚠️ Group not found. Please check the name.")
elif admin_password:
    st.error("Incorrect password.")
