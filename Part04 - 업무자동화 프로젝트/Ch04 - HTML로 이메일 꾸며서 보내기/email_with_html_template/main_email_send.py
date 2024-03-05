import os

from libs.email_sender import EmailSender

if __name__ == '__main__':
    es = EmailSender("크리드", "polozh@naver.com", os.getenv("MY_NAVER_PASSWORD"),
                     template_file_name="templates/email_template1.html")
    es.send_all_emails("sample_with_name.xlsx")
