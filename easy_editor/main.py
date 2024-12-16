import os

from PyQt5.QtWidgets import(
    QApplication, QWidget, QFileDialog, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget
)
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from PIL import Image

from PIL import ImageFilter

from PIL.ImageFilter import(
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask
)

app = QApplication([])

app.setStyleSheet("""
                  QWidget{
                     background: DarkMagenta; 
                  }
                  QFileDialog {
                      background-color: gray;
                      border-radius: 7px;
                      border: 3px solid green;
                      font-family: EB Garamond;
                      font-size: 20px;
                      color: white;
                   }
                   QPushButton {
                      background-color: PaleVioletRed;
                      border-radius: 10px;
                      border: 3px HotPink;
                      font-family: EB Garamond;
                      font-size: 25px;
                      color: black;
                      
                  }
                  QListWidget {
                    background-color: LightSteelBlue;
                    border-radius: 10px;
                    border: 3px solid black;
                    font-family: EB Garamond;
                    font-size: 25px;
                    color: black;
                  }
                  QLable {
                    background-color: LightSteelBlue;
                    border-radius: 10px;
                    border: 3px solid black;
                    font-family: EB Garamond;
                    font-size: 20px;
                    color: black;
                      
                   }
                  
                  """)





win = QWidget()
win.resize(800, 600)
win.setWindowTitle('Easy Editor')

lb_image = QLabel('Image')
btn_dir = QPushButton('Choose Folder')
lw_files = QListWidget()

btn_left = QPushButton('Previous Image')
btn_right = QPushButton('Next Image')
btn_flip = QPushButton('Flip Image')
btn_sharp = QPushButton('Sharp Image')
btn_bw = QPushButton('Be Image')

btn_blur = QPushButton("Blur")
btn_contuor = QPushButton("Contuor")
btn_detail = QPushButton("Detail")
btn_smooth = QPushButton("Smooth")
btn_edge_enchance = QPushButton("Edge_enchance")

btn_edge_enchance_more = QPushButton("Edge_enchance_more")
btn_emboss = QPushButton("Emboss")
btn_find_edges = QPushButton("Find_edges")
btn_smooth_more = QPushButton("Smooth_more")
btn_GaussianBlur = QPushButton("GaussianBlur")
btn_UnsharpMask = QPushButton("UnsharpMask")

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)

row_tools = QHBoxLayout()

row_tools2 = QHBoxLayout()

row_tools3 = QHBoxLayout()

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

row_tools2.addWidget(btn_blur)
row_tools2.addWidget(btn_contuor)
row_tools2.addWidget(btn_detail)
row_tools2.addWidget(btn_smooth)
row_tools2.addWidget(btn_edge_enchance)

row_tools3.addWidget(btn_edge_enchance_more)
row_tools3.addWidget(btn_emboss)
row_tools3.addWidget(btn_find_edges)
row_tools3.addWidget(btn_smooth_more)
row_tools3.addWidget(btn_GaussianBlur)
row_tools3.addWidget(btn_UnsharpMask)

col2.addLayout(row_tools)

col2.addLayout(row_tools2)

col2.addLayout(row_tools3)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)

win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)

    return result


def choose_Workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenameList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.avif',
                  '.svg', '.eps', '.bmp']
    
    choose_Workdir()
    files = filter(os.listdir(workdir), extensions)

    lw_files.clear()
    for filename in files:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenameList)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'modified/'

    def load_image(self, filename):
        self.filename = filename
        full_filename = os.path.join(workdir, filename)
        self.image = Image.open(full_filename)
    
    def save_image(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        full_filename = os.path.join(path, self.filename)
        
        self.image.save(full_filename)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
    
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_contuor(self):
        self.image = self.image.filter(CONTOUR)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_detail(self):
        self.image = self.image.filter(DETAIL)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_smooth(self):
        self.image = self.image.filter(SMOOTH)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_edge_enchance(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_edge_enchance_more(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_emboss(self):
        self.image = self.image.filter(EMBOSS)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_find_edges(self):
        self.image = self.image.filter(FIND_EDGES)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_smooth_more(self):
        self.image = self.image.filter(SMOOTH_MORE)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_GaussianBlur(self):
        self.image = self.image.filter(GaussianBlur)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)
        
    def do_UnsharpMask(self):
        self.image = self.image.filter(UnsharpMask)
        self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)


    def show_image(self, path):
        lb_image.hide()
        pix_map_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pix_map_image = pix_map_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pix_map_image)
        lb_image.show()

def show_chosen_image():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        work_image.load_image(filename)
        work_image.show_image(os.path.join(workdir, work_image.filename))

work_image = ImageProcessor()
lw_files.currentRowChanged.connect(show_chosen_image)

btn_left.clicked.connect(work_image.do_left)
btn_right.clicked.connect(work_image.do_right)
btn_flip.clicked.connect(work_image.do_flip)
btn_sharp.clicked.connect(work_image.do_sharpen)
btn_bw.clicked.connect(work_image.do_bw)

btn_blur.clicked.connect(work_image.do_blur)
btn_contuor.clicked.connect(work_image.do_contuor)
btn_detail.clicked.connect(work_image.do_detail)
btn_smooth.clicked.connect(work_image.do_smooth)
btn_edge_enchance.clicked.connect(work_image.do_edge_enchance)

btn_edge_enchance_more.clicked.connect(work_image.do_edge_enchance_more)
btn_emboss.clicked.connect(work_image.do_emboss)
btn_smooth_more.clicked.connect(work_image.do_smooth_more)
btn_smooth.clicked.connect(work_image.do_smooth)
btn_GaussianBlur.clicked.connect(work_image.do_GaussianBlur)
btn_UnsharpMask.clicked.connect(work_image.do_UnsharpMask)

app.exec_()

