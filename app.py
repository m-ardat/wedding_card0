# ИМПОРТ БИБЛИОТЕК
import streamlit as st

# КОНФИГУРАЦИЯ ПРИЛОЖЕНИЯ
st.set_page_config(
    page_title="Happy Birthday Card",
    page_icon=":material/featured_seasonal_and_gifts:",
    layout="wide",
    menu_items=None
)

# ОФОРМЛЕНИЕ
st.markdown(
    """
    <style>    
    /* НАСТРОЙКИ ШРИФТА */
    /* Изменение цвета текста и шрифта в label */
    [data-testid="stWidgetLabel"] {
        font-size: 14px;                        /* Размер текста */
        font-family: 'Helvetica', sans-serif;   /* Шрифт текста */
    }

    /* Изменение шрифта */
    bodybody, h1, h2, h3, h4, h5, h6, p, div, span, li, a, blockquote, pre, code {
        font-family: 'Helvetica', sans-serif;
    }
    .st-emotion-cache-16tyu1 h1, 
    .st-emotion-cache-16tyu1 h2, 
    .st-emotion-cache-16tyu1 h3, 
    .st-emotion-cache-16tyu1 h4, 
    .st-emotion-cache-16tyu1 h5, 
    .st-emotion-cache-16tyu1 h6, 
    .st-emotion-cache-102y9h7 h1, 
    .st-emotion-cache-102y9h7 h2, 
    .st-emotion-cache-102y9h7 h3, 
    .st-emotion-cache-102y9h7 h4, 
    .st-emotion-cache-102y9h7 h5, 
    .st-emotion-cache-102y9h7 h6,
    .st-emotion-cache-16tyu1 td {
        font-family: 'Helvetica', sans-serif;
    }   

    /* Скрыть кнопку увеличение изображения */
    .st-emotion-cache-z56u96 {
        display: none;
    }
    
    /* Скрыть якорь заголовка */
    .st-emotion-cache-gi0tri {
        display: none !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

#ФРОНТ
# Заголовок
st.markdown("""
<h1 style="text-align: center; 
           margin: -81px 0 15px 0;   /* top, right, bottom, left */
           color: #2e2e2e; 
           font-family: 'Helvetica', sans-serif; 
           font-size: 4rem;
           font-weight: bold;">
    С днём свадьбы! 🎉
</h1>
""", unsafe_allow_html=True)

text = """Дорогие Денис и Юля! 

Сегодня вы вступаете в новый этап вашей жизни, и пусть он будет полон любви, взаимопонимания и уважения! Желаем вам всегда поддерживать друг друга и делиться радостью. Пусть ваша жизнь будет наполнена не только счастливыми моментами, но и мудростью, которая поможет преодолевать любые преграды.

Создавайте свою уникальную историю, где каждый из вас будет не только партнером, но и лучшим другом. Сегодня вы написали новую главу в книге вашей жизни. Пусть эта книга окажется изумительным романом - впечатляющим и завораживающим с каждой новой страницей!

С любовью, Максим и Алина"""

# URL изображения
image_url = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2xibW1zMDZwbTJsbms4YnRrcTJ0ZWE2dDY2b3llbG9tZnh4bjJnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hgQQQg35t2veHJr9Ww/giphy.gif"

col1, col2 = st.columns([3,7])

with col1:
    # Отображение изображения
    st.image(image_url, use_container_width=None)
with col2:
    st.markdown(f"""
            <div 
                style="background-color: #FFFAFA; 
                padding: 20px; 
                border-radius: 8px; 
                text-align: left; 
                font-style: italic; 
                color: #2E2E2E;
                white-space: pre-line;
                margin: 0;">
                {text}
            """, unsafe_allow_html=True)
