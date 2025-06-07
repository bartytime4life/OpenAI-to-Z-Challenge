import tensorflow as tf
import joblib

REVIVALNET_PATH = "/models/revivalnet.h5"
TIMEFOLDNET_PATH = "/models/timefoldnet.h5"
ENSEMBLE_PATH    = "/models/ensemble.pkl"

def load_models():
    revival = tf.keras.models.load_model(REVIVALNET_PATH)
    timefold = tf.keras.models.load_model(TIMEFOLDNET_PATH)
    ensemble = joblib.load(ENSEMBLE_PATH)
    return revival, timefold, ensemble
