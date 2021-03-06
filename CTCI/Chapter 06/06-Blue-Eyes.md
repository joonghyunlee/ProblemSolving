# 가정
* 각각은 다른 모든 사람의 눈동자 색을 안다.
* 자신의 눈동자 색은 알 수 없다.
* 다른 사람의 눈동자 색을 알려 줄 수 없다.
* 최소 한 명 이상의 파란색 눈동자가 있다는 사실을 안다.

# 풀이
* 파란색 눈동자를 가진 사람이 한 명인 경우 (n = 1)
  * 파란색 눈동자를 가진 사람은 파란색 눈동자가 존재하지 않는다는 사실을 확인할 수 있다.
  * 첫 날에 자신이 파란색 눈동자를 가졌다는 사실을 알 수 있다.
  * 즉, 모두 떠나는 데 하루가 걸린다.
* 파란색 눈동자를 가진 사람이 두 명인 경우 (n = 2)
  * 파란색 눈동자를 가진 사람이 한 명이상 확인할 수 있다.
  * 따라서 첫 날에는 아무도 떠나지 않는다.
  * 파란색 눈동자를 가진 사람은 파란색 눈동자를 가진 사람 한명만 확인할 수 있기 때문에, 첫 날에 떠날 것으로 예상한다.
    * 그러나 떠나지 않았다.
    * 따라서 자신도 파란색 눈동자를 가졌다는 것을 알게 된다.
    * 두 명 모두 둘째 날 떠나게 된다.
  * 파란색 눈동자를 가지지 않은 사람은 두 명의 파란색 눈동자를 가진 사람을 확인한다.
    * 첫 날에 떠날 것이라 생각하지 못한다.
    * 둘 째날 모두 함께 떠난다.
* 파란색 눈동자를 가진 사람이 k 명인 경우 (n = k)
  * 앞서의 방법과 같은 방법으로 파란색 눈동자를 가진 사람이 k명 이라면, k일째 날 모두 떠날 것으로 예상한다.
  * 파란색 눈동자를 가진 사람은 k-1 명만 확인할 수 있고, k-1일째 날 모두 떠날 것으로 예상한다.
    * 그러나 k-1일째 날 아무도 떠나지 않기 때문에 자신도 파란색 눈동자를 가진 것을 안다.
  * 따라서 k 명 모두 k일째 날 떠나게 된다.