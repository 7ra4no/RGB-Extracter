from skimage import io
import glob
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def rgb_extractor(image_path):
    # Read image
    image = io.imread(image_path)
    # Split into RGB components
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    # Sum of luminance values by RGB
    red_p = np.sum(red)
    green_p = np.sum(green)
    blue_p = np.sum(blue)
    # Graph setting
    plt.rcParams['font.family'] = "Hiragino Maru Gothic Pro"
    fig = plt.figure()
    # RGB histogram
    ax1 = fig.add_subplot(1,2,1,title='RGBヒストグラム')
    # luminance histogram *comment out*
    # ax1 = plt.hist(image.ravel(), bins = 256, color = 'orange', )
    ax1 = plt.hist(red.ravel(), bins = np.arange(256), color = 'red', alpha = 0.4,rwidth=1)
    ax1 = plt.hist(green.ravel(), bins = np.arange(256), color = 'Green', alpha = 0.4,rwidth=1)
    ax1 = plt.hist(blue.ravel(), bins = np.arange(256), color = 'Blue', alpha = 0.4,rwidth=1)
    ax1 = plt.xlabel('輝度値')
    ax1 = plt.ylabel('画素数')
    ax1 = plt.legend(['赤', '緑', '青'])
    # File path splitting
    savepath = image_path.split('/')
    # Subject image
    ax2 = fig.add_subplot(2,2,2)
    ax2 = plt.title(savepath[1], y=-0.25)
    ax2 = plt.imshow(image)
    ax2 = plt.xticks([])
    ax2 = plt.yticks([])
    # Total luminance value by RGB
    ax3 = fig.add_subplot(2,2,4,title='RGB別合計輝度値')
    x = [1,2,3]
    y = [blue_p,green_p,red_p]
    y_max = max(y)
    label_x = ["青","緑","赤"]
    y_ = [0,y_max]
    label_y = ["0",str(y_max)]
    colorlist = ["b","g","r"]
    ax3 = plt.barh(x,y,color=colorlist)
    ax3 = plt.xlabel('画素毎の合計輝度値')
    ax3 = plt.ylabel('色の種類')
    ax3 = plt.yticks(x, label_x)
    ax3 = plt.xticks(y_, label_y)
    # Graph layout
    fig.set_figheight(4)
    fig.set_figwidth(8)
    fig.tight_layout()
    # Debug
    print(savepath)
    # Save graph
    fig.savefig(savepath[0]+"/color_detect/"+savepath[1]+"_color.png",dpi=500, bbox_inches='tight',pad_inches = 0.05)
    # Memory allocation
    plt.clf()
    plt.close()
    return

def main():
    # Image folder
    imgfold_path = glob.glob("sinbi-image/*.png")
    for i in range(len(imgfold_path)):
        rgb_extractor(imgfold_path[i])

if __name__ == "__main__":
    main()
