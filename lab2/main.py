from PIL import Image
import numpy as np
import math
from scipy import stats


def relative_entropy(img1, img2):
    hist1 = np.array(img1.histogram())
    hist2 = np.array(img2.histogram())

    rel_entropy = stats.entropy(pk=hist2, qk=hist1, base=2)

    return rel_entropy


if __name__ == '__main__':

    file_extension = '.jpg'
    img_color = Image.open('image' + file_extension)

    if img_color.mode != 'RGB':
        img = img_color.convert('RGB')

    img_gray = img_color.convert('L')
    img_gray.save('image_gray' + file_extension)

    if img_gray.getextrema()[1] - img_gray.getextrema()[0] < 64:
        print("Image has less than 64 grads")
        exit(0)
    else:
        print("Кількість градацій:", img_gray.getextrema()[1] - img_gray.getextrema()[0])

    print("Висота зображення:", img_gray.height, ", його ширина:", img_gray.width)

    entropy = img_gray.entropy()
    print("Ентропія початкового зображення:", entropy)

    # Дискретизація зображення з кроком 2
    img_discrete_2 = img_gray.copy()
    img_discrete_2 = img_discrete_2.resize((img_discrete_2.width//2, img_discrete_2.height//2), resample=Image.BOX)
    img_discrete_2.save('img_discrete_2' + file_extension)
    print("Висота дискретизованого з кроком 2 зображення:", img_discrete_2.height, ", ширина:", img_discrete_2.width)

    # Дискретизація зображення з кроком 4
    img_discrete_4 = img_gray.copy()
    img_discrete_4 = img_discrete_4.resize((img_discrete_4.width//4, img_discrete_4.height//4), resample=Image.BOX)
    img_discrete_4.save('img_discrete_4' + file_extension)
    print("Висота дискретизованого з кроком 4 зображення:", img_discrete_4.height, ", ширина:", img_discrete_4.width)

    # Квантування img_gray на 8, 16, та 64 рівнів
    img_quant_8 = img_gray.quantize(8).convert("L")
    img_quant_8.save('img_quant_8' + file_extension)
    img_quant_16 = img_gray.quantize(16).convert("L")
    img_quant_16.save('img_quant_16' + file_extension)
    img_quant_64 = img_gray.quantize(64).convert("L")
    img_quant_64.save('img_quant_64' + file_extension)

    # Квантування img_discrete_2 на 8, 16, та 64 рівнів
    img_discrete_2_quant_8 = img_discrete_2.quantize(8).convert("L")
    img_discrete_2_quant_8.save('img_discrete_2_quant_8' + file_extension)
    img_discrete_2_quant_16 = img_discrete_2.quantize(16).convert("L")
    img_discrete_2_quant_16.save('img_discrete_2_quant_16' + file_extension)
    img_discrete_2_quant_64 = img_discrete_2.quantize(64).convert("L")
    img_discrete_2_quant_64.save('img_discrete_2_quant_64' + file_extension)

    # Квантування img_discrete_4 на 8, 16, та 64 рівнів
    img_discrete_4_quant_8 = img_discrete_4.quantize(8).convert("L")
    img_discrete_4_quant_8.save('img_discrete_4_quant_8' + file_extension)
    img_discrete_4_quant_16 = img_discrete_4.quantize(16).convert("L")
    img_discrete_4_quant_16.save('img_discrete_4_quant_16' + file_extension)
    img_discrete_4_quant_64 = img_discrete_4.quantize(64).convert("L")
    img_discrete_4_quant_64.save('img_discrete_4_quant_64' + file_extension)

    # обчислення ентропії
    print("Ентропія початкового зображення, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 8 рівнів:", img_quant_8.entropy())

    print("Ентропія початкового зображення, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 16 рівнів:", img_quant_16.entropy())

    print("Ентропія початкового зображення, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 64 рівні:", img_quant_64.entropy())

    print("Ентропія зображення, дискретизованого з кроком 2:", img_discrete_2.entropy())
    print("Ентропія зображення, дискретизованого з кроком 4:", img_discrete_4.entropy())

    print("Ентропія зображення, дискретизованого з кроком 2, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 8 рівнів:", img_discrete_2_quant_8.entropy())

    print("Ентропія зображення, дискретизованого з кроком 2, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 16 рівнів:", img_discrete_2_quant_16.entropy())

    print("Ентропія зображення, дискретизованого з кроком 2, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 64 рівні:", img_discrete_2_quant_64.entropy())

    print("Ентропія зображення, дискретизованого з кроком 4, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 8 рівнів:", img_discrete_4_quant_8.entropy())

    print("Ентропія зображення, дискретизованого з кроком 4, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 16 рівнів:", img_discrete_4_quant_16.entropy())

    print("Ентропія зображення, дискретизованого з кроком 4, для якого проведено"
          "рівномірне квантування діапазону яскравостей зображення на 64 рівні:", img_discrete_4_quant_64.entropy())

    # відновлення зображень після дискретизації
    nearest_neighbor_img_discrete_2 = img_discrete_2.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_2 = img_discrete_2.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_2 = img_discrete_2.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_4 = img_discrete_4.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_4 = img_discrete_4.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_4 = img_discrete_4.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_2_quant_8 = img_discrete_2_quant_8.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_2_quant_8 = img_discrete_2_quant_8.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_2_quant_8 = img_discrete_2_quant_8.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_2_quant_16 = img_discrete_2_quant_16.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_2_quant_16 = img_discrete_2_quant_16.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_2_quant_16 = img_discrete_2_quant_16.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_2_quant_64 = img_discrete_2_quant_64.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_2_quant_64 = img_discrete_2_quant_64.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_2_quant_64 = img_discrete_2_quant_64.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_4_quant_8 = img_discrete_4_quant_8.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_4_quant_8 = img_discrete_4_quant_8.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_4_quant_8 = img_discrete_4_quant_8.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_4_quant_16 = img_discrete_4_quant_16.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_4_quant_16 = img_discrete_4_quant_16.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_4_quant_16 = img_discrete_4_quant_16.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    nearest_neighbor_img_discrete_4_quant_64 = img_discrete_4_quant_64.resize((img_gray.width, img_gray.height), resample=Image.NEAREST)
    bilinear_img_discrete_4_quant_64 = img_discrete_4_quant_64.resize((img_gray.width, img_gray.height), resample=Image.BILINEAR)
    bicubic_img_discrete_4_quant_64 = img_discrete_4_quant_64.resize((img_gray.width, img_gray.height), resample=Image.BICUBIC)

    # збереження відновлених зображень
    nearest_neighbor_img_discrete_2.save('nearest_neighbor_img_discrete_2' + file_extension)
    bilinear_img_discrete_2.save('bilinear_img_discrete_2' + file_extension)
    bicubic_img_discrete_2.save('bicubic_img_discrete_2' + file_extension)

    nearest_neighbor_img_discrete_4.save('nearest_neighbor_img_discrete_4' + file_extension)
    bilinear_img_discrete_4.save('bilinear_img_discrete_4' + file_extension)
    bicubic_img_discrete_4.save('bicubic_img_discrete_4' + file_extension)

    nearest_neighbor_img_discrete_2_quant_8.save('nearest_neighbor_img_discrete_2_quant_8' + file_extension)
    bilinear_img_discrete_2_quant_8.save('bilinear_img_discrete_2_quant_8' + file_extension)
    bicubic_img_discrete_2_quant_8.save('bicubic_img_discrete_2_quant_8' + file_extension)

    nearest_neighbor_img_discrete_2_quant_16.save('nearest_neighbor_img_discrete_2_quant_16' + file_extension)
    bilinear_img_discrete_2_quant_16.save('bilinear_img_discrete_2_quant_16' + file_extension)
    bicubic_img_discrete_2_quant_16.save('bicubic_img_discrete_2_quant_16' + file_extension)

    nearest_neighbor_img_discrete_2_quant_64.save('nearest_neighbor_img_discrete_2_quant_64' + file_extension)
    bilinear_img_discrete_2_quant_64.save('bilinear_img_discrete_2_quant_64' + file_extension)
    bicubic_img_discrete_2_quant_64.save('bicubic_img_discrete_2_quant_64' + file_extension)

    nearest_neighbor_img_discrete_4_quant_8.save('nearest_neighbor_img_discrete_4_quant_8' + file_extension)
    bilinear_img_discrete_4_quant_8.save('bilinear_img_discrete_4_quant_8' + file_extension)
    bicubic_img_discrete_4_quant_8.save('bicubic_img_discrete_4_quant_8' + file_extension)

    nearest_neighbor_img_discrete_4_quant_16.save('nearest_neighbor_img_discrete_4_quant_16' + file_extension)
    bilinear_img_discrete_4_quant_16.save('bilinear_img_discrete_4_quant_16' + file_extension)
    bicubic_img_discrete_4_quant_16.save('bicubic_img_discrete_4_quant_16' + file_extension)

    nearest_neighbor_img_discrete_4_quant_64.save('nearest_neighbor_img_discrete_4_quant_64' + file_extension)
    bilinear_img_discrete_4_quant_64.save('bilinear_img_discrete_4_quant_64' + file_extension)
    bicubic_img_discrete_4_quant_64.save('bicubic_img_discrete_4_quant_64' + file_extension)

    # обрахуємо відносні ентропії зображень
    print("Розрахуємо ентропію наступних зображень відносно початкового:")

    print()
    print("проквантованого на 8 рівнів:", relative_entropy(img_gray, img_quant_8))
    print("проквантованого на 16 рівнів:", relative_entropy(img_gray, img_quant_16))
    print("проквантованого на 64 рівні:", relative_entropy(img_gray, img_quant_64))

    print()
    print("дискретизованого з кроком 2:", relative_entropy(img_gray, img_discrete_2))
    print("дискретизованого з кроком 4:", relative_entropy(img_gray, img_discrete_4))

    print()
    print("крок дискретизації: 2; рівнів квантування 8", relative_entropy(img_gray, img_discrete_2_quant_8))
    print("крок дискретизації: 2; рівнів квантування 16", relative_entropy(img_gray, img_discrete_2_quant_16))
    print("крок дискретизації: 2; рівнів квантування 64", relative_entropy(img_gray, img_discrete_2_quant_64))

    print()
    print("крок дискретизації: 4; рівнів квантування 8", relative_entropy(img_gray, img_discrete_4_quant_8))
    print("крок дискретизації: 4; рівнів квантування 16", relative_entropy(img_gray, img_discrete_4_quant_16))
    print("крок дискретизації: 4; рівнів квантування 64", relative_entropy(img_gray, img_discrete_4_quant_64))

    print()
    print("дискретизованого з кроком 2"
          "та відновленого методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_2))
    print("дискретизованого з кроком 2"
          "та відновленого методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_2))
    print("дискретизованого з кроком 2"
          "та відновленого методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_2))

    print()
    print("дискретизованого з кроком 4"
          "та відновленого методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_4))
    print("дискретизованого з кроком 4"
          "та відновленого методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_4))
    print("дискретизованого з кроком 4"
          "та відновленого методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_4))

    print()
    print("крок дискретизації: 2; рівнів квантування 8;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_2_quant_8))
    print("крок дискретизації: 2; рівнів квантування 8;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_2_quant_8))
    print("крок дискретизації: 2; рівнів квантування 8;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_2_quant_8))

    print()
    print("крок дискретизації: 2; рівнів квантування 16;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_2_quant_16))
    print("крок дискретизації: 2; рівнів квантування 16;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_2_quant_16))
    print("крок дискретизації: 2; рівнів квантування 16;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_2_quant_16))

    print()
    print("крок дискретизації: 2; рівнів квантування 64;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_2_quant_64))
    print("крок дискретизації: 2; рівнів квантування 64;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_2_quant_64))
    print("крок дискретизації: 2; рівнів квантування 64;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_2_quant_64))

    print()
    print("крок дискретизації: 4; рівнів квантування 8;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_4_quant_8))
    print("крок дискретизації: 4; рівнів квантування 8;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_4_quant_8))
    print("крок дискретизації: 4; рівнів квантування 8;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_4_quant_8))

    print()
    print("крок дискретизації: 4; рівнів квантування 16;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_4_quant_16))
    print("крок дискретизації: 4; рівнів квантування 16;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_4_quant_16))
    print("крок дискретизації: 4; рівнів квантування 16;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_4_quant_16))

    print()
    print("крок дискретизації: 4; рівнів квантування 64;"
          "відновлено методом найближчого сусіда", relative_entropy(img_gray, nearest_neighbor_img_discrete_4_quant_64))
    print("крок дискретизації: 4; рівнів квантування 64;"
          " відновлено методом білінійної інтерполяції", relative_entropy(img_gray, bilinear_img_discrete_4_quant_64))
    print("крок дискретизації: 4; рівнів квантування 64;"
          "та відновлено методом бікубічної інтерполяції", relative_entropy(img_gray, bicubic_img_discrete_4_quant_64))
