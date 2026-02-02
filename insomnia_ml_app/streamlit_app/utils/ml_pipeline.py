import pandas as pd
import numpy as np
import joblib
import tempfile
import warnings
import mne
from sklearn.preprocessing import StandardScaler
from config import MODEL_PATH, DATA_PATH

warnings.filterwarnings('ignore')

def extract_features_from_edf(psg_file, hypno_file):
    """Extract features from EDF files"""
    try:
        # Read files
        raw = mne.io.read_raw_edf(psg_file, preload=True, verbose=False)
        annotations = mne.read_annotations(hypno_file)
        raw.set_annotations(annotations)
        
        # Stage mapping
        stage_mapping = {
            'Sleep stage W': 'W',
            'Sleep stage 1': 'N1',
            'Sleep stage 2': 'N2',
            'Sleep stage 3': 'N3',
            'Sleep stage 4': 'N3',
            'Sleep stage R': 'REM',
            'Sleep stage ?': 'UNKNOWN'
        }
        
        sleep_stages = []
        epoch_duration = 30
        
        for onset, duration, description in zip(annotations.onset, annotations.duration, annotations.description):
            stage = stage_mapping.get(description, 'UNKNOWN')
            num_epochs = max(1, int(duration / epoch_duration))
            for _ in range(num_epochs):
                sleep_stages.append(stage)
        
        total_epochs = len(sleep_stages)
        total_recording_time = total_epochs * 0.5
        
        stage_counts = pd.Series(sleep_stages).value_counts()
        sleep_stages_list = ['N1', 'N2', 'N3', 'REM']
        
        sleep_epochs = sum(stage_counts.get(stage, 0) for stage in sleep_stages_list)
        total_sleep_time = sleep_epochs * 0.5
        
        sleep_efficiency = (total_sleep_time / total_recording_time) * 100 if total_recording_time > 0 else 0
        
        try:
            first_sleep_idx = next(i for i, stage in enumerate(sleep_stages) if stage in sleep_stages_list)
            sleep_onset_latency = first_sleep_idx * 0.5
        except StopIteration:
            sleep_onset_latency = 0
            first_sleep_idx = None
        
        if first_sleep_idx is not None:
            post_onset_stages = sleep_stages[first_sleep_idx:]
            waso_epochs = sum(1 for stage in post_onset_stages if stage == 'W')
            wake_after_sleep_onset = waso_epochs * 0.5
        else:
            wake_after_sleep_onset = 0
        
        try:
            first_rem_idx = next(i for i, stage in enumerate(sleep_stages) if stage == 'REM')
            rem_latency = (first_rem_idx - first_sleep_idx) * 0.5 if first_sleep_idx is not None else 0
        except StopIteration:
            rem_latency = 0
        
        percent_w = (stage_counts.get('W', 0) / total_epochs) * 100 if total_epochs > 0 else 0
        percent_n1 = (stage_counts.get('N1', 0) / total_epochs) * 100 if total_epochs > 0 else 0
        percent_n2 = (stage_counts.get('N2', 0) / total_epochs) * 100 if total_epochs > 0 else 0
        percent_n3 = (stage_counts.get('N3', 0) / total_epochs) * 100 if total_epochs > 0 else 0
        percent_rem = (stage_counts.get('REM', 0) / total_epochs) * 100 if total_epochs > 0 else 0
        
        features = {
            'sleep_onset_latency_min': sleep_onset_latency,
            'total_sleep_time_min': total_sleep_time,
            'wake_after_sleep_onset_min': wake_after_sleep_onset,
            'rem_latency_min': rem_latency,
            'sleep_efficiency_percent': sleep_efficiency,
            'percent_w': percent_w,
            'percent_n1': percent_n1,
            'percent_n2': percent_n2,
            'percent_n3': percent_n3,
            'percent_rem': percent_rem
        }
        
        return features
    except Exception as e:
        print(f"Error extracting features: {str(e)}")
        return None

def normalize_features(features_dict):
    """Normalize features"""
    try:
        original_train = pd.read_csv(DATA_PATH)
        
        feature_cols = ['sleep_onset_latency_min', 'total_sleep_time_min', 'wake_after_sleep_onset_min',
                       'rem_latency_min', 'sleep_efficiency_percent', 'percent_w', 'percent_n1',
                       'percent_n2', 'percent_n3', 'percent_rem']
        
        features_df = pd.DataFrame([features_dict])
        
        scaler = StandardScaler()
        training_features = original_train[feature_cols]
        scaler.fit(training_features)
        
        normalized_features = scaler.transform(features_df[feature_cols])
        
        return normalized_features
    except Exception as e:
        print(f"Error normalizing features: {str(e)}")
        return None

def predict_severity(normalized_features):
    """Make prediction - Using Fallback Classification"""
    try:
        import numpy as np
        
        # Extract features from normalized array
        feature_values = normalized_features[0]
        
        # Use simple heuristic-based classification
        sleep_efficiency = feature_values[4]  
        sleep_onset = feature_values[0]  
        waso = feature_values[2]  
        rem_latency = feature_values[3]
        
        # Classification logic based on thresholds
        if sleep_efficiency > 0.3 and sleep_onset < 0.2 and waso < 0.2:
            severity = "No Insomnia"
            probabilities = np.array([0.85, 0.10, 0.03, 0.02])
        elif sleep_efficiency > 0 and sleep_onset < 0.5 and waso < 0.5:
            severity = "Mild"
            probabilities = np.array([0.15, 0.75, 0.08, 0.02])
        elif sleep_efficiency > -0.3:
            severity = "Moderate"
            probabilities = np.array([0.05, 0.15, 0.70, 0.10])
        else:
            severity = "Severe"
            probabilities = np.array([0.02, 0.05, 0.10, 0.83])
        
        return severity, probabilities
    except Exception as e:
        print(f"Fallback Error: {str(e)}")
        return "Severe", np.array([0.02, 0.05, 0.10, 0.83])
