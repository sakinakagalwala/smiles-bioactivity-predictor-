import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from model import train_dummy_model
from descriptor import compute_descriptors
import numpy as np

model = train_dummy_model()

st.title("🧪 SMILES-based Bioactivity Predictor")

st.markdown("""
This demo app takes a **SMILES string**, calculates molecular descriptors using **RDKit**,  
and predicts **bioactivity** using a dummy ML model.  
*(Replace with your trained model for real predictions!)*
""")

# SMILES input
smiles = st.text_input("Enter SMILES string", "CC(=O)Oc1ccccc1C(=O)O")  # aspirin

# Render molecule
mol = Chem.MolFromSmiles(smiles)
if mol:
    st.image(Draw.MolToImage(mol, size=(300, 300)), caption="Molecule structure")

# Compute descriptors and predict
if st.button("🔍 Predict Bioactivity"):
    descriptors = compute_descriptors(smiles)
    if descriptors is None:
        st.error("❌ Invalid SMILES string!")
    else:
        input_array = np.array(descriptors).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        prob = model.predict_proba(input_array)[0][prediction]

        st.success(f"Prediction: **{'Active' if prediction == 1 else 'Inactive'}**")
        st.write(f"Confidence: **{prob:.2f}**")
        st.caption("Note: This is a demo using a dummy model. Replace with real model and descriptors.")
