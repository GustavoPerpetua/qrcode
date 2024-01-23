import streamlit as st
import qrcode
import os

# Directory to save QR code images
qr_code_dir = "qr_codes"

# Ensure the directory exists, or create it
if not os.path.exists(qr_code_dir):
    os.makedirs(qr_code_dir)

# Function to generate QR code
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(qr_code_dir, filename))

# Create a streamlit app
st.set_page_config(page_title="QR Code Generator", page_icon="🌐", layout="centered")
st.title("QR Code Generator")
url = st.text_input("Enter the URL")

if st.button("Generate QR Code"):
    generate_qr_code(url, "qr_code.png")  
    st.image(os.path.join(qr_code_dir, "qr_code.png"), use_column_width=True)
