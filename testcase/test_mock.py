#-*- coding:utf-8 -*-
from unittest.mock import Mock
import unittest
from unittest.mock import patch

#mock = Mock()
#print(dir(mock))
#print(type(dir(mock)))
#print(type(help(mock)))
#mock.return_value = 3
#print(mock())

class Person:
    def __init__(self):
        self.__age = 10

    def get_fullname(self,first_name,last_name):
        return first_name + ' ' + last_name

    def get_age(self):
        return self.__age

    @staticmethod
    def get_class_name():
        return Person.__name__


class test_Person(unittest.TestCase):
    # 1.返回固定值
   def test_should_get_age(self):
        p = Person()
        # 不mock时，get_age应该返回10
        self.assertEqual(p.get_age(),10)
        # mock掉get_age方法，让它返回20
        p.get_age = Mock(return_value=20)
        self.assertEqual(p.get_age(),20)

   def test_should_get_fullname(self):
        p = Person()
        # mock掉get_fullname，让它返回'James Harden'
        p.get_fullname = Mock(return_value='Until Tom')
        self.assertEqual(p.get_class_name(),'Until Tom')

        #2. 校验参数个数，再返回固定值
        # 上面的例子你也许已经注意到了，调用p.get_fullname时没有给任何的参数，但是依然可以工作。如果想校验参数需要用create_autospec模块方法替代Mock类。
   def test_should_get_fullname_params(self):
        p = Person()
        p.get_fullname = unittest.mock.create_autospec(p.get_fullname, return_value='James Harden')
        #随便给两个参数，依然会返回mock的值
        self.assertEqual(p.get_fullname('1','2'),'James Harden')
        # 如果参数个数不对，会报错TypeError: missing a required argument: 'last_name'
        p.get_fullname('1')

    #3. 使用side_effect, 依次返回指定值
   def test_should_get_age3(self):
        p = Person()
        p.get_age = Mock(side_effect=[10,11,12])
        self.assertEqual(p.get_age(),10)
        self.assertEqual(p.get_age(),11)
        self.assertEqual(p.get_age(),12)

    #4. 根据参数不同，返回不同的值
   def test_should_get_fullname(self):
       p = Person()
       values = {('James', 'Harden'): 'James Harden', ('Tracy', 'Grady'): 'Tracy Grady'}
       p.get_fullname = Mock(side_effect=lambda x,y:values[(x,y)])
       self.assertEqual(p.get_fullname('James', 'Harden'), 'James Harden')
       self.assertEqual(p.get_fullname('Tracy', 'Grady'), 'Tracy Grady')

    #5. 抛出异常
   def test_should_raise_exception(self):
        p = Person()
        p.get_age = Mock(side_effect=TypeError('integer type'))
        # 只要调就会抛出异常
        self.assertRaises(TypeError,p.get_age)

    #6. 检验是否调用
   def test_should_validate_method_calling(self):
        p.get_fullname = Mock(return_value='James Harden')
        #没调用过
        p.get_fullname.assert_not_called()  #Python3.5
        p.get_fullname('1','2')
        #调用过任意次数
        p.get_fullname.assert_called() #Python3.6
        #只调用过一次，不管参数
        p.get_fullname.assert_called_once() #Python3.6
        #只调用过一次，并且符合指定的参数
        p.get_fullname.assert_called_once_with('1','2')
        p.get_fullname('3', '4')
        #只用调用过即可，必须指定参数
        p.get_fullname.assert_any_call('1','2')
        #重置mock，重置之后相当于没有调用过
        p.get_fullname.reset_mock()
        p.get_fullname.assert_not_called()
        # Mock对象里除了return_value, side_effect属性外，
        # called表示是否调用过，call_count可以返回调用的次数
        self.assertEqual(p.get_fullname.called,False)
        self.assertEqual(p.get_fullname.call_count,0)
        p.get_fullname('1', '2')
        p.get_fullname('3', '4')
        self.assertEqual(p.get_fullname.called, True)
        self.assertEqual(p.get_fullname.call_count, 2)

   #7.在测试方法参数中得到Mock对象
   # 以字符串的形式列出静态方法的路径，在测试的参数里会自动得到一个Mock对象
   @patch('your.package.module.Person.get_class_name')
   def test_should_get_class_name(self, mock_get_class_name):
        mock_get_class_name.return_value = 'Guy'
        self.assertEqual(Person.get_class_name(), 'Guy')

   #8.在patch中设置Mock对象
   mock_get_class_name = Mock(return_value='Guy')  # 在patch中给出定义好的Mock的对象，好处是定义好的对象可以复用
   @patch('your.package.module.Person.get_class_name', mock_get_class_name)
   def test_should_get_class_name(self):
        self.assertEqual(Person.get_class_name(), 'Guy')

   #9.使用patch.object
   mock_get_class_name = Mock(return_value='Guy')  # 使用patch.object来mock，好处是Person类不是以字符串形式给出的
   @patch.object(Person, 'get_class_name', mock_get_class_name)
   def test_should_get_class_name(self, ):
        self.assertEqual(Person.get_class_name(), 'Guy')

   #10.使用with控制作用域 # 作用域之外，依然返回真实值
   def test_should_get_class_name(self, ):
        mock_get_class_name = Mock(return_value='Guy')
        with patch('your.package.module.Person.get_class_name', mock_get_class_name):
            self.assertEqual(Person.get_class_name(), 'Guy')
        self.assertEqual(Person.get_class_name(), 'Person')


if __name__=='__main__':
    #unittest.main(verbosity=2)
    p = Person()
    print(p.get_age)
    print(p.get_age())