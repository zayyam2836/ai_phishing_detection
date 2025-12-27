# This would be a Jupyter Notebook file
# Since StackBlitz doesn't support .ipynb directly, create a .py file instead:

# Create `src/demo.py` instead:

"""
Demo Script for AI Phishing Detector
"""

print("🔒 AI Phishing Detector - Demo Script")
print("=" * 60)

# Import modules
try:
    from feature_extractor import URLFeatureExtractor
    from data_processor import DataProcessor
    from model_trainer import ModelTrainer
    from real_time_detector import RealTimePhishingDetector
    
    print("✓ All modules imported successfully")
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    print("⚠️ Running in limited mode")

# Demo 1: Feature Extraction
print("\n" + "=" * 60)
print("DEMO 1: Feature Extraction")
print("=" * 60)

extractor = URLFeatureExtractor()
test_url = "https://secure-bank-login-verify.com/account/update"

features = extractor.extract_all_features(test_url)
print(f"URL: {test_url}")
print(f"Total features extracted: {len(features)}")
print("\nKey Features:")
for key in ['url_length', 'has_https', 'has_ip', 'suspicious_keywords', 'entropy']:
    if key in features:
        print(f"  {key}: {features[key]}")

# Demo 2: Data Processing
print("\n" + "=" * 60)
print("DEMO 2: Data Processing")
print("=" * 60)

processor = DataProcessor()
df = processor.generate_dataset(500)  # Smaller dataset for demo
stats = processor.get_stats(df)

print("Dataset Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")

# Demo 3: Model Training
print("\n" + "=" * 60)
print("DEMO 3: Model Training")
print("=" * 60)

trainer = ModelTrainer()
model_info = trainer.train_simulated_model()

print("\nModel Performance:")
for metric, value in model_info['performance'].items():
    if metric != 'confusion_matrix':
        print(f"  {metric}: {value*100:.1f}%")

# Demo 4: Real-time Detection
print("\n" + "=" * 60)
print("DEMO 4: Real-time Detection")
print("=" * 60)

detector = RealTimePhishingDetector()

test_urls = [
    "https://www.google.com",
    "http://192.168.1.1/admin",
    "https://github.com"
]

print("Testing URLs:")
for url in test_urls:
    result = detector.analyze_url(url)
    status = "🔴 PHISHING" if result['is_phishing'] else "🟢 SAFE"
    print(f"  {url[:40]:40} → {status} ({result['confidence']:.1f}%)")

print("\n" + "=" * 60)
print("✅ Demo completed successfully!")
print("=" * 60)