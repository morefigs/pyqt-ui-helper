# This file was autogenerated using pyqt_helper.py, do NOT edit!


class DummyUiHelper:

    @property
    def some_action(self) -> bool:
        return self.ui.action_some_action.isChecked()

    @some_action.setter
    def some_action(self, value: bool) -> None:
        self.ui.action_some_action.setChecked(value)

    @property
    def some_action_enabled(self) -> bool:
        return self.ui.action_some_action.isEnabled()

    @some_action_enabled.setter
    def some_action_enabled(self, enabled: bool) -> None:
        self.ui.action_some_action.setEnabled(enabled)

    @property
    def some_combo(self) -> int:
        return self.ui.comboBox_some_combo.currentIndex()

    @some_combo.setter
    def some_combo(self, value: int) -> None:
        self.ui.comboBox_some_combo.setCurrentIndex(value)

    @property
    def some_combo_enabled(self) -> bool:
        return self.ui.comboBox_some_combo.isEnabled()

    @some_combo_enabled.setter
    def some_combo_enabled(self, enabled: bool) -> None:
        self.ui.comboBox_some_combo.setEnabled(enabled)

    @property
    def some_button(self) -> bool:
        return self.ui.pushButton_some_button.isChecked()

    @some_button.setter
    def some_button(self, value: bool) -> None:
        self.ui.pushButton_some_button.setChecked(value)

    @property
    def some_button_enabled(self) -> bool:
        return self.ui.pushButton_some_button.isEnabled()

    @some_button_enabled.setter
    def some_button_enabled(self, enabled: bool) -> None:
        self.ui.pushButton_some_button.setEnabled(enabled)

    @property
    def some_spin_box(self) -> int:
        return self.ui.spinBox_some_spin_box.value()

    @some_spin_box.setter
    def some_spin_box(self, value: int) -> None:
        self.ui.spinBox_some_spin_box.setValue(value)

    @property
    def some_spin_box_enabled(self) -> bool:
        return self.ui.spinBox_some_spin_box.isEnabled()

    @some_spin_box_enabled.setter
    def some_spin_box_enabled(self, enabled: bool) -> None:
        self.ui.spinBox_some_spin_box.setEnabled(enabled)
