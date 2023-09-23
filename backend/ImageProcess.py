from cv2 import Mat, imread , imwrite
import numpy as np

# 520x500
star: Mat = imread("./assets/star.png")


def create_frame(input: Mat, star_num: int) -> Mat:
    """
    """
    w, h = 1200, 900

    w_s, h_s = 200, 200
    # Scaleは1200:900を想定
    resized_img = input.resize((1200, 900))

    resized_star = star.resize((200, 200))

    x_offset = 30
    y_offset = 30
    for i in range(star_num):
        x_pos = w - x_offset*(i+1)
        y_pos = h - y_offset
        resized_img[y_pos-h_s:y_pos,  x_pos-w_s:x_pos] = resized_star

    return resized_img

def test():
    src = imread("./src/chiikawa.jpg")
    frame = create_frame(src,3)
    imwrite("./dist/chiiawa.png",frame)


test()