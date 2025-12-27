"""
Machine Learning Model Trainer for Phishing Detection
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

class ModelTrainer:
    """
    Simulated ML Model Trainer for demonstration
    In a real project, this would use scikit-learn
    """
    
    def __init__(self):
        self.model_info = {
            'name': 'Random Forest Classifier',
            'version': '1.0.0',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'features_used': 14,
            'performance': {}
        }
    
    def train_simulated_model(self, dataset_path='data/processed_data.csv'):
        """
        Simulate model training process
        """
        print("=" * 60)
        print("SIMULATED ML MODEL TRAINING")
        print("=" * 60)
        
        # Step 1: Load dataset
        print("\n1. Loading dataset...")
        if not os.path.exists(dataset_path):
            print(f"   Error: Dataset not found at {dataset_path}")
            print("   Generating sample dataset...")
            from .data_processor import DataProcessor
            processor = DataProcessor()
            df = processor.generate_dataset(1000, dataset_path)
        else:
            df = pd.read_csv(dataset_path)
        
        print(f"   ✓ Dataset loaded: {len(df)} samples")
        print(f"   ✓ Features: {len(df.columns) - 2}")  # Exclude url and target
        
        # Step 2: Data preprocessing
        print("\n2. Preprocessing data...")
        print("   ✓ Handling missing values")
        print("   ✓ Normalizing features")
        print("   ✓ Splitting dataset (80% train, 20% test)")
        
        # Simulated split
        train_size = int(0.8 * len(df))
        print(f"   ✓ Training samples: {train_size}")
        print(f"   ✓ Testing samples: {len(df) - train_size}")
        
        # Step 3: Feature selection
        print("\n3. Selecting features...")
        features = [
            'url_length', 'num_dots', 'num_hyphens', 'num_digits',
            'has_https', 'has_ip', 'suspicious_keywords', 'entropy',
            'special_char_ratio', 'domain_length', 'num_subdomains',
            'has_subdomain', 'tld_length', 'path_length'
        ]
        
        print(f"   ✓ Selected {len(features)} features:")
        for i, feature in enumerate(features, 1):
            print(f"     {i:2d}. {feature}")
        
        # Step 4: Model training
        print("\n4. Training model...")
        print("   ✓ Initializing Random Forest Classifier")
        print("   ✓ Setting parameters:")
        print("     - n_estimators: 100")
        print("     - max_depth: 10")
        print("     - random_state: 42")
        print("     - class_weight: balanced")
        
        # Simulate training epochs
        print("   ✓ Training progress:")
        accuracies = [0.65, 0.78, 0.85, 0.90, 0.92, 0.94, 0.95, 0.952]
        for epoch, acc in enumerate(accuracies, 1):
            print(f"     Epoch {epoch:2d}/8 - Accuracy: {acc*100:.1f}%")
        
        # Step 5: Model evaluation
        print("\n5. Evaluating model...")
        
        # Simulated metrics
        self.model_info['performance'] = {
            'accuracy': 0.952,
            'precision': 0.938,
            'recall': 0.921,
            'f1_score': 0.929,
            'roc_auc': 0.965,
            'confusion_matrix': {
                'true_negative': 280,
                'false_positive': 12,
                'false_negative': 15,
                'true_positive': 93
            }
        }
        
        print("   ✓ Evaluation metrics:")
        for metric, value in self.model_info['performance'].items():
            if metric != 'confusion_matrix':
                print(f"     {metric.capitalize():12s}: {value*100:.1f}%")
        
        # Step 6: Save model
        print("\n6. Saving model...")
        self._save_model()
        
        print("\n" + "=" * 60)
        print("✅ MODEL TRAINING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        return self.model_info
    
    def _save_model(self):
        """Save model information to file"""
        os.makedirs('models', exist_ok=True)
        
        # Save model info
        model_path = 'models/model_info.json'
        with open(model_path, 'w') as f:
            json.dump(self.model_info, f, indent=2)
        
        # Create placeholder model file
        with open('models/phishing_model.pkl', 'w') as f:
            f.write("# Simulated ML Model File\n")
            f.write("# In real implementation, this would be a pickle file\n")
            f.write(f"# Created: {datetime.now()}\n")
        
        print(f"   ✓ Model info saved to: {model_path}")
        print(f"   ✓ Model file saved to: models/phishing_model.pkl")
    
    def load_model_info(self):
        """Load model information"""
        try:
            with open('models/model_info.json', 'r') as f:
                self.model_info = json.load(f)
            return self.model_info
        except FileNotFoundError:
            print("Model info not found. Train model first.")
            return None
    
    def get_model_summary(self):
        """Get model summary for display"""
        if not self.model_info.get('performance'):
            self.load_model_info()
        
        summary = {
            'model_name': self.model_info.get('name', 'Random Forest'),
            'version': self.model_info.get('version', '1.0.0'),
            'created_at': self.model_info.get('created_at', 'N/A'),
            'features': self.model_info.get('features_used', 14),
            'accuracy': f"{self.model_info.get('performance', {}).get('accuracy', 0) * 100:.1f}%",
            'precision': f"{self.model_info.get('performance', {}).get('precision', 0) * 100:.1f}%",
            'recall': f"{self.model_info.get('performance', {}).get('recall', 0) * 100:.1f}%",
            'f1_score': f"{self.model_info.get('performance', {}).get('f1_score', 0) * 100:.1f}%"
        }
        
        return summary
    
    def simulate_prediction(self, features):
        """
        Simulate model prediction based on features
        Returns: probability of being phishing (0-1)
        """
        # Simple rule-based simulation
        score = 0
        
        # Rule 1: URL length
        if features.get('url_length', 0) > 60:
            score += 0.2
        
        # Rule 2: Has IP address
        if features.get('has_ip', 0) == 1:
            score += 0.3
        
        # Rule 3: Suspicious keywords
        keyword_score = min(features.get('suspicious_keywords', 0) * 0.1, 0.3)
        score += keyword_score
        
        # Rule 4: No HTTPS
        if features.get('has_https', 0) == 0:
            score += 0.2
        
        # Rule 5: High entropy
        if features.get('entropy', 0) > 3.5:
            score += 0.1
        
        # Add some randomness
        score += np.random.uniform(-0.1, 0.1)
        
        # Ensure between 0 and 1
        return max(0, min(1, score))

# Test function
if __name__ == "__main__":
    print("Testing Model Trainer")
    print("-" * 50)
    
    trainer = ModelTrainer()
    
    # Train model
    print("Training simulated model...")
    model_info = trainer.train_simulated_model()
    
    # Show model summary
    print("\nModel Summary:")
    summary = trainer.get_model_summary()
    for key, value in summary.items():
        print(f"{key:15s}: {value}")
    
    # Test prediction
    print("\nTesting predictions:")
    test_features = [
        {'url_length': 45, 'has_ip': 0, 'suspicious_keywords': 0, 'has_https': 1, 'entropy': 2.5},
        {'url_length': 85, 'has_ip': 1, 'suspicious_keywords': 3, 'has_https': 0, 'entropy': 4.2}
    ]
    
    for i, features in enumerate(test_features, 1):
        prob = trainer.simulate_prediction(features)
        status = "PHISHING" if prob > 0.5 else "SAFE"
        print(f"Test {i}: Probability = {prob:.2%} → {status}")