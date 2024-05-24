import pandas as pd

rowdata = {
    "电影名称": ["无问西东", "后来的我们", "前任3", "红海行动", "唐人街探案", "战狼2"],
    "打斗镜头": [1, 5, 12, 108, 112, 115],
    "接吻镜头": [101, 89, 97, 5, 9, 8],
    "电影类型": ["爱情片", "爱情片", "爱情片", "动作片", "动作片", "动作片"],
}
new_data = [24, 67]
movie_data = pd.DataFrame(rowdata)


#
def classify0(inX, dataSet, k):
    result = []
    dist = list((((dataSet.iloc[:, 1:3] - inX) ** 2).sum(1)) ** 0.5)
    dist_l = pd.DataFrame({"dist": dist, "labels": (dataSet.iloc[:, 3])})
    dr = dist_l.sort_values(by="dist")[:k]
    re = dr.loc[:, "labels"].value_counts()
    result.append(re.index[0])
    return result


if __name__ == "__main__":
    inX = new_data
    dataSet = movie_data
    k = 3
    res = classify0(inX, dataSet, k)
    print(res)
