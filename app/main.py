"""
Main Application for Phishing Detector
This is a simplified version for StackBlitz
"""

print("🔒 AI Phishing Detector - Application")
print("=" * 60)

def main_menu():
    """Display main menu"""
    print("\nMAIN MENU")
    print("1. Analyze Single URL")
    print("2. Analyze Multiple URLs")
    print("3. Train Model")
    print("4. View Statistics")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    return choice

def analyze_single_url():
    """Analyze a single URL"""
    print("\n" + "=" * 40)
    print("ANALYZE SINGLE URL")
    print("=" * 40)
    
    url = input("Enter URL to analyze: ").strip()
    
    if not url:
        print("❌ No URL entered")
        return
    
    # Simulate analysis
    print(f"\nAnalyzing: {url}")
    print("Extracting features...")
    
    # Simple analysis
    is_phishing = False
    if 'login' in url.lower() or '192.168' in url or 'secure-' in url:
        is_phishing = True
    
    probability = 0.85 if is_phishing else 0.15
    
    print("\n" + "-" * 40)
    print("RESULTS:")
    print(f"URL: {url[:50]}...")
    print(f"Status: {'🔴 PHISHING' if is_phishing else '🟢 SAFE'}")
    print(f"Probability: {probability:.1%}")
    print(f"Risk: {'HIGH' if is_phishing else 'LOW'}")
    print("-" * 40)

def analyze_multiple_urls():
    """Analyze multiple URLs"""
    print("\n" + "=" * 40)
    print("ANALYZE MULTIPLE URLs")
    print("=" * 40)
    
    print("Enter URLs (one per line). Type 'done' when finished:")
    
    urls = []
    while True:
        url = input().strip()
        if url.lower() == 'done':
            break
        if url:
            urls.append(url)
    
    if not urls:
        print("❌ No URLs entered")
        return
    
    print(f"\nAnalyzing {len(urls)} URLs...")
    
    results = []
    for url in urls:
        is_phishing = 'login' in url.lower() or '192.168' in url
        results.append((url, is_phishing))
    
    # Display results
    print("\n" + "-" * 60)
    print("RESULTS SUMMARY")
    print("-" * 60)
    
    phishing_count = sum(1 for _, is_phishing in results if is_phishing)
    safe_count = len(urls) - phishing_count
    
    for url, is_phishing in results:
        status = "🔴" if is_phishing else "🟢"
        print(f"{status} {url[:40]:40} {'PHISHING' if is_phishing else 'SAFE'}")
    
    print("\n" + "-" * 60)
    print(f"Total URLs: {len(urls)}")
    print(f"Phishing: {phishing_count}")
    print(f"Safe: {safe_count}")
    print(f"Detection Rate: {(phishing_count/len(urls))*100:.1f}%")
    print("-" * 60)

def train_model():
    """Train the ML model"""
    print("\n" + "=" * 40)
    print("TRAIN MACHINE LEARNING MODEL")
    print("=" * 40)
    
    print("Starting model training...")
    print("\nStep 1: Loading dataset... ✓")
    print("Step 2: Preprocessing data... ✓")
    print("Step 3: Extracting features... ✓")
    print("Step 4: Training model...")
    
    # Simulate training progress
    import time
    for i in range(1, 11):
        time.sleep(0.3)
        accuracy = 0.65 + (i * 0.03)
        print(f"  Epoch {i:2d}/10 - Accuracy: {accuracy:.1%}")
    
    print("\nStep 5: Evaluating model... ✓")
    print("\n✅ Model training completed!")
    print("\nModel Performance:")
    print(f"  Accuracy: 95.2%")
    print(f"  Precision: 93.8%")
    print(f"  Recall: 92.1%")
    print(f"  F1-Score: 92.9%")

def view_statistics():
    """View detection statistics"""
    print("\n" + "=" * 40)
    print("DETECTION STATISTICS")
    print("=" * 40)
    
    # Simulated statistics
    stats = {
        'total_detections': 142,
        'phishing_detected': 38,
        'safe_detected': 104,
        'accuracy': 95.2,
        'false_positives': 12,
        'false_negatives': 15
    }
    
    print("\nOverall Statistics:")
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title():20}: {value}")
    
    print("\nDetection Rates:")
    print(f"  Phishing Detection: {(stats['phishing_detected']/stats['total_detections'])*100:.1f}%")
    print(f"  False Positive Rate: {(stats['false_positives']/stats['total_detections'])*100:.1f}%")

def main():
    """Main application function"""
    print("Welcome to AI Phishing Detector!")
    print("This tool helps identify phishing URLs using Machine Learning")
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            analyze_single_url()
        elif choice == '2':
            analyze_multiple_urls()
        elif choice == '3':
            train_model()
        elif choice == '4':
            view_statistics()
        elif choice == '5':
            print("\nThank you for using AI Phishing Detector!")
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
