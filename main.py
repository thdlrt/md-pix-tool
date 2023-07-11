# mdpixtool desingned by thdlrt with chatgpt4
# 用于处理图片，便于知识分享
# 下载并替换md中的图床连接
# 规范化图片格式，便于上传到各大论坛
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from mainWindow_ui import Ui_Form
from mdpixtool import mode1, mode2 
import shutil
import os

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 功能相关
        self.input_path = ''
        self.output_path = ''
        self.mode1_choice = False
        self.mode2_choice = False

        # 显示初始化
        self.ui.input_line.setReadOnly(True)
        self.ui.input_line.setText("请选择输入路径")
        self.ui.output_line.setReadOnly(True)
        self.ui.output_line.setText("另存（若不指定则在源文件上修改）")
        self.ui.label.setText('<a href="https://github.com/thdlrt/md-pix-tool">https://github.com/thdlrt/md-pix-tool</a>')

        # 事件绑定
        self.ui.input_btn_1.clicked.connect(self.open_input_1_dialog)
        self.ui.input_btn_2.clicked.connect(self.open_input_2_dialog)
        self.ui.output_btn.clicked.connect(self.open_output_dialog)
        self.ui.check_1.stateChanged.connect(self.mode1_choice_changed)
        self.ui.check_2.stateChanged.connect(self.mode2_choice_changed)
        self.ui.start_btn.clicked.connect(self.start)
    # 事件处理
    # 文件选取
    def open_input_1_dialog(self):
        file_dialog = QFileDialog(self)
        self.input_path, _ = file_dialog.getOpenFileName() 
        if self.input_path:
            self.ui.input_line.setText(self.input_path)
    # 文件夹选取
    def open_input_2_dialog(self):
        file_dialog = QFileDialog(self)
        self.input_path= file_dialog.getExistingDirectory() 
        if self.input_path:
            self.ui.input_line.setText(self.input_path)

    def open_output_dialog(self):
        file_dialog = QFileDialog(self)
        self.output_path= file_dialog.getExistingDirectory() 
        if self.output_path:
            self.ui.output_line.setText(self.output_path) 
    # 功能选择
    def mode1_choice_changed(self):
        if self.ui.check_1.isChecked():
            self.mode1_choice = True
        else:
            self.mode1_choice = False

    def mode2_choice_changed(self):
        if self.ui.check_2.isChecked():
            self.mode2_choice = True
        else:
            self.mode2_choice = False
    # 开始操作
    def start(self):
        # 判断输入输出路径是否为空
        if not self.input_path:
            return
        self.setEnabled(False)
        # 将文件复制到新路径
        # 判段路径类型
        if self.output_path:
            filename = os.path.basename(self.input_path)
            output = os.path.join(self.output_path, filename)
        else:
            output = self.input_path
        if os.path.isfile(self.input_path):
            if self.output_path:
                shutil.copyfile(self.input_path, output)
            if self.mode1_choice:
                mode1(output)
            if self.mode2_choice:
                mode2(output)
        elif os.path.isdir(self.input_path):
            if self.output_path:
                shutil.copytree(self.input_path, output)
            for dirpath, dirnames, filenames in os.walk(output):
                # 遍历每个文件
                for filename in filenames:
                    # 检查文件的扩展名，如果为.md，那么对它执行特定的操作
                    if filename.endswith('.md'):
                        # 获取文件的全路径
                        file_path = os.path.join(dirpath, filename)
                        # 对文件执行特定的操作
                        if self.mode1_choice:
                            mode1(file_path)
                        if self.mode2_choice:
                            mode2(file_path)
        msgBox = QMessageBox()
        msgBox.setText("转化已经完成!")  # 设置消息文本
        msgBox.exec()
        # 复位
        self.ui.input_line.setText("请选择输入路径")
        self.ui.output_line.setText("另存（若不指定则在源文件上修改）")
        self.ui.check_1.setChecked(False)
        self.ui.check_2.setChecked(False)
        self.mode1_choice = False
        self.mode2_choice = False
        self.input_path = ''
        self.output_path = ''
        self.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('MDPixTool')
    window.show()  # Display the UI
    sys.exit(app.exec())