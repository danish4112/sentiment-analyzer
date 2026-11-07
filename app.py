import streamlit as st

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="📊")

st.title("📊 AI-Powered Sentiment Analyzer (Urdu/English)")
st.write("Yeh app aap ke text ka mood (Positive/Negative) analyze karti hai—chahe aap English mein likhein ya Roman Urdu mein!")

# Text input for user
user_text = st.text_area("Yahan koi bhi sentence likhein:", placeholder="Misal ke tor par: Yeh product bohot achi hai / I love this!")

if st.button("Analyze Sentiment"):
    if user_text.strip() != "":
        text_lower = user_text.lower()
        
        # English + Roman Urdu positive words
        positive_words = [
            "love", "great", "awesome", "good", "amazing", "best", "happy", "zabardast", 
            "achi", "acha", "behtareen", "shandar", "pyar", "pasand", "kamaal", "bohot achi"
        ]
        
        # English + Roman Urdu negative words
        negative_words = [
            "bad", "worst", "hate", "terrible", "poor", "sad", 
            "bekar", "bura", "kharab", "fazool", "ghalat", "nahi"
        ]
        
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        st.subheader("Results:")
        if pos_count > neg_count:
            st.success("😊 Positive Sentiment (Khushi, Tareef ya Achhi baat)")
        elif neg_count > pos_count:
            st.error("😞 Negative Sentiment (Narazgi, Bura ya Shikayat)")
        else:
            st.info("😐 Neutral Sentiment (Aam baat)")
            
        # Extra Stats
        st.write(f"**Total Words:** {len(user_text.split())}")
    else:
        st.warning("Barah-e-karam pehle kuch text enter karein!")