import cv2
import os


def resize_img(h: int = 100, v: int=100, dir_images_to_resize: str='resized_images'):
    """
    h - кол-во писелей по горизонтали,
    v - по вертикали
    dir_images_to_resize - имя папки в какую сохранить переработаные фотографии
    """

    if not os.path.exists(dir_images_to_resize + '/'):
        os.mkdir(dir_images_to_resize + '/')
    list_images = os.listdir("resize_all_images/")
    for image in list_images:
        img = cv2.imread(f"resize_all_images/{image}",1)
        resize_image = cv2.resize(img, (h, v))
        if not os.path.exists(f"{dir_images_to_resize}/resize_{image}"):
            cv2.imwrite(f"{dir_images_to_resize}/resize_{image}", resize_image)
        else:
            print(f"Image {image} already been resized")

if __name__ == '__main__':
    resize_img(h=100, v=200, dir_images_to_resize='pypa')

# Решение учителя
# import cv2
# import glob

# images=glob.glob("*.jpg")

# for image in images:
    # img=cv2.imread(image,0)
    # re=cv2.resize(img,(100,100))
    # cv2.imshow("Hey",re)
    # cv2.waitKey(500)
    # cv2.destroyAllWindows()
    # cv2.imwrite("resized_"+image,re)
