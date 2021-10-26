import copy

class SelfReferncingEntity:
    def __init__(self):
        self.parent = None


    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """

    """
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref


    def __copy__(self):
        """

        :return:
        """
        print("Invoke __copy__")
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new


    def __deepcopy__(self, memodict={}):
        print("Invoke __deepcipy__")
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memodict)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memodict)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__)
        return new

if __name__ == "__main__":
    list_of_objects = [1, {1,2,3}, [1,2,3]]
    circular_ref = SelfReferncingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    shallow_copied_component = copy.copy(component)
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print("Modify the shallow copy successfully-1")
    else:
        print("Modify the shallow copy failed-1")

    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print("Modify the shallow copy successfully-2")
    else:
        print("Modify the shallow copy failed-2")

    deep_copied_component = copy.deepcopy(component)
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print("Modify the deep copy successfully-1")
    else:
        print("Modify the deep copy failed-1")
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print("Modify the deep copy successfully-2")
    else:
        print("Modify the deep copy failed-2")

    print("deep_copied")