def pre_order(self):
    print(self.value)  # процедура обработки

    if self.left_child is not None:  # если левый потомок существует
        self.left_child.pre_order()  # рекурсивно вызываем функцию

    if self.right_child is not None:  # если правый потомок существует
        self.right_child.pre_order()  # рекурсивно вызываем функцию


print(self.value)  # процедура обработки
