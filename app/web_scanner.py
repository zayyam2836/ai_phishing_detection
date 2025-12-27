"""
Web Page Scanner for additional analysis
"""

class WebPageScanner:
    """
    Scanner for web page content analysis
    """
    
    def __init__(self):
        self.phishing_indicators = {
            'keywords': ['password', 'login', 'sign in', 'verify', 'account', 'bank', 'secure'],
            'form_fields': ['password', 'passwd', 'pwd', 'creditcard', 'cvv', 'ssn'],
            'suspicious_actions': ['submit', 'update', 'confirm', 'verify']
        }
    
    def scan_url(self, url):
        """
        Simulate web page scanning
        In real implementation, this would fetch and parse the webpage
        """
        print(f"Scanning webpage: {url}")
        
        # Simulated scan results
        scan_result = {
            'url': url,
            'has_login_form': 'login' in url.lower(),
            'has_password_field': 'password' in url.lower() or 'passwd' in url.lower(),
            'suspicious_keywords_found': self._check_keywords(url),
            'has_ssl': url.startswith('https'),
            'page_title': self._simulate_title(url),
            'risk_score': self._calculate_risk_score(url)
        }
        
        return scan_result
    
    def _check_keywords(self, url):
        """Check for suspicious keywords in URL"""
        found = []
        for keyword in self.phishing_indicators['keywords']:
            if keyword in url.lower():
                found.append(keyword)
        return found
    
    def _simulate_title(self, url):
        """Simulate page title extraction"""
        if 'google' in url:
            return "Google Search"
        elif 'login' in url:
            return "Account Login - Verify Your Identity"
        elif 'bank' in url:
            return "Online Banking - Secure Login"
        else:
            return "Web Page"
    
    def _calculate_risk_score(self, url):
        """Calculate risk score based on URL analysis"""
        score = 0
        
        # URL-based scoring
        if 'login' in url.lower():
            score += 30
        if 'secure' in url.lower():
            score += 20
        if 'verify' in url.lower():
            score += 25
        if '192.168' in url or '10.0' in url:
            score += 40
        if not url.startswith('https'):
            score += 15
        
        return min(score, 100)
    
    def generate_report(self, scan_result):
        """Generate human-readable report"""
        print("\n" + "=" * 60)
        print("WEB PAGE SCAN REPORT")
        print("=" * 60)
        
        print(f"URL: {scan_result['url']}")
        print(f"Page Title: {scan_result['page_title']}")
        print(f"SSL/TLS: {'Yes (Secure)' if scan_result['has_ssl'] else 'No (Not Secure)'}")
        
        print("\nSecurity Findings:")
        print(f"  Login Form Detected: {'Yes ⚠️' if scan_result['has_login_form'] else 'No'}")
        print(f"  Password Field: {'Yes ⚠️' if scan_result['has_password_field'] else 'No'}")
        
        keywords = scan_result['suspicious_keywords_found']
        if keywords:
            print(f"  Suspicious Keywords: {', '.join(keywords)} ⚠️")
        else:
            print(f"  Suspicious Keywords: None")
        
        print(f"\nRisk Score: {scan_result['risk_score']}/100")
        
        if scan_result['risk_score'] > 70:
            print("Risk Level: 🔴 HIGH - Potential phishing page")
        elif scan_result['risk_score'] > 40:
            print("Risk Level: 🟡 MEDIUM - Suspicious, exercise caution")
        else:
            print("Risk Level: 🟢 LOW - Appears legitimate")

# Test function
if __name__ == "__main__":
    print("Testing Web Page Scanner")
    print("-" * 50)
    
    scanner = WebPageScanner()
    
    test_urls = [
        "https://www.google.com",
        "http://secure-bank-login.com",
        "https://github.com/login"
    ]
    
    for url in test_urls:
        result = scanner.scan_url(url)
        scanner.generate_report(result)
        print("\n")