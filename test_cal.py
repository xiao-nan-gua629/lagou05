import pytest
import yaml
from pythoncode.calculator import Calculator

def setup_module():
    print("\nsetup_module:整个test_cal.py模块开始前只执行一次")

def teardown_module():
        print("\nsetup_module:整个test_cal.py模块结束后只执行一次")


class TestCalc:
    def setup_class(self):
        print("\nsetup_class:类中所有用例执行前执行一次")
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def teardown_class(self):
            print("\nteardown_class:类中所有用例执行结束后执行一次")
    def setup_method(self):
        print("\n开始计算")
    def teardown_method(self):
        print("\n计算结束")

    def get_datas():

        with open("E:/Mypytest/lagou05/pythoncode/calc.yml") as f:
            datas = yaml.safe_load(f)
            print(datas)
        add_datas = datas["adddatas"]

        sub_datas = datas["subdatas"]

        mul_datas = datas["muldatas"]

        div_datas = datas["divdatas"]

        cal_ids = datas["calids"]

        return [add_datas,sub_datas,mul_datas,div_datas,cal_ids]



    #  使用参数化
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[4])
    # 测试add函数
    def test_add(self,a,b,expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a,b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[1],ids=get_datas()[4])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[2],ids=get_datas()[4])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",get_datas()[3],ids=get_datas()[4])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect