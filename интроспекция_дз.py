def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    info['module'] = obj.__class__.__module__

    return info

if __name__ == "__main__":
    number_info = introspection_info(42)
    print(number_info)

    class ExampleClass:
        def __init__(self):
            self.value = 10

        def example_method(self):
            return self.value

    example_object = ExampleClass()
    example_info = introspection_info(example_object)
    print(example_info)