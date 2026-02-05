
from my_phone import MyPhone

# print(MyPhone.type)
# print(MyPhone.model)
# print(MyPhone.color)
# print(MyPhone.size)
#
# print(MyPhone.__dict__)

class MobilePhone:
    # ctor constructor
    def __init__(self, type, model, color, size):
        print('Creating phone......')
        self.type = type
        self.model = model
        self.color = color
        self.size = size
        self.contacts = None

iphone = MobilePhone(type='iphone', model='14 Pro', color='Black', size=6.5)
#iphone.type = 'iphone'; iphone.model = '4 Pro'; iphone.color = 'Black'; iphone.size = 6.5;
print(iphone.type)
print(iphone.__dict__)

samsung = MobilePhone('Galaxy', '25 NoteBook', 'White', 6.9)
#samsung.type = 'Galaxy'; samsung.model = '25 Galaxy';  samsung.Size = 6.9;
print(samsung.__dict__)

# class Car -- foloow the example above using __init__ and self.<filed> = <value>
#     brand [Mitsubishi]
#     model [Outlander]
#     price [240_000]
#     seats [7]
# create 2 cars