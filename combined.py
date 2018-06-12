#!/usr/bin/env python

class FooAndBar:
    
    import components
    
    def foo(self):
        self.components.foo.foo()
    def bar(self):
        self.components.bar.bar()

def main():
    foo_and_bar = FooAndBar()
    foo_and_bar.foo()
    foo_and_bar.bar()

if __name__ == '__main__':
    main()
