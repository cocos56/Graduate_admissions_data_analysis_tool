raw = r'<option value="0251">(0251)金融</option><option value="0252">(0252)应用统计</option><option value="0253">(0253)税务</option><option value="0254">(0254)国际商务</option><option value="0255">(0255)保险</option><option value="0256">(0256)资产评估</option><option value="0257">(0257)审计</option><option value="0351">(0351)法律</option><option value="0352">(0352)社会工作</option><option value="0353">(0353)警务</option><option value="0451">(0451)教育</option><option value="0452">(0452)体育</option><option value="0453">(0453)汉语国际教育</option><option value="0454">(0454)应用心理</option><option value="0551">(0551)翻译</option><option value="0552">(0552)新闻与传播</option><option value="0553">(0553)出版</option><option value="0651">(0651)文物与博物馆</option><option value="0851">(0851)建筑学</option><option value="0853">(0853)城市规划</option><option value="0854">(0854)电子信息</option><option value="0855">(0855)机械</option><option value="0856">(0856)材料与化工</option><option value="0857">(0857)资源与环境</option><option value="0858">(0858)能源动力</option><option value="0859">(0859)土木水利</option><option value="0860">(0860)生物与医药</option><option value="0861">(0861)交通运输</option><option value="0951">(0951)农业</option><option value="0952">(0952)兽医</option><option value="0953">(0953)风景园林</option><option value="0954">(0954)林业</option><option value="1051">(1051)临床医学</option><option value="1052">(1052)口腔医学</option><option value="1053">(1053)公共卫生</option><option value="1054">(1054)护理</option><option value="1055">(1055)药学</option><option value="1056">(1056)中药学</option><option value="1057">(1057)中医</option><option value="1151">(1151)军事</option><option value="1251">(1251)工商管理</option><option value="1252">(1252)公共管理</option><option value="1253">(1253)会计</option><option value="1254">(1254)旅游管理</option><option value="1255">(1255)图书情报</option><option value="1256">(1256)工程管理</option><option value="1351">(1351)艺术</option></select>'

from V3_0.Selector.api import findAllWithRe

data = findAllWithRe(raw, r"<option value=\"(\d+)\">")
# print("len=", len(data))
c = 0
for i in data:
	print("'%s'," % i, end=' ')
	c+=1
	if c%10==0:
		print()
