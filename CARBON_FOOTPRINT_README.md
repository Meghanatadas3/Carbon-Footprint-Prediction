# 🌍 AI-Powered Carbon Footprint Predictor

Predict and reduce your environmental impact with machine learning

[![Streamlit App](https://carbon-footprint-predictions.streamlit.app/)](#)

## 🎯 Overview

This project implements an AI-driven system for predicting individual carbon footprints based on lifestyle choices. Using machine learning algorithms, the system analyzes daily habits including transportation, energy consumption, shopping patterns, and provides personalized recommendations for reducing environmental impact.

## ✨ Features

- **Real-Time Predictions**: Instant carbon footprint calculations based on user inputs
- **Interactive Visualizations**:
  - Gauge charts showing emission levels
  - Pie charts breaking down emission sources
  - Comparative bar charts vs. national/global averages
- **Personalized Recommendations**: AI-driven suggestions for reducing carbon emissions
- **Impact Categorization**: Color-coded system (Low/Medium/High) for easy understanding
- **Yearly Projections**: Estimates annual carbon emissions
- **Tree Offset Calculator**: Shows trees needed to offset your footprint
- **Model Performance Tracking**: Detailed ML model comparison and metrics

## 🚀 Demo

- **Live Application**: [https://carbon-footprint-predictions.streamlit.app/]
- **Video Demo**: [https://gismauniversity-my.sharepoint.com/:v:/g/personal/meghana_tadas_gisma-student_com/IQCjoblDOaMWT7ldlMwNvncCARQN06MZUEHR1xtfkaI_CfY?e=MoYUkO]

## 📊 Dataset

**Input Features**:
- Monthly Grocery Bill (₹)
- Vehicle Monthly Distance (Km)
- Daily TV/PC Usage (hours)
- New Clothes Purchased Monthly
- Daily Internet Usage (hours)

**Output**: Predicted Carbon Emission (units)

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS
- **ML Framework**: Scikit-learn
- **Visualization**: Plotly (interactive charts)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Streamlit Cloud

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/[username]/carbon-footprint-predictor.git
cd carbon-footprint-predictor

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app1.py
```

## 💻 Usage

### Basic Prediction

1. **Enter Your Data**:
   - Monthly grocery spending
   - Vehicle distance traveled
   - Screen time (TV/PC)
   - Clothing purchases
   - Internet usage

2. **Click "Calculate Carbon Footprint"**

3. **View Results**:
   - Total CO₂ emission estimate
   - Yearly projection
   - Trees needed for offset
   - Emission breakdown by category

### Understanding Your Results

| Emission Level | Units | Status |
|---------------|-------|--------|
| Low | < 1,500 | ✅ Excellent |
| Medium | 1,500 - 3,000 | ⚠️ Moderate |
| High | > 3,000 | 🚨 Action Needed |

## 📈 Model Performance

The system uses the best-performing model selected from multiple ML algorithms:

- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **Support Vector Regressor**

Model selection based on:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🗂️ Project Structure

```
carbon-footprint-predictor/
├── app1.py                         # Main Streamlit application
├── requirements.txt                # Python dependencies
├── Carbon_Emission.csv             # Training dataset
├── Carbon_footprint_prediction.ipynb # Model training notebook
├── best_model.pkl                  # Trained ML model (best performer)
├── model.pkl                       # Alternative model
├── best_model_info.txt             # Best model metrics
├── model_info.txt                  # Alternative model metrics
└── model_comparison.csv            # Model comparison results
```

## 🎨 Features Breakdown

### 1. Interactive Input Form
- User-friendly sliders and number inputs
- Real-time value updates
- Helpful tooltips for each parameter

### 2. Visualization Dashboard
- **Gauge Chart**: Visual representation of emission level
- **Pie Chart**: Breakdown by category (Grocery, Transportation, Electronics, Fashion)
- **Bar Chart**: Comparison with national/global averages

### 3. Personalized Recommendations
Dynamic suggestions based on:
- Transportation habits (vehicle distance > 1000 km)
- Screen time (TV + internet > 10 hours)
- Fashion consumption (clothes > 10 items)
- Grocery spending (bill > ₹5000)

### 4. Impact Calculations
- Monthly emission estimate
- Yearly projection (monthly × 12)
- Trees required for carbon offset (emission / 20)
- Percentage comparison vs. average (2000 units baseline)

## 🌱 Recommendations Engine

The system provides targeted advice:

### High Impact Users (> 3000 units)
- 🚨 Urgent action required
- Specific interventions for each category
- Focus on highest-contributing factors

### Medium Impact Users (1500-3000 units)
- ⚠️ Improvement opportunities
- Balanced recommendations
- Gradual reduction strategies

### Low Impact Users (< 1500 units)
- ✅ Positive reinforcement
- Maintenance tips
- Encouragement to inspire others

## 📊 Carbon Emission Breakdown

### Category Contributions:
1. **Grocery**: Monthly bill × 0.5
2. **Transportation**: Vehicle distance × 0.6
3. **Electronics**: (TV hours + Internet hours) × 30
4. **Fashion**: New clothes × 40

## 🔬 Model Training Details

Located in `Carbon_footprint_prediction.ipynb`:

1. **Data Preprocessing**:
   - Missing value handling
   - Feature scaling
   - Train-test split (80-20)

2. **Model Training**:
   - Multiple algorithm comparison
   - Hyperparameter tuning
   - Cross-validation

3. **Model Selection**:
   - Best model based on R² score
   - Saved as `best_model.pkl`

4. **Performance Metrics**:
   - Stored in `model_comparison.csv`
   - Detailed info in `best_model_info.txt`

## 🎯 Impact Levels Reference

| Level | Range | Trees Needed | Action |
|-------|-------|--------------|--------|
| Excellent | < 1,500 | < 75 | Maintain habits |
| Good | 1,500-2,000 | 75-100 | Minor improvements |
| Moderate | 2,000-2,500 | 100-125 | Active changes |
| High | 2,500-3,000 | 125-150 | Significant changes |
| Very High | > 3,000 | > 150 | Urgent action |

## 💡 Tips for Reducing Carbon Footprint

### Transportation 🚗
- Use public transport
- Carpool when possible
- Bike/walk for short distances
- Plan efficient routes

### Energy 💡
- Reduce screen time
- Use energy-efficient devices
- Unplug unused electronics
- Optimize heating/cooling

### Shopping 🛒
- Buy local and seasonal
- Reduce food waste
- Choose sustainable products
- Minimize packaging

### Fashion 👕
- Buy quality over quantity
- Choose sustainable brands
- Repair instead of replace
- Second-hand shopping

## 🔮 Future Enhancements

- [ ] User accounts for tracking progress over time
- [ ] Gamification with achievement badges
- [ ] Social sharing features
- [ ] Integration with smart home devices
- [ ] Mobile app development
- [ ] Expanded dataset with regional variations
- [ ] Real-time environmental impact news
- [ ] Carbon offset marketplace integration

## 👥 Author

**[Your Friend's Name]**
- Programme: MSc Big Data & AI
- Module: M516 Business Project in Big Data & AI
- Institution: Gisma University of Applied Sciences

## 📄 License

This project is developed for academic purposes as part of MSc Big Data & AI program.

## 🙏 Acknowledgments

- Environmental data sources
- Streamlit framework
- Scikit-learn library
- Plotly visualization tools
- UCI Machine Learning Repository

## 📞 Contact

For questions or feedback:
- GitHub: [Profile Link]
- Email: [Email Address]
- LinkedIn: [Profile Link]

---

<p align="center">
  <b>Made with ❤️ for a sustainable future</b>
  <br>
  <i>Every small action counts in fighting climate change</i>
</p>
