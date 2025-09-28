import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots

# إعداد الصفحة
st.set_page_config(
    page_title="نماذج القياس الاقتصادي التطبيقية",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS للتنسيق
st.markdown("""
<style>
    .main {
        direction: rtl;
        text-align: right;
    }
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 10rem;
    }
    h1 {
        color: #1e3a8a;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    h2 {
        color: #1e40af;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    h3 {
        color: #1d4ed8;
        margin-top: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .model-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .job-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .ai-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .tech-tag {
        background: rgba(255,255,255,0.2);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    .salary-info {
        background: #f8fafc;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .sidebar .sidebar-content {
        direction: rtl;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("""
<h1>📊 نماذج القياس الاقتصادي التطبيقية في الواقع العملي</h1>
<div style="text-align: center; color: #6b7280; font-size: 1.2rem; margin-bottom: 3rem;">
    تقرير شامل إعداد: الدكتور مروان رودان<br>
    <em>دليل متخصص للنماذج والتقنيات والوظائف في عصر الذكاء الاصطناعي</em>
</div>
""", unsafe_allow_html=True)

# الشريط الجانبي للتنقل
st.sidebar.title("🗂️ فهرس المحتويات")
page = st.sidebar.selectbox(
    "اختر القسم:",
    [
        "📈 النظرة العامة والإحصائيات",
        "🧮 النماذج الأساسية للتطبيق",
        "🤖 الذكاء الاصطناعي والتعلم العميق",
        "💼 الوظائف والمهن",
        "🔧 المهارات التقنية المطلوبة",
        "🌍 التطبيقات العملية",
        "📚 التوصيات والمسار المهني"
    ]
)

if page == "📈 النظرة العامة والإحصائيات":
    st.header("📈 النظرة العامة والإحصائيات الرئيسية")

    # الإحصائيات الأساسية
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>2.1 مليار دولار</h3>
            <p>حجم سوق برمجيات القياس الاقتصادي العالمي بحلول 2025</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>22% نمو سنوي</h3>
            <p>معدل النمو المتوقع لوظائف علماء البيانات مع خلفية اقتصادية</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>$120K متوسط الراتب</h3>
            <p>متوسط الراتب السنوي للاقتصاديين التطبيقيين في الصناعة</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>65% زيادة الطلب</h3>
            <p>زيادة الطلب على مهارات القياس الاقتصادي + الذكاء الاصطناعي</p>
        </div>
        """, unsafe_allow_html=True)

    # إضافة قسم متخصص لأدوات نمذجة المزيج التسويقي
    st.subheader("📊 أدوات ومكتبات نمذجة المزيج التسويقي المتخصصة")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="model-card">
            <h4>🔧 أدوات MMM المفتوحة المصدر</h4>
            <h5>Meta Robyn:</h5>
            <ul>
                <li>نمذجة بايزية متقدمة</li>
                <li>معايرة تلقائية للهايبر بارامترز</li>
                <li>نمذجة التشبع والتأخير</li>
                <li>تحسين الميزانية المدمج</li>
            </ul>
            <h5>Google LightweightMMM:</h5>
            <ul>
                <li>مبني على JAX للسرعة</li>
                <li>نماذج بايزية هرمية</li>
                <li>دعم البيانات الجغرافية</li>
                <li>تقدير عدم اليقين</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>📈 أدوات التطوير والتحليل</h4>
            <h5>Python:</h5>
            <ul>
                <li>PyMC3/PyMC4 (Bayesian modeling)</li>
                <li>Stan/PyStan (MCMC sampling)</li>
                <li>Prophet (time series decomposition)</li>
                <li>scikit-learn (preprocessing)</li>
                <li>plotly/matplotlib (visualization)</li>
            </ul>
            <h5>R:</h5>
            <ul>
                <li>brms (Bayesian regression)</li>
                <li>prophet (forecasting)</li>
                <li>bsts (Bayesian structural time series)</li>
                <li>CausalImpact (causal inference)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="model-card">
            <h4>🏢 الحلول التجارية</h4>
            <h5>منصات متقدمة:</h5>
            <ul>
                <li>Nielsen Marketing Cloud</li>
                <li>Analytic Partners</li>
                <li>MarketShare (Google)</li>
                <li>Marketing Evolution</li>
                <li>Adstock (Decideware)</li>
            </ul>
            <h5>أدوات التصور والتقارير:</h5>
            <ul>
                <li>Tableau (dashboards)</li>
                <li>Power BI (Microsoft)</li>
                <li>Looker (Google Cloud)</li>
                <li>Custom Shiny Apps (R)</li>
                <li>Streamlit (Python)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # رسم بياني للنمو في الوظائف
    st.subheader("📊 نمو الوظائف حسب القطاع (2023-2028)")

    sectors_data = {
        'القطاع': ['الخدمات المالية', 'التكنولوجيا', 'الاستشارات', 'الحكومة', 'الصحة', 'التجارة الإلكترونية'],
        'نمو_النسبة_المئوية': [35, 28, 18, 12, 15, 22],
        'عدد_الوظائف_الجديدة': [8500, 6800, 4200, 2800, 3500, 5100]
    }

    df_sectors = pd.DataFrame(sectors_data)

    fig = px.bar(df_sectors, x='القطاع', y='نمو_النسبة_المئوية',
                 color='عدد_الوظائف_الجديدة',
                 title="معدل النمو في الوظائف حسب القطاع (%)",
                 color_continuous_scale='viridis')
    fig.update_layout(
        font=dict(size=14),
        title_x=0.5,
        xaxis_title="القطاع",
        yaxis_title="معدل النمو (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

    # الفجوة بين الأكاديميا والصناعة
    st.subheader("⚖️ الفجوة بين التكوين الأكاديمي والواقع الصناعي")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 15px;">
        <h3>🎓 ما تتعلمه في الأكاديميا</h3>
        <ul style="line-height: 1.8;">
        <li>✅ النظرية الإحصائية المتقدمة</li>
        <li>✅ اشتقاق النماذج النظرية</li>
        <li>✅ منهجية البحث</li>
        <li>✅ الكتابة الأكاديمية</li>
        <li>✅ مراجعة الأدبيات</li>
        <li>❌ فهم السياق التجاري</li>
        <li>❌ التعامل مع البيانات الفورية</li>
        <li>❌ التواصل مع أصحاب القرار</li>
        <li>❌ البرمجة للإنتاج</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 1.5rem; border-radius: 15px;">
        <h3>🏢 ما تطلبه الصناعة</h3>
        <ul style="line-height: 1.8;">
        <li>✅ حل المشاكل العملية</li>
        <li>✅ التركيز على الأثر التجاري</li>
        <li>✅ التعاون متعدد التخصصات</li>
        <li>✅ الحلول القابلة للتطوير</li>
        <li>✅ سرد البيانات</li>
        <li>✅ إدارة المشاريع</li>
        <li>✅ الكفاءة التقنية</li>
        <li>❌ المعرفة النظرية العميقة</li>
        <li>❌ خبرة النشر</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "🧮 النماذج الأساسية للتطبيق":
    st.header("🧮 النماذج الأساسية للقياس الاقتصادي التطبيقي")

    # تصنيف النماذج حسب الغرض
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
        ["🔍 الاستدلال السببي", "📈 التنبؤ والتوقع", "💰 التسعير والتحسين", "⚖️ تقييم السياسات",
         "📊 القياس الاقتصادي عالي الأبعاد", "⚠️ نمذجة المخاطر", "🎯 قياس اقتصاديات التفاعل الاستراتيجي",
         "🌐 اقتصاديات البيانات الضخمة والشبكات", "💹 نماذج الأسواق المالية المتقدمة"])

    with tab1:
        st.subheader("🔍 نماذج الاستدلال السببي (Causal Inference Models)")

        models_causal = [
            {
                "name_ar": "تحليل الفروق في الفروق",
                "name_en": "Difference-in-Differences (DiD)",
                "applications": "تقييم أثر السياسات، إطلاق المنتجات، التدخلات التسويقية",
                "modern_versions": "Callaway-Sant'Anna, Sun-Abraham, Staggered DiD",
                "industry_use": "95%",
                "complexity": "متوسط"
            },
            {
                "name_ar": "انحدار الانقطاع",
                "name_en": "Regression Discontinuity Design (RDD)",
                "applications": "برامج الولاء، العتبات الائتمانية، المنح والإعانات",
                "modern_versions": "Sharp RDD, Fuzzy RDD, Multi-cutoff RDD",
                "industry_use": "75%",
                "complexity": "متوسط"
            },
            {
                "name_ar": "المتغيرات الآلية",
                "name_en": "Instrumental Variables (IV)",
                "applications": "مرونة الأسعار، تأثير الإعلانات، العوامل الداخلية",
                "modern_versions": "2SLS, GMM, ML-based IV, DeepIV",
                "industry_use": "85%",
                "complexity": "عالي"
            },
            {
                "name_ar": "التحكم التركيبي",
                "name_en": "Synthetic Control Methods (SCM)",
                "applications": "تقييم السياسات الجغرافية، تغييرات المنصات، التدخلات الكبرى",
                "modern_versions": "Augmented SCM, Matrix Completion SCM",
                "industry_use": "65%",
                "complexity": "متوسط إلى عالي"
            }
        ]

        for model in models_causal:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>الإصدارات الحديثة:</strong> {model['modern_versions']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                    <span class="tech-tag">استخدام صناعي: {model['industry_use']}</span>
                    <span class="tech-tag">التعقيد: {model['complexity']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.subheader("📈 نماذج التنبؤ والتوقع")

        forecasting_models = [
            {
                "name_ar": "النماذج الهيكلية الحالية",
                "name_en": "State-Space Models",
                "applications": "التنبؤ الاقتصادي، إدارة المخزون، التخطيط المالي",
                "tools": "Kalman Filter, BSTS, Prophet",
                "advantage": "التعامل مع البيانات المفقودة والمكونات المتغيرة"
            },
            {
                "name_ar": "نماذج الذاكرة طويلة المدى",
                "name_en": "Long Short-Term Memory (LSTM)",
                "applications": "التنبؤ بالطلب، أسعار الأسهم، سلوك المستهلك",
                "tools": "TensorFlow, PyTorch, Keras",
                "advantage": "قدرة على تعلم التبعيات طويلة المدى"
            },
            {
                "name_ar": "محولات الانتباه",
                "name_en": "Transformer Models",
                "applications": "التنبؤ متعدد المتغيرات، تحليل النصوص الاقتصادية",
                "tools": "Attention Mechanism, BERT for Time Series",
                "advantage": "معالجة السلاسل الطويلة والانتباه للأجزاء المهمة"
            },
            {
                "name_ar": "النماذج الهجينة",
                "name_en": "Hybrid ML-Econometric Models",
                "applications": "الجمع بين القابلية للتفسير والدقة",
                "tools": "Prophet + ML, ARIMAX + Neural Networks",
                "advantage": "الاستفادة من مزايا النماذج التقليدية والحديثة"
            }
        ]

        for model in forecasting_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
                <p><strong>الميزة الرئيسية:</strong> {model['advantage']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.subheader("💰 نماذج التسعير والتحسين")

        pricing_models = [
            {
                "name_ar": "نماذج الاختيار المتقطع",
                "name_en": "Discrete Choice Models",
                "variants": "Multinomial Logit (MNL), Nested Logit, Mixed Logit",
                "applications": "تسعير المنتجات، تخطيط التشكيلة، تفضيلات المستهلك"
            },
            {
                "name_ar": "تحليل الترابط المتداخل",
                "name_en": "Conjoint Analysis",
                "variants": "Choice-Based Conjoint, Adaptive Conjoint",
                "applications": "تطوير المنتجات، استراتيجيات التسعير، تجزئة السوق"
            },
            {
                "name_ar": "نماذج المرونة الديناميكية",
                "name_en": "Dynamic Pricing Models",
                "variants": "Contextual Bandits, Reinforcement Learning",
                "applications": "التسعير في الوقت الفعلي، المزادات، المنصات الرقمية"
            }
        ]

        for model in pricing_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>المتغيرات:</strong> {model['variants']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
            </div>
            """, unsafe_allow_html=True)

        # إضافة نمذجة المزيج التسويقي
        st.markdown("#### 📊 نمذجة المزيج التسويقي والقياس")

        mmm_models = [
            {
                "name_ar": "نمذجة المزيج التسويقي التقليدية",
                "name_en": "Traditional Marketing Mix Modeling (MMM)",
                "description": "نماذج انحدار متعددة لقياس تأثير القنوات التسويقية على المبيعات",
                "applications": "قياس ROI للقنوات، تحسين الميزانية، تخطيط الحملات",
                "challenges": "التداخل الخطي، التأثيرات المتأخرة، القياس الصحيح للتشبع"
            },
            {
                "name_ar": "نمذجة المزيج التسويقي البايزية",
                "name_en": "Bayesian Marketing Mix Modeling",
                "description": "استخدام النهج البايزي لنمذجة عدم اليقين والتأثيرات المعقدة",
                "applications": "تقدير عدم اليقين، دمج المعرفة المسبقة، النماذج الهرمية",
                "tools": "Robyn (Meta), LightweightMMM (Google), PyMC3, Stan"
            },
            {
                "name_ar": "نماذج التشبع والتأخير التسويقي",
                "name_en": "Marketing Adstock & Saturation Models",
                "description": "نمذجة التأثيرات المتأخرة والعوائد المتناقصة في الإعلان",
                "applications": "قياس الأثر طويل المدى، تحسين التوقيت، فهم منحنيات الاستجابة",
                "methods": "Adstock Transformation, Hill Saturation, Geometric Decay"
            },
            {
                "name_ar": "نماذج الإسناد التسويقي",
                "name_en": "Marketing Attribution Models",
                "description": "توزيع الفضل في التحويلات على نقاط الاتصال المختلفة",
                "applications": "تحسين رحلة العميل، تخصيص الميزانية، فهم التفاعلات",
                "methods": "First-touch, Last-touch, Multi-touch, Algorithmic Attribution"
            }
        ]

        for model in mmm_models:
            st.markdown(f"""
            <div class="ai-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الوصف:</strong> {model['description']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>{"الأدوات" if "tools" in model else "الطرق" if "methods" in model else "التحديات"}:</strong> {model.get('tools', model.get('methods', model.get('challenges', '')))}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.subheader("⚖️ نماذج تقييم السياسات والبرامج")

        policy_models = [
            {
                "name_ar": "التقييم التأثيري للبرامج",
                "name_en": "Program Impact Evaluation",
                "methods": "RCT, Quasi-experiments, Natural experiments",
                "applications": "البرامج الحكومية، المبادرات الاجتماعية، السياسات العامة"
            },
            {
                "name_ar": "تحليل التكلفة والعائد",
                "name_en": "Cost-Benefit Analysis",
                "methods": "NPV, IRR, Social Return on Investment",
                "applications": "مشاريع البنية التحتية، البرامج الصحية، السياسات البيئية"
            },
            {
                "name_ar": "نماذج المحاكاة الاقتصادية",
                "name_en": "Economic Simulation Models",
                "methods": "Agent-Based Models, DSGE, Microsimulation",
                "applications": "تحليل السيناريوهات، التنبؤ بالأثر، تصميم السياسات"
            }
        ]

        for model in policy_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الطرق:</strong> {model['methods']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.subheader("📊 القياس الاقتصادي عالي الأبعاد (High-Dimensional Econometrics)")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>🎯 متى نحتاج للقياس الاقتصادي عالي الأبعاد؟</h4>
        <p>عندما يكون عدد المتغيرات (p) أكبر بكثير من عدد الملاحظات (n). شائع في علم الوراثة، المالية، وتحليلات المستخدمين.</p>
        </div>
        """, unsafe_allow_html=True)

        high_dim_models = [
            {
                "name_ar": "الانحدار المقيد - لاسو",
                "name_en": "LASSO (Least Absolute Shrinkage and Selection Operator)",
                "description": "يضيف عقوبة L1 لتحقيق انتقاء المتغيرات التلقائي",
                "applications": "اختيار المتغيرات، النمذجة التنبؤية، تحليل الجينوم الاقتصادي",
                "advantages": "انتقاء متغيرات تلقائي، نموذج متناثر وقابل للتفسير",
                "tools": "scikit-learn, glmnet (R), statsmodels"
            },
            {
                "name_ar": "انحدار الانكماش - ريدج",
                "name_en": "Ridge Regression",
                "description": "يضيف عقوبة L2 للتعامل مع التداخل الخطي المتعدد",
                "applications": "التنبؤ المالي، نمذجة عوائد الأسهم، التحكم في التباين",
                "advantages": "استقرار الحل، التعامل مع التداخل الخطي، تحسين دقة التنبؤ",
                "tools": "scikit-learn, ridge (R), sklearn.linear_model"
            },
            {
                "name_ar": "الشبكة المرنة",
                "name_en": "Elastic Net",
                "description": "يجمع بين عقوبات L1 و L2 للحصول على توازن أمثل",
                "applications": "النمذجة التنبؤية المالية، تحليل البيانات الاقتصادية الضخمة",
                "advantages": "يوازن بين اختيار المتغيرات والاستقرار",
                "tools": "scikit-learn, glmnet, ElasticNetCV"
            },
            {
                "name_ar": "التحليل العاملي الديناميكي",
                "name_en": "Dynamic Factor Models (DFM)",
                "description": "استخراج العوامل المشتركة من البيانات عالية الأبعاد",
                "applications": "التنبؤ الاقتصادي الكلي، تحليل المؤشرات المتعددة، الآن الاقتصادي",
                "advantages": "تقليل الأبعاد، استخراج الاتجاهات العامة",
                "tools": "statsmodels, R (vars), MATLAB Econometrics Toolbox"
            },
            {
                "name_ar": "نماذج فيكتور الانحدار الذاتي المقيد",
                "name_en": "Penalized Vector Autoregression (VAR)",
                "description": "تطبيق تقنيات التقييد على نماذج VAR عالية الأبعاد",
                "applications": "التنبؤ الاقتصادي الكلي، تحليل الصدمات، السياسة النقدية",
                "advantages": "التعامل مع العديد من السلاسل الزمنية المترابطة",
                "tools": "BigVAR (R), vars, MTS"
            },
            {
                "name_ar": "التعلم الآلي السببي عالي الأبعاد",
                "name_en": "High-Dimensional Causal Machine Learning",
                "description": "تطبيق DML وCausal Forests في بيئات عالية الأبعاد",
                "applications": "تقدير التأثيرات العلاجية مع آلاف المتغيرات الضابطة",
                "advantages": "استدلال سببي قوي في البيانات المعقدة",
                "tools": "EconML, grf (R), DoubleML"
            }
        ]

        for model in high_dim_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الوصف:</strong> {model['description']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>المزايا:</strong> {model['advantages']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab6:
        st.subheader("⚠️ نمذجة المخاطر (Risk Modeling)")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>🏦 أهمية نمذجة المخاطر في الصناعة المالية</h4>
        <p>نمذجة المخاطر أساسية لإدارة رؤوس الأموال، الامتثال التنظيمي، واتخاذ قرارات الاستثمار المدروسة.</p>
        </div>
        """, unsafe_allow_html=True)

        risk_models = [
            {
                "name_ar": "قيمة المخاطرة",
                "name_en": "Value at Risk (VaR)",
                "types": "Historical VaR, Parametric VaR, Monte Carlo VaR",
                "applications": "إدارة مخاطر السوق، تخصيص رأس المال، التقارير التنظيمية",
                "regulations": "Basel III, Solvency II",
                "tools": "Python (scipy, numpy), R (rugarch), MATLAB Risk Management Toolbox"
            },
            {
                "name_ar": "قيمة المخاطرة المشروطة",
                "name_en": "Conditional Value at Risk (CVaR/ES)",
                "types": "Expected Shortfall, Spectral Risk Measures",
                "applications": "تحسين المحافظ، قياس المخاطر المفرطة، إدارة المخاطر المتطرفة",
                "regulations": "Basel III (من 2016), FRTB",
                "tools": "CVXpy, CVXR, PerformanceAnalytics"
            },
            {
                "name_ar": "نماذج التقلب المشروط",
                "name_en": "Conditional Volatility Models",
                "types": "GARCH, EGARCH, GJR-GARCH, FIGARCH, MGARCH",
                "applications": "التنبؤ بالتقلبات، تسعير الخيارات، إدارة مخاطر السوق",
                "regulations": "Market Risk Framework, IFRS 9",
                "tools": "arch (Python), rugarch (R), MFE Toolbox"
            },
            {
                "name_ar": "نماذج المخاطر الائتمانية",
                "name_en": "Credit Risk Models",
                "types": "PD Models, LGD Models, EAD Models, Credit VaR",
                "applications": "قرارات الإقراض، تسعير القروض، حساب مخصصات الخسائر",
                "regulations": "IFRS 9, CECL, Basel III",
                "tools": "Python (lifelines, scikit-survival), R (survival), SAS"
            },
            {
                "name_ar": "نماذج المخاطر العملياتية",
                "name_en": "Operational Risk Models",
                "types": "Loss Distribution Approach, Scenario Analysis, Scorecard Approach",
                "applications": "قياس مخاطر العمليات، تخصيص رأس المال التنظيمي",
                "regulations": "Basel III AMA, SMA",
                "tools": "R (ActuariaR), Python (scipy.stats), @RISK"
            },
            {
                "name_ar": "نمذجة المخاطر النظامية",
                "name_en": "Systemic Risk Modeling",
                "types": "Network Models, Contagion Models, Stress Testing",
                "applications": "تقييم استقرار النظام المالي، اختبارات الضغط الكلية",
                "regulations": "CCAR, DFAST, EU Stress Testing",
                "tools": "NetworkX, igraph, MATLAB Econometrics"
            },
            {
                "name_ar": "نماذج مخاطر السيولة",
                "name_en": "Liquidity Risk Models",
                "types": "Liquidity Coverage Ratio, Net Stable Funding Ratio, Cash Flow at Risk",
                "applications": "إدارة السيولة، التمويل قصير المدى، تخطيط رأس المال",
                "regulations": "Basel III LCR, NSFR",
                "tools": "Python (pandas), R (quantmod), Bloomberg API"
            }
        ]

        for model in risk_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الأنواع:</strong> {model['types']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>اللوائح التنظيمية:</strong> {model['regulations']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab7:
        st.subheader("🎯 قياس اقتصاديات التفاعل الاستراتيجي (Econometrics of Strategic Interaction)")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>🎲 فهم السلوك الاستراتيجي في الأسواق</h4>
        <p>دراسة كيف تؤثر قرارات الشركات على بعضها البعض في الأسواق القليلة المنافسة والمزادات والألعاب الاقتصادية.</p>
        </div>
        """, unsafe_allow_html=True)

        strategic_models = [
            {
                "name_ar": "نماذج الألعاب الهيكلية",
                "name_en": "Structural Game Models",
                "types": "Simultaneous Games, Sequential Games, Dynamic Games",
                "applications": "تحليل المنافسة، استراتيجيات التسعير، دخول وخروج الشركات",
                "estimation": "Two-Step Estimation, MPEC, Nested Fixed Point",
                "examples": "منافسة شركات الطيران، حروب الأسعار، استراتيجيات الإعلان"
            },
            {
                "name_ar": "نماذج دخول السوق الاستراتيجية",
                "name_en": "Strategic Market Entry Models",
                "types": "Entry Games, Location Choice, Product Differentiation",
                "applications": "قرارات الاستثمار، توقع سلوك المنافسين، تحليل الاندماج",
                "estimation": "Coherency Conditions, Multiple Equilibria, Selection",
                "examples": "دخول متاجر التجزئة، مواقع المطاعم، منصات التكنولوجيا"
            },
            {
                "name_ar": "اقتصاديات المزادات",
                "name_en": "Auction Economics",
                "types": "First-Price Auctions, Second-Price Auctions, Multi-Unit Auctions",
                "applications": "تصميم المزادات، تقدير استراتيجيات العطاء، تحليل الإيرادات",
                "estimation": "Nonparametric Identification, Kernel Methods, Machine Learning",
                "examples": "مزادات الإعلانات الرقمية، مزادات الطيف، المشتريات الحكومية"
            },
            {
                "name_ar": "نماذج التفاعل الاجتماعي",
                "name_en": "Social Interaction Models",
                "types": "Network Effects, Peer Effects, Spatial Competition",
                "applications": "تأثيرات الشبكة، انتشار التبني، التفاعلات الاجتماعية",
                "estimation": "Network Econometrics, Spatial Econometrics, ML for Networks",
                "examples": "انتشار التكنولوجيا، التفاعلات على وسائل التواصل، التجمعات الصناعية"
            },
            {
                "name_ar": "الألعاب الديناميكية",
                "name_en": "Dynamic Games",
                "types": "Markov Perfect Equilibrium, State Space Models, Learning Models",
                "applications": "استراتيجيات طويلة المدى، التكيف والتعلم، الاستثمار الديناميكي",
                "estimation": "Value Function Iteration, Policy Function Iteration, Machine Learning",
                "examples": "سباق التسلح التكنولوجي، الاستثمار في R&D، استراتيجيات الأسعار الديناميكية"
            },
            {
                "name_ar": "نماذج المعلومات غير المتماثلة",
                "name_en": "Asymmetric Information Models",
                "types": "Signaling Models, Screening Models, Mechanism Design",
                "applications": "تصميم العقود، استراتيجيات التسعير التمييزي، اختيار المعاكس",
                "estimation": "Maximum Likelihood, Bayesian Methods, Simulation-Based",
                "examples": "تسعير التأمين، قروض البنوك، أسواق المستعملين"
            },
            {
                "name_ar": "التعلم المعزز متعدد الوكلاء",
                "name_en": "Multi-Agent Reinforcement Learning",
                "types": "Nash-Q Learning, Multi-Agent Deep Q-Networks, Policy Gradient Methods",
                "applications": "التعلم التكيفي، التحسين التعاوني، المنافسة الخوارزمية",
                "estimation": "Deep Learning, Neural Networks, Game-Theoretic Learning",
                "examples": "التداول الخوارزمي، التسعير التلقائي، المنصات الرقمية"
            }
        ]

        for model in strategic_models:
            st.markdown(f"""
            <div class="ai-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الأنواع:</strong> {model['types']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>طرق التقدير:</strong> {model['estimation']}</p>
                <p><strong>أمثلة عملية:</strong> {model['examples']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab8:
        st.subheader("🌐 اقتصاديات البيانات الضخمة والشبكات")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>💡 قياس اقتصاديات البيانات الضخمة (Econometrics of Big Data)</h4>
        <p>التعامل مع البيانات الاقتصادية الضخمة التي تتجاوز القدرات التقليدية للمعالجة والتحليل</p>
        </div>
        """, unsafe_allow_html=True)

        big_data_models = [
            {
                "name_ar": "القياس الاقتصادي الموزع",
                "name_en": "Distributed Econometrics",
                "description": "تطبيق النماذج الاقتصادية على البيانات الموزعة عبر عدة خوادم",
                "applications": "تحليل البيانات الجغرافية الضخمة، بيانات المعاملات المصرفية، بيانات IoT الاقتصادية",
                "tools": "Apache Spark (PySpark), Hadoop, Dask, Ray",
                "challenges": "تجميع النتائج، التعامل مع البيانات غير المتجانسة"
            },
            {
                "name_ar": "التعلم الآلي للبيانات الضخمة الاقتصادية",
                "name_en": "Machine Learning for Economic Big Data",
                "description": "تطبيق خوارزميات التعلم الآلي على مجموعات البيانات الاقتصادية الضخمة",
                "applications": "تحليل سلوك المستهلك، التنبؤ الاقتصادي الكلي، تحليل أسواق المال",
                "tools": "XGBoost, LightGBM, TensorFlow, PyTorch, H2O.ai",
                "challenges": "تجنب فرط الملائمة، التفسير، الكفاءة الحاسوبية"
            },
            {
                "name_ar": "معالجة البيانات النصية الاقتصادية",
                "name_en": "Economic Text Data Processing",
                "description": "استخراج المؤشرات الاقتصادية من النصوص الضخمة",
                "applications": "تحليل التقارير المالية، الأخبار الاقتصادية، وسائل التواصل الاجتماعي",
                "tools": "NLTK, spaCy, BERT, GPT models, Elasticsearch",
                "challenges": "استخراج المعنى، التحيز اللغوي، المعايرة الزمنية"
            },
            {
                "name_ar": "التحليل الفوري للبيانات الاقتصادية",
                "name_en": "Real-time Economic Data Analysis",
                "description": "تحليل البيانات الاقتصادية في الوقت الفعلي",
                "applications": "مراقبة الأسواق، التنبيهات الاقتصادية، التداول عالي التردد",
                "tools": "Apache Kafka, Apache Storm, Redis, InfluxDB",
                "challenges": "زمن الاستجابة، دقة النتائج الفورية، إدارة الذاكرة"
            }
        ]

        for model in big_data_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الوصف:</strong> {model['description']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
                <p><strong>التحديات:</strong> {model['challenges']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>🕸️ اقتصاديات الشبكات (Network Econometrics)</h4>
        <p>دراسة كيفية تأثير هيكل الشبكات على النتائج الاقتصادية والسلوك الاقتصادي</p>
        </div>
        """, unsafe_allow_html=True)

        network_models = [
            {
                "name_ar": "نماذج الانتشار الاقتصادي",
                "name_en": "Economic Diffusion Models",
                "description": "نمذجة كيفية انتشار المعلومات، التكنولوجيا، أو الأزمات عبر الشبكات الاقتصادية",
                "applications": "انتشار الأزمات المالية، انتشار التكنولوجيا، انتشار السياسات",
                "tools": "NetworkX, igraph, SNAP, Gephi",
                "methods": "SIR Models, Threshold Models, Cascade Models"
            },
            {
                "name_ar": "نماذج التكوين الداخلي للشبكات",
                "name_en": "Endogenous Network Formation Models",
                "description": "نمذجة كيفية تشكيل الشبكات الاقتصادية بناءً على الحوافز الاقتصادية",
                "applications": "تشكيل شبكات التجارة، التحالفات الاستراتيجية، الشبكات المالية",
                "tools": "R (ergm, statnet), Python (networkx), MATLAB",
                "methods": "ERGM, SAOM, Dynamic Network Models"
            },
            {
                "name_ar": "قياس الأثر الشبكي الاقتصادي",
                "name_en": "Network Economic Impact Measurement",
                "description": "قياس كيفية تأثير الموقع في الشبكة على النتائج الاقتصادية",
                "applications": "تأثير الموقع الجغرافي، المركزية في الشبكات المالية، تأثيرات النظراء",
                "tools": "Spatial Econometrics packages, Network Analysis tools",
                "methods": "Network Autocorrelation, Spatial Durbin Models, Network IV"
            },
            {
                "name_ar": "تحليل الشبكات المالية النظامية",
                "name_en": "Systemic Financial Network Analysis",
                "description": "تحليل كيفية انتشار المخاطر عبر الشبكات المالية",
                "applications": "تقييم المخاطر النظامية، مراقبة الاستقرار المالي، تحليل العدوى",
                "tools": "R (systemicrisk), Python (networkx), MATLAB Financial Toolbox",
                "methods": "Contagion Models, Centrality Measures, Stress Testing"
            }
        ]

        for model in network_models:
            st.markdown(f"""
            <div class="ai-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الوصف:</strong> {model['description']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
                <p><strong>الطرق:</strong> {model['methods']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab9:
        st.subheader("💹 النماذج المتقدمة للأسواق المالية")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
        <h4>📈 النماذج المتقدمة لاقتصاديات الأسواق المالية</h4>
        <p>نماذج متطورة لفهم ديناميكيات الأسواق المالية وسلوك الأسعار المعقد</p>
        </div>
        """, unsafe_allow_html=True)

        financial_models = [
            {
                "name_ar": "نماذج البنية الدقيقة للأسواق",
                "name_en": "Market Microstructure Models",
                "types": "Order Flow Models, Market Making Models, High-Frequency Models",
                "applications": "التداول عالي التردد، تحليل السيولة، تكلفة التداول، تأثير السوق",
                "tools": "LOBSTER data, TAQ data, Python (zipline), R (xts, quantmod)",
                "advanced_features": "Hawkes Processes, Point Processes, Machine Learning for Order Flow"
            },
            {
                "name_ar": "نماذج التقلبات الكامنة",
                "name_en": "Latent Volatility Models",
                "types": "Stochastic Volatility Models, Regime-Switching Models, Jump-Diffusion Models",
                "applications": "تسعير المشتقات، إدارة المخاطر، استراتيجيات التداول المتقلبة",
                "tools": "R (stochvol, bssm), Python (pymc3, stan), MATLAB Econometrics",
                "advanced_features": "Particle Filters, Bayesian Estimation, Machine Learning Integration"
            },
            {
                "name_ar": "نماذج الهيكل الزمني لمعدلات الفائدة",
                "name_en": "Term Structure Models",
                "types": "Affine Models, HJM Models, LIBOR Market Models, Nelson-Siegel Models",
                "applications": "تسعير السندات، إدارة مخاطر أسعار الفائدة، استراتيجيات المحفظة",
                "tools": "QuantLib, R (RQuantLib), MATLAB Financial Instruments",
                "advanced_features": "Multi-Factor Models, Machine Learning Calibration, Real-Time Implementation"
            },
            {
                "name_ar": "نماذج المخاطر الائتمانية المهيكلة",
                "name_en": "Structural Credit Risk Models",
                "types": "Merton Models, Reduced-Form Models, Jump-to-Default Models, Network Credit Models",
                "applications": "تسعير CDS، تقييم مخاطر الشركات، محافظ الائتمان، الضمانات المدعومة بالأصول",
                "tools": "Python (quantlib, creditrisk), R (CreditMetrics), Bloomberg API",
                "advanced_features": "Machine Learning Default Prediction, Dynamic Models, Counterparty Risk"
            },
            {
                "name_ar": "نماذج التسعير متعددة الأصول",
                "name_en": "Multi-Asset Pricing Models",
                "types": "Copula Models, Factor Models, Regime-Switching Models, Vine Copulas",
                "applications": "تنويع المحافظ، المشتقات متعددة الأصول، إدارة المخاطر المعقدة",
                "tools": "R (copula, VineCopula), Python (copulas), MATLAB Econometrics",
                "advanced_features": "Dynamic Copulas, Machine Learning Copula Selection, High-Dimensional Models"
            },
            {
                "name_ar": "نماذج السيولة والتمويل",
                "name_en": "Liquidity and Funding Models",
                "types": "Liquidity Risk Models, Funding Valuation Adjustments, XVA Models",
                "applications": "تقييم السيولة، تكلفة التمويل، تعديلات التقييم، إدارة الضمانات",
                "tools": "QuantLib, MATLAB Financial Toolbox, Bloomberg BVAL",
                "advanced_features": "Machine Learning for Liquidity Prediction, Real-Time Risk Management"
            },
            {
                "name_ar": "نماذج التداول الخوارزمي المتقدمة",
                "name_en": "Advanced Algorithmic Trading Models",
                "types": "Optimal Execution Models, Market Impact Models, Portfolio Optimization with Transaction Costs",
                "applications": "الإجراء الأمثل، تقليل تكلفة التداول، التداول عالي التردد",
                "tools": "Python (zipline, backtrader), R (quantstrat), C++ (proprietary)",
                "advanced_features": "Reinforcement Learning, Deep Learning, Multi-Agent Systems"
            },
            {
                "name_ar": "نماذج التمويل السلوكي الكمي",
                "name_en": "Quantitative Behavioral Finance Models",
                "types": "Prospect Theory Models, Behavioral GARCH, Sentiment Models, Herding Models",
                "applications": "تحليل السلوك النفسي، تأثير المشاعر، فقاعات الأسواق، شذوذات التسعير",
                "tools": "Python (behavioral finance packages), R (behavioral models), Text Analytics",
                "advanced_features": "NLP Sentiment Analysis, Social Network Analysis, Machine Learning Psychology"
            }
        ]

        for model in financial_models:
            st.markdown(f"""
            <div class="model-card">
                <h4>{model['name_ar']} / {model['name_en']}</h4>
                <p><strong>الأنواع:</strong> {model['types']}</p>
                <p><strong>التطبيقات:</strong> {model['applications']}</p>
                <p><strong>الأدوات:</strong> {model['tools']}</p>
                <p><strong>الميزات المتقدمة:</strong> {model['advanced_features']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "🤖 الذكاء الاصطناعي والتعلم العميق":
    st.header("🤖 دمج الذكاء الاصطناعي مع القياس الاقتصادي")

    # الذكاء الاصطناعي السببي
    st.subheader("🧠 الذكاء الاصطناعي السببي (Causal AI)")

    causal_ai_models = [
        {
            "name_ar": "التعلم الآلي المزدوج/المصحح التحيز",
            "name_en": "Double/Debiased Machine Learning (DML)",
            "description": "يستخدم التعلم الآلي لنمذجة المتغيرات المزعجة ثم يقدر التأثير السببي من البواقي",
            "libraries": "EconML, DoWhy, CausalML",
            "applications": "قياس تأثير الحملات التسويقية، تقييم السياسات في بيئة عالية الأبعاد"
        },
        {
            "name_ar": "الغابات السببية",
            "name_en": "Causal Forests",
            "description": "امتداد للغابات العشوائية لتقدير التأثيرات العلاجية غير المتجانسة",
            "libraries": "grf (R), EconML (Python)",
            "applications": "الطب الشخصي، التسويق المستهدف، تخصيص السياسات"
        },
        {
            "name_ar": "المتعلمات الفوقية",
            "name_en": "Meta-Learners (S/T/X/R-Learner)",
            "description": "إطارات مختلفة لدمج التعلم الآلي مع التقدير السببي",
            "libraries": "EconML, CausalML",
            "applications": "تحسين الاستهداف، تقدير التأثير التفاضلي، الطب الدقيق"
        }
    ]

    for model in causal_ai_models:
        st.markdown(f"""
        <div class="ai-card">
            <h4>{model['name_ar']} / {model['name_en']}</h4>
            <p><strong>الوصف:</strong> {model['description']}</p>
            <p><strong>المكتبات:</strong> {model['libraries']}</p>
            <p><strong>التطبيقات:</strong> {model['applications']}</p>
        </div>
        """, unsafe_allow_html=True)

    # التعلم العميق في الاقتصاد
    st.subheader("🔥 التعلم العميق في الاقتصاد")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="ai-card">
            <h4>🧠 الشبكات العصبية للتنبؤ الاقتصادي</h4>
            <ul>
                <li><strong>LSTM/GRU:</strong> للسلاسل الزمنية الاقتصادية</li>
                <li><strong>CNN:</strong> لتحليل الصور الاقتصادية (خرائط، رسوم بيانية)</li>
                <li><strong>Transformer:</strong> للتنبؤ متعدد المتغيرات</li>
                <li><strong>VAE/GAN:</strong> لتوليد السيناريوهات الاقتصادية</li>
            </ul>
            <div class="tech-tag">PyTorch</div>
            <div class="tech-tag">TensorFlow</div>
            <div class="tech-tag">Keras</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="ai-card">
            <h4>📊 معالجة اللغات الطبيعية في الاقتصاد</h4>
            <ul>
                <li><strong>BERT/GPT:</strong> تحليل التقارير المالية</li>
                <li><strong>Sentiment Analysis:</strong> مؤشرات المشاعر الاقتصادية</li>
                <li><strong>Topic Modeling:</strong> استخراج المواضيع الاقتصادية</li>
                <li><strong>Named Entity Recognition:</strong> تحديد الكيانات الاقتصادية</li>
            </ul>
            <div class="tech-tag">Transformers</div>
            <div class="tech-tag">spaCy</div>
            <div class="tech-tag">NLTK</div>
        </div>
        """, unsafe_allow_html=True)

    # التعلم المعزز في السياسات الاقتصادية
    st.subheader("🎯 التعلم المعزز في السياسات الاقتصادية")

    rl_applications = [
        {
            "application": "السياسة النقدية الذكية",
            "description": "استخدام Deep Q-Networks لتحديد أسعار الفائدة المثلى",
            "algorithms": "DQN, DDPG, PPO",
            "example": "البنك المركزي الأوروبي يختبر نماذج RL لاتخاذ قرارات السياسة النقدية"
        },
        {
            "application": "السياسة المالية التكيفية",
            "description": "تحسين الإنفاق الحكومي والضرائب باستخدام Multi-Agent RL",
            "algorithms": "MADDPG, QMIX, Multi-Agent Policy Gradient",
            "example": "وزارة المالية الأمريكية تستخدم RL لتحسين توزيع الميزانية"
        },
        {
            "application": "تنظيم الأسواق المالية",
            "description": "مراقبة وتنظيم التداول الخوارزمي والمخاطر النظامية",
            "algorithms": "Actor-Critic Methods, Soft Actor-Critic",
            "example": "هيئة الأوراق المالية تطور نظم RL للكشف عن التلاعب"
        }
    ]

    for app in rl_applications:
        st.markdown(f"""
        <div class="ai-card">
            <h4>🎯 {app['application']}</h4>
            <p><strong>الوصف:</strong> {app['description']}</p>
            <p><strong>الخوارزميات:</strong> {app['algorithms']}</p>
            <p><strong>مثال عملي:</strong> {app['example']}</p>
        </div>
        """, unsafe_allow_html=True)

    # مشروع Microsoft ALICE
    st.subheader("🚀 مشروع Microsoft ALICE: دراسة حالة")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 15px; margin: 1rem 0;">
        <h4>🔬 مشروع ALICE: التعلم الآلي المؤتمت للسببية والاقتصاد</h4>
        <p><strong>الهدف:</strong> دمج الذكاء الاصطناعي مع القياس الاقتصادي لاتخاذ قرارات اقتصادية مؤتمتة</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>🎯 الأهداف الرئيسية</h5>
                <ul>
                    <li>دمج التعلم الآلي مع الاستدلال السببي</li>
                    <li>أتمتة اتخاذ القرارات الاقتصادية المعقدة</li>
                    <li>إضفاء الطابع الديمقراطي على التقنيات التحليلية المتقدمة</li>
                    <li>سد الفجوة بين البحث الأكاديمي والتطبيقات الصناعية</li>
                </ul>
            </div>

            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>🛠️ التقنيات الأساسية</h5>
                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 15px 0;">
                    <span class="tech-tag">مكتبة EconML</span>
                    <span class="tech-tag">Double Machine Learning</span>
                    <span class="tech-tag">Causal Forests</span>
                    <span class="tech-tag">Orthogonal ML</span>
                    <span class="tech-tag">Python SDK</span>
                    <span class="tech-tag">Azure Integration</span>
                </div>
            </div>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 10px; margin: 20px 0;">
            <h5>🚀 التأثير العملي</h5>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
                <div>
                    <h6>🛍️ تحسين التجارة</h6>
                    <p>قياس التأثيرات السببية لاستراتيجيات التسعير على سلوك العملاء</p>
                </div>
                <div>
                    <h6>📊 تحليل السياسات</h6>
                    <p>تقييم فعالية التدخل الحكومي</p>
                </div>
                <div>
                    <h6>🎯 الإسناد التسويقي</h6>
                    <p>فهم العائد الحقيقي للاستثمار في الحملات التسويقية</p>
                </div>
                <div>
                    <h6>🏥 اقتصاديات الصحة</h6>
                    <p>تقييم فعالية العلاج وتحليل التكلفة والعائد</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "💼 الوظائف والمهن":
    st.header("💼 خريطة الوظائف والمهن في القياس الاقتصادي التطبيقي")

    # تحديث البيانات لتشمل النماذج الجديدة
    salary_data = {
        'الوظيفة': [
            'عالم بيانات - استدلال سببي',
            'محلل كمي (Quant)',
            'عالم اقتصادي تطبيقي',
            'متخصص نماذج المزيج التسويقي',
            'محلل مخاطر ائتمانية',
            'محلل تسعير',
            'مستشار اقتصادي',
            'محلل عمليات وتنبؤ',
            'متخصص النماذج عالية الأبعاد',
            'محلل المخاطر المتقدم',
            'محلل التفاعل الاستراتيجي'
        ],
        'الحد_الأدنى': [95, 105, 80, 85, 75, 70, 90, 65, 110, 95, 105],
        'المتوسط': [140, 160, 115, 125, 110, 105, 135, 95, 150, 135, 145],
        'الحد_الأعلى': [200, 250, 170, 180, 150, 140, 210, 130, 185, 160, 175]
    }

    df_salary = pd.DataFrame(salary_data)

    fig = go.Figure()

    # إضافة الأعمدة
    fig.add_trace(go.Bar(
        name='الحد الأدنى',
        x=df_salary['الوظيفة'],
        y=df_salary['الحد_الأدنى'],
        marker_color='lightblue'
    ))

    fig.add_trace(go.Bar(
        name='المتوسط',
        x=df_salary['الوظيفة'],
        y=df_salary['المتوسط'],
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        name='الحد الأعلى',
        x=df_salary['الوظيفة'],
        y=df_salary['الحد_الأعلى'],
        marker_color='darkblue'
    ))

    fig.update_layout(
        title="متوسط الرواتب السنوية (بالألف دولار)",
        xaxis_title="نوع الوظيفة",
        yaxis_title="الراتب السنوي (ألف دولار)",
        barmode='group',
        font=dict(size=12),
        title_x=0.5,
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)

    # الوظائف التفصيلية حسب القطاع
    st.subheader("🏢 الوظائف حسب القطاع")

    # الخدمات المالية
    st.markdown("### 🏦 الخدمات المالية (35% من الفرص)")

    financial_jobs = [
        {
            "title": "محلل كمي (Quantitative Analyst)",
            "title_en": "Quantitative Analyst",
            "salary": "$95K - $180K",
            "skills": "تحليل السلاسل الزمنية، تسعير المشتقات، نمذجة المخاطر",
            "models": "GARCH, VaR, Monte Carlo, Black-Scholes",
            "companies": "Goldman Sachs, JPMorgan, BlackRock, Citadel",
            "growth": "12% سنوياً"
        },
        {
            "title": "متخصص نمذجة المزيج التسويقي",
            "title_en": "Marketing Mix Modeling Specialist",
            "salary": "$90K - $155K",
            "skills": "MMM، Bayesian modeling، Media planning، ROI measurement",
            "models": "Robyn, LightweightMMM, Adstock models, Attribution models",
            "companies": "Meta, Google, P&G, Unilever, Nielsen",
            "growth": "28% سنوياً"
        },
        {
            "title": "محلل مخاطر (Risk Analyst)",
            "title_en": "Risk Analyst",
            "salary": "$80K - $140K",
            "skills": "نمذجة VaR، اختبارات الضغط، الامتثال التنظيمي",
            "models": "Credit Risk Models, Market Risk, Operational Risk",
            "companies": "Wells Fargo, Bank of America, Credit Suisse",
            "growth": "8% سنوياً"
        },
        {
            "title": "مطور نماذج مخاطر ائتمانية",
            "title_en": "Credit Risk Modeler",
            "salary": "$85K - $150K",
            "skills": "نمذجة احتمالية التخلف، IFRS 9، Basel III",
            "models": "PD/LGD/EAD, Survival Analysis, Logistic Regression",
            "companies": "Capital One, American Express, Discover",
            "growth": "10% سنوياً"
        }
    ]

    for job in financial_jobs:
        st.markdown(f"""
        <div class="job-card">
            <h4>{job['title']} / {job['title_en']}</h4>
            <div class="salary-info">
                <strong>الراتب:</strong> {job['salary']} | <strong>النمو:</strong> {job['growth']}
            </div>
            <p><strong>المهارات الأساسية:</strong> {job['skills']}</p>
            <p><strong>النماذج المطلوبة:</strong> {job['models']}</p>
            <p><strong>أمثلة الشركات:</strong> {job['companies']}</p>
        </div>
        """, unsafe_allow_html=True)

    # التكنولوجيا والتجارة الإلكترونية
    st.markdown("### 💻 التكنولوجيا والتجارة الإلكترونية (28% من الفرص)")

    tech_jobs = [
        {
            "title": "عالم بيانات - التجريب",
            "title_en": "Data Scientist - Experimentation",
            "salary": "$120K - $200K",
            "skills": "اختبار A/B، الاستدلال السببي، تصميم التجارب",
            "models": "Causal Inference, Randomized Controlled Trials, Quasi-experiments",
            "companies": "Google, Facebook, Netflix, Uber",
            "growth": "22% سنوياً"
        },
        {
            "title": "محلل تسعير",
            "title_en": "Pricing Analyst",
            "salary": "$85K - $140K",
            "skills": "مرونة الأسعار، التنبؤ بالطلب، التحسين",
            "models": "Demand Systems, Discrete Choice, Dynamic Pricing",
            "companies": "Amazon, Airbnb, Spotify, Adobe",
            "growth": "18% سنوياً"
        },
        {
            "title": "متخصص النماذج عالية الأبعاد",
            "title_en": "High-Dimensional Modeling Specialist",
            "salary": "$110K - $185K",
            "skills": "LASSO, Ridge, Elastic Net, تحليل البيانات الضخمة",
            "models": "Regularized Regression, Dynamic Factor Models, Penalized VAR",
            "companies": "Two Sigma, Renaissance Technologies, D.E. Shaw",
            "growth": "25% سنوياً"
        },
        {
            "title": "محلل المخاطر المتقدم",
            "title_en": "Advanced Risk Analyst",
            "salary": "$95K - $160K",
            "skills": "VaR, CVaR, نماذج التقلب، اختبارات الضغط",
            "models": "GARCH Models, Credit Risk Models, Operational Risk",
            "companies": "Goldman Sachs, Morgan Stanley, Blackstone",
            "growth": "15% سنوياً"
        },
        {
            "title": "محلل التفاعل الاستراتيجي",
            "title_en": "Strategic Interaction Analyst",
            "salary": "$105K - $175K",
            "skills": "نظرية الألعاب، التحليل الهيكلي، اقتصاديات المزادات",
            "models": "Game Theory Models, Auction Models, Network Models",
            "companies": "Google, Amazon, Microsoft, Uber",
            "growth": "20% سنوياً"
        },
        {
            "title": "عالم البيانات الضخمة الاقتصادية",
            "title_en": "Economic Big Data Scientist",
            "salary": "$115K - $190K",
            "skills": "Spark, Hadoop, معالجة البيانات الموزعة، التعلم الآلي على نطاق واسع",
            "models": "Distributed ML, Real-time Analytics, Text Mining",
            "companies": "Netflix, Spotify, Palantir, Two Sigma",
            "growth": "30% سنوياً"
        },
        {
            "title": "محلل الشبكات الاقتصادية",
            "title_en": "Economic Network Analyst",
            "salary": "$95K - $165K",
            "skills": "تحليل الشبكات، NetworkX، نماذج الانتشار، تحليل الشبكات المالية",
            "models": "Network Models, Diffusion Models, Contagion Models",
            "companies": "Federal Reserve, World Bank, JPMorgan, BlackRock",
            "growth": "25% سنوياً"
        },
        {
            "title": "مطور النماذج المالية المتقدمة",
            "title_en": "Advanced Financial Model Developer",
            "salary": "$120K - $210K",
            "skills": "QuantLib، تسعير المشتقات، نماذج التقلب، XVA",
            "models": "Derivatives Pricing, Volatility Models, Market Microstructure",
            "companies": "Goldman Sachs, Citadel, D.E. Shaw, Renaissance Technologies",
            "growth": "18% سنوياً"
        }
    ]

    for job in tech_jobs:
        st.markdown(f"""
        <div class="job-card">
            <h4>{job['title']} / {job['title_en']}</h4>
            <div class="salary-info">
                <strong>الراتب:</strong> {job['salary']} | <strong>النمو:</strong> {job['growth']}
            </div>
            <p><strong>المهارات الأساسية:</strong> {job['skills']}</p>
            <p><strong>النماذج المطلوبة:</strong> {job['models']}</p>
            <p><strong>أمثلة الشركات:</strong> {job['companies']}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🔧 المهارات التقنية المطلوبة":
    st.header("🔧 المهارات التقنية المطلوبة للنجاح في الصناعة")

    # مقارنة المهارات
    st.subheader("📊 أهمية المهارات المختلفة")

    skills_data = {
        'المهارة': [
            'Python/R Programming',
            'SQL & Database Management',
            'Machine Learning',
            'Causal Inference Methods',
            'Data Visualization',
            'Cloud Platforms (AWS/Azure/GCP)',
            'Statistical Software (Stata/SAS)',
            'Version Control (Git)',
            'Business Understanding',
            'Communication Skills',
            'Big Data Processing',
            'Network Analysis',
            'Deep Learning',
            'Financial Modeling',
            'Data Engineering'
        ],
        'الأهمية': [95, 90, 85, 80, 85, 75, 60, 70, 90, 85, 80, 70, 75, 85, 80],
        'الطلب_في_السوق': [90, 85, 95, 70, 80, 80, 50, 65, 85, 80, 85, 65, 90, 80, 75]
    }

    df_skills = pd.DataFrame(skills_data)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_skills['الأهمية'],
        y=df_skills['الطلب_في_السوق'],
        mode='markers+text',
        text=df_skills['المهارة'],
        textposition="top center",
        marker=dict(
            size=15,
            color=df_skills['الأهمية'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="مستوى الأهمية")
        )
    ))

    fig.update_layout(
        title="خريطة المهارات: الأهمية مقابل الطلب في السوق",
        xaxis_title="الأهمية (%)",
        yaxis_title="الطلب في السوق (%)",
        font=dict(size=12),
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

    # تفصيل المهارات التقنية
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["💻 المهارات البرمجية", "📊 المهارات التحليلية", "☁️ المهارات السحابية", "🌐 البيانات الضخمة والشبكات",
         "📈 علم البيانات والتعلم الآلي", "💹 النمذجة المالية المتقدمة"])

    with tab1:
        st.subheader("💻 المهارات البرمجية")
        programming_skills = [
            {
                "skill": "Python for Econometrics",
                "skill_ar": "بايثون للقياس الاقتصادي",
                "libraries": "pandas, numpy, statsmodels, scikit-learn, scipy",
                "specialized": "EconML, DoWhy, CausalML, LinearModels",
                "importance": "حاسمة",
                "learning_time": "3-6 أشهر"
            },
            {
                "skill": "R for Statistical Analysis",
                "skill_ar": "R للتحليل الإحصائي",
                "libraries": "dplyr, ggplot2, tidyverse, caret",
                "specialized": "fixest, did, plm, AER, Robyn",
                "importance": "عالية",
                "learning_time": "2-4 أشهر"
            },
            {
                "skill": "SQL & Database Management",
                "skill_ar": "SQL وإدارة قواعد البيانات",
                "libraries": "PostgreSQL, MySQL, BigQuery, Snowflake",
                "specialized": "Window Functions, CTEs, Query Optimization",
                "importance": "حاسمة",
                "learning_time": "2-3 أشهر"
            }
        ]

        for skill in programming_skills:
            st.markdown(f"""
            <div class="model-card">
                <h4>{skill['skill_ar']} / {skill['skill']}</h4>
                <p><strong>المكتبات الأساسية:</strong> {skill['libraries']}</p>
                <p><strong>المكتبات المتخصصة:</strong> {skill['specialized']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                    <span class="tech-tag">الأهمية: {skill['importance']}</span>
                    <span class="tech-tag">وقت التعلم: {skill['learning_time']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.subheader("📊 المهارات التحليلية")
        analytical_skills = [
            {
                "category": "الاستدلال السببي",
                "methods": "DiD, RDD, IV, SCM, Causal ML",
                "tools": "EconML, DoWhy, CausalImpact",
                "applications": "تقييم السياسات، قياس ROI، A/B Testing"
            },
            {
                "category": "التنبؤ والتوقع",
                "methods": "ARIMA, LSTM, Prophet, State-Space Models",
                "tools": "Prophet, TensorFlow, PyTorch, statsmodels",
                "applications": "تخطيط الطلب، التنبؤ المالي، إدارة المخزون"
            },
            {
                "category": "نمذجة الاختيار والتسعير",
                "methods": "Discrete Choice, Conjoint, Dynamic Pricing",
                "tools": "pylogit, mlogit, scikit-learn",
                "applications": "استراتيجيات التسعير، تطوير المنتجات"
            },
            {
                "category": "نمذجة المزيج التسويقي",
                "methods": "Bayesian MMM, Adstock Models, Media Mix Optimization, Attribution Models",
                "tools": "Robyn (Meta), LightweightMMM (Google), PyMC3, Stan, R (prophet)",
                "applications": "قياس ROI التسويقي، تخصيص الميزانية، تحسين المزيج الإعلامي، قياس التأثير طويل المدى"
            }
        ]

        for skill in analytical_skills:
            st.markdown(f"""
            <div class="ai-card">
                <h4>{skill['category']}</h4>
                <p><strong>الطرق:</strong> {skill['methods']}</p>
                <p><strong>الأدوات:</strong> {skill['tools']}</p>
                <p><strong>التطبيقات:</strong> {skill['applications']}</p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.subheader("☁️ المهارات السحابية")
        cloud_skills = [
            {
                "platform": "Amazon Web Services (AWS)",
                "platform_ar": "خدمات أمازون السحابية",
                "services": "S3, EC2, RDS, Redshift, SageMaker, Lambda",
                "certifications": "AWS Solutions Architect, AWS Data Analytics",
                "market_share": "32%"
            },
            {
                "platform": "Microsoft Azure",
                "platform_ar": "مايكروسوفت أزور",
                "services": "Blob Storage, SQL Database, Machine Learning, Functions",
                "certifications": "Azure Data Scientist Associate, Azure Solutions Architect",
                "market_share": "23%"
            },
            {
                "platform": "Google Cloud Platform (GCP)",
                "platform_ar": "منصة جوجل السحابية",
                "services": "BigQuery, Cloud Storage, AI Platform, Cloud Functions",
                "certifications": "Professional Data Engineer, Professional ML Engineer",
                "market_share": "10%"
            }
        ]

        for platform in cloud_skills:
            st.markdown(f"""
            <div class="model-card">
                <h4>{platform['platform_ar']} / {platform['platform']}</h4>
                <p><strong>الخدمات الرئيسية:</strong> {platform['services']}</p>
                <p><strong>الشهادات المهنية:</strong> {platform['certifications']}</p>
                <span class="tech-tag">حصة السوق: {platform['market_share']}</span>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.subheader("🌐 البيانات الضخمة والشبكات")
        big_data_skills = [
            {
                "category": "معالجة البيانات الضخمة",
                "category_en": "Big Data Processing",
                "tools": "Apache Spark (PySpark), Hadoop, Dask, Ray, Apache Kafka",
                "applications": "تحليل بيانات التجارة الضخمة، معالجة البيانات المالية، تحليل السلوك الاستهلاكي",
                "learning_priority": "عالية جداً"
            },
            {
                "category": "تحليل الشبكات",
                "category_en": "Network Analysis",
                "tools": "NetworkX, igraph, SNAP, Gephi, Cytoscape",
                "applications": "تحليل الشبكات المالية، انتشار المخاطر، التأثيرات الاجتماعية",
                "learning_priority": "عالية"
            },
            {
                "category": "قواعد البيانات الموزعة",
                "category_en": "Distributed Databases",
                "tools": "MongoDB, Cassandra, HBase, Redis, Elasticsearch",
                "applications": "تخزين البيانات المالية، البحث في النصوص الاقتصادية، التحليل الفوري",
                "learning_priority": "متوسطة إلى عالية"
            },
            {
                "category": "الحوسبة السحابية للبيانات الضخمة",
                "category_en": "Cloud Big Data Computing",
                "tools": "AWS EMR, Azure HDInsight, Google Dataflow, Databricks",
                "applications": "تحليل بيانات ضخمة، التعلم الآلي على نطاق واسع، معالجة فورية",
                "learning_priority": "عالية"
            }
        ]

        for skill in big_data_skills:
            st.markdown(f"""
            <div class="ai-card">
                <h4>{skill['category']} / {skill['category_en']}</h4>
                <p><strong>الأدوات:</strong> {skill['tools']}</p>
                <p><strong>التطبيقات:</strong> {skill['applications']}</p>
                <span class="tech-tag">أولوية التعلم: {skill['learning_priority']}</span>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.subheader("📈 علم البيانات والتعلم الآلي")
        data_science_skills = [
            {
                "category": "تحليل البيانات الاستكشافية",
                "category_en": "Exploratory Data Analysis (EDA)",
                "tools": "pandas, numpy, matplotlib, seaborn, plotly, altair",
                "techniques": "Statistical summaries, Data visualization, Missing data analysis, Outlier detection",
                "applications": "فهم البيانات الاقتصادية، اكتشاف الأنماط، تحضير البيانات للنمذجة",
                "importance": "أساسية"
            },
            {
                "category": "هندسة البيانات",
                "category_en": "Data Engineering",
                "tools": "Apache Airflow, Luigi, dbt, Prefect, Docker, Kubernetes",
                "techniques": "ETL/ELT pipelines, Data orchestration, Data quality, Version control",
                "applications": "بناء أنابيب البيانات، أتمتة العمليات، ضمان جودة البيانات",
                "importance": "عالية جداً"
            },
            {
                "category": "التعلم الآلي التطبيقي",
                "category_en": "Applied Machine Learning",
                "tools": "scikit-learn, XGBoost, LightGBM, CatBoost, AutoML tools",
                "techniques": "Feature engineering, Model selection, Cross-validation, Hyperparameter tuning",
                "applications": "التنبؤ الاقتصادي، تصنيف العملاء، كشف الاحتيال، تحليل الائتمان",
                "importance": "عالية جداً"
            },
            {
                "category": "التعلم العميق",
                "category_en": "Deep Learning",
                "tools": "TensorFlow, PyTorch, Keras, Fastai, Hugging Face",
                "techniques": "Neural networks, CNNs, RNNs/LSTMs, Transformers, Transfer learning",
                "applications": "معالجة اللغات الطبيعية، تحليل السلاسل الزمنية، تحليل النصوص المالية",
                "importance": "عالية"
            },
            {
                "category": "MLOps وإدارة دورة حياة النماذج",
                "category_en": "MLOps & Model Lifecycle Management",
                "tools": "MLflow, Kubeflow, DVC, Weights & Biases, Neptune",
                "techniques": "Model versioning, Experiment tracking, Model deployment, Monitoring",
                "applications": "نشر النماذج في الإنتاج، مراقبة الأداء، التحديث التلقائي للنماذج",
                "importance": "عالية"
            },
            {
                "category": "تفسيرية النماذج",
                "category_en": "Model Interpretability (XAI)",
                "tools": "SHAP, LIME, ELI5, Yellowbrick, What-If Tool",
                "techniques": "Feature importance, Partial dependence, Counterfactual explanations",
                "applications": "تفسير القرارات للمنظمين، فهم سلوك النماذج، بناء الثقة",
                "importance": "عالية جداً"
            }
        ]

        for skill in data_science_skills:
            st.markdown(f"""
            <div class="model-card">
                <h4>{skill['category']} / {skill['category_en']}</h4>
                <p><strong>الأدوات:</strong> {skill['tools']}</p>
                <p><strong>التقنيات:</strong> {skill['techniques']}</p>
                <p><strong>التطبيقات:</strong> {skill['applications']}</p>
                <span class="tech-tag">الأهمية: {skill['importance']}</span>
            </div>
            """, unsafe_allow_html=True)

    with tab6:
        st.subheader("💹 النمذجة المالية المتقدمة")
        financial_modeling_skills = [
            {
                "category": "نمذجة المخاطر المتقدمة",
                "category_en": "Advanced Risk Modeling",
                "tools": "QuantLib, RiskMetrics, MATLAB Financial Toolbox, R (rugarch, rmgarch)",
                "techniques": "Monte Carlo simulation, Copula modeling, Extreme value theory, Stress testing",
                "applications": "VaR/CVaR، نماذج التقلبات، مخاطر الائتمان، اختبارات الضغط",
                "regulations": "Basel III, IFRS 9, CECL, Solvency II"
            },
            {
                "category": "تسعير المشتقات المعقدة",
                "category_en": "Complex Derivatives Pricing",
                "tools": "QuantLib, Bloomberg API, MATLAB, C++/Python implementations",
                "techniques": "Finite difference methods, Monte Carlo methods, Fourier methods, Calibration",
                "applications": "خيارات متعددة الأصول، مقايضات الائتمان، منتجات هيكلية، خيارات حقيقية",
                "regulations": "FRTB, SA-CCR, CVA/DVA/FVA"
            },
            {
                "category": "التداول الكمي والتنفيذ الأمثل",
                "category_en": "Quantitative Trading & Optimal Execution",
                "tools": "zipline, backtrader, QuantConnect, TradingView APIs, Custom C++",
                "techniques": "TWAP/VWAP, Implementation shortfall, Market impact models, Signal processing",
                "applications": "استراتيجيات التداول، التنفيذ الأمثل، التداول عالي التردد، إدارة المحافظ",
                "regulations": "MiFID II, Reg NMS, Best Execution"
            },
            {
                "category": "نماذج السيولة والتمويل",
                "category_en": "Liquidity & Funding Models",
                "tools": "Bloomberg API, Reuters Eikon, QuantLib, Custom implementations",
                "techniques": "Liquidity risk metrics, Funding costs, XVA calculations, Collateral optimization",
                "applications": "إدارة السيولة، تكلفة التمويل، تعديلات التقييم، إدارة الضمانات",
                "regulations": "Basel III LCR/NSFR, BCBS guidelines"
            },
            {
                "category": "التمويل السلوكي الكمي",
                "category_en": "Quantitative Behavioral Finance",
                "tools": "Python NLP libraries, R behavioral packages, Alternative data APIs",
                "techniques": "Sentiment analysis, Social network analysis, Behavioral biases modeling",
                "applications": "تحليل المشاعر السوقية، نماذج الفقاعات، شذوذات التسعير، تأثير القطيع",
                "regulations": "Market manipulation detection, Fair dealing"
            }
        ]

        for skill in financial_modeling_skills:
            st.markdown(f"""
            <div class="job-card">
                <h4>{skill['category']} / {skill['category_en']}</h4>
                <p><strong>الأدوات:</strong> {skill['tools']}</p>
                <p><strong>التقنيات:</strong> {skill['techniques']}</p>
                <p><strong>التطبيقات:</strong> {skill['applications']}</p>
                <p><strong>اللوائح التنظيمية:</strong> {skill['regulations']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "🌍 التطبيقات العملية":
    st.header("🌍 التطبيقات العملية للقياس الاقتصادي في القطاعات المختلفة")

    # رسم بياني للتطبيقات حسب القطاع
    st.subheader("📊 توزيع التطبيقات حسب القطاع")

    # تحديث بيانات القطاعات لتشمل المجالات الجديدة
    applications_data = {
        'القطاع': ['الخدمات المالية', 'التكنولوجيا', 'الحكومة', 'الصحة', 'التجارة', 'الطاقة', 'المخاطر المتقدمة',
                   'التفاعل الاستراتيجي'],
        'عدد_التطبيقات': [245, 198, 156, 134, 167, 89, 145, 112],
        'متوسط_الاستثمار': [2.5, 3.2, 1.8, 2.1, 1.9, 2.8, 3.8, 4.2]
    }

    df_apps = pd.DataFrame(applications_data)

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('عدد التطبيقات', 'متوسط الاستثمار (مليون دولار)'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )

    fig.add_trace(
        go.Bar(x=df_apps['القطاع'], y=df_apps['عدد_التطبيقات'],
               marker_color='lightblue', name='عدد التطبيقات'),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df_apps['القطاع'], y=df_apps['متوسط_الاستثمار'],
               marker_color='orange', name='متوسط الاستثمار'),
        row=1, col=2
    )

    fig.update_layout(
        title_text="التطبيقات والاستثمار في القياس الاقتصادي حسب القطاع",
        title_x=0.5,
        font=dict(size=12)
    )

    st.plotly_chart(fig, use_container_width=True)

    # تطبيقات تفصيلية
    st.subheader("💼 التطبيقات التفصيلية حسب القطاع")

    sector_applications = {
        "🏦 الخدمات المالية": {
            "applications": [
                {
                    "name": "إدارة مخاطر الائتمان",
                    "name_en": "Credit Risk Management",
                    "models": "Logistic Regression, Survival Analysis, Machine Learning",
                    "description": "تقدير احتمالية التخلف عن السداد وتحسين قرارات الإقراض",
                    "roi": "25-40% تحسن في دقة التنبؤ"
                },
                {
                    "name": "كشف الاحتيال",
                    "name_en": "Fraud Detection",
                    "models": "Anomaly Detection, Deep Learning, Network Analysis",
                    "description": "تحديد المعاملات المشبوهة في الوقت الفعلي",
                    "roi": "60% تقليل في الخسائر"
                },
                {
                    "name": "التداول الخوارزمي",
                    "name_en": "Algorithmic Trading",
                    "models": "Time Series, Reinforcement Learning, High-Frequency Models",
                    "description": "تطوير استراتيجيات التداول المؤتمتة",
                    "roi": "15-20% عائد إضافي"
                }
            ]
        },
        "📱 التسويق والإعلان الرقمي": {
            "applications": [
                {
                    "name": "نمذجة المزيج التسويقي المتقدمة",
                    "name_en": "Advanced Marketing Mix Modeling",
                    "models": "Bayesian MMM, Robyn, LightweightMMM, Hierarchical Models",
                    "description": "قياس وتحسين تأثير جميع القنوات التسويقية على المبيعات والتحويلات",
                    "roi": "30-50% تحسن في كفاءة الإنفاق التسويقي"
                },
                {
                    "name": "نماذج الإسناد متعددة اللمسات",
                    "name_en": "Multi-Touch Attribution Models",
                    "models": "Algorithmic Attribution, Shapley Value, Markov Chain Attribution",
                    "description": "فهم مساهمة كل نقطة اتصال في رحلة العميل نحو التحويل",
                    "roi": "20-35% تحسن في تخصيص الميزانية"
                },
                {
                    "name": "تحليل التشبع والعوائد المتناقصة",
                    "name_en": "Saturation & Diminishing Returns Analysis",
                    "models": "Hill Saturation Models, S-curve Analysis, Adstock Models",
                    "description": "تحديد النقاط المثلى للإنفاق وتجنب الإفراط في الاستثمار",
                    "roi": "15-25% تحسن في الكفاءة الإعلانية"
                },
                {
                    "name": "قياس الأثر التراكمي والمتأخر",
                    "name_en": "Carryover & Long-term Impact Measurement",
                    "models": "Geometric Adstock, Convolutional Adstock, Media Memory Models",
                    "description": "قياس التأثيرات طويلة المدى للحملات التسويقية والبناء التراكمي للعلامة التجارية",
                    "roi": "10-20% قيمة إضافية مكتشفة من التأثيرات طويلة المدى"
                },
                {
                    "name": "تحليل التفاعلات بين القنوات",
                    "name_en": "Cross-Channel Interaction Analysis",
                    "models": "Interaction Effects Models, Synergy Analysis, Media Ecosystem Models",
                    "description": "فهم كيفية تفاعل القنوات المختلفة وتعزيز بعضها البعض",
                    "roi": "12-18% زيادة من تحسين التآزر بين القنوات"
                },
                {
                    "name": "تحسين الميزانية التسويقية",
                    "name_en": "Marketing Budget Optimization",
                    "models": "Constrained Optimization, Genetic Algorithms, Gradient-based Optimization",
                    "description": "تخصيص الميزانية الأمثل عبر القنوات لتحقيق أقصى عائد",
                    "roi": "25-40% تحسن في العائد الإجمالي للاستثمار التسويقي"
                }
            ]
        },
        "💻 التكنولوجيا والمنصات الرقمية": {
            "applications": [
                {
                    "name": "التسعير الديناميكي",
                    "name_en": "Dynamic Pricing",
                    "models": "Multi-Armed Bandits, Reinforcement Learning, Price Elasticity",
                    "description": "تحسين الأسعار بناءً على الطلب والمنافسة",
                    "roi": "10-15% زيادة في الإيرادات"
                },
                {
                    "name": "أنظمة التوصية",
                    "name_en": "Recommendation Systems",
                    "models": "Collaborative Filtering, Deep Learning, Causal Inference",
                    "description": "تحسين تجربة المستخدم وزيادة المبيعات",
                    "roi": "20-30% زيادة في المشاركة"
                },
                {
                    "name": "تحليل تأثير الميزات الجديدة",
                    "name_en": "Feature Impact Analysis",
                    "models": "A/B Testing, Difference-in-Differences, Causal ML",
                    "description": "قياس تأثير الميزات الجديدة على مقاييس الأداء",
                    "roi": "30% تحسن في اتخاذ القرارات"
                },
                {
                    "name": "نمذجة المزيج التسويقي للمنصات الرقمية",
                    "name_en": "Digital Platform Marketing Mix Modeling",
                    "models": "Bayesian MMM, Multi-touch Attribution, Cross-platform Analytics",
                    "description": "قياس وتحسين الإنفاق التسويقي عبر القنوات الرقمية المتعددة",
                    "roi": "25-40% تحسن في ROI التسويقي"
                }
            ]
        },
        "🏛️ القطاع الحكومي والسياسات العامة": {
            "applications": [
                {
                    "name": "تقييم السياسات الاقتصادية",
                    "name_en": "Economic Policy Evaluation",
                    "models": "Difference-in-Differences, RDD, Synthetic Control",
                    "description": "قياس تأثير السياسات على المؤشرات الاقتصادية",
                    "roi": "تحسن 40% في فعالية السياسات"
                },
                {
                    "name": "تحليل تكلفة-عائد البرامج الاجتماعية",
                    "name_en": "Social Program Cost-Benefit Analysis",
                    "models": "Program Evaluation, Randomized Controlled Trials",
                    "description": "تقييم الجدوى الاقتصادية للبرامج الاجتماعية",
                    "roi": "25% تحسن في تخصيص الموارد"
                }
            ]
        },
        "🎯 التفاعلات الاستراتيجية والمزادات": {
            "applications": [
                {
                    "name": "تحليل المنافسة الاستراتيجية",
                    "name_en": "Strategic Competition Analysis",
                    "models": "Game Theory Models, Entry Games, Dynamic Competition",
                    "description": "فهم استراتيجيات المنافسين وتحسين القرارات التنافسية",
                    "roi": "15-25% تحسن في حصة السوق"
                },
                {
                    "name": "تصميم وتحليل المزادات",
                    "name_en": "Auction Design and Analysis",
                    "models": "First-Price Auctions, Multi-Unit Auctions, Mechanism Design",
                    "description": "تحسين عوائد المزادات الرقمية والحكومية",
                    "roi": "20-35% زيادة في الإيرادات"
                },
                {
                    "name": "تحليل تأثيرات الشبكة",
                    "name_en": "Network Effects Analysis",
                    "models": "Network Econometrics, Social Interaction Models",
                    "description": "قياس كيفية انتشار المنتجات عبر الشبكات الاجتماعية",
                    "roi": "30% تحسن في استراتيجيات النمو"
                }
            ]
        },
        "📊 البيانات عالية الأبعاد والتمويل الكمي": {
            "applications": [
                {
                    "name": "نمذجة المحافظ عالية الأبعاد",
                    "name_en": "High-Dimensional Portfolio Modeling",
                    "models": "LASSO, Ridge, Elastic Net, Factor Models",
                    "description": "بناء محافظ استثمارية مع آلاف الأصول",
                    "roi": "10-20% تحسن في نسبة شارب"
                },
                {
                    "name": "كشف الأنماط في البيانات المالية",
                    "name_en": "Financial Pattern Detection",
                    "models": "Regularized Regression, Dynamic Factor Models",
                    "description": "اكتشاف إشارات التداول من آلاف المؤشرات",
                    "roi": "25% تحسن في دقة التنبؤ"
                }
            ]
        },
        "⚠️ إدارة المخاطر المتقدمة": {
            "applications": [
                {
                    "name": "إدارة مخاطر السوق المتكاملة",
                    "name_en": "Integrated Market Risk Management",
                    "models": "VaR, CVaR, GARCH Models, Stress Testing",
                    "description": "إدارة شاملة لمخاطر السوق مع اختبارات الضغط",
                    "roi": "30% تقليل في خسائر التداول"
                },
                {
                    "name": "نمذجة المخاطر الائتمانية المتقدمة",
                    "name_en": "Advanced Credit Risk Modeling",
                    "models": "PD/LGD/EAD Models, Survival Analysis, Machine Learning",
                    "description": "تحسين دقة تقدير مخاطر الائتمان",
                    "roi": "40% تحسن في دقة التنبؤ بالتخلف"
                }
            ]
        },
        "🌐 البيانات الضخمة والتحليلات المتقدمة": {
            "applications": [
                {
                    "name": "تحليل البيانات الاقتصادية الضخمة",
                    "name_en": "Big Economic Data Analysis",
                    "models": "Distributed Computing, Spark ML, Deep Learning on Big Data",
                    "description": "استخراج الأنماط الاقتصادية من مليارات المعاملات والتفاعلات",
                    "roi": "45% تحسن في دقة التنبؤات الاقتصادية"
                },
                {
                    "name": "تحليل الشبكات الاقتصادية والمالية",
                    "name_en": "Economic & Financial Network Analysis",
                    "models": "Network Econometrics, Graph Neural Networks, Diffusion Models",
                    "description": "فهم كيفية انتشار المخاطر والفرص عبر الشبكات الاقتصادية",
                    "roi": "35% تحسن في إدارة المخاطر النظامية"
                },
                {
                    "name": "معالجة النصوص الاقتصادية والمالية",
                    "name_en": "Economic & Financial Text Processing",
                    "models": "NLP, BERT, GPT models, Sentiment Analysis",
                    "description": "استخراج المؤشرات الاقتصادية من الأخبار والتقارير والوسائط الاجتماعية",
                    "roi": "25% تحسن في التنبؤ بتحركات الأسواق"
                }
            ]
        },
        "💹 النمذجة المالية المتطورة": {
            "applications": [
                {
                    "name": "تسعير المشتقات المعقدة",
                    "name_en": "Complex Derivatives Pricing",
                    "models": "Stochastic Volatility Models, Jump-Diffusion, Copula Models",
                    "description": "تطوير نماذج تسعير متطورة للمنتجات المالية المعقدة",
                    "roi": "20-30% تحسن في دقة التسعير"
                },
                {
                    "name": "التداول الخوارزمي المتقدم",
                    "name_en": "Advanced Algorithmic Trading",
                    "models": "Reinforcement Learning, Market Microstructure, Optimal Execution",
                    "description": "تطوير استراتيجيات تداول ذكية ونماذج التنفيذ الأمثل",
                    "roi": "15-25% تحسن في الأداء التجاري"
                },
                {
                    "name": "إدارة المخاطر المتكاملة",
                    "name_en": "Integrated Risk Management",
                    "models": "Multi-Asset Risk Models, Stress Testing, Machine Learning Risk",
                    "description": "بناء أنظمة شاملة لإدارة جميع أنواع المخاطر المالية",
                    "roi": "40% تقليل في الخسائر غير المتوقعة"
                }
            ]
        }
    }

    for sector, data in sector_applications.items():
        st.markdown(f"#### {sector}")

        for app in data["applications"]:
            st.markdown(f"""
            <div class="model-card">
                <h4>{app['name']} / {app['name_en']}</h4>
                <p><strong>النماذج المستخدمة:</strong> {app['models']}</p>
                <p><strong>الوصف:</strong> {app['description']}</p>
                <span class="tech-tag">العائد على الاستثمار: {app['roi']}</span>
            </div>
            """, unsafe_allow_html=True)

elif page == "📚 التوصيات والمسار المهني":
    st.header("📚 التوصيات والمسار المهني للانتقال من الأكاديميا إلى الصناعة")

    # خطة انتقالية مفصلة
    st.subheader("🗓️ خطة الانتقال المهني (12 شهر)")

    phases = [
        {
            "phase": "المرحلة الأولى: الأساسيات والأدوات",
            "duration": "3-4 أشهر",
            "goals": [
                "إتقان Python للتحليل الاقتصادي",
                "تعلم SQL وإدارة قواعد البيانات",
                "إعداد بيئة العمل (Git, Docker, Cloud)",
                "بناء 3-5 مشاريع محفظة أساسية"
            ],
            "resources": [
                "Python for Econometrics (Online Courses)",
                "SQL Fundamentals (Coursera, edX)",
                "Git/GitHub Tutorials",
                "AWS/Azure Free Tier"
            ]
        },
        {
            "phase": "المرحلة الثانية: التخصص والتطبيق",
            "duration": "4-5 أشهر",
            "goals": [
                "التعمق في تقنيات التعلم الآلي",
                "إتقان نماذج الاستدلال السببي",
                "الحصول على شهادات مهنية",
                "بناء مشاريع صناعية واقعية"
            ],
            "resources": [
                "EconML, CausalML Documentation",
                "Causal Inference: The Mixtape (Book)",
                "AWS/Azure/GCP Certifications",
                "Kaggle Competitions"
            ]
        },
        {
            "phase": "المرحلة الثالثة: التطبيق والشبكات المهنية",
            "duration": "4-5 أشهر",
            "goals": [
                "اكتساب الخبرة العملية (تدريب/استشارة)",
                "تطوير المهارات القيادية والتواصلية",
                "بناء شبكة مهنية قوية",
                "إعداد استراتيجية البحث عن عمل"
            ],
            "resources": [
                "LinkedIn Learning (Communication Skills)",
                "Industry Conferences and Meetups",
                "Professional Networking Events",
                "Mock Interviews and Resume Reviews"
            ]
        }
    ]

    for i, phase in enumerate(phases, 1):
        st.markdown(f"""
        <div class="ai-card">
            <h4>📅 {phase['phase']}</h4>
            <p><strong>المدة:</strong> {phase['duration']}</p>

            <h5>🎯 الأهداف:</h5>
            <ul>
                {"".join(f"<li>{goal}</li>" for goal in phase['goals'])}
            </ul>

            <h5>📖 المصادر المقترحة:</h5>
            <ul>
                {"".join(f"<li>{resource}</li>" for resource in phase['resources'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # أفكار مشاريع المحفظة
    st.subheader("💼 أفكار مشاريع المحفظة المهنية")

    portfolio_projects = [
        {
            "title": "نموذج المزيج التسويقي للتجارة الإلكترونية المتقدم",
            "title_en": "Advanced E-commerce Marketing Mix Model",
            "description": "بناء نموذج بايزي شامل لقياس تأثير جميع القنوات التسويقية مع نمذجة التشبع والتأخير",
            "skills": "Bayesian Modeling, Marketing Analytics, ROI Optimization, Media Planning",
            "tools": "Python, Robyn (Meta), LightweightMMM, PyMC3, Tableau, Google Analytics API",
            "deliverables": "نموذج MMM مُدرَّب، لوحة تحكم ROI تفاعلية، تقرير توصيات إعادة تخصيص الميزانية، نموذج تحسين الإنفاق"
        },
        {
            "title": "تقييم أثر السياسة باستخدام الفروق في الفروق",
            "title_en": "Policy Impact Evaluation using Difference-in-Differences",
            "description": "تحليل تأثير سياسة اقتصادية باستخدام التقنيات الحديثة لـ DiD",
            "skills": "Causal Inference, Policy Analysis, Statistical Testing",
            "tools": "R (fixest), Python (linearmodels), Stata",
            "deliverables": "تقرير سياسي، رسوم بيانية للتأثيرات، اختبارات الحساسية"
        },
        {
            "title": "نظام التنبؤ بالطلب متعدد المستويات",
            "title_en": "Hierarchical Demand Forecasting System",
            "description": "بناء نظام تنبؤ للطلب على مستوى SKU مع تحسين سياسات المخزون",
            "skills": "Time Series Analysis, Hierarchical Modeling, Inventory Optimization",
            "tools": "Python (Prophet, scikit-learn), SQL, Tableau",
            "deliverables": "API للتنبؤ، لوحة تحكم، سياسة أمان المخزون الموصى بها"
        },
        {
            "title": "نموذج تسعير ديناميكي بالتعلم المعزز",
            "title_en": "Dynamic Pricing with Reinforcement Learning",
            "description": "تطوير نظام تسعير ذكي يتكيف مع ظروف السوق",
            "skills": "Reinforcement Learning, Dynamic Pricing, Real-time Analytics",
            "tools": "Python (Stable-Baselines3), TensorFlow, FastAPI",
            "deliverables": "نموذج تسعير مُدرَّب، محاكي السوق، API للتطبيق"
        },
        {
            "title": "تحليل التفاعل الاستراتيجي في الأسواق",
            "title_en": "Strategic Market Interaction Analysis",
            "description": "نمذجة كيفية تأثير قرارات الشركات على بعضها البعض",
            "skills": "Game Theory, Structural Estimation, Competition Analysis",
            "tools": "Python (PyGame), R (games), MATLAB Game Theory Toolbox",
            "deliverables": "محاكي التفاعل الاستراتيجي، تحليل التوازن، توصيات الاستراتيجية"
        },
        {
            "title": "نظام إدارة المخاطر المتكامل",
            "title_en": "Integrated Risk Management System",
            "description": "بناء نظام شامل لإدارة أنواع مختلفة من المخاطر المالية",
            "skills": "VaR, CVaR, GARCH, Credit Risk, Operational Risk",
            "tools": "Python (scipy, arch), R (rugarch), Risk Metrics",
            "deliverables": "لوحة مخاطر شاملة، تقارير تنظيمية، نماذج اختبار الضغط"
        },
        {
            "title": "تحليل البيانات عالية الأبعاد للاستثمار",
            "title_en": "High-Dimensional Investment Analysis",
            "description": "استخدام تقنيات التقييد لبناء محافظ من آلاف الأصول",
            "skills": "LASSO, Ridge, Factor Models, Portfolio Optimization",
            "tools": "Python (scikit-learn, cvxpy), R (glmnet), Portfolio Analytics",
            "deliverables": "نموذج اختيار المحفظة، تحليل المخاطر، تقرير الأداء"
        },
        {
            "title": "منصة تحليل الشبكات الاقتصادية",
            "title_en": "Economic Networks Analysis Platform",
            "description": "بناء منصة لتحليل انتشار المخاطر والفرص عبر الشبكات الاقتصادية",
            "skills": "Network Analysis, Graph Neural Networks, Visualization",
            "tools": "Python (NetworkX, PyTorch Geometric), D3.js, Neo4j",
            "deliverables": "منصة تفاعلية، نماذج انتشار، تقارير المخاطر النظامية"
        },
        {
            "title": "نظام معالجة البيانات الاقتصادية الضخمة",
            "title_en": "Big Economic Data Processing System",
            "description": "بناء نظام موزع لمعالجة وتحليل البيانات الاقتصادية الضخمة",
            "skills": "Apache Spark, Distributed Computing, Real-time Processing",
            "tools": "PySpark, Kafka, Elasticsearch, Docker, Kubernetes",
            "deliverables": "نظام معالجة موزع، واجهات برمجة التطبيقات، لوحات تحكم فورية"
        },
        {
            "title": "محرك تسعير المشتقات المتقدمة",
            "title_en": "Advanced Derivatives Pricing Engine",
            "description": "تطوير محرك تسعير للمنتجات المالية المعقدة باستخدام النماذج المتقدمة",
            "skills": "Quantitative Finance, Monte Carlo Methods, Stochastic Calculus",
            "tools": "QuantLib, Python (numpy, scipy), C++ optimization",
            "deliverables": "محرك تسعير، واجهة برمجية، تقارير دقة النموذج"
        },
        {
            "title": "نظام كشف الأنماط السلوكية في الأسواق",
            "title_en": "Market Behavioral Patterns Detection System",
            "description": "استخدام معالجة اللغات الطبيعية والتعلم الآلي لكشف الأنماط السلوكية",
            "skills": "NLP, Sentiment Analysis, Behavioral Finance, Deep Learning",
            "tools": "Python (transformers, spaCy), TensorFlow, Alternative Data APIs",
            "deliverables": "نموذج كشف الأنماط، مؤشرات المشاعر، تنبؤات السوق"
        }
    ]

    for project in portfolio_projects:
        st.markdown(f"""
        <div class="model-card">
            <h4>{project['title']} / {project['title_en']}</h4>
            <p><strong>الوصف:</strong> {project['description']}</p>
            <p><strong>المهارات المكتسبة:</strong> {project['skills']}</p>
            <p><strong>الأدوات:</strong> {project['tools']}</p>
            <p><strong>المخرجات:</strong> {project['deliverables']}</p>
        </div>
        """, unsafe_allow_html=True)

    # إضافة قسم جديد للمسارات المهنية المتخصصة
    st.subheader("🎓 المسارات المهنية المتخصصة الجديدة")

    specialized_paths = [
        {
            "path": "عالم البيانات الاقتصادية الضخمة",
            "path_en": "Economic Big Data Scientist",
            "duration": "18-24 شهر",
            "skills": [
                "Apache Spark & PySpark",
                "Distributed Computing (Dask, Ray)",
                "Cloud Platforms (AWS, Azure, GCP)",
                "Real-time Processing (Kafka, Storm)",
                "NoSQL Databases (MongoDB, Cassandra)",
                "Machine Learning at Scale"
            ],
            "certifications": [
                "Databricks Certified Associate Developer",
                "AWS Certified Big Data - Specialty",
                "Google Professional Data Engineer"
            ],
            "expected_salary": "$115K - $190K"
        },
        {
            "path": "محلل الشبكات الاقتصادية",
            "path_en": "Economic Networks Analyst",
            "duration": "12-18 شهر",
            "skills": [
                "Network Analysis (NetworkX, igraph)",
                "Graph Neural Networks",
                "Social Network Analysis",
                "Spatial Econometrics",
                "Visualization (D3.js, Gephi)",
                "Complex Systems Theory"
            ],
            "certifications": [
                "Network Analysis Specialization (Coursera)",
                "Graph Analytics Certificate",
                "Complex Systems Certificate"
            ],
            "expected_salary": "$95K - $165K"
        },
        {
            "path": "مطور النماذج المالية المتقدمة",
            "path_en": "Advanced Financial Models Developer",
            "duration": "24-30 شهر",
            "skills": [
                "Quantitative Finance (QuantLib)",
                "Derivatives Pricing Models",
                "Risk Management (VaR, CVaR)",
                "High-Performance Computing",
                "Financial Regulations Knowledge",
                "C++/Python for Finance"
            ],
            "certifications": [
                "CQF (Certificate in Quantitative Finance)",
                "FRM (Financial Risk Manager)",
                "PRM (Professional Risk Manager)"
            ],
            "expected_salary": "$120K - $210K"
        },
        {
            "path": "متخصص نمذجة المزيج التسويقي",
            "path_en": "Marketing Mix Modeling Specialist",
            "duration": "15-20 شهر",
            "skills": [
                "Bayesian Statistics & Modeling",
                "Marketing Analytics & Attribution",
                "Media Planning & Optimization",
                "Advanced MMM Tools (Robyn, LightweightMMM)",
                "Statistical Software (R, Python, Stan)",
                "Business Intelligence & Visualization"
            ],
            "certifications": [
                "Google Analytics Individual Qualification",
                "Meta Marketing Science Certification",
                "Marketing Analytics Certificate (UC Davis)",
                "Bayesian Statistics Specialization"
            ],
            "expected_salary": "$90K - $155K"
        }
    ]

    for path in specialized_paths:
        st.markdown(f"""
        <div class="ai-card">
            <h4>{path['path']} / {path['path_en']}</h4>
            <p><strong>مدة التخصص:</strong> {path['duration']}</p>
            <p><strong>الراتب المتوقع:</strong> {path['expected_salary']}</p>

            <h5>المهارات الأساسية:</h5>
            <ul>
                {"".join(f"<li>{skill}</li>" for skill in path['skills'])}
            </ul>

            <h5>الشهادات الموصى بها:</h5>
            <ul>
                {"".join(f"<li>{cert}</li>" for cert in path['certifications'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # المكتبات والأدوات المتخصصة الجديدة
    st.subheader("📦 المكتبات والأدوات المتخصصة للنماذج المتقدمة")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="ai-card">
            <h4>📊 البيانات عالية الأبعاد</h4>
            <h5>Python:</h5>
            <ul>
                <li>scikit-learn (LASSO, Ridge, Elastic Net)</li>
                <li>statsmodels (regularized regression)</li>
                <li>cvxpy (convex optimization)</li>
                <li>sklearn.feature_selection</li>
            </ul>
            <h5>R:</h5>
            <ul>
                <li>glmnet (regularized regression)</li>
                <li>lars (least angle regression)</li>
                <li>hdm (high-dimensional metrics)</li>
                <li>BigVAR (large VAR models)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="ai-card">
            <h4>⚠️ نمذجة المخاطر</h4>
            <h5>Python:</h5>
            <ul>
                <li>arch (GARCH models)</li>
                <li>scipy.stats (risk distributions)</li>
                <li>pyfolio (portfolio risk analytics)</li>
                <li>quantlib (derivatives pricing)</li>
            </ul>
            <h5>R:</h5>
            <ul>
                <li>rugarch (GARCH models)</li>
                <li>rmgarch (multivariate GARCH)</li>
                <li>RiskPortfolios (portfolio risk)</li>
                <li>VaR (value at risk)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="ai-card">
            <h4>🎯 التفاعل الاستراتيجي</h4>
            <h5>Python:</h5>
            <ul>
                <li>nashpy (game theory)</li>
                <li>gambit (game analysis)</li>
                <li>networkx (network games)</li>
                <li>mesa (agent-based modeling)</li>
            </ul>
            <h5>R:</h5>
            <ul>
                <li>RGameTheory (game theory tools)</li>
                <li>igraph (network analysis)</li>
                <li>spatstat (spatial games)</li>
                <li>games (strategic games)</li>
            </ul>
            <h5>Specialized:</h5>
            <ul>
                <li>MATLAB Game Theory Toolbox</li>
                <li>Gambit Software Suite</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # الشهادات المهنية الموصى بها
    st.subheader("🏆 الشهادات المهنية الموصى بها")

    certifications = [
        {
            "category": "شهادات التكنولوجيا السحابية",
            "certs": [
                "AWS Certified Data Analytics - Specialty",
                "Microsoft Azure Data Scientist Associate",
                "Google Professional Data Engineer",
                "Databricks Certified Associate Developer"
            ]
        },
        {
            "category": "شهادات التحليل والبيانات",
            "certs": [
                "SAS Certified Statistical Business Analyst",
                "Tableau Desktop Specialist/Certified Associate",
                "Microsoft Power BI Data Analyst Associate",
                "Alteryx Designer Core Certification"
            ]
        },
        {
            "category": "شهادات الذكاء الاصطناعي والتعلم الآلي",
            "certs": [
                "Google Professional Machine Learning Engineer",
                "AWS Certified Machine Learning - Specialty",
                "Microsoft Azure AI Engineer Associate",
                "IBM Data Science Professional Certificate"
            ]
        }
    ]

    for cert_category in certifications:
        st.markdown(f"""
        <div class="ai-card">
            <h4>{cert_category['category']}</h4>
            <ul>
                {"".join(f"<li>{cert}</li>" for cert in cert_category['certs'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # الكتب والمصادر التعليمية
    st.subheader("📖 المكتبة المرجعية الأساسية")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="model-card">
            <h4>📚 كتب الاستدلال السببي</h4>
            <ul>
                <li>"Causal Inference: The Mixtape" - Scott Cunningham</li>
                <li>"Causal Inference for Statistics" - Pearl, Glymour, Jewell</li>
                <li>"Mostly Harmless Econometrics" - Angrist & Pischke</li>
                <li>"The Effect" - Nick Huntington-Klein</li>
                <li>"Impact Evaluation in Practice" - Gertler et al.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>🤖 كتب الذكاء الاصطناعي والتعلم الآلي</h4>
            <ul>
                <li>"Hands-On Machine Learning" - Aurélien Géron</li>
                <li>"Python for Data Analysis" - Wes McKinney</li>
                <li>"Deep Learning" - Ian Goodfellow</li>
                <li>"Reinforcement Learning: An Introduction" - Sutton & Barto</li>
                <li>"Pattern Recognition and Machine Learning" - Bishop</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # خطة الشبكات المهنية
    st.subheader("🤝 استراتيجية بناء الشبكة المهنية")

    networking_strategy = [
        {
            "platform": "LinkedIn",
            "strategy": "إنشاء ملف شخصي قوي، نشر محتوى تقني، التفاعل مع خبراء الصناعة",
            "time_investment": "1-2 ساعات أسبوعياً"
        },
        {
            "platform": "GitHub",
            "strategy": "نشر مشاريع المحفظة، المساهمة في المشاريع مفتوحة المصدر",
            "time_investment": "3-5 ساعات أسبوعياً"
        },
        {
            "platform": "مؤتمرات وفعاليات الصناعة",
            "strategy": "حضور PyData, Data Science conferences, Economic conferences",
            "time_investment": "2-4 فعاليات سنوياً"
        },
        {
            "platform": "المجتمعات المهنية",
            "strategy": "الانضمام لـ Kaggle, Stack Overflow, Reddit communities",
            "time_investment": "2-3 ساعات أسبوعياً"
        }
    ]

    for strategy in networking_strategy:
        st.markdown(f"""
        <div class="job-card">
            <h4>{strategy['platform']}</h4>
            <p><strong>الاستراتيجية:</strong> {strategy['strategy']}</p>
            <span class="tech-tag">الاستثمار الزمني: {strategy['time_investment']}</span>
        </div>
        """, unsafe_allow_html=True)

    # نصائح للمقابلات الشخصية
    st.subheader("💼 نصائح للمقابلات الشخصية في الصناعة")

    st.markdown("""
    <div class="ai-card">
        <h4>🎯 الاستعداد للمقابلات التقنية</h4>

        <h5>أسئلة الاستدلال السببي الشائعة:</h5>
        <ul>
            <li>متى تستخدم DiD بدلاً من RDD؟</li>
            <li>ما هي افتراضات Parallel Trends وكيف تختبرها؟</li>
            <li>اشرح الفرق بين التأثير السببي والارتباط مع مثال عملي</li>
            <li>كيف تتعامل مع المتغيرات المربكة غير المرصودة؟</li>
        </ul>

        <h5>أسئلة التطبيق العملي:</h5>
        <ul>
            <li>كيف تقيس تأثير حملة تسويقية على المبيعات؟</li>
            <li>صمم تجربة لاختبار فعالية ميزة جديدة</li>
            <li>كيف تبني نموذج تنبؤ للطلب مع البيانات المفقودة؟</li>
            <li>اشرح كيف تتعامل مع البيانات غير المتوازنة في نماذج التصنيف</li>
        </ul>

        <h5>أسئلة التواصل والأعمال:</h5>
        <ul>
            <li>كيف تشرح نتائج نموذج معقد لمدير غير تقني؟</li>
            <li>ما هي المقاييس الرئيسية لقياس نجاح مشروع تحليل البيانات؟</li>
            <li>كيف تحدد أولويات المشاريع في بيئة موارد محدودة؟</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # خلاصة التوصيات
    st.subheader("🎯 خلاصة التوصيات الرئيسية")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); color: white; padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h4>💡 المبادئ الأساسية للنجاح</h4>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>🎓 التعلم المستمر</h5>
                <p>تابع أحدث التطورات في القياس الاقتصادي والذكاء الاصطناعي. الصناعة تتطور بسرعة.</p>
            </div>

            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>💼 التطبيق العملي</h5>
                <p>ركز على حل مشاكل الأعمال الحقيقية. النظرية مهمة ولكن التطبيق هو ما يهم الصناعة.</p>
            </div>

            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>🗣️ التواصل الفعال</h5>
                <p>تعلم كيف تترجم النتائج التقنية إلى رؤى عملية قابلة للتنفيذ.</p>
            </div>

            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h5>🤝 بناء الشبكات</h5>
                <p>الشبكة المهنية القوية أساسية للنجاح في الانتقال من الأكاديميا للصناعة.</p>
            </div>
        </div>

        <div style="text-align: center; margin-top: 2rem; font-size: 1.2rem; font-weight: bold;">
            "النجاح في صناعة القياس الاقتصادي يتطلب دمج الدقة الأكاديمية مع البراغماتية التجارية والكفاءة التقنية"
        </div>
    </div>
    """, unsafe_allow_html=True)

# الخاتمة
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; margin: 2rem 0;">
    <h3>📊 تقرير شامل: نماذج القياس الاقتصادي التطبيقية</h3>
    <p style="font-size: 1.1rem; margin: 1rem 0;">إعداد: الدكتور مروان رودان</p>
    <p style="margin: 1rem 0;">هذا التقرير يقدم خريطة طريق شاملة للانتقال من الأكاديميا إلى التطبيق العملي في عالم القياس الاقتصادي</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">آخر تحديث: 2025</p>
</div>
""", unsafe_allow_html=True)