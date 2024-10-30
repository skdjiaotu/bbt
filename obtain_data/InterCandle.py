class InterCandle{
# 在InterCandle类的初始化过程中，设置几个中间变量，用于存储鼠标状态
def __init__(self, data, my_style):
    # 鼠标按键状态，False为按键未按下，True为按键按下
    self.press = False
    # 鼠标按下时的x坐标
    self.xpress = None

    # 以下部分代码与本节开头的完全相同，为节省篇幅，略去不表
    ...

    # 下面的代码在__init__()中，告诉matplotlib哪些回调函数用于响应哪些事件
    # 鼠标按下事件与self.on_press回调函数绑定
    fig.canvas.mpl_connect('button_press_event', self.on_press)
    # 鼠标按键释放事件与self.on_release回调函数绑定
    fig.canvas.mpl_connect('button_release_event', self.on_release)
    # 鼠标移动事件与self.on_motion回调函数绑定
    fig.canvas.mpl_connect('motion_notify_event', self.on_motion)


def on_press(self, event):
    # 当鼠标按键按下时，调用该函数，event为事件信息，是一个dict对象，包含事件相关的信息
    # 如坐标、按键类型、是否在某个Axes对象内等等
    # event.inaxes可用于判断事件发生时，鼠标是否在某个Axes内，在这里我们指定，只有鼠
    # 标在ax1内时，才能平移K线图，否则就退出事件处理函数
    if not event.inaxes == self.ax1:
        return
    # 检查是否按下了鼠标左键，如果不是左键，同样退出事件处理函数
    if event.button != 1:
        return
    # 如果鼠标在ax1范围内，且按下了左键，条件满足，设置鼠标状态为pressed
    self.pressed = True
    # 同时记录鼠标按下时的x坐标，退出函数，等待鼠标移动事件发生
    self.xpress = event.xdata

    # 鼠标移动事件处理


def on_motion(self, event):
    # 如果鼠标按键没有按下pressed == False，则什么都不做，退出处理函数
    if not self.pressed:
        return
    # 如果移动出了ax1的范围，也退出处理函数
    if not event.inaxes == self.ax1:
        return
    # 如果鼠标在ax1范围内，且左键按下，则开始计算dx，并根据dx计算新的K线图起点
    dx = int(event.xdata - self.xpress)
    # 前面介绍过了，新的起点N(new) = N - dx
    new_start = self.idx_start - dx
    # 设定平移的左右界限，如果平移后超出界限，则不再平移
    if new_start <= 0:
        new_start = 0
    if new_start >= len(self.data) - 100:
        new_start = len(self.data) - 100
        # 清除各个图表Axes中的内容，准备以新的起点重新绘制
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
    # 更新图表上的文字、以新的起点开始绘制K线图
    self.refresh_texts(self.data.iloc[new_start])
    self.refresh_plot(new_start)


# 鼠标按键释放
def on_release(self, event):
    # 按键释放后，设置鼠标的pressed为False
    self.pressed = False
    # 此时别忘了最后一次更新K线图的起点，否则下次拖拽的时候就不会从这次的起点开始移动了
    dx = int(event.xdata - self.xpress)
    self.idx_start -= dx
    if self.idx_start <= 0:
        self.idx_start = 0
    if self.idx_start >= len(self.data) - 100:
        self.idx_start = len(self.data) - 100

}
