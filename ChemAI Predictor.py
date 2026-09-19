import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Note: Requires 'rdkit' library (install via: pip install rdkit scikit-learn pandas)
try:
    from rdkit import Chem # type: ignore
    from rdkit.Chem import Descriptors, AllChem # type: ignore
except ImportError:
    print("RDKit library required. Run: pip install rdkit")

def generate_molecular_descriptors(smiles_list):
    """
    AI/ML Feature Engineering: Converts chemical SMILES strings 
    into numerical molecular descriptors and fingerprints.
    """
    features = []
    valid_indices = []
    
    for i, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            # Extract physicochemical descriptors (Molecular Weight, LogP, TPSA, etc.)
            mw = Descriptors.MolWt(mol)
            logp = Descriptors.MolLogP(mol)
            tpsa = Descriptors.TPSA(mol)
            h_donors = Descriptors.NumHDonors(mol)
            h_acceptors = Descriptors.NumHAcceptors(mol)
            
            # Combine into a feature vector
            features.append([mw, logp, tpsa, h_donors, h_acceptors])
            valid_indices.append(i)
            
    return np.array(features), valid_indices

def run_ai_qsar_pipeline():
    print("="*50)
    print("AI/ML CHEMINFORMATICS: QSAR TOXICITY PREDICTOR")
    print("="*50)

    # 1. Mock dataset of chemical structures (SMILES) and target labels (e.g., 1 = Toxic/Active, 0 = Safe/Inactive)
    data = {
        'SMILES': [
            'CCO', 'CC(=O)OC1=CC=CC=C1C(=O)O', 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', 
            'c1ccccc1', 'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O', 'O=C(O)C1=CC=CC=C1O',
            'ClC=C(Cl)Cl', 'CCCCCCCC(=O)O', 'CCN(CC)CC', 'CN(C)C(=O)H'
        ],
        'Is_Toxic': [0, 0, 0, 1, 0, 0, 1, 0, 1, 1] # Target label
    }
    df = pd.DataFrame(data)

    # 2. Extract AI features using RDKit
    X, valid_idx = generate_molecular_descriptors(df['SMILES'].tolist())
    y = df['Is_Toxic'].values[valid_idx]

    if len(X) == 0:
        print("Error: No valid molecules could be processed.")
        return

    # 3. Train-Test Split for Machine Learning Validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 4. Train an AI/ML Classifier (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Evaluate Predictions
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\nModel Training Complete!")
    print(f"Machine Learning Test Accuracy: {acc * 100:.1f}%")
    print("-" * 50)
    print("Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("="*50)

# Execute pipeline
if __name__ == "__main__":
    run_ai_y = run_ai_qsar_pipeline()