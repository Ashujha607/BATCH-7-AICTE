# Veritas - AI-Powered Fact Checker 🛡️

An intelligent fake news and misinformation detector powered by Machine Learning and AI. Combines TF-IDF-based classification with advanced LLM fact-checking to verify news claims in real-time.

---

## 🌟 Features

- **🤖 AI-Powered Verification**: Uses Groq's LLM (Llama 3.1) for intelligent fact-checking
- **📊 ML Classification**: TF-IDF + Logistic Regression for pattern-based detection
- **🎨 Modern UI**: Premium dark-themed Streamlit interface with glassmorphism
- **🌐 Bilingual Support**: Results in both English and Hinglish
- **📈 Visual Analytics**: Comprehensive model evaluation with charts and metrics
- **⚡ Real-Time Analysis**: Instant verification of news claims

---

## 📸 Demo

### Streamlit Web Application

<img width="683" height="490" alt="Veritas AI Fact Checker Interface" src="https://github.com/user-attachments/assets/d68c9b02-fe94-48d5-85ce-06b292e38dbb" />

**Key Features:**
- Clean, modern dark theme with gradient backgrounds
- Real-time AI fact-checking with detailed reasoning
- Bilingual conclusions (English + Hinglish)
- Responsive card-based layout
- Smooth animations and transitions

---

## 📁 Project Structure

```
Fake-News-Detector-main/
│
├── .streamlit/
│   ├── secrets.toml.example     # API key configuration template
│   └── secrets.toml              # Your API keys (gitignored)
│
├── data/
│   ├── True.csv                  # Real news dataset (999 rows)
│   └── Fake.csv                  # Fake news dataset (999 rows)
│
├── outputs/
│   ├── model.joblib              # Trained Logistic Regression model
│   ├── vectorizer.joblib         # TF-IDF vectorizer
│   ├── pipeline.joblib           # Combined ML pipeline
│   ├── metrics.json              # Model performance metrics
│   ├── confusion_matrix.png      # Confusion matrix visualization
│   ├── roc_curve.png             # ROC curve plot
│   └── pr_curve.png              # Precision-Recall curve
│
├── src/
│   ├── streamlit_app.py          # Main web application
│   ├── train_model.py            # Model training script
│   ├── detect_fake_news.py       # CLI prediction tool
│   ├── text_clean.py             # Text preprocessing utilities
│   ├── utils.py                  # Helper functions
│   ├── test_prob.py              # Probability testing
│   ├── test_real_fake.py         # Classification testing
│   ├── list_models.py            # Model listing utility
│   └── debug_keys.py             # API key debugging
│
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── LICENSE                       # Project license
└── README.md                     # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Groq API key (get one at [console.groq.com](https://console.groq.com))

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Fake-News-Detector-main.git
   cd Fake-News-Detector-main
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   
   Create `.streamlit/secrets.toml` from the example:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```
   
   Edit `.streamlit/secrets.toml` and add your Groq API key:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

5. **Train the Model** (Optional - pre-trained models included)
   ```bash
   python src/train_model.py --real data/True.csv --fake data/Fake.csv --text-col text --outdir outputs
   ```

---

## 🎯 Usage

### Web Application

Launch the Streamlit app:
```bash
streamlit run src/streamlit_app.py
```

Then open your browser to:
```
http://localhost:8502
```

**How to Use:**
1. Enter or paste a news claim in the text area
2. Click "🔎 VERIFY TRUTH"
3. Review the AI-powered analysis with:
   - Verdict (FAKE or REAL)
   - Detailed reasoning in English
   - Bilingual conclusion in Hinglish

### Command-Line Interface

For quick predictions without the web UI:
```bash
python src/detect_fake_news.py \
  --model outputs/model.joblib \
  --vectorizer outputs/vectorizer.joblib \
  --text "Your news claim here"
```

---

## 📊 Dataset

| File | Type | Rows | Columns |
|------|------|------|---------|
| `True.csv` | Real news | 999 | `title`, `text`, `subject`, `date` |
| `Fake.csv` | Fake news | 999 | `title`, `text`, `subject`, `date` |

