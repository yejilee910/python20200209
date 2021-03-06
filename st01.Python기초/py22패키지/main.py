
# 패키지의 모듈을 사용해보겠습니다. 다음 내용을 프로젝트 폴더(C:\project) 안에 main.py 파일로 저장한 뒤 실행해보세요(main.py 파일을 game.graphic 패키지 폴더 안에 넣으면 안 됩니다).
#
# import 패키지.모듈
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()
# main.py


# game.graphic 패키지의 geometry 모듈을 가져옴
import game.graphic.geometry
import game.graphic.test

# game.sound 패키지의 echo 모듈을 가져옴
import game.sound.echo
import game.sound.test

# game.operation 패키지의 run 모듈을 가져옴
import game.operation.run
import game.operation.test

# game.graphic 패키지 geometry 모듈의 triangle_area 함수 사용
print(game.graphic.geometry.triangle_area(30, 40))

# game.graphic 패키지 geometry 모듈의 rectangle_area 함수 사용
print(game.graphic.geometry.rectangle_area(30, 40))

# game.graphic 패키지 test 모듈의 test_graphic 함수 사용
print(game.graphic.test.test_graphic())

# game.operation 패키지 run 모듈의 render_test 함수 사용
print(game.operation.run.render_test())
