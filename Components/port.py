from PyQt5 import QtGui, QtCore, QtWidgets
from Model import constants

__all__ = ["Port"]


class Port(QtWidgets.QGraphicsWidget):
    def __init__(self, port_type, parent):
        super(Port, self).__init__(parent)
        self.type = port_type
        # BASIC SETTINGS
        self.setAcceptHoverEvents(True)
        self.setFlag(self.ItemSendsScenePositionChanges, True)
        self.setZValue(constants.Z_VAL_PORT)
        self.setCacheMode(constants.ITEM_CACHE_MODE)

        # STORE PIPES
        self.pipes = list()

        # DRAW PARAMETERS
        self.width = 22.0
        self.height = 22.0
        self.color = (49, 115, 100, 255)
        self.border_size = 1
        self.border_color = (29, 202, 151, 255)
        self.hovered = False
        self.hovered_color = (17, 43, 82, 255)
        self.hovered_border_color = (136, 255, 35, 255)
        self.activated_color = (14, 45, 59, 255)
        self.activated_border_color = (107, 166, 193, 255)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0.0, 0.0, self.width, self.height)

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget=None) -> None:
        # SIZE
        rect_width = self.width / 1.8
        rect_height = self.height / 1.8
        rect_x = self.boundingRect().center().x() - (rect_width / 2)
        rect_y = self.boundingRect().center().y() - (rect_height / 2)
        port_rect = QtCore.QRectF(rect_x, rect_y, rect_width, rect_height)

        # COLOR
        if self.hovered:
            color = QtGui.QColor(*self.hovered_color)
            border_color = QtGui.QColor(*self.hovered_border_color)
        elif self.pipes:
            color = QtGui.QColor(*self.activated_color)
            border_color = QtGui.QColor(*self.activated_border_color)
        else:
            color = QtGui.QColor(*self.color)
            border_color = QtGui.QColor(*self.border_color)

        # PAINTER
        pen = QtGui.QPen(border_color, 1.8)
        painter.setPen(pen)
        painter.setBrush(color)
        painter.drawEllipse(port_rect)

        # OTHER OPTIONS
        if self.pipes and not self.hovered:
            painter.setBrush(border_color)
            w = port_rect.width() / 2.5
            h = port_rect.height() / 2.5
            rect = QtCore.QRectF(port_rect.center().x() - w / 2,
                                 port_rect.center().y() - h / 2,
                                 w, h)
            border_color = QtGui.QColor(*self.border_color)
            pen = QtGui.QPen(border_color, 1.6)
            painter.setPen(pen)
            painter.setBrush(border_color)
            painter.drawEllipse(rect)
        elif self.hovered:
            if len(self.pipes) >= 2:
                pen = QtGui.QPen(border_color, 1.4)
                painter.setPen(pen)
                painter.setBrush(color)
                w = port_rect.width() / 1.8
                h = port_rect.height() / 1.8
            else:
                painter.setBrush(border_color)
                w = port_rect.width() / 3.5
                h = port_rect.height() / 3.5
            rect = QtCore.QRectF(port_rect.center().x() - w / 2,
                                 port_rect.center().y() - h / 2,
                                 w, h)
            painter.drawEllipse(rect)

    # def itemChange(self, change: QGraphicsItem.GraphicsItemChange, value):
    #     if change == self.ItemScenePositionHasChanged:
    #         self.redraw_pipes()
    #     return super(Port, self).itemChange(change, value)

    def hoverEnterEvent(self, event: QtWidgets.QGraphicsSceneHoverEvent) -> None:
        self.hovered = True
        super(Port, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: QtWidgets.QGraphicsSceneHoverEvent) -> None:
        self.hovered = False
        super(Port, self).hoverLeaveEvent(event)