**Dataset Source:**  
Based on the [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) by Clément Bisaillon (Kaggle).  
Data has been cleaned, balanced, and downsampled to 999 samples per class for optimal training.

**License:** Used for educational and research purposes only.

---

## 🧠 How It Works

### Dual-Layer Verification System

#### 1. Machine Learning Layer (TF-IDF + Logistic Regression)
- **Text Preprocessing**: Removes noise, URLs, special characters
- **Feature Extraction**: TF-IDF vectorization (Term Frequency-Inverse Document Frequency)
- **Classification**: Logistic Regression model predicts FAKE vs REAL
- **Output**: Probability score and binary classification

#### 2. AI Intelligence Layer (Groq LLM)
- **Model**: Llama 3.1 8B Instant via Groq API
- **Analysis**: Cross-references claims with knowledge base
- **Reasoning**: Provides detailed evidence-based conclusions
- **Bilingual**: Outputs in both English and Hinglish for accessibility

### Processing Pipeline

```
User Input → Text Cleaning → TF-IDF Vectorization → ML Prediction
                                                    ↓
                                            AI Fact-Checking
                                                    ↓
                                        Structured Verdict + Reasoning
```

---

## 📈 Model Performance

### Metrics Summary

| Metric | Value |
|--------|-------|
| **Accuracy** | 100% |
| **Precision (FAKE)** | 1.00 |
| **Recall (FAKE)** | 1.00 |
| **F1-Score** | 1.00 |
| **ROC-AUC** | 1.00 |

### Confusion Matrix

<img width="1050" height="900" alt="confusion_matrix" src="https://github.com/user-attachments/assets/15735f60-4216-4aae-bf07-e265c034e5ef" />

| True Label | Predicted REAL | Predicted FAKE |
|------------|----------------|----------------|
| **REAL** | 999 ✅ | 0 ❌ |
| **FAKE** | 0 ❌ | 999 ✅ |

Perfect classification on the test set (1,998 samples).

### ROC Curve

<img width="1050" height="900" alt="roc_curve" src="https://github.com/user-attachments/assets/a1b60b15-69f3-4440-ade5-92346731ffa9" />

**AUC = 1.00** - Perfect class separability

### Precision-Recall Curve

<img width="1050" height="900" alt="pr_curve" src="https://github.com/user-attachments/assets/a0786968-55f4-40ad-92ca-6684e0312e50" />

Both precision and recall achieve **1.00** - Zero false predictions on test data.

> **Note:** While the model achieves perfect accuracy on this curated dataset, real-world performance may vary due to evolving misinformation tactics and diverse writing styles.

---

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.10+** - Primary programming language
- **Streamlit 1.33+** - Web application framework
- **scikit-learn 1.3+** - Machine learning library

### Machine Learning
- **TF-IDF Vectorizer** - Text feature extraction
- **Logistic Regression** - Binary classification
- **joblib** - Model serialization

### AI Integration
- **Groq API** - LLM inference platform
- **OpenAI SDK** - API client library
- **Llama 3.1 8B** - Language model for fact-checking

### Data & Visualization
- **pandas 2.0+** - Data manipulation
- **numpy 1.25+** - Numerical computing
- **matplotlib 3.7+** - Chart generation

### UI/UX
- **Custom CSS** - Modern dark theme with glassmorphism
- **Google Fonts (Inter)** - Premium typography
- **Gradient backgrounds** - Visual polish

---

## 📝 Code Modules

| Module | Purpose |
|--------|---------|
| `streamlit_app.py` | Main web application with modern UI and AI integration |
| `train_model.py` | Model training pipeline with evaluation and visualization |
| `detect_fake_news.py` | Command-line prediction interface |
| `text_clean.py` | Text preprocessing and normalization utilities |
| `utils.py` | File I/O helpers and directory management |
| `test_prob.py` | Probability distribution testing |
| `test_real_fake.py` | Classification accuracy testing |
| `list_models.py` | Model inventory and metadata |
| `debug_keys.py` | API key validation and debugging |

---

## 🔧 Configuration

### API Keys

The application supports multiple configuration methods:

1. **Streamlit Secrets** (Recommended for deployment)
   ```toml
   # .streamlit/secrets.toml
   GROQ_API_KEY = "gsk_..."
   ```

