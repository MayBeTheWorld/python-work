company = {
    '总经理办公室': {
        '张三': {
            '工号': '001',
            '姓名': '张三',
            '性别': '男',
            '手机号': '1234567890'
        },
        '李四': {
            '工号': '002',
            '姓名': '李四',
            '性别': '女',
            '手机号': '9876543210'
        },
        '王五': {
            '工号': '003',
            '姓名': '王五',
            '性别': '男',
            '手机号': '1357924680'
        }
    },
    '人事部': {
        '赵六': {
            '工号': '101',
            '姓名': '赵六',
            '性别': '女',
            '手机号': '2468135790'
        },
        '钱七': {
            '工号': '102',
            '姓名': '钱七',
            '性别': '男',
            '手机号': '1111111111'
        },
        '孙八': {
            '工号': '103',
            '姓名': '孙八',
            '性别': '女',
            '手机号': '2222222222'
        }
    },
    '财务部': {
        '周九': {
            '工号': '201',
            '姓名': '周九',
            '性别': '男',
            '手机号': '3333333333'
        },
        '吴十': {
            '工号': '202',
            '姓名': '吴十',
            '性别': '女',
            '手机号': '4444444444'
        },
        '郑十一': {
            '工号': '203',
            '姓名': '郑十一',
            '性别': '男',
            '手机号': '5555555555'
        }

    },
    '生产部': {
        '王十二': {
            '工号': '301',
            '姓名': '王十二',
            '性别': '女',
            '手机号': '6666666666'
        },
        '克十三': {
            '工号': '302',
            '姓名': '克十三',
            '性别': '男',
            '手机号': '7777777777'
        },
        '何十四': {
            '工号': '303',
            '姓名': '何十四',
            '性别': '女',
            '手机号': '8888888888'
        }
    },
    '销售部': {
        '李十五': {
            '工号': '401',
            '姓名': '李十五',
            '性别': '女',
            '手机号': '9999999999'
        },
        '吴十六': {
            '工号': '402',
            '姓名': '吴十六',
            '性别': '女',
            '手机号': '1010101010'
        },
        '王十七': {
            '工号': '403',
            '姓名': '王十七',
            '性别': '女',
            '手机号': '1212121212'
        },
    }
}

# 访问公司组织结构信息示例
search_info1 = ['总经理办公室']
print("总经理办公室员工信息:")
for employee_name,  employee_info in company[search_info1[0]].items():
    print(employee_info['工号'], employee_info['姓名'], employee_info['性别'], employee_info['手机号'])

# 访问特定员工信息示例
search_info2 = ['财务部', '周九']
employee_info = company[search_info2[0]][search_info2[1]]
print(f"\n{search_info2[0]}的员工{search_info2[1]}，工号是 {employee_info['工号']}，手机号是 {employee_info['手机号']}")