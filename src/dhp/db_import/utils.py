def clean_text(text):
    return text.strip()


def student_code_format(text):
    return clean_text(text).split(' ')[0]