2. **Environment Variables**
   ```bash
   export GROQ_API_KEY="gsk_..."
   ```

### Model Configuration

Models are automatically loaded from the `outputs/` directory:
- `pipeline.joblib` - Complete ML pipeline (preferred)
- `model.joblib` + `vectorizer.joblib` - Separate components

---

## 🎨 UI Features

### Modern Design Elements

- **Dark Theme**: Gradient background (#0f172a → #1e293b)
- **Typography**: Inter font family for premium feel
- **Color Palette**:
  - FAKE verdict: Red (#ef4444)
  - REAL verdict: Green (#10b981)
  - Accent: Blue (#3b82f6)
- **Animations**: Smooth hover effects and transitions
- **Cards**: Glassmorphism-inspired result containers
- **Responsive**: Centered layout with optimal reading width

---

## 🚦 Training the Model

### Basic Training

```bash
python src/train_model.py \
  --real data/True.csv \
  --fake data/Fake.csv \
  --text-col text \
  --outdir outputs
```

### Training Process

1. **Data Loading**: Reads real and fake news CSV files
2. **Preprocessing**: Cleans text using `text_clean.py`
3. **Feature Engineering**: Applies TF-IDF vectorization
4. **Model Training**: Trains Logistic Regression classifier
5. **Evaluation**: Generates metrics and visualization charts
6. **Serialization**: Saves models to `outputs/` directory

### Output Files

- `model.joblib` - Trained classifier
- `vectorizer.joblib` - Fitted TF-IDF vectorizer
- `pipeline.joblib` - Combined pipeline
- `metrics.json` - Performance statistics
- `confusion_matrix.png` - Classification matrix
- `roc_curve.png` - ROC analysis
- `pr_curve.png` - Precision-Recall analysis

---

## 🧪 Testing

### Test Scripts

1. **Probability Testing**
   ```bash
   python src/test_prob.py
   ```

2. **Classification Testing**
   ```bash
   python src/test_real_fake.py
   ```

3. **API Key Validation**
   ```bash
   python src/debug_keys.py
   ```

---

## 🌐 Deployment

### Streamlit Community Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add `GROQ_API_KEY` to Secrets in the dashboard
5. Deploy!

### Local Production

```bash
streamlit run src/streamlit_app.py --server.port 8502
```

---

## 🔮 Future Improvements

### Planned Features

- [ ] **Advanced NLP Models**: Integrate BERT/DistilBERT for contextual understanding
- [ ] **Multi-Language Support**: Extend to Spanish, French, Hindi, etc.
- [ ] **Explainable AI**: Add LIME/SHAP for model transparency
- [ ] **Source Verification**: Cross-reference with trusted news sources
- [ ] **Browser Extension**: Real-time fact-checking while browsing
- [ ] **API Endpoint**: RESTful API for third-party integrations
- [ ] **User Feedback Loop**: Crowdsourced verification system
- [ ] **Historical Tracking**: Database of verified claims
- [ ] **Confidence Scoring**: Nuanced probability ranges
- [ ] **Mobile App**: Native iOS/Android applications

### Technical Enhancements

- [ ] Model versioning and A/B testing
- [ ] Caching layer for repeated queries
- [ ] Rate limiting and API quota management
- [ ] Automated retraining pipeline
- [ ] Performance monitoring and logging

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/Fake-News-Detector-main](https://github.com/yourusername/Fake-News-Detector-main)

---

## 🙏 Acknowledgments

- **Dataset**: Clément Bisaillon for the Fake and Real News Dataset
- **Groq**: For providing fast LLM inference
- **Streamlit**: For the excellent web framework
- **scikit-learn**: For robust ML tools

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/Fake-News-Detector-main/issues) page
2. Create a new issue with detailed information
3. Ensure your API keys are properly configured

---

## ⭐ Star This Repository

If you find this project useful, please consider giving it a star! It helps others discover the project.

---

<div align="center">

**Built with ❤️ for a more truthful internet**

[Report Bug](https://github.com/yourusername/Fake-News-Detector-main/issues) · [Request Feature](https://github.com/yourusername/Fake-News-Detector-main/issues)

</div>
