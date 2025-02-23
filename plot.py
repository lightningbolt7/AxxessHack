import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path)
    data = data.sort_values(by="DeviceDtTmDaysFromEnroll")
    return data

data = load_data("data2.csv")

def update_glucose_chart(new_glucose, insulin_dose, recent_days=30):
    global data
    
    # Append new data
    new_entry = {
        "DeviceDtTmDaysFromEnroll": data["DeviceDtTmDaysFromEnroll"].max() + 1,
        "GlucoseValue": new_glucose,
        "InsulinDose": insulin_dose
    }
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    
    # Filter for recent days if applicable
    recent_cutoff = data["DeviceDtTmDaysFromEnroll"].max() - recent_days
    recent_data = data[data["DeviceDtTmDaysFromEnroll"] >= recent_cutoff]
    
    # Define color coding
    colors = recent_data['GlucoseValue'].apply(lambda x: 
        'red' if x < 55 else 
        'orange' if x < 70 else 
        'purple' if x > 180 else 
        'blue')
    
    # Highlight the most recent entry
    recent_data["Size"] = 20  # Default size
    recent_data.loc[recent_data["DeviceDtTmDaysFromEnroll"] == new_entry["DeviceDtTmDaysFromEnroll"], "Size"] = 80

    # Plot the updated glucose values
    plt.figure(figsize=(10, 5))
    plt.scatter(recent_data['DeviceDtTmDaysFromEnroll'], recent_data['GlucoseValue'], c=colors, alpha=0.6, s=recent_data["Size"], label="Glucose Levels")
    
    # Add polynomial regression trend line
    if len(recent_data) > 2:  # Need at least 3 points for polynomial regression
        x = recent_data['DeviceDtTmDaysFromEnroll']
        y = recent_data['GlucoseValue']
        
        # Fit a 2nd-degree polynomial (quadratic)
        poly_coeffs = np.polyfit(x, y, 2)
        poly_eq = np.poly1d(poly_coeffs)

        # Generate smooth curve points
        x_smooth = np.linspace(x.min(), x.max(), 100)
        y_smooth = poly_eq(x_smooth)
        
        plt.plot(x_smooth, y_smooth, color='gray', linestyle='dashed', linewidth=2, alpha=0.7, label="Trend Line (Polynomial)")
    
    # Reference lines
    plt.axhline(70, color='orange', linestyle='dashed', label="Hypoglycemia (70 mg/dL)")
    plt.axhline(55, color='red', linestyle='dashed', label="Severe Hypoglycemia (55 mg/dL)")
    plt.axhline(180, color='purple', linestyle='dashed', label="Hyperglycemia (180 mg/dL)")
    
    plt.xlabel("Days from Enrollment")
    plt.ylabel("Glucose Value (mg/dL)")
    plt.title("Recent Glucose Levels Over Time")
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    file_path = "data2.csv"
    data = load_data(file_path)
    update_glucose_chart(new_glucose=120, insulin_dose=5)
