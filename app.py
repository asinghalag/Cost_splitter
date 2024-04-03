import streamlit as st
import pandas as pd

# Function to calculate equal split
def calculate_equal_split(amount, participants):
    split_amount = amount / len(participants)
    return {participant: split_amount for participant in participants}

# Function to calculate weighted split
def calculate_weighted_split(amount, weights):
    total_weight = sum(weights.values())
    return {participant: (weight / total_weight) * amount for participant, weight in weights.items()}

st.title('Shared Expense Splitter')

with st.form("expense_form", clear_on_submit=True):
    expense_name = st.text_input('Expense Name')
    total_amount = st.number_input('Total Amount', min_value=0.0, format='%.2f')
    num_participants = st.number_input('Number of Participants', min_value=1, step=1, format='%d')
    
    split_type = st.radio("Split Type", ('Equal', 'Weighted'))
    
    participants = {}
    if split_type == 'Weighted':
        for i in range(int(num_participants)):
            name = st.text_input(f'Participant {i+1} Name', key=f'name_{i}')
            weight = st.number_input(f'Participant {i+1} Weight', min_value=0.01, format='%.2f', key=f'weight_{i}')
            participants[name] = weight
    else:
        for i in range(int(num_participants)):
            name = st.text_input(f'Participant {i+1} Name', key=f'name_{i}')
            participants[name] = 1  # Equal weight
    
    submitted = st.form_submit_button("Calculate Splits")
    
    if submitted and participants:
        if split_type == 'Equal':
            splits = calculate_equal_split(total_amount, participants.keys())
        else:
            splits = calculate_weighted_split(total_amount, participants)
        
        st.subheader('Split Details:')
        for participant, amount in splits.items():
            st.write(f"{participant} owes: ${amount:.2f}")

