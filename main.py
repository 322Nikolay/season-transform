import cv2
import numpy as np


def autumn_to_summer(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)

    # Маска осенних оттенков (желто-оранжевые)
    mask = ((h > 10) & (h < 40))

    # Переводим оттенки в зеленые
    h[mask] = 60  # зелёный оттенок
    s[mask] = np.clip(s[mask] + 40, 0, 255)
    v[mask] = np.clip(v[mask] + 20, 0, 255)

    new_hsv = cv2.merge([h, s, v])
    return cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)


def summer_to_autumn(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)

    # Маска зеленых оттенков
    mask = ((h > 35) & (h < 85))

    # Переводим в желто-оранжевые
    h[mask] = 25
    s[mask] = np.clip(s[mask] + 30, 0, 255)
    v[mask] = np.clip(v[mask] - 20, 0, 255)

    new_hsv = cv2.merge([h, s, v])
    return cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)


def main():
    photo1 = cv2.imread("Photo1.jpg")  # осень
    photo2 = cv2.imread("Photo2.jpg")  # лето

    if photo1 is None or photo2 is None:
        print("Ошибка загрузки изображений")
        return

    summer_version = autumn_to_summer(photo1)
    autumn_version = summer_to_autumn(photo2)

    cv2.imwrite("Photo1_to_summer.jpg", summer_version)
    cv2.imwrite("Photo2_to_autumn.jpg", autumn_version)

    print("Готово! Файлы сохранены.")


if __name__ == "__main__":
    main()
