import streamlit as st
from textblob import TextBlob

# Professional UI Settings
st.set_page_config(page_title="Pro Sentiment Analyzer", page_icon="📈", layout="centered")

st.title("📈 Commercial Sentiment Analysis Tool")
st.markdown("Analyze customer reviews, social media feedback, and corporate text instantly using Natural Language Processing (NLP).")
st.divider()

# Input area
user_text = st.text_area("Enter text for analysis:", height=150, placeholder="e.g., The product quality is absolutely outstanding and the customer support is extremely helpful!")

if st.button("Analyze Text", type="primary"):
    if user_text.strip():
        # Using NLP for analysis
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        st.subheader("Analysis Results:")
        
        # Displaying results in a professional grid
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if polarity > 0.1:
                st.success("Positive 😊")
            elif polarity < -0.1:
                st.error("Negative 😞")
            else:
                st.info("Neutral 😐")
                
        with col2:
            st.metric(label="Polarity Score", value=f"{polarity:.2f}", help="-1 is highly negative, 1 is highly positive.")
            
        with col3:
            st.metric(label="Subjectivity Score", value=f"{subjectivity:.2f}", help="0 is objective (fact), 1 is subjective (opinion).")
            
        st.divider()
        st.markdown("**Detailed Breakdown:**")
        st.progress(max(0.0, min(1.0, (polarity + 1) / 2))) # Progress bar for visual appeal
        st.caption("Sentiment Meter (Left = Negative, Right = Positive)")
        
    else:
        st.warning("Please enter some text to proceed with the analysis.")
