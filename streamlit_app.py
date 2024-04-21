import streamlit as st
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def ocr_app():
    st.title("Aplicación de OCR con Streamlit")

    st.sidebar.title("Configuración")
    threshold = st.sidebar.slider("Umbral de binarización", min_value=0, max_value=255, value=150)

    uploaded_image = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png", "gif"])

    if uploaded_image is not None:
        st.subheader("Imagen original:")
        st.image(uploaded_image, caption="Imagen original", use_column_width=True)

        # Agregar botón para extraer texto
        if st.button("Extraer texto"):
            # Cargar la imagen
            img = Image.open(uploaded_image)

            # Convertir a escala de grises y mejorar el contraste
            img_gray = ImageEnhance.Contrast(img.convert('L')).enhance(2.0)

            # Aplicar filtro para reducir el ruido
            img_smooth = img_gray.filter(ImageFilter.SMOOTH)

            # Binarización de la imagen
            img_bin = img_smooth.point(lambda p: p > threshold and 255)

            # Realizar OCR en la imagen preprocesada
            text = pytesseract.image_to_string(img_bin, lang='spa', config='--psm 6')

            # Mostrar el texto extraído
            st.subheader("Texto extraído:")
            st.text(text)

ocr_app()
