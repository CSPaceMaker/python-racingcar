import pytest

# split 메서드를 사용하여 주어진 값을 구분하는 테스트
def test_split_메서드로_값_구분():
    """
    'split' 메서드를 사용하여 문자열을 쉼표로 구분하는 테스트입니다.
    결과로 분리된 값이 예상대로 반환되는지 확인합니다.
    """
    input_str = "1,2"
    result = input_str.split(',')

    # 값이 올바르게 포함되어 있는지 확인
    assert "2" in result
    # 정확하게 구분되었는지 확인
    assert result == ["1", "2"]

# split 메서드 사용 시 구분자가 없는 경우의 테스트
def test_split_메서드_구분자_없을때_그대로_반환():
    """
    'split' 메서드 사용 시 구분자가 없을 경우,
    입력값이 그대로 반환되는지 확인하는 테스트입니다.
    """
    input_str = "1"
    result = input_str.split(',')

    # 값이 그대로 반환되었는지 확인
    assert "1" in result

# substring 메서드를 사용하여 특정 구간 값을 반환하는 테스트
def test_substring_메서드로_특정_구간_반환():
    """
    Python의 슬라이싱을 사용하여 특정 구간의 값을 반환하는 테스트입니다.
    문자열에서 (1,2) 구간을 추출하여 '1,2'가 반환되는지 확인합니다.
    """
    input_str = "(1,2)"
    result = input_str[1:4]  # 슬라이싱을 사용하여 1부터 4 전까지 추출

    # 구간이 올바르게 추출되었는지 확인
    assert result == "1,2"

# charAt 메서드를 사용하여 특정 위치의 문자를 찾는 테스트
def test_charAt_메서드_특정_위치_문자_찾기():
    """
    문자열에서 특정 위치의 문자를 찾는 테스트입니다.
    'abc' 문자열에서 첫 번째 문자가 'a'인지 확인합니다.
    """
    input_str = "abc"
    char_at_element = input_str[0]  # Python에서는 인덱스 접근을 통해 첫 번째 문자 추출

    # 첫 번째 문자가 'a'인지 확인
    assert char_at_element == 'a'

# charAt 메서드에서 문자열의 길이보다 큰 위치의 문자를 찾을 때 예외 처리 테스트
def test_charAt_메서드_위치_잘못된_경우_예외():
    """
    문자열의 길이를 초과하는 위치에서 문자를 찾으려 할 때,
    'IndexError'가 발생하는지 확인하는 테스트입니다.
    """
    input_str = "abc"

    # 문자열 범위를 벗어나는 위치에 접근할 때 예외가 발생하는지 확인
    with pytest.raises(IndexError, match="string index out of range"):
        _ = input_str[5]
