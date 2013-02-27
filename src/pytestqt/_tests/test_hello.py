from pytestqt.qt_compat import QtGui 
import pytest


#===================================================================================================
# setup
#===================================================================================================
@pytest.fixture
def setup(qt):
    print 'setup:%s' % qt
    w = QtGui.QWidget()
    qt.addWidget(w)
    return w

#===================================================================================================
# test_hello_1
#===================================================================================================
def test_hello_1(qt, setup):
    widget = QtGui.QWidget()
    qt.addWidget(widget)
    widget.setWindowTitle('W1')
    widget.show()
    
    
#===================================================================================================
# test_hello_2
#===================================================================================================
def test_hello_2(qt):
    widget = QtGui.QWidget()
    qt.addWidget(widget)
    widget.setWindowTitle('W2')
    widget.show()
    

#===================================================================================================
# main
#===================================================================================================
if __name__ == '__main__':
    pytest.main(args=['-s'])