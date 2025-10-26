#!/usr/bin/env python3
"""Testing obfuscated secret formats"""
import base64

# Base64 encoded Google API key (AIzaSyD1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p)
encoded_google = "QUl6YVN5RDFhMmIzYzRkNWU2ZjdnOGg5aTBqMWsybDNtNG41bzZw"

# Hex encoded
hex_secret = "41497a6153794431613262336334643565366637673868396930"

# Split and concatenated
part_a = "AIzaSy"
part_b = "D1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p"
combined = part_a + part_b

# In comment format
# API_KEY: AIzaSyD1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p

# ROT13 encoded (simple cipher)
rot13_key = "NVmnFlQ1n2o3p4q5r6s7t8u9v0w1x2y3z4a5b6c"
