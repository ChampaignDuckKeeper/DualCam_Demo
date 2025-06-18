import sys
from PySide6 import QtGui
from PySide6.QtCore import QEvent, QObject, QThread, Signal, Slot, Qt, QRectF  # Signal and Slot are replaced with Signal and Slot
from PySide6.QtGui import QPixmap, QImage, QPainter, QPen, QFont, QRegularExpressionValidator, QIntValidator, QDoubleValidator, QTransform, QIcon
from PySide6.QtWidgets import QVBoxLayout,QGraphicsRectItem, QApplication, QMainWindow, QFileDialog, QGraphicsScene, QHeaderView, QTableWidgetItem, QMessageBox, QGraphicsPixmapItem, QDialog, QFormLayout, QPushButton, QLabel, QLineEdit, QGroupBox, QGraphicsView
from PySide6.QtCore import QRegularExpression, QTimer,QEvent  # QRegularExpression is replaced by QRegularExpression
import numpy as np
import traceback
from hgui3 import Ui_MainWindow

import os

# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
#blahblah
# 构建lib路径
lib_path = os.path.join(current_dir, "lib")

# 检查目录是否存在
if not os.path.exists(lib_path):
    print(f"Creating lib directory: {lib_path}")
    os.makedirs(lib_path, exist_ok=True)

# 添加到Python路径
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)  # 插入到路径列表的开头
    print(f"Added to Python path: {lib_path}")

# 验证路径是否添加成功
print("Python search paths:")
for path in sys.path:
    print(f"  {path}")

import isp_engine_py as isp_engine
import time

# 创建一个中介对象来处理帧回调和信号
class FrameProcessor(QObject):
    # 定义信号
    frame_ready = Signal(object, int, int)
    
    def __init__(self):
        super().__init__()
    
    def frame_callback(self, buffer, width, height):
        try:
            # 仅将数据转发到信号，不在这里处理
            self.frame_ready.emit(buffer, width, height)
        except Exception as e:
            print(f"帧处理器回调中的错误: {e}")

class Burstprocessor(QObject):
    # 定义信号
    burst_ready = Signal(bool)
    
    def __init__(self):
        super().__init__()
 
    def burst_callback(self, status):
        # self.printf(f"\nburst Done: {status}")
        try:
            # 仅将数据转发到信号，不在这里处理
            self.burst_ready.emit(status)
        except Exception as e:
            print(f"连续拍摄结果返回回调中的错误: {e}")
        

class InitForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(InitForm, self).__init__()
        try:
            self.setupUi(self)
            self.setWindowIcon(QIcon("./icon/logo_color.ico"))            # 检查 Burst 按钮是否存在
            if not hasattr(self, 'Burst'):
                print("Warning: Burst button not found in UI")
                return
            self.scene = QGraphicsScene()
            self.graphicsView.setScene(self.scene)
            self.pixitem = QGraphicsPixmapItem()
            self.scene.addItem(self.pixitem)


            self.isp = isp_engine.ISPEngine()
            self.FrameProcessor = FrameProcessor()
            self.burstprocessor = Burstprocessor()
            self.FrameProcessor.frame_ready.connect(self.update_video_display)
            self.burstprocessor.burst_ready.connect(self.update_burst_status)

            #是否启流
            self.is_streaming = False

            
            # 帧计数和FPS计算
            self.frame_count = 0
            self.last_fps_update = time.time()
            self.fps = 0.0

                    
            # 设置更新定时器 - 用于更新UI状态
            self.update_timer = QTimer()
            self.update_timer.timeout.connect(self.update_ui_status)
            self.update_timer.start(500)  # 每500ms更新一次
        ##################################界面初始化############################
            display_mode    = 0         
            ROI_enable      = False
            AutoAFEC_enable = False
            TargetPL_data   = 440
            Exp_data        = 333
            Gain_data       = 10
            dGain_data      = 100
            pose_data       = 200
            AWB_APPLY_MIS   = False
            Burst_enable   = False

            self.menuData = []
            self.menuData.append(display_mode)          #0 
            self.menuData.append(ROI_enable)            #1
            self.menuData.append(AutoAFEC_enable)       #2
            self.menuData.append(TargetPL_data)         #3
            self.menuData.append(Exp_data)              #4
            self.menuData.append(Gain_data)             #5
            self.menuData.append(dGain_data)            #6
            self.menuData.append(pose_data)             #7
            self.menuData.append(AWB_APPLY_MIS)         #8
            self.menuData.append(Burst_enable)          #9


            self.disp_switch_scene1()

            self.disp_Scene1.clicked.connect(self.disp_switch_scene1)
            self.disp_Scene2.clicked.connect(self.disp_switch_scene2)
            self.disp_Compare.clicked.connect(self.disp_switch_compare)
            self.disp_RAW.clicked.connect(self.disp_switch_RAW)
            self.disp_MIS.clicked.connect(self.disp_switch_mis)

            #self.EN_touchROI.stateChanged.connect(self.touchROI_changed)
            #self.EN_MIS_AWB.stateChanged.connect(self.MIS_AWB_changed)

            self.b_zoom_in.setCheckable(True)
            self.b_zoom_out.setCheckable(True)        
            self.b_zoom_in.toggled.connect(self.on_zoom_in_toggled)
            self.b_zoom_out.toggled.connect(self.on_zoom_out_toggled)
            self.b_reset.clicked.connect(self.on_reset_clicked)

            self.Capture_all.clicked.connect(self.Capture_all_clicked)
            self.Burst.clicked.connect(self.show_burst_dialog)
            # self.EN_Burst.stateChanged.connect(self.Brust_changed)
            # self.N_capture.setValidator(QIntValidator(1, 301))
            self.B_Stream_on.clicked.connect(self.Stream_on_clicked)
            #self.Exit.clicked.connect(self.close)

            self.graphicsView.viewport().installEventFilter(self)

            self.EN_AutoAF.stateChanged.connect(self.AutoAFEC_changed)
            self.s_TargetPL.sliderReleased.connect(self.TargetPL_changed)
            self.s_TargetPL.sliderMoved.connect(self.TargetPL_moved)

            self.t_TargetPL.setValidator(QIntValidator(0, 256))
            self.t_TargetPL.editingFinished.connect(self.TargetPL_editored)

            # self.B_AEC.clicked.connect(self.AEC_clicked)
            # self.B_AF.clicked.connect(self.AF_clicked)

            # self.s_Exp.sliderReleased.connect(self.Exp_changed)
            # self.s_Exp.sliderMoved.connect(self.Exp_moved)

            # self.t_Exp.setValidator(QIntValidator(1, 100))
            # self.t_Exp.editingFinished.connect(self.Exp_editored)


            # self.s_Gain.sliderReleased.connect(self.Gain_changed)
            # self.s_Gain.sliderMoved.connect(self.Gain_moved)

            # self.t_Gain.setValidator(QDoubleValidator(1, 32, 1))
            # self.t_Gain.editingFinished.connect(self.Gain_editored)


            # self.s_dGain.sliderReleased.connect(self.dGain_changed)
            # self.s_dGain.sliderMoved.connect(self.dGain_moved)

            # self.t_dGain.setValidator(QDoubleValidator(0, 10, 1))
            # self.t_dGain.editingFinished.connect(self.dGain_editored)


            self.s_Pose.sliderReleased.connect(self.Pose_changed)
            self.s_Pose.sliderMoved.connect(self.Pose_moved)

            self.t_Pose.setValidator(QIntValidator(0, 100))
            self.t_Pose.editingFinished.connect(self.Pose_editored)


            self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        except Exception as e:
            print(f"初始化错误: {e}")
            import traceback
            traceback.print_exc()
    ##################################高级设置初始化############################
        
        # self.manual_AWB = False
        # self.manual_Rgain = 1.
        # self.manual_Ggain = 1.
        # self.manual_Bgain = 1.
        # self.Advanced.clicked.connect(self.open_advanced_dialog)

    ###############################显示缓存######################################
        self.CCT = None
    
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.pixitem = QGraphicsPixmapItem()
        self.scene.addItem(self.pixitem)

        # 网格覆盖层
        self.grid_item = QGraphicsPixmapItem()
        self.grid_item.setZValue(1)  # 保证网格层在图片层之上
        self.scene.addItem(self.grid_item)


        self.base_scale = 1.0
        self.min_scale = 0.8
        self.max_scale = 1.2
        self.current_scale = 1.0
        self.grid_visible = False
        self.grid_timer = QTimer()
        self.grid_timer.setInterval(30)
        self.grid_timer.timeout.connect(self.update_grid)
        
        self.current_left = QPixmap()   # 当前左侧图像
        self.current_right = QPixmap()  # 当前右侧图像
        self.pending_left = None        # 等待处理的左侧新帧
        self.pending_right = None       # 等待处理的右侧新帧
        self.processing = False         # 标志是否有帧正在处理
    ###############################函数#########################################
    def update_ui_status(self):
        try:
            # 更新UI显示当前的相机状态
            self.CCT = self.isp.get_CCT()
            if self.EN_AutoAF.isChecked():
                # 如果自动曝光开启，更新显示的参数
                current_exposure = self.isp.get_current_exposure()
                current_gain = self.isp.get_current_gain()
                current_pose = self.isp.get_current_focus_position()
                # current_ev = self.isp.get_current_ev()
                
                # 更新标签
                #self.t_Exp.setText(f"{(current_exposure//1000):.0f}")
                #self.t_Gain.setText(f"{current_gain:.1f}")
                self.t_Pose.setText(f"{(current_pose-200)/8:.0f}%")
                # self.ev_label.setText(f"EV: {current_ev:+d}")
                
                self.menuData[4] = int(current_exposure/100)  # 更新曝光时间
                self.menuData[5] = int(current_gain*10)  # 更新增益
                # 更新滑块位置（但不触发valueChanged信号）
                # self.s_Exp.blockSignals(True)
                # self.s_Exp.setValue(int(current_exposure/100))
                # self.s_Exp.blockSignals(False)
                
                # self.s_Gain.blockSignals(True)
                # self.s_Gain.setValue(int(current_gain*10))
                # self.s_Gain.blockSignals(False)

                self.s_Pose.blockSignals(True)
                self.s_Pose.setValue(current_pose)
                self.s_Pose.blockSignals(False)
                
                
                # self.ev_slider.blockSignals(True)
                # self.ev_slider.setValue(current_ev)
                # self.ev_slider.blockSignals(False)
            
            # # 更新对焦指标
            # focus_metric = self.isp.get_current_focus_metric()
            # self.focus_metric_label.setText(f"Focus Metric: {focus_metric:.2f}")
            
            # # 更新状态栏
            # exposure_status = "Auto" if self.auto_exposure_checkbox.isChecked() else "Manual"
            # focus_status = "Auto" if self.auto_focus_checkbox.isChecked() else "Manual"
            # self.statusBar().showMessage(f"Exposure: {exposure_status} | Focus: {focus_status}")
        except Exception as e:
            print(f"更新UI状态时出错: {e}")


    def disp_switch_scene1(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.menuData[0] = 0
        self.disp_Scene1.setEnabled(False)  
        self.disp_Compare.setEnabled(True)
        self.disp_RAW.setEnabled(True)
        self.disp_MIS.setEnabled(True)
        self.disp_Scene2.setEnabled(True)
        self.first_frame = True
        self.switch_count = 0
        # self.EN_touchROI.setChecked(False)
        # self.EN_touchROI.setEnabled(True)
        self.printf("Display Scene with traditional AWB")
        ######connect c++ here#####
        self.MIS_AWB_changed(False)  # 确保MIS AWB被禁用
        self.isp.set_display_mode(1)
        ###########################
    def disp_switch_compare(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.menuData[0] = 2
        self.disp_Compare.setEnabled(False) 
        self.disp_Scene1.setEnabled(True)
        self.disp_MIS.setEnabled(True)
        self.disp_RAW.setEnabled(True)
        self.disp_Scene2.setEnabled(True)
        self.first_frame = True
        self.switch_count = 0
        # self.EN_touchROI.setChecked(False)
        # self.EN_touchROI.setEnabled(False)
        self.printf("Compare RGB(L) and MIS(R) AWB effect")
        ######connect c++ here#####
        self.isp.set_display_mode(3)
        ###########################
    def disp_switch_scene2(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.menuData[0] = 1
        self.disp_Scene2.setEnabled(False)  
        self.disp_Compare.setEnabled(True)
        self.disp_MIS.setEnabled(True)
        self.disp_RAW.setEnabled(True)
        self.disp_Scene1.setEnabled(True)
        self.first_frame = True
        self.switch_count = 0
        #self.EN_touchROI.setChecked(False)
        #self.EN_touchROI.setEnabled(True)
        self.printf("Display Scene with MIS AWB")
        ######connect c++ here#####
        self.MIS_AWB_changed(True)  # 确保MIS AWB被禁用
        self.isp.set_display_mode(1)
        ###########################
    def disp_switch_mis(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.menuData[0] = 3
        self.disp_MIS.setEnabled(False)  
        self.disp_Compare.setEnabled(True)
        self.disp_Scene1.setEnabled(True)
        self.disp_Scene2.setEnabled(True)
        self.disp_RAW.setEnabled(True)
        self.first_frame = True
        self.switch_count = 0
        #self.EN_touchROI.setChecked(False)
        #self.EN_touchROI.setEnabled(False)
        self.printf("Displaying MIS channels")
        ######connect c++ here#####
        self.isp.set_display_mode(2)
        ###########################
    def disp_switch_RAW(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.menuData[0] = 4
        self.disp_RAW.setEnabled(False)
        self.disp_Compare.setEnabled(True)
        self.disp_Scene1.setEnabled(True)
        self.disp_Scene2.setEnabled(True)
        self.disp_MIS.setEnabled(True)
        self.first_frame = True
        self.switch_count = 0
        #self.EN_touchROI.setChecked(False)
        #self.EN_touchROI.setEnabled(False)
        self.printf("still developing")
        ######connect c++ here#####
        self.isp.set_display_mode(4)
        ###########################
    # def touchROI_changed(self,state):
    #     if not self.is_streaming:
    #         self.printf("\nPlease start stream first")
    #         return
    #     state = Qt.CheckState(state)
    #     if state == Qt.Checked:
    #         self.menuData[1]=True
    #         self.printf("\nTouch ROI enabled, click scene to select ROI for focus")
    #         ######control logic here###

    #         ###########################
    #     else:
    #         self.menuData[1]=False
    #         self.printf("\nTouch ROI disabled")
    #         ######control logic here###

    #         ###########################
    
    def MIS_AWB_changed(self,state):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        if state:
            self.menuData[8]=True
            self.printf("apply AWB from MIS")
            ######control logic here###
            self.isp.set_MIS_AWB(True)

            ###########################
        else:
            self.menuData[8]=False
            self.printf("apply AWB from Main Camera")
            ######control logic here###
            self.isp.set_MIS_AWB(False)

            ###########################



    def on_zoom_in_toggled(self, checked: bool):
        """放大按钮切换事件处理。"""
        if checked:
            # 若放大模式开启，则关闭缩小模式
            self.b_zoom_out.setChecked(False)

    def on_zoom_out_toggled(self, checked: bool):
        """缩小按钮切换事件处理。"""
        if checked:
            # 若缩小模式开启，则关闭放大模式
            self.b_zoom_in.setChecked(False)

    def eventFilter(self, obj, event):
        # 仅拦截 graphicsView 的视口点击事件
        if obj is self.graphicsView.viewport(): 
            if event.type() == QEvent.MouseButtonPress:
                # 当处于缩放模式时，执行以点击点为中心的缩放
                if self.b_zoom_in.isChecked() or self.b_zoom_out.isChecked():
                    # 选择缩放因子：放大1.2倍或缩小0.8倍
                    factor = 1.2 if self.b_zoom_in.isChecked() else 0.8
                    # 获取鼠标点击位置对应的场景坐标
                    scene_pos = self.graphicsView.mapToScene(event.pos())
                    # 将该场景坐标移到视图中心:contentReference[oaicite:6]{index=6}
                    self.graphicsView.centerOn(scene_pos)
                    # 按指定比例缩放视图:contentReference[oaicite:7]{index=7}
                    self.graphicsView.scale(factor, factor)
                    return True  # 事件已处理
            if event.type() == QEvent.Enter and self.menuData[0] == 1:
                # 仅在显示模式为0时显示网格
                self.grid_visible = True
                #self.printf("\n current_scale:"+str(self.current_scale) )
                self.grid_item.setVisible(self.grid_visible)
            elif event.type() == QEvent.Leave:
                self.grid_visible = False
                self.grid_item.setVisible(False)
        # 其他情况交给基类处理
        return super(InitForm, self).eventFilter(obj, event)
    
    def on_reset_clicked(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        self.center_and_fit()
        # """复位按钮点击事件处理。"""
        # # 重置视图的变换矩阵（清除缩放和平移）
        # self.graphicsView.resetTransform()
        # # 将图像缩放以适应视图窗口（保持长宽比）
        # self.graphicsView.fitInView(self.pixitem, Qt.KeepAspectRatio)
        # # 取消缩放按钮的选中状态
        # self.b_zoom_in.setChecked(False)
        # self.b_zoom_out.setChecked(False)
        

    def Capture_all_clicked(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
        try:
        #if not self.menuData[9]:
            self.printf("Capturing JPEG and RAW...")
            if self.isp.capture_all():
                self.printf(f"all saved")
            else:
                    self.printf("Failed to save file")
            # else:
            #     self.printf("Burst capture")
            #     if self.isp.BurstCap(int(self.N_capture.text())):
            #         self.Capture_all.setEnabled(False)
            #     else:
            #         self.printf("Failed to save file")
        except Exception as e:
            print(f"捕获图像时出错: {e}")
            self.statusBar().showMessage(f"capture error: {e}")

    def show_burst_dialog(self):
        if not self.is_streaming:
            self.printf("Please start stream first")
            return
            
        dialog = BurstSettingDialog(self)
        result = dialog.exec()
        
        if result == QDialog.Accepted:
            try:
                burst_count = int(dialog.input_field.text())
                self.printf(f"Starting burst capture: {burst_count} frames")
                if self.isp.BurstCap(burst_count):
                    self.Capture_all.setEnabled(False)
                    self.Burst.setEnabled(False)
                else:
                    self.printf("Failed to start burst capture")
            except ValueError:
                self.printf("Invalid input for burst capture count")

    # def Brust_changed(self,state):
    #     state = Qt.CheckState(state)
    #     if state == Qt.Checked:
    #         self.menuData[9]=True
    #         self.N_capture.setEnabled(True) 
    #     else:
    #         self.menuData[9]=False
    #         self.N_capture.setEnabled(False) 

    @Slot(object, bool)
    def update_burst_status(self,status):
        self.printf(f"burst Done: {status}")
        if status:
            self.Capture_all.setEnabled(True)
            self.Burst.setEnabled(True)


    def Stream_on_clicked(self):
        if self.is_streaming:
            self.close()
            return
        if self.isp.initialize():
            print("Camera initialized successfully!")
        else:
            print("Error initializing camera!")
            return
        # 开始预览
        self.isp.set_frame_callback(self.FrameProcessor.frame_callback)
        self.isp.set_burstcap_callback(self.burstprocessor.burst_callback)
        print("Frame callback registered")
        self.first_frame = True
        self.switch_count = 1
        if self.isp.start_preview():
            print("Preview started successfully!")
            self.is_streaming = True
            # 注册帧回调 - 使用帧处理器的回调方法
            self.AutoAFEC_changed(Qt.Checked)
            self.B_Stream_on.setStyleSheet("""font-size: 18px; background-color: #711617; color: black;""")
            self.B_Stream_on.setText("Stop&&Quit\n⏹️")
        else:
            print("Error starting preview!")
        
    def exit_clicked(self):
        ######connect c++ here#####
        #close everything

        ###########################
        QApplication.instance().quit()  #
    def AutoAFEC_changed(self,state):
        state = Qt.CheckState(state)
        if state == Qt.Checked:
            self.menuData[2]=True
            # self.B_AF.setEnabled(False)
            # self.B_AEC.setEnabled(False)
            # self.s_Exp.setEnabled(False)
            # self.s_Gain.setEnabled(False)
            # self.s_dGain.setEnabled(False)
            self.s_Pose.setEnabled(False)
            # self.t_Exp.setEnabled(False)
            # self.t_Gain.setEnabled(False)
            # self.t_dGain.setEnabled(False)
            self.t_Pose.setEnabled(False)        
            self.s_TargetPL.setMinimum(0)       # 设置最小值
            self.s_TargetPL.setMaximum(959)       # 设置最大值
            self.s_TargetPL.setSingleStep(1)     # 设置步长
            self.s_TargetPL.setValue(self.menuData[3])         # 设置当前位置
            self.label_7.setText("Target\nBrightness")
            self.t_TargetPL.setValidator(QIntValidator(0, 256))
            self.t_TargetPL.setText(str((self.menuData[3]+64)//4))  # 设置标签显示值
            self.printf("Auto AF/AEC enabled")
            ######control logic here###
            self.isp.set_auto_exposure(True)
            self.isp.set_auto_focus(True)
            ###########################
        else:
            self.menuData[2]=False
            # self.B_AF.setEnabled(   True)
            # self.B_AEC.setEnabled(  True)
            # self.s_Exp.setEnabled(  True)
            # self.s_Gain.setEnabled( True)
            # self.s_dGain.setEnabled(True)
            self.s_Pose.setEnabled( True)
            # self.t_Exp.setEnabled(  True)
            # self.t_Gain.setEnabled( True)
            # self.t_dGain.setEnabled(True)
            self.t_Pose.setEnabled( True)
            self.s_TargetPL.setMinimum(-20)       # 设置最小值
            self.s_TargetPL.setMaximum(60)       # 设置最大值
            self.s_TargetPL.setSingleStep(1)     # 设置步长
            self.s_TargetPL.setValue(int(np.log2(self.menuData[4]*self.menuData[5]/333/10)*10))         # 设置当前位置
            self.label_7.setText("EV")
            self.t_TargetPL.setValidator(QDoubleValidator(-2, 6,1))
            self.t_TargetPL.setText(f"{(np.log2(self.menuData[4]*self.menuData[5]/333/10)):.1f}")  # 设置标签显示值
            self.printf("Auto AF/AEC disabled")
            ######control logic here###
            self.isp.set_auto_exposure(False)
            self.isp.set_auto_focus(False)
            ###########################

    def TargetPL_editored(self):
        """当标签编辑完成时，更新目标亮度值"""
        try:
            if(self.menuData[2]):
                show_value = int(self.t_TargetPL.text())
                if show_value < 0:
                    show_value = 0
                elif show_value > 256:
                    show_value  = 256
                value = (show_value * 4) - 64
                self.s_TargetPL.setValue(value)
                self.TargetPL_changed()
            else:
                show_value = float(self.t_TargetPL.text())
                if show_value < -2:
                    show_value = -2
                elif show_value > 6:
                    show_value = 6
                value = show_value * 10
                self.s_TargetPL.setValue(value)
                self.TargetPL_changed()
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid Target PL value (0-256).")

    def TargetPL_moved(self, value):
        """实时更新标签显示值"""
        if self.menuData[2]:
            show_value = (value+64) // 4
            self.t_TargetPL.setText(str(int(show_value)))
        else:
            show_value = value / 10.
            self.t_TargetPL.setText(f"{show_value:.1f}")

    def TargetPL_changed(self):
        if self.menuData[2]:
            value = self.s_TargetPL.value()
            self.menuData[3] = value
            show_value = (value+64) // 4
            self.t_TargetPL.setText(str(int(show_value)))
            self.printf('set Target brightness: '+str(show_value))
            ######connect c++ here#####
            self.isp.set_ev(show_value)
            ###########################
        else:
            value = self.s_TargetPL.value()
            show_value = value / 10.
            self.t_TargetPL.setText(f"{show_value:.1f}")
            multiplier = 2**(value / 10.0)
            if multiplier <= 1:
                exp_stages = np.floor(multiplier * 4)
                exp = 1000/120 * exp_stages
                gain = multiplier/exp_stages*4
                self.isp.set_exposure(int(exp*1000))
                self.isp.set_gain(int(gain*1000))
                self.menuData[4] = int(np.round(exp*10))  # 更新曝光时间
                self.menuData[5] = int(np.round(gain*10))  # 更新增益
            elif multiplier <= 32:
                exp = 1000/120 * 4
                gain = multiplier
                self.isp.set_exposure(int(exp*1000))
                self.isp.set_gain(int(gain*1000))
                self.menuData[4] = int(np.round(exp*10))
                self.menuData[5] = int(np.round(gain*10))  # 更新增益
            else:
                exp_stages = np.floor(multiplier * 4)
                exp = 1000/120 * exp_stages
                gain = 32
                self.isp.set_exposure(int(exp*1000))
                self.isp.set_gain(int(gain*1000))
                self.menuData[4] = int(np.round(exp*10))
                self.menuData[5] = int(np.round(gain*10))
    # def AF_clicked(self):
    #     self.printf('AF start')
    #     ######connect c++ here#####

    #     ###########################
    #     pass
    # def AEC_clicked(self):
    #     self.printf('AEC start')
    #     ######connect c++ here#####

    #     ###########################
    #     pass

    # def Exp_editored(self):
    #     """当标签编辑完成时，更新曝光值"""
    #     try:
    #         show_value = int(self.t_Exp.text())
    #         if show_value < 1:
    #             show_value = 1
    #         elif show_value > 100:
    #             show_value = 100
    #         value = show_value * 10
    #         self.s_Exp.setValue(value)
    #         self.Exp_changed()
    #     except ValueError:
    #         QMessageBox.warning(self, "Invalid Input", "Please enter a valid Exposure value (0-100).")

    # def Exp_moved(self, value):
    #     """实时更新标签显示值"""
    #     show_value = (value) // 10
    #     self.t_Exp.setText(str(show_value))
    # def Exp_changed(self):
    #     value = self.s_Exp.value()
    #     self.menuData[4] = value
    #     show_value = (value) / 10
    #     self.t_Exp.setText(str(int(show_value)))
    #     self.printf('\nset Exposure: '+str(show_value) + 'ms')
    #     ######connect c++ here#####
    #     self.isp.set_exposure(value*100)
    #     ###########################

    # def Gain_editored(self):
    #     """当标签编辑完成时，更新增益值"""
    #     try:
    #         show_value = float(self.t_Gain.text())
    #         if show_value < 1:
    #             show_value = 1
    #         elif show_value > 32:
    #             show_value = 32
    #         value = show_value * 10
    #         self.s_Gain.setValue(value)
    #         self.Gain_changed()
    #     except ValueError:
    #         QMessageBox.warning(self, "Invalid Input", "Please enter a valid Gain value (1-32).")

    # def Gain_moved(self, value):
    #     """实时更新标签显示值"""
    #     show_value = (value) / 10
    #     self.t_Gain.setText(str(show_value))
    # def Gain_changed(self):
    #     value = self.s_Gain.value()
    #     self.menuData[5] = value
    #     show_value = (value) / 10
    #     self.t_Gain.setText(str(show_value))
    #     self.printf('\nset Gain: '+str(show_value) + 'x')
    #     ######connect c++ here#####
    #     self.isp.set_gain(value*100)
    #     ###########################
    
    # def dGain_editored(self):
    #     """当标签编辑完成时，更新数字增益值"""
    #     try:
    #         show_value = int(float(self.t_dGain.text()))
    #         if show_value < 0:
    #             show_value = 0
    #         elif show_value > 10:
    #             show_value = 10
    #         value = show_value * 10
    #         self.s_dGain.setValue(value)
    #         self.dGain_changed()
    #     except ValueError:
    #         QMessageBox.warning(self, "Invalid Input", "Please enter a valid Digital Gain value (1-10).")

    # def dGain_moved(self, value):
    #     """实时更新标签显示值"""
    #     if value>=100 and value<110:
    #         show_value = 1
    #     elif value>=110:
    #         show_value =( value - 100)/10.
    #     else:
    #         show_value = value/100.
    #     self.t_dGain.setText(f"{show_value:.1f}")
    # def dGain_changed(self):
    #     value = self.s_dGain.value()
    #     self.menuData[6] = value
    #     if value>=100 and value<110:
    #         show_value = 1
    #     elif value>=110:
    #         show_value =( value - 100)/10.
    #     else:
    #         show_value = value/100.
    #     self.t_dGain.setText(f"{show_value:.1f}")
    #     self.printf('\nset digital Gain: '+str(show_value) + 'x')
    #     ######connect c++ here#####
    #     ###########################

    def Pose_editored(self):
        """当标签编辑完成时，更新对焦位置值"""
        try:
            show_value = int(self.t_Pose.text())
            if show_value < 0:
                show_value = 0
            elif show_value > 100:
                show_value = 100
            value = (show_value * 8) + 200
            self.s_Pose.setValue(value)
            self.Pose_changed()
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid Focus Position value (0-100).")

    def Pose_moved(self, value):
        """实时更新标签显示值"""
        show_value = (value-200)/8
        self.t_Pose.setText(str(int(show_value))+'%')
    def Pose_changed(self):
        value = self.s_Pose.value()
        self.menuData[7] = value
        show_value = (value-200)/8
        self.t_Pose.setText(str(int(show_value))+'%')
        self.printf('set Af Position: '+f"{show_value:.1f}" + '%')
        ######connect c++ here#####
        self.isp.set_focus_position(value)
        ###########################
    closing = Signal()
    def closeEvent(self, event):
        print("关闭应用程序...")
        try:
            # 设置标志位，防止回调函数继续处理
            self.is_closing = True
            
            # 先停止定时器
            if hasattr(self, 'update_timer') and self.update_timer.isActive():
                print("停止定时器...")
                self.update_timer.stop()
            
            # 允许界面更新
            QApplication.processEvents()
            
            # 设置超时监控
            import threading
            timeout_reached = False
            
            def timeout_monitor():
                nonlocal timeout_reached
                time.sleep(5)  # 5秒超时
                if not timeout_reached:
                    print("清理超时，强制退出...")
                    timeout_reached = True
                    import os
                    os._exit(0)  # 强制退出
            
            # 启动超时监控线程
            timeout_thread = threading.Thread(target=timeout_monitor)
            timeout_thread.daemon = True
            timeout_thread.start()
            
            if hasattr(self, 'isp'):
                print("清理资源...")
                self.isp.cleanup()
                # 停止预览线程
                print("停止预览...")
                
                # 允许UI更新
                QApplication.processEvents()
                
            
            # 标记已完成，防止触发超时
            timeout_reached = True
            
        except Exception as e:
            print(f"关闭时出错: {e}")
            import traceback
            traceback.print_exc()
            
            # 确保应用能够关闭
            import os
            os._exit(0)
        
        print("关闭完成")

    # def open_advanced_dialog(self):
    #     dialog = CustomDialog(self)
    #     dialog.exec()

    def set_AWB_gain(self):
        self.isp.set_awb_gain(self.manual_Rgain,self.manual_Ggain,self.manual_Bgain)

    def get_AWB_gain(self):
        self.manual_Rgain,self.manual_Ggain,self.manual_Bgain = self.isp.get_awb_gain()
    
    def set_manual_awb(self,enable):
        self.isp.set_auto_awb(not enable)


    def printf(self, mes):
        # self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        # self.cursot = self.textBrowser.textCursor()
        # self.textBrowser.moveCursor(self.cursot.MoveOperation.End)
        # QApplication.processEvents()
        self.Info.setText( mes )  # 在指定的区域显示提示信息
            
    @Slot(object, int, int)
    def update_video_display(self, buffer, width, height):
        try:
            img_array = np.frombuffer(buffer, dtype=np.uint8)
            if len(img_array) == width * height * 3:
                img = img_array.reshape((height, width, 3))
                qimg = QImage(img.data, width, height, width * 3, QImage.Format_BGR888)
                
                # 保存原始图像（不再缩放）
                self.original_pixmap = QPixmap.fromImage(qimg)
                self.pixitem.setPixmap(self.original_pixmap)
                
                # 首次显示时自动适应视图
                if self.first_frame:
                    self.switch_count+=1
                    if self.switch_count > 2:
                        self.center_and_fit()
                        self.first_frame = False
                
                # 更新帧计数和FPS
                self.frame_count += 1
                current_time = time.time()
                if current_time - self.last_fps_update >= 1.0:
                    self.fps = self.frame_count / (current_time - self.last_fps_update)
                    self.frame_count = 0
                    self.last_fps_update = current_time
                    self.fps_label.setText(f"FPS: {self.fps:.1f}")
                    self.update_grid()
            else:
                print(f"数据大小不匹配: 实际={len(img_array)}, 期望={width*height*3}")
        except Exception as e:
            print(f"更新视频显示错误: {e}")
            traceback.print_exc()
    def center_image(self):
        """仅将图像居中显示，保持当前缩放比例"""
        if not self.pixitem.pixmap().isNull():
            # 获取视图和图像的当前尺寸
            view_rect = self.graphicsView.viewport().rect()
            scene_rect = self.pixitem.sceneBoundingRect()  # 使用sceneBoundingRect获取实际显示大小
            
            # 计算居中位置
            pos_x = (view_rect.width() - scene_rect.width()) / 2
            pos_y = (view_rect.height() - scene_rect.height()) / 2
            
            # 设置位置
            self.pixitem.setPos(pos_x, pos_y)
            
            # 更新视图
            self.graphicsView.update()
    def center_and_fit(self):
        """将图像在视图中居中并适应显示，同时保持图像比例"""
        if not self.pixitem.pixmap().isNull():
            # 重置所有变换
            self.graphicsView.resetTransform()
            
            # 将图像项重置到原点
            self.pixitem.setPos(0, 0)
            
            # 确保场景大小更新
            self.scene.setSceneRect(self.pixitem.boundingRect())
            
            # 使用fitInView自动计算并应用合适的缩放和位置
            self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
            
            # 获取当前变换的缩放比例
            transform = self.graphicsView.transform()
            self.current_scale = transform.m11()  # m11是水平缩放因子
            
            # 确保视图更新
            self.graphicsView.viewport().update()

    def update_grid(self):
        if not self.grid_visible:
            return
        if self.CCT is None:
            return

        pixmap_size = self.pixitem.pixmap().size()
        grid_pixmap = QPixmap(pixmap_size)
        grid_pixmap.fill(Qt.transparent)

        painter = QPainter(grid_pixmap)
        pen = QPen(Qt.red, 5)
        font = QFont("Arial", 30)
        painter.setPen(pen)
        painter.setFont(font)

        grid_h,grid_w = self.CCT.shape  # 8x6 网格
        # print(self.CCT.shape)
        cell_width = pixmap_size.width() // grid_w
        cell_height = pixmap_size.height() // grid_h

        for row in range(grid_h):
            for col in range(grid_w):
                x = col * cell_width
                y = row * cell_height
                painter.drawRect(x, y, cell_width, cell_height)
                painter.drawText(x + 5, y + 45, f"{self.CCT[row, col]}")

        painter.end()
        self.grid_item.setPixmap(grid_pixmap)     

    def process_combined_frame(self):
        if self.pending_left:
            self.current_left = self.pending_left
            self.pending_left = None
        if self.pending_right:
            self.current_right = self.pending_right
            self.pending_right = None
        if self.current_left.isNull() or self.current_right.isNull():
            # 没有足够图像拼接，标记空闲并返回等待
            self.processing = False
            return
        # 确定基准高度为两图像较大高度，保持两图比例一致
        h_left = self.current_left.height()
        h_right = self.current_right.height()
        # 将左右图像缩放到相同高度
        if h_left != h_right:
            target_height = max(h_left, h_right)
            if h_left < target_height:
                # 左图较低，放大左图到目标高度
                self.current_left = self.current_left.scaledToHeight(target_height, Qt.SmoothTransformation)
            if h_right < target_height:
                # 右图较低，放大右图到目标高度
                self.current_right = self.current_right.scaledToHeight(target_height, Qt.SmoothTransformation)
            # 更新宽高（放大后宽度也变化）
            h_left = self.current_left.height()
            h_right = self.current_right.height()
        # 此时 h_left == h_right == target_height
        combined_height = h_left  # 合成图高度
        combined_width = self.current_left.width() + self.current_right.width()

        # 创建合并后的 Pixmap 并绘制两张图
        combined_pixmap = QPixmap(combined_width, combined_height)
        combined_pixmap.fill(Qt.black)  # 底色填充，以防存在空隙
        painter = QPainter(combined_pixmap)
        painter.drawPixmap(0, 0, self.current_left)
        painter.drawPixmap(self.current_left.width(), 0, self.current_right)
        painter.end()

        # 获取视图当前大小限制，必要时缩放合成图
        view_size = self.graphicsView.viewport().size()
        max_w, max_h = view_size.width(), view_size.height()
        if combined_pixmap.width() > max_w or combined_pixmap.height() > max_h:
            # 等比例缩小到视图大小以内
            combined_pixmap = combined_pixmap.scaled(max_w, max_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 在图形视图中显示合成后的图像
        self.pixitem.setPixmap(combined_pixmap)

        # 一帧处理完成，检查是否有新帧在等待
        if (self.pending_left or self.pending_right) and self.menuData[0] == 2:
            # 有新帧等待，继续处理下一帧
            QTimer.singleShot(0, self.process_combined_frame)
        else:
            # 没有等待帧，标记空闲状态
            self.processing = False

class BurstSettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Burst capture setting")
        self.setFixedSize(250, 150)  # 设置固定大小
        
        # 设置对话框背景色和样式
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #395d39;
                color: white;
                border: none;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4a734a;
            }
            QPushButton:pressed {
                background-color: #2d492d;
            }
        """)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        layout.setSpacing(10)  # 设置控件之间的间距
        layout.setContentsMargins(20, 20, 20, 20)  # 设置边距
        
        # 创建并添加标签
        self.label = QLabel("Burst capture number:")
        layout.addWidget(self.label)
        
        # 创建并添加输入框
        self.input_field = QLineEdit()
        self.input_field.setValidator(QIntValidator(1, 3000))  # 限制输入1-3000的整数
        self.input_field.setText("10")  # 设置默认值
        layout.addWidget(self.input_field)
        
        # 创建并添加确认按钮
        self.confirm_button = QPushButton("Start Burst Capture")
        self.confirm_button.clicked.connect(self.accept)
        layout.addWidget(self.confirm_button)
        
        # 设置布局
        self.setLayout(layout)
# from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout,QCheckBox,QFrame

# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Advanced setting')
#         self.setGeometry(200, 200, 400, 150)

#         label_style = "font-weight: bold;"  # 加粗样式

#         self.EN_manual_AWB = QCheckBox('Enable Manuall AWB')  # 新增复选框
#         self.EN_manual_AWB.setChecked(self.parent().manual_AWB)

#         self.label_info1 = QLabel('Rgain:')
#         self.label_info1.setStyleSheet(label_style)
#         self.manual_R_Gain = QLineEdit()

#         self.label_info2 = QLabel('Ggain:')
#         self.label_info2.setStyleSheet(label_style)
#         self.manual_G_Gain = QLineEdit()

#         self.label_info3 = QLabel('BGain:')
#         self.label_info3.setStyleSheet(label_style)
#         self.manual_B_Gain = QLineEdit()


#         self.button_close = QPushButton('Close')
#         self.button_close.clicked.connect(self.close)

#         # 水平布局
#         layout1 = QHBoxLayout()
#         layout1.addWidget(self.label_info1)
#         layout1.addWidget(self.manual_R_Gain)

#         layout2 = QHBoxLayout()
#         layout2.addWidget(self.label_info2)
#         layout2.addWidget(self.manual_G_Gain)

#         layout3 = QHBoxLayout()
#         layout3.addWidget(self.label_info3)
#         layout3.addWidget(self.manual_B_Gain)

#         # 垂直布局
#         main_layout = QVBoxLayout()
#         main_layout.addLayout(layout1)
#         main_layout.addLayout(layout2)
#         main_layout.addLayout(layout3)
#         main_layout.addWidget(self.EN_manual_AWB)  # 添加复选框

#         line = QFrame()
#         line.setFrameShape(QFrame.HLine)
#         line.setFrameShadow(QFrame.Sunken)

#         bottom_label = QLabel("Extra Option:")
#         bottom_button = QPushButton("Apply")

#         bottom_layout = QHBoxLayout()
#         bottom_layout.addWidget(bottom_label)
#         bottom_layout.addStretch()
#         bottom_layout.addWidget(bottom_button)

#         main_layout.addWidget(line)
#         main_layout.addLayout(bottom_layout)

#         main_layout.addWidget(self.button_close)

#         self.setLayout(main_layout)

#         self.manual_R_Gain.setText(str(self.parent().manual_Rgain))
#         self.manual_G_Gain.setText(str(self.parent().manual_Ggain))
#         self.manual_B_Gain.setText(str(self.parent().manual_Bgain))

#         self.manual_R_Gain.setEnabled(self.parent().manual_AWB)
#         self.manual_G_Gain.setEnabled(self.parent().manual_AWB)
#         self.manual_B_Gain.setEnabled(self.parent().manual_AWB)

#         self.EN_manual_AWB.stateChanged.connect(self.ManualAWB_changed)
#         self.manual_R_Gain.editingFinished.connect(self.AWB_Gain_set)
#         self.manual_G_Gain.editingFinished.connect(self.AWB_Gain_set)
#         self.manual_B_Gain.editingFinished.connect(self.AWB_Gain_set)
#     def AWB_Gain_set(self):
#         self.parent().manual_Rgain,self.parent().manual_Ggain,self.parent().manual_Bgain = float(self.manual_R_Gain.text()), float(self.manual_G_Gain.text()), float(self.manual_B_Gain.text())
#         self.parent().set_AWB_gain()
#     def ManualAWB_changed(self,state):
#         state = Qt.CheckState(state)
#         if state == Qt.Checked:
#             self.parent().manual_AWB = True
#             self.parent().get_AWB_gain()
#             self.parent().set_AWB_gain()
#             self.manual_R_Gain.setEnabled(self.parent().manual_AWB)
#             self.manual_G_Gain.setEnabled(self.parent().manual_AWB)
#             self.manual_B_Gain.setEnabled(self.parent().manual_AWB)
#             self.manual_R_Gain.setText(str(self.parent().manual_Rgain))
#             self.manual_G_Gain.setText(str(self.parent().manual_Ggain))
#             self.manual_B_Gain.setText(str(self.parent().manual_Bgain))
#             self.parent().set_manual_awb(self.parent().manual_AWB)
            
#         else:
#             self.parent().manual_AWB = False
#             self.manual_R_Gain.setEnabled(self.parent().manual_AWB)
#             self.manual_G_Gain.setEnabled(self.parent().manual_AWB)
#             self.manual_B_Gain.setEnabled(self.parent().manual_AWB)
#             self.parent().set_manual_awb(self.parent().manual_AWB)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # app.setStyleSheet(dark_stylesheet)
    initform = InitForm()
    initform.closing.connect(initform.close)
    initform.show()
    # ui.pushButton.clicked.connect(partial(convert, ui))
    sys.exit(app.exec())
