import tkinter as tk


root = tk.Tk()
root.title("滚动显示歌词内容")


root.geometry("800x600")


root.config(bg="black")

# 创建一个文本框用于显示文本内容，单列文本框
text_box = tk.Text(root, font=("Times New Roman", 40), wrap=tk.WORD, bg="black", fg="white", spacing1=1.5, padx=20,
                   pady=20)
text_box.pack(expand=True)



def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
    return content



class TextScroller:
    def __init__(self, content, text_widget, lines_per_scroll=13):
        self.content = content
        self.text_widget = text_widget
        self.lines_per_scroll = lines_per_scroll
        self.current_pos = 0

        # 设置文本框中的每行居中对齐
        self.text_widget.tag_configure("center", justify="center")  # 设置居中对齐
        self.update_text_display()

    def on_mouse_wheel(self, event):
        # 向上滚动
        if event.delta > 0:
            self.scroll_up()
        # 向下滚动
        elif event.delta < 0:
            self.scroll_down()

    def scroll_up(self):
        # 向上滚动，确保不会越过文本开始处
        self.current_pos = max(0, self.current_pos - self.lines_per_scroll)
        self.update_text_display()

    def scroll_down(self):
        # 向下滚动，确保不会超出文本末尾
        self.current_pos = min(len(self.content) - self.lines_per_scroll, self.current_pos + self.lines_per_scroll)
        self.update_text_display()

    def update_text_display(self):

        visible_text = "\n".join(self.content[self.current_pos:self.current_pos + self.lines_per_scroll])


        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)  # 清空当前显示的内容

        # 将每行文本添加到文本框并应用居中对齐
        for line in visible_text.splitlines():
            self.text_widget.insert(tk.END, line + "\n", "center")  # 每行使用 "center" 标签居中显示

        self.text_widget.config(state=tk.DISABLED)



file_path = "x.txt"
content = load_file(file_path)


scroller = TextScroller(content, text_box)

# 绑定鼠标滚轮事件
root.bind("<MouseWheel>", scroller.on_mouse_wheel)


root.mainloop()
