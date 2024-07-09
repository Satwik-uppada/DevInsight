import streamlit as st
import time

# Function to simulate progress
def simulate_progress():
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for percent_complete in range(101):
        # Update progress bar
        progress_bar.progress(percent_complete)
        
        # Update status text
        status_text.text(f'Progress: {percent_complete}%')
        
        # Add a delay to simulate work being done
        time.sleep(0.1)

    # After completion, replace progress bar with a message
    status_text.text('Progress completed!')

# Run the progress simulation function
simulate_progress()
