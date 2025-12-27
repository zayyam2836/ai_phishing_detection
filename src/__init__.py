"""
AI Phishing Detector - Source Package
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "AI Powered Phishing URL Detection System"

# Package imports
from .feature_extractor import URLFeatureExtractor
from .data_processor import DataProcessor
from .model_trainer import ModelTrainer
from .real_time_detector import RealTimePhishingDetector

__all__ = [
    'URLFeatureExtractor',
    'DataProcessor',
    'ModelTrainer',
    'RealTimePhishingDetector'
]