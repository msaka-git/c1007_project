#/bin/env python
from gui_lib import gui_code



if __name__ == "__main__":
    import sys
    app = gui_code.QtWidgets.QApplication(sys.argv)
    Form = gui_code.QtWidgets.QWidget()
    ui = gui_code.Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

