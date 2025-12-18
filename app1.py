import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title='Carbon Footprint Predictor',
    page_icon='🌍',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    h1 {
        color: #2c3e50;
        font-weight: 700;
        text-align: center;
        padding: 20px 0;
    }
    h2, h3 {
        color: #34495e;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 15px 30px;
        border-radius: 25px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(102, 126, 234, 0.4);
    }
    .recommendation-box {
        background: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin: 10px 0;
    }
    .warning-box {
        background: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    .danger-box {
        background: #f8d7da;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🌍 AI-Powered Carbon Footprint Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d; font-size: 18px;'>Predict and reduce your environmental impact with AI</p>", unsafe_allow_html=True)

# Load trained model
@st.cache_resource
def load_model():
    try:
        with open('best_model.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        with open('model.pkl', 'rb') as f:
            return pickle.load(f)

model = load_model()

# Sidebar
with st.sidebar:
    #st.image("leaf_img.png", width=150)
    st.title("About")
    st.info("""
    This AI-powered tool predicts your carbon footprint based on your lifestyle choices.
    
    **Features:**
    - Multiple ML models comparison
    - Real-time predictions
    - Personalized recommendations
    - Interactive visualizations
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Carbon Impact Levels")
    st.success("✅ Low: < 1500 units")
    st.warning("⚠️ Medium: 1500-3000 units")
    st.error("🚨 High: > 3000 units")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Enter Your Lifestyle Data")
    
    with st.container():
        col_a, col_b = st.columns(2)
        
        with col_a:
            monthly_grocery_bill = st.number_input(
                '🛒 Monthly Grocery Bill (₹)',
                min_value=0,
                max_value=100000,
                value=2000,
                step=100,
                help="Your average monthly spending on groceries"
            )
            
            tv_hours = st.slider(
                '📺 Daily TV/PC Usage (hours)',
                min_value=0,
                max_value=24,
                value=5,
                help="Hours spent watching TV or using PC daily"
            )
            
            internet_hours = st.slider(
                '🌐 Daily Internet Usage (hours)',
                min_value=0,
                max_value=24,
                value=4,
                help="Hours spent online daily"
            )
        
        with col_b:
            vehicle_distance = st.number_input(
                '🚗 Monthly Vehicle Distance (Km)',
                min_value=0,
                max_value=20000,
                value=500,
                step=50,
                help="Total distance traveled by vehicle per month"
            )
            
            clothes = st.slider(
                '👕 New Clothes Per Month',
                min_value=0,
                max_value=50,
                value=5,
                help="Number of new clothing items purchased monthly"
            )

with col2:
    st.markdown("### 💡 Quick Tips")
    st.info("""
    **Reduce your footprint:**
    - Use public transport
    - Buy local products
    - Reduce screen time
    - Buy sustainable fashion
    - Plan efficient routes
    """)

# Prediction button
if st.button('🔮 Calculate Carbon Footprint', use_container_width=True):
    # Prepare input data
    input_data = pd.DataFrame({
        'Monthly Grocery Bill': [monthly_grocery_bill],
        'Vehicle Monthly Distance Km': [vehicle_distance],
        'How Long TV PC Daily Hour': [tv_hours],
        'How Many New Clothes Monthly': [clothes],
        'How Long Internet Daily Hour': [internet_hours]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display results
    st.markdown("---")
    st.markdown("## 📊 Your Carbon Footprint Results")
    
    # Metric cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Estimated CO₂ Emission",
            value=f"{prediction:,.0f} units",
            delta=f"{((prediction/2000)-1)*100:.1f}% vs avg"
        )
    
    with col2:
        yearly_emission = prediction * 12
        st.metric(
            label="Yearly Projection",
            value=f"{yearly_emission:,.0f} units"
        )
    
    with col3:
        trees_needed = int(prediction / 20)
        st.metric(
            label="Trees to Offset",
            value=f"{trees_needed} trees"
        )
    
    # Gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=prediction,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Carbon Footprint Level", 'font': {'size': 24}},
        delta={'reference': 2000, 'increasing': {'color': "red"}},
        gauge={
            'axis': {'range': [None, 5000], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 1500], 'color': '#4caf50'},
                {'range': [1500, 3000], 'color': '#ffc107'},
                {'range': [3000, 5000], 'color': '#f44336'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': prediction
            }
        }
    ))
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    # Breakdown chart
    st.markdown("### 📈 Emission Breakdown by Category")
    
    # Calculate contribution percentages
    breakdown = {
        'Grocery': monthly_grocery_bill * 0.5,
        'Transportation': vehicle_distance * 0.6,
        'Electronics': (tv_hours + internet_hours) * 30,
        'Fashion': clothes * 40
    }
    
    fig2 = px.pie(
        values=list(breakdown.values()),
        names=list(breakdown.keys()),
        title="Carbon Emission Sources",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Personalized recommendations
    st.markdown("### 🎯 Personalized Recommendations")
    
    if prediction < 1500:
        st.markdown('<div class="recommendation-box">✅ <b>Excellent!</b> Your carbon footprint is low. Keep up the great work!</div>', unsafe_allow_html=True)
    elif prediction < 3000:
        st.markdown('<div class="warning-box">⚠️ <b>Moderate Impact.</b> Consider these improvements:</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="danger-box">🚨 <b>High Impact!</b> Urgent action recommended:</div>', unsafe_allow_html=True)
    
    recommendations = []
    
    if vehicle_distance > 1000:
        recommendations.append("🚴 Consider using public transport or carpooling to reduce vehicle emissions")
    
    if tv_hours + internet_hours > 10:
        recommendations.append("💡 Reduce screen time and use energy-efficient devices")
    
    if clothes > 10:
        recommendations.append("👗 Adopt sustainable fashion: buy less, choose quality over quantity")
    
    if monthly_grocery_bill > 5000:
        recommendations.append("🥗 Buy local and seasonal produce to reduce transportation emissions")
    
    if not recommendations:
        recommendations.append("🌱 Continue your eco-friendly habits and inspire others!")
    
    for rec in recommendations:
        st.markdown(f"- {rec}")
    
    # Comparison with averages
    st.markdown("### 📊 How You Compare")
    comparison_data = pd.DataFrame({
        'Category': ['You', 'National Avg', 'Global Avg', 'Target'],
        'Emission': [prediction, 2000, 2500, 1000]
    })
    
    fig3 = px.bar(
        comparison_data,
        x='Category',
        y='Emission',
        color='Emission',
        color_continuous_scale='RdYlGn_r',
        text='Emission'
    )
    fig3.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig3.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

# Model performance section
with st.expander("🔬 Model Performance Details"):
    try:
        model_comparison = pd.read_csv('model_comparison.csv')
        st.dataframe(model_comparison, use_container_width=True)
        
        with open('best_model_info.txt', 'r') as f:
            info = f.read()
        st.code(info)
    except:
        with open('model_info.txt', 'r') as f:
            info = f.read()
        st.code(info)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #95a5a6;'>Made with ❤️ for a sustainable future.</p>",
    unsafe_allow_html=True
)