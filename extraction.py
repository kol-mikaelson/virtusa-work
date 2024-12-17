import easyocr


def extract_text(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    return result

def skew_correct(image):
    from jdeskew.estimator import get_angle
    angle = get_angle(image)

    from jdeskew.utility import rotate
    output_image = rotate(image, angle)
    return output_image
