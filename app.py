import streamlit as st
from PIL import Image
import base64
from io import BytesIO


st.set_page_config(page_title="فوتو - ساحل طلایی",page_icon="logo.png")


with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)


def main():
    cv1, cv2 = st.columns(2)

    with cv1:
        st.image('logo.png',width=200)

        

        c1,c2 = st.columns(2)
        with c1:
     # st.markdown(f'<a href="tel:{phone_number}">{phone_number}</a>', unsafe_allow_html=True)
            st.markdown("[شمار ه تماس](tel:989025342900)")
    
    

        with c2:
            st.write("جهت رزرو (هتل ساحل طلایی) تماس بگیرید")
    
    with cv2:
        st.title("فوتو - ساحل طلایی")


    st.divider()
    st.write("تغییر سایز عکس با فوتو قشمی خیلی سریع و آسان")

    # بارگذاری تصویر
    uploaded_image = st.file_uploader("تصویر را انتخاب کنید", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # باز کردن تصویر با استفاده از PIL
        image = Image.open(uploaded_image)

        # نمایش تصویر قبل از بزرگنمایی
        st.subheader("تصویر قبل از بزرگنمایی")
        st.image(image, use_column_width=True)

        # بزرگنمایی تصویر
        width = st.slider("عرض تصویر (پیکسل)", 100, 2000, 500)
        height = st.slider("ارتفاع تصویر (پیکسل)", 100, 2000, 500)
        resized_image = image.resize((width, height))

        # نمایش تصویر بعد از بزرگنمایی
        st.subheader("تصویر بعد از بزرگنمایی")
        st.image(resized_image, use_column_width=True)

        # دکمه دانلود تصویر بزرگنمایی شده
        download_button(resized_image)

def download_button(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="resized_image.png">دانلود تصویر ویرایش شده</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

st.divider()

st.markdown("[ساخته شده توسط عبدالله چلاسی](https://abdollahchelasi.streamlit.app/)")
