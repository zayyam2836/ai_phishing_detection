"""
Feature Extractor for URL Analysis
"""

import re
import numpy as np
from urllib.parse import urlparse

class URLFeatureExtractor:
    """
    Extract security features from URLs for phishing detection
    """
    
    def __init__(self):
        # Suspicious keywords commonly found in phishing URLs
        self.suspicious_keywords = [
            'login', 'signin', 'verify', 'confirm', 'secure',
            'account', 'banking', 'update', 'password', 'wallet',
            'paypal', 'ebay', 'amazon', 'apple', 'microsoft',
            'click', 'here', 'urgent', 'important', 'alert',
            'suspended', 'locked', 'unlock', 'restore', 'recover'
        ]
        
        # Legitimate TLDs
        self.legitimate_tlds = ['.com', '.org', '.edu', '.gov', '.net', '.io']
        
        # URL shortening services
        self.shortening_services = [
            'bit.ly', 'tinyurl.com', 'goo.gl', 'ow.ly', 'is.gd',
            'buff.ly', 't.co', 'lnkd.in', 'db.tt', 'qr.ae'
        ]
    
    def extract_all_features(self, url):
        """
        Extract all features from a URL
        Returns: Dictionary of 25+ features
        """
        features = {}
        
        # 1. Basic URL Features
        features.update(self._extract_basic_features(url))
        
        # 2. Security Features
        features.update(self._extract_security_features(url))
        
        # 3. Domain Features
        features.update(self._extract_domain_features(url))
        
        # 4. Statistical Features
        features.update(self._extract_statistical_features(url))
        
        return features
    
    def _extract_basic_features(self, url):
        """Extract basic URL features"""
        features = {}
        
        # URL Length
        features['url_length'] = len(url)
        
        # Character counts
        features['num_dots'] = url.count('.')
        features['num_hyphens'] = url.count('-')
        features['num_underscores'] = url.count('_')
        features['num_slashes'] = url.count('/')
        features['num_questionmarks'] = url.count('?')
        features['num_equals'] = url.count('=')
        features['num_ats'] = url.count('@')
        features['num_ampersands'] = url.count('&')
        
        # Digit and letter counts
        features['num_digits'] = sum(c.isdigit() for c in url)
        features['num_letters'] = sum(c.isalpha() for c in url)
        
        return features
    
    def _extract_security_features(self, url):
        """Extract security-related features"""
        features = {}
        
        # Protocol
        features['has_https'] = 1 if url.startswith('https://') else 0
        features['has_http'] = 1 if url.startswith('http://') else 0
        
        # IP Address in URL
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        features['has_ip'] = 1 if re.search(ip_pattern, url) else 0
        
        # URL Shortening
        features['is_shortened'] = 1 if any(service in url for service in self.shortening_services) else 0
        
        # Suspicious keywords
        suspicious_count = 0
        for keyword in self.suspicious_keywords:
            if keyword in url.lower():
                suspicious_count += 1
        features['suspicious_keywords'] = suspicious_count
        
        # Non-standard port
        features['has_port'] = 1 if re.search(r':\d+', url) else 0
        
        return features
    
    def _extract_domain_features(self, url):
        """Extract domain-related features"""
        features = {}
        
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            
            # Domain length
            features['domain_length'] = len(domain)
            
            # Subdomain analysis
            parts = domain.split('.')
            features['num_subdomains'] = max(0, len(parts) - 2)
            features['has_subdomain'] = 1 if len(parts) > 2 else 0
            
            # TLD analysis
            if len(parts) >= 2:
                tld = '.' + parts[-1]
                features['tld_length'] = len(tld)
                features['has_legitimate_tld'] = 1 if tld in self.legitimate_tlds else 0
            else:
                features['tld_length'] = 0
                features['has_legitimate_tld'] = 0
            
            # Path analysis
            path = parsed.path
            features['path_length'] = len(path)
            features['has_path'] = 1 if path and path != '/' else 0
            
            # Query parameters
            query = parsed.query
            features['has_query'] = 1 if query else 0
            features['num_params'] = len(query.split('&')) if query else 0
            
        except:
            # Default values if parsing fails
            features.update({
                'domain_length': 0,
                'num_subdomains': 0,
                'has_subdomain': 0,
                'tld_length': 0,
                'has_legitimate_tld': 0,
                'path_length': 0,
                'has_path': 0,
                'has_query': 0,
                'num_params': 0
            })
        
        return features
    
    def _extract_statistical_features(self, url):
        """Extract statistical features"""
        features = {}
        
        # Entropy (measure of randomness)
        features['entropy'] = self._calculate_entropy(url)
        
        # Character ratios
        total_chars = len(url)
        if total_chars > 0:
            features['digit_ratio'] = sum(c.isdigit() for c in url) / total_chars
            features['letter_ratio'] = sum(c.isalpha() for c in url) / total_chars
            features['special_char_ratio'] = sum(not c.isalnum() for c in url) / total_chars
        else:
            features['digit_ratio'] = 0
            features['letter_ratio'] = 0
            features['special_char_ratio'] = 0
        
        # Vowel/Consonant ratio in letters
        letters = [c for c in url if c.isalpha()]
        if letters:
            vowels = sum(1 for c in letters if c.lower() in 'aeiou')
            features['vowel_ratio'] = vowels / len(letters)
        else:
            features['vowel_ratio'] = 0
        
        return features
    
    def _calculate_entropy(self, text):
        """Calculate Shannon entropy of text"""
        if not text:
            return 0
        
        # Count character frequencies
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Calculate entropy
        entropy = 0
        length = len(text)
        for count in char_counts.values():
            probability = count / length
            entropy -= probability * np.log2(probability)
        
        return entropy
    
    def extract_features_for_model(self, url):
        """
        Extract features in the order expected by ML model
        """
        all_features = self.extract_all_features(url)
        
        # Select features for model (in specific order)
        model_features = [
            'url_length',
            'num_dots',
            'num_hyphens',
            'num_digits',
            'has_https',
            'has_ip',
            'suspicious_keywords',
            'entropy',
            'special_char_ratio',
            'domain_length',
            'num_subdomains',
            'has_subdomain',
            'tld_length',
            'path_length'
        ]
        
        # Ensure all features exist
        result = {}
        for feature in model_features:
            result[feature] = all_features.get(feature, 0)
        
        return result
    
    def explain_features(self, url):
        """
        Provide human-readable explanation of features
        """
        features = self.extract_all_features(url)
        
        print(f"URL Analysis: {url}")
        print("=" * 50)
        
        categories = {
            'Basic Features': ['url_length', 'num_dots', 'num_hyphens', 'num_digits', 'num_letters'],
            'Security Features': ['has_https', 'has_ip', 'is_shortened', 'suspicious_keywords'],
            'Domain Features': ['domain_length', 'num_subdomains', 'has_legitimate_tld'],
            'Statistical Features': ['entropy', 'special_char_ratio', 'digit_ratio']
        }
        
        for category, feature_list in categories.items():
            print(f"\n{category}:")
            for feature in feature_list:
                if feature in features:
                    print(f"  {feature}: {features[feature]}")
        
        # Risk assessment
        risk_score = self._calculate_risk_score(features)
        print(f"\nRisk Score: {risk_score}/100")
        
        if risk_score > 70:
            print("Risk Level: 🔴 HIGH (Potential Phishing)")
        elif risk_score > 40:
            print("Risk Level: 🟡 MEDIUM (Suspicious)")
        else:
            print("Risk Level: 🟢 LOW (Likely Safe)")
    
    def _calculate_risk_score(self, features):
        """Calculate phishing risk score (0-100)"""
        score = 0
        
        # Weighted scoring
        weights = {
            'has_ip': 20,
            'suspicious_keywords': 15,
            'is_shortened': 10,
            'has_https': -10,  # HTTPS reduces risk
            'entropy': 0.5,    # per unit
            'special_char_ratio': 100,  # per unit (0-1)
            'num_subdomains': 5  # per subdomain
        }
        
        for feature, weight in weights.items():
            if feature in features:
                if feature == 'has_https':
                    if features[feature] == 1:
                        score += weight  # Negative weight reduces score
                else:
                    score += features[feature] * weight
        
        # Cap score between 0 and 100
        return max(0, min(100, score))

# Test function
if __name__ == "__main__":
    extractor = URLFeatureExtractor()
    
    # Test URLs
    test_urls = [
        "https://www.google.com/search?q=python",
        "http://192.168.1.1/login.php",
        "https://secure-bank-login-verify-account.com/update",
        "https://github.com/user/repo",
        "http://bit.ly/2xYz8k9"
    ]
    
    print("Testing URL Feature Extractor")
    print("=" * 60)
    
    for i, url in enumerate(test_urls, 1):
        print(f"\n{i}. URL: {url}")
        features = extractor.extract_all_features(url)
        
        print(f"   Total features extracted: {len(features)}")
        
        # Show key features
        key_features = ['url_length', 'has_https', 'has_ip', 'suspicious_keywords', 'entropy']
        for feature in key_features:
            if feature in features:
                print(f"   {feature}: {features[feature]}")
        
        # Risk assessment
        risk_score = extractor._calculate_risk_score(features)
        print(f"   Risk Score: {risk_score}")