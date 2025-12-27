"""
Data Processor for Phishing URL Dataset
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

class DataProcessor:
    """
    Process and manage phishing URL datasets
    """
    
    def __init__(self):
        self.safe_domains = [
            'google.com', 'github.com', 'youtube.com', 'facebook.com',
            'twitter.com', 'instagram.com', 'linkedin.com', 'microsoft.com',
            'apple.com', 'amazon.com', 'netflix.com', 'stackoverflow.com',
            'wikipedia.org', 'reddit.com', 'whatsapp.com'
        ]
        
        self.phishing_patterns = [
            'login', 'verify', 'secure', 'account', 'bank',
            'update', 'confirm', 'password', 'wallet', 'paypal'
        ]
    
    def generate_dataset(self, n_samples=2000, save_path='data/processed_data.csv'):
        """
        Generate synthetic dataset for demonstration
        """
        print(f"Generating {n_samples} synthetic URL samples...")
        
        data = []
        np.random.seed(42)  # For reproducibility
        
        for i in range(n_samples):
            # Decide if this is phishing or safe
            is_phishing = np.random.choice([0, 1], p=[0.7, 0.3])
            
            if is_phishing:
                # Generate phishing URL
                url = self._generate_phishing_url()
                features = self._extract_phishing_features(url)
            else:
                # Generate safe URL
                url = self._generate_safe_url()
                features = self._extract_safe_features(url)
            
            # Add to dataset
            features['url'] = url
            features['is_phishing'] = is_phishing
            data.append(features)
        
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Save to file
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df.to_csv(save_path, index=False)
        
        print(f"Dataset saved to {save_path}")
        print(f"Shape: {df.shape}")
        print(f"Phishing samples: {df['is_phishing'].sum()}")
        print(f"Safe samples: {len(df) - df['is_phishing'].sum()}")
        
        return df
    
    def _generate_phishing_url(self):
        """Generate a synthetic phishing URL"""
        protocols = ['http://', 'https://']
        subdomains = ['', 'www.', 'secure.', 'login.', 'verify.', 'account.']
        domains = ['bank-', 'paypal-', 'apple-', 'google-', 'facebook-', 'amazon-']
        tlds = ['.com', '.net', '.org', '.info']
        paths = ['', '/login', '/verify', '/account', '/update', '/secure']
        
        protocol = np.random.choice(protocols, p=[0.6, 0.4])
        subdomain = np.random.choice(subdomains)
        domain = np.random.choice(domains) + np.random.choice(['security', 'update', 'verify', 'login'])
        tld = np.random.choice(tlds)
        path = np.random.choice(paths)
        
        # Sometimes add IP address
        if np.random.random() > 0.7:
            ip = f"{np.random.randint(1, 255)}.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}"
            return f"{protocol}{ip}{path}"
        
        return f"{protocol}{subdomain}{domain}{tld}{path}"
    
    def _generate_safe_url(self):
        """Generate a synthetic safe URL"""
        protocols = ['https://', 'http://']
        subdomains = ['', 'www.', 'blog.', 'news.', 'shop.', 'api.']
        domain = np.random.choice(self.safe_domains)
        paths = ['', '/', '/about', '/contact', '/help', '/privacy']
        
        protocol = np.random.choice(protocols, p=[0.8, 0.2])
        subdomain = np.random.choice(subdomains)
        path = np.random.choice(paths)
        
        return f"{protocol}{subdomain}{domain}{path}"
    
    def _extract_phishing_features(self, url):
        """Extract features for phishing URL"""
        return {
            'url_length': len(url),
            'num_dots': url.count('.'),
            'num_hyphens': url.count('-'),
            'num_digits': sum(c.isdigit() for c in url),
            'has_https': 1 if url.startswith('https') else 0,
            'has_ip': 1 if any(char.isdigit() and url.count('.') >= 3 for char in url.split('/')[2]) else 0,
            'suspicious_words': sum(1 for word in self.phishing_patterns if word in url),
            'entropy': np.random.uniform(3.5, 4.5),
            'special_char_ratio': np.random.uniform(0.2, 0.4)
        }
    
    def _extract_safe_features(self, url):
        """Extract features for safe URL"""
        return {
            'url_length': len(url),
            'num_dots': url.count('.'),
            'num_hyphens': url.count('-'),
            'num_digits': sum(c.isdigit() for c in url),
            'has_https': 1 if url.startswith('https') else 0,
            'has_ip': 0,
            'suspicious_words': 0,
            'entropy': np.random.uniform(2.0, 3.0),
            'special_char_ratio': np.random.uniform(0.05, 0.15)
        }
    
    def load_dataset(self, filepath='data/processed_data.csv'):
        """Load dataset from CSV"""
        try:
            df = pd.read_csv(filepath)
            print(f"Dataset loaded from {filepath}")
            print(f"Shape: {df.shape}")
            return df
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
    
    def get_stats(self, df):
        """Get dataset statistics"""
        stats = {
            'total_samples': len(df),
            'phishing_count': df['is_phishing'].sum(),
            'safe_count': len(df) - df['is_phishing'].sum(),
            'phishing_percentage': (df['is_phishing'].sum() / len(df)) * 100,
            'features_count': len(df.columns) - 2  # Exclude url and target
        }
        return stats

# Test the class
if __name__ == "__main__":
    processor = DataProcessor()
    
    # Generate dataset
    df = processor.generate_dataset(1000)
    
    # Display stats
    stats = processor.get_stats(df)
    print("\nDataset Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Show sample data
    print("\nSample Data (first 5 rows):")
    print(df[['url', 'is_phishing', 'url_length', 'has_https']].head())