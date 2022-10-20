# 使用python3编辑程序，一个小练习，非常糟糕，不是面向对象编程的
# 基本功能
# 1.读取excel表格财务数据
# 2.存储表格财务数据
# 3.对财务数据进行处理
# 4.输出资产负债表、利润表、现金流量表、重要的财务指标
# 5.退出系统

#正式代码

financial_data = [
     {
     'id' : '00001',
     '日期' : '2020-1-1',
     '编号' : '001',
     '摘要' : '向老妈借钱100元',
     '科目' : '货币资金',
     '借贷' : '借',
     '金额' : 100,
     },
     {
     'id': '00002',
     '日期' : '2020-1-1',
     '编号' : '001',
     '摘要' : '向老妈借钱100元',
     '科目' : '借款',
     '借贷' : '贷',
     '金额' : 100,
     },
     {
     'id' : '00003',
     '日期' : '2020-1-1',
     '编号' : '002',
     '摘要' : '买面包',
     '科目' : '生活支出',
     '借贷' : '借',
     '金额' : 5,
     },
     {
     'id' : '00004',
     '日期' : '2020-1-1',
     '编号' : '002',
     '摘要' : '买面包',
     '科目' : '货币资金',
     '借贷' : '贷',
     '金额' : 5,
     }
]

# 1.读取excel表格财务数据
# 美化显示
def beauty_print(financial_data_list):
     for index, record in enumerate(financial_data_list):  # financial_data_list是形参，不用定义
          print(f'序号：{index}', end='\t')
          print(f'日期：{record["日期"]}',end='\t')
          print(f'编号：{record["编号"]}',end='\t')
          print(f'摘要：{record["摘要"]}',end='\t')
          print(f'科目：{record["科目"]}',end='\t')
          print(f'借贷：{record["借贷"]}',end='\t')
          print(f'金额：{record["金额"]}')



#输入日期
def input_riqi():
     while True:
          riqi = input('输入日期：').strip()
          if riqi:
              return riqi
          else:
               continue


#选择科目
def choose_kemu():
     while True:
          print('1(货币资金)；2（借款）；3（生活支出）')
          n = input('选择性别：')
          if n == '1':
               return '货币资金'
          elif n == '2':
               return '借款'
          elif n == '3':
               return '生活支出'
          else:
               continue



# 显示所有财务数据
def show_all_financial_data():
     beauty_print(financial_data)



# 新建财务数据
def create_financial_data():
     riqi = input_riqi()
     bianhao = input('输入编号：')
     zhaiyao = input('输入摘要：')
     kemu = choose_kemu()
     jiedai = input('输入借贷：')
     jiner = input('输入金额：')
     record = {
          '日期':riqi,
          '编号':bianhao,
          '摘要':zhaiyao,
          '科目':kemu,
          '借贷':jiedai,
          '金额':jiner
     }
     financial_data.append(record)


# 查询财务数据
def find_financial_data():
     riqi = input('查询日期：')
     for record in financial_data:
          if record['日期'] == riqi:
               print(record)
               return
     else:
          print('查无此日期')
     bianhao = input('查询编号：')
     zhaiyao = input('查询摘要：')
     kemu = input('查询科目：')
     jiedai = input('查询借贷：')
     jiner = input('查询金额：')

# 修改财务数据
def modify_financial_data():
     riqi = input('查询日期：')
     for record in financial_data:
          if record['日期'] == riqi:
               print(record)
               record['日期'] = input('输入日期：')
               record['编号'] = input('输入编号：')
               record['摘要'] = input('输入摘要：')
               record['科目'] = input('输入科目：')
               record['借贷']  = input('输入借贷：')
               record['金额'] = input('输入金额：')
               return
     else:
          print('查无此日期')

# 删除财务数据
def remove_financial_data():
     riqi = input('查询日期：')
     for record in financial_data:
          if record['日期'] == riqi:
               print(record)
               financial_data.remove(record)
               return
     else:
          print('查无此日期')

# 2.存储表格财务数据
# 3.对财务数据进行处理
# 4.输出资产负债表、利润表、现金流量表、重要的财务指标
# 5.退出系统



while True:
      print(
          '''
          **************************************************
          欢迎使用【个人财务系统】Version 1.0
               1.读取excel表格财务数据
               # 显示所有财务数据
               # 新建财务数据
               # 查询财务数据
               # 修改财务数据
               # 删除财务数据
               2.存储表格财务数据
               3.对财务数据进行处理
               4.输出资产负债表、利润表、现金流量表、重要的财务指标
               5.退出系统
          **************************************************
          '''
     )
      operation = input('请输入序号：')
      if operation == '1':
           print('读取excel表格财务数据--待完善')
      elif operation == '显示':
           show_all_financial_data()
      elif operation == '新建':
           create_financial_data()
      elif operation == '查询':
           find_financial_data()
      elif operation == '修改':
           modify_financial_data()
      elif operation == '删除':
           remove_financial_data()
      elif operation == '2':
           print('存储表格财务数据--待完善')
      elif operation == '3':
           print('对财务数据进行处理--待完善')
      elif operation == '4':
           print('输出资产负债表、利润表、现金流量表、重要的财务指标--待完善')
      elif operation == '5':
           print('退出系统')
           break




# 1.读取excel表格财务数据
# 2.存储表格财务数据
# 3.对财务数据进行处理
# accounting_entries 会计分录
# 4.输出资产负债表balance_sheet、利润表income_statement、现金流量表cash_flow_statement、重要的财务指标
#liabilities负债、equity所有者权益、
# 5.退出系统

# input ("\n\n按下 enter 键后退出。")
