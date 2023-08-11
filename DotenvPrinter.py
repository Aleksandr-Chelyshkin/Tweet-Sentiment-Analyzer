#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the values
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Print the values
print(f"api_key = {api_key}")
print(f"api_secret = {api_secret}")
print(f"access_token = {access_token}")
print(f"access_token_secret = {access_token_secret}")
