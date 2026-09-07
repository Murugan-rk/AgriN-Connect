import pandas as pd


def load_pest_data():
    """Load BRICS pest alert dataset."""
    return pd.read_csv("data/pest_alerts.csv")


def get_country_data(country):
    """Return pest alerts for a selected country."""
    df = load_pest_data()
    return df[df["country"].str.lower() == country.lower()]


def get_high_risk_alerts():
    """Return only high-risk pest alerts."""
    df = load_pest_data()
    return df[df["risk_level"].str.lower() == "high"]


def get_crop_data(crop):
    """Return pest alerts for a selected crop."""
    df = load_pest_data()
    return df[df["crop"].str.lower() == crop.lower()]