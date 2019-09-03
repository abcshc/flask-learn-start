# content of test_sample.py
def func(x):
    return x + 1

def sort_result(result):
    """
    정렬
    input data type(dictionary)
    [{
        name: "소희철"
        cnt: 5
        time: 4
    }]
    
    """
    return sorted(result, key=lambda k: (k['count'], k['time']))

def test_answer():
    assert func(3) == 4

def test_sort_result():
    result1 = [
        {"name": "소희철", "count": 5, "time": 4},
        {"name": "이진희", "count": 4, "time": 8},
        {"name": "강경연", "count": 6, "time": 1},
        {"name": "조성준", "count": 5, "time": 2}
    ]
    sorted1 = [
        {"name": "이진희", "count": 4, "time": 8},
        {"name": "조성준", "count": 5, "time": 2},
        {"name": "소희철", "count": 5, "time": 4},
        {"name": "강경연", "count": 6, "time": 1}

    ]
    for info in sorted1:
        print(f'이름: {info["name"]}, 횟수: {info["count"]}, 시간: {info["time"]}')
    assert sort_result(result1) == sorted1