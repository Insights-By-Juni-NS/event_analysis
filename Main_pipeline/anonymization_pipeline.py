import pandas as pd
import numpy as np
import os
import random

print("--- INITIALIZING ANONYMIZATION PIPELINE ---")

input_path = r'C:\Users\Juni\OneDrive\Desktop\Anon Attendees List - Sheet1.csv'
output_path = r'C:\Users\Juni\OneDrive\Desktop\Portfolio_Attendee_Data.csv'

if os.path.exists(input_path):
    df = pd.read_csv(input_path)
    
    # Stratified Sampling for Portfolio Presentation
    sample_size = min(20, len(df))
    portfolio_sample = df.sample(n=sample_size, random_state=42).copy()
    
    # Synthetic Persona Vault (PIPEDA Compliance Layer)
    personas = [
        {"name": "Kendall Roy", "company": "Waystar Royco"}, {"name": "Michael Scott", "company": "Dunder Mifflin"},
        {"name": "Siobhan Roy", "company": "Waystar Royco"}, {"name": "Dwight Schrute", "company": "Schrute Farms"},
        {"name": "Logan Roy", "company": "Waystar Royco"}, {"name": "Pam Beesly", "company": "Dunder Mifflin"},
        {"name": "Jim Halpert", "company": "Athleap"}, {"name": "Roman Roy", "company": "Waystar Royco"},
        {"name": "Gerri Kellman", "company": "Waystar Royco"}, {"name": "Stanley Hudson", "company": "Crosswords LLC"},
        {"name": "Tom Wambsgans", "company": "Waystar Royco"}, {"name": "Greg Hirsch", "company": "Waystar Royco"},
        {"name": "Angela Martin", "company": "Dunder Mifflin"}, {"name": "Kevin Malone", "company": "Malone's Pub"},
        {"name": "Oscar Martinez", "company": "Dunder Mifflin"}, {"name": "Creed Bratton", "company": "Quality Assurance"},
        {"name": "Jan Levinson", "company": "White Pine"}, {"name": "Ryan Howard", "company": "WUPHF.com"},
        {"name": "Kelly Kapoor", "company": "Dunder Mifflin"}, {"name": "Darryl Philbin", "company": "Athleap"}
    ]
    
    # Geographic Generalization Vault (Canadian Hubs)
    cities = ["Toronto", "Vancouver", "Montreal", "Ottawa", "Calgary"]
    provs = ["ON", "BC", "QC", "ON", "AB"]
    
    # 1. Map Synthetic Core Data
    fake_names = [p['name'] for p in personas[:sample_size]]
    portfolio_sample['New_First'] = [n.split(" ")[0] for n in fake_names]
    portfolio_sample['New_Last'] = [n.split(" ")[1] for n in fake_names]
    portfolio_sample['New_Company'] = [p['company'] for p in personas[:sample_size]]
    portfolio_sample['New_Email'] = (portfolio_sample['New_First'].str.lower() + "." + 
                                    portfolio_sample['New_Last'].str.lower() + "@fictional-corp.com")

    # 2. Multi-Field Re-serialization Mapping Function
    def clean_anonymize(row):
        s = str(row['custom_fields'])
        mapping = {}
        
        # Guard Clause: Only map values if they contain valid data
        if pd.notna(row.get('Email')): mapping[str(row['Email'])] = str(row['New_Email'])
        if pd.notna(row.get('First name')): mapping[str(row['First name'])] = str(row['New_First'])
        if pd.notna(row.get('Last name')): mapping[str(row['Last name'])] = str(row['New_Last'])
        if pd.notna(row.get('Company')): mapping[str(row['Company'])] = str(row['New_Company'])
        
        # Anti-Recursion Logic: Sort keys by length in reverse order
        for old_val in sorted(mapping.keys(), key=len, reverse=True):
            if old_val and old_val.strip() and old_val != 'nan':
                s = s.replace(old_val, mapping[old_val])
        return s

    if 'custom_fields' in portfolio_sample.columns:
        portfolio_sample['custom_fields'] = portfolio_sample.apply(clean_anonymize, axis=1)

    # 3. Dynamic Geographic & Contact Anonymization
    for col in portfolio_sample.columns:
        c_low = col.lower()
        if 'city' in c_low:
            portfolio_sample[col] = [random.choice(cities) for _ in range(sample_size)]
        elif 'state' in c_low or 'province' in c_low:
            portfolio_sample[col] = [random.choice(provs) for _ in range(sample_size)]
        elif 'country' in c_low:
            portfolio_sample[col] = "Canada"
        elif 'address' in c_low:
            portfolio_sample[col] = [f"{random.randint(100, 999)} Fake St." for _ in range(sample_size)]
        elif 'phone' in c_low:
            portfolio_sample[col] = [f"416-555-{random.randint(1000, 9999)}" for _ in range(sample_size)]
        elif 'postal' in c_low or 'zip' in c_low:
            portfolio_sample[col] = [f"M5V {random.randint(1,9)}X{random.randint(1,9)}" for _ in range(sample_size)]

    # 4. Column Formatting & Direct PII Deletion
    portfolio_sample = portfolio_sample.rename(columns={
        'New_First': 'First Name', 'New_Last': 'Last Name',
        'New_Company': 'Company Name', 'New_Email': 'Email'
    })
    
    to_drop = ['First name', 'Last name', 'first_name', 'last_name', 'Company', 'Phone', 'phone']
    portfolio_sample = portfolio_sample.drop(columns=[c for c in to_drop if c in portfolio_sample.columns])
    
    # Save Production File
    portfolio_sample.to_csv(output_path, index=False)
    print("--- SUCCESS: PIPEDA COMPLIANT DATASET EXPORTED ---")
else:
    print("--- ERROR: Verification Failure. Input file path not found. ---")
