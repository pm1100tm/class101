import os
import django
import traceback
import backend101.settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend101.settings')
django.setup()

from django.db.models import Max
from django.db        import transaction

from menu.models import *


def add_main_menu():
    """ 메인 메뉴 생성
    author: swd
    updater: swd
    created_at: 2021.09.17
    updated_at: 2021.09.17
    history:
        -
    """
    MainMenu.objects.create(id=1, name='이벤트')
    MainMenu.objects.create(id=2, name='바로 수강')
    MainMenu.objects.create(id=3, name='신규 클래스')
    MainMenu.objects.create(id=4, name='오픈 예정')
    MainMenu.objects.create(id=5, name='시그니처')
    MainMenu.objects.create(id=6, name='키즈')
    MainMenu.objects.create(id=7, name='Created by')

def add_first_category():
    """ 전체 카테고리 중 첫 번째 카테고리 생성
    author: swd
    updater: swd
    created_at: 2021.09.17
    updated: 2021.09.17
    history:
        -
    """
    FirstCategory.objects.create(id=1, index_number=1, name='크리에이티브')
    FirstCategory.objects.create(id=2, index_number=2, name='수익 창출')
    FirstCategory.objects.create(id=3, index_number=3, name='커리어')
    FirstCategory.objects.create(id=4, index_number=4, name='키즈')
    FirstCategory.objects.create(id=5, index_number=5, name='준비물/키트')

def add_second_category():
    """ 전체 카테고리 중 두번째 카테고리 생성
    author: swd
    updater: swd
    created_at: 2021.09.17
    updated: 2021.09.17
    history:
        -
    """
    first_category_1 = FirstCategory.objects.get(name='크리에이티브')
    SecondCategory.objects.create(first_category=first_category_1, id=1, index_number=1, name='디지털드로잉')
    SecondCategory.objects.create(first_category=first_category_1, id=2, index_number=2, name='드로잉')
    SecondCategory.objects.create(first_category=first_category_1, id=3, index_number=3, name='공예')
    SecondCategory.objects.create(first_category=first_category_1, id=4, index_number=4, name='요리•음료')
    SecondCategory.objects.create(first_category=first_category_1, id=5, index_number=5, name='베이킹•디저트')
    SecondCategory.objects.create(first_category=first_category_1, id=6, index_number=6, name='음악')
    SecondCategory.objects.create(first_category=first_category_1, id=7, index_number=7, name='운동')
    SecondCategory.objects.create(first_category=first_category_1, id=8, index_number=8, name='라이프')
    SecondCategory.objects.create(first_category=first_category_1, id=9, index_number=9, name='사진•영상')

    first_category_2 = FirstCategory.objects.get(name='수익 창출')
    SecondCategory.objects.create(first_category=first_category_2, id=10, index_number=10, name='금융•재테크')
    SecondCategory.objects.create(first_category=first_category_2, id=11, index_number=11, name='창업•부업')
    SecondCategory.objects.create(first_category=first_category_2, id=12, index_number=12, name='성공 마인드')

    first_category_3 = FirstCategory.objects.get(name='커리어')
    SecondCategory.objects.create(first_category=first_category_3, id=13, index_number=13, name='디자인')
    SecondCategory.objects.create(first_category=first_category_3, id=14, index_number=14, name='개발•데이터')
    SecondCategory.objects.create(first_category=first_category_3, id=15, index_number=15, name='직무교육')
    SecondCategory.objects.create(first_category=first_category_3, id=16, index_number=16, name='글쓰기')
    SecondCategory.objects.create(first_category=first_category_3, id=17, index_number=17, name='언어•외국어')

    first_category_4 = FirstCategory.objects.get(name='키즈')
    SecondCategory.objects.create(first_category=first_category_4, id=18, index_number=18, name='아동 교육')

def add_third_category():
    """ 전체 카테고리 중 세번째 카테고리 생성
    author: swd
    updater: swd
    created_at: 2021.09.17
    updated: 2021.09.17
    history:
        -
    """
    second_category_1 = SecondCategory.objects.get(name='디지털드로잉')
    ThirdCategory.objects.create(second_category=second_category_1, id=1, index_number=1, name='일러스트')
    ThirdCategory.objects.create(second_category=second_category_1, id=2, index_number=2, name='컨셉아트')
    ThirdCategory.objects.create(second_category=second_category_1, id=3, index_number=3, name='캐릭터 드로잉')
    ThirdCategory.objects.create(second_category=second_category_1, id=4, index_number=4, name='인물 드로잉')
    ThirdCategory.objects.create(second_category=second_category_1, id=5, index_number=5, name='굿즈.이모티콘')
    ThirdCategory.objects.create(second_category=second_category_1, id=6, index_number=6, name='웹툰')
    ThirdCategory.objects.create(second_category=second_category_1, id=7, index_number=7, name='캘리그라피')
    ThirdCategory.objects.create(second_category=second_category_1, id=8, index_number=8, name='더 새로운 디지털 드로잉')

    second_category_2 = SecondCategory.objects.get(name='드로잉')
    ThirdCategory.objects.create(second_category=second_category_2, id= 9, index_number= 9, name='펜•연필')
    ThirdCategory.objects.create(second_category=second_category_2, id=10, index_number=10, name='마카')
    ThirdCategory.objects.create(second_category=second_category_2, id=11, index_number=11, name='색연필')
    ThirdCategory.objects.create(second_category=second_category_2, id=12, index_number=12, name='수채화')
    ThirdCategory.objects.create(second_category=second_category_2, id=13, index_number=13, name='오일파스텔')
    ThirdCategory.objects.create(second_category=second_category_2, id=14, index_number=14, name='과슈•아크릴화')
    ThirdCategory.objects.create(second_category=second_category_2, id=15, index_number=15, name='유화')
    ThirdCategory.objects.create(second_category=second_category_2, id=16, index_number=16, name='동양화')
    ThirdCategory.objects.create(second_category=second_category_2, id=17, index_number=17, name='캘리그라피')
    ThirdCategory.objects.create(second_category=second_category_2, id=18, index_number=18, name='더 새로운 디지털 드로잉')

    second_category_3 = SecondCategory.objects.get(name='공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=19, index_number=19, name='대바늘 뜨개')
    ThirdCategory.objects.create(second_category=second_category_3, id=20, index_number=20, name='코바늘 뜨개')
    ThirdCategory.objects.create(second_category=second_category_3, id=21, index_number=21, name='자수')
    ThirdCategory.objects.create(second_category=second_category_3, id=22, index_number=22, name='실 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=23, index_number=23, name='패브릭 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=24, index_number=24, name='비누 .캔들 .향')
    ThirdCategory.objects.create(second_category=second_category_3, id=25, index_number=25, name='나무 .라탄 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=26, index_number=26, name='가죽 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=27, index_number=27, name='레진 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=28, index_number=28, name='도예')
    ThirdCategory.objects.create(second_category=second_category_3, id=29, index_number=29, name='플라워 공예')
    ThirdCategory.objects.create(second_category=second_category_3, id=30, index_number=30, name='더 새로운 공예')

    second_category_4 = SecondCategory.objects.get(name='요리•음료')
    ThirdCategory.objects.create(second_category=second_category_4, id=31, index_number=31, name='한식')
    ThirdCategory.objects.create(second_category=second_category_4, id=32, index_number=32, name='일식•중식')
    ThirdCategory.objects.create(second_category=second_category_4, id=33, index_number=33, name='양식')
    ThirdCategory.objects.create(second_category=second_category_4, id=34, index_number=34, name='세계요리')
    ThirdCategory.objects.create(second_category=second_category_4, id=35, index_number=35, name='건강•다이어트식')
    ThirdCategory.objects.create(second_category=second_category_4, id=36, index_number=36, name='비건•채소')
    ThirdCategory.objects.create(second_category=second_category_4, id=37, index_number=37, name='도시락•케이터링')
    ThirdCategory.objects.create(second_category=second_category_4, id=38, index_number=38, name='음료•술')
    ThirdCategory.objects.create(second_category=second_category_4, id=39, index_number=39, name='더 새로운 요리 음료')

    second_category_5 = SecondCategory.objects.get(name='베이킹•디저트')
    ThirdCategory.objects.create(second_category=second_category_5, id=40, index_number=40, name='케이크')
    ThirdCategory.objects.create(second_category=second_category_5, id=41, index_number=41, name='제과')
    ThirdCategory.objects.create(second_category=second_category_5, id=42, index_number=42, name='제빵')
    ThirdCategory.objects.create(second_category=second_category_5, id=43, index_number=43, name='떡•전통다과')
    ThirdCategory.objects.create(second_category=second_category_5, id=44, index_number=44, name='비건')
    ThirdCategory.objects.create(second_category=second_category_5, id=45, index_number=45, name='더 새로운 베이킹•디저트')

    second_category_6 = SecondCategory.objects.get(name='음악')
    ThirdCategory.objects.create(second_category=second_category_6, id=46, index_number=46, name='악기')
    ThirdCategory.objects.create(second_category=second_category_6, id=47, index_number=47, name='보컬•랩')
    ThirdCategory.objects.create(second_category=second_category_6, id=48, index_number=48, name='작곡•프로듀싱')

    second_category_7 = SecondCategory.objects.get(name='운동')
    ThirdCategory.objects.create(second_category=second_category_7, id=49, index_number=49, name='요가')
    ThirdCategory.objects.create(second_category=second_category_7, id=50, index_number=50, name='필라테스')
    ThirdCategory.objects.create(second_category=second_category_7, id=51, index_number=51, name='발레')
    ThirdCategory.objects.create(second_category=second_category_7, id=52, index_number=52, name='순환•스트레칭')
    ThirdCategory.objects.create(second_category=second_category_7, id=53, index_number=53, name='재활•자세•개선')
    ThirdCategory.objects.create(second_category=second_category_7, id=54, index_number=54, name='피트니스')
    ThirdCategory.objects.create(second_category=second_category_7, id=55, index_number=55, name='러닝 사이클')
    ThirdCategory.objects.create(second_category=second_category_7, id=56, index_number=56, name='스포츠')
    ThirdCategory.objects.create(second_category=second_category_7, id=57, index_number=57, name='더 새로운 운동')

    second_category_8 = SecondCategory.objects.get(name='라이프')
    ThirdCategory.objects.create(second_category=second_category_8, id=58, index_number=58, name='뷰티')
    ThirdCategory.objects.create(second_category=second_category_8, id=59, index_number=59, name='영상')
    ThirdCategory.objects.create(second_category=second_category_8, id=60, index_number=60, name='심리')
    ThirdCategory.objects.create(second_category=second_category_8, id=61, index_number=61, name='타로•사주•운세')
    ThirdCategory.objects.create(second_category=second_category_8, id=62, index_number=62, name='게임•e스포츠')
    ThirdCategory.objects.create(second_category=second_category_8, id=63, index_number=63, name='라이프•해킹')
    ThirdCategory.objects.create(second_category=second_category_8, id=64, index_number=64, name='댄스•무용')
    ThirdCategory.objects.create(second_category=second_category_8, id=65, index_number=65, name='반려동물')
    ThirdCategory.objects.create(second_category=second_category_8, id=66, index_number=66, name='인문학')
    ThirdCategory.objects.create(second_category=second_category_8, id=67, index_number=67, name='더 새로운 라이프')

    second_category_9 = SecondCategory.objects.get(name='사진•영상',)
    ThirdCategory.objects.create(second_category=second_category_9, id=68, index_number=68, name='사진')
    ThirdCategory.objects.create(second_category=second_category_9, id=69, index_number=69, name='영상')


def create_data():
    try:
        print('*'*80)
        print("데이터를 생성합니다.")
        
        add_main_menu()
        print("add_main_menu 데이터가 생성되었습니다.")
        
        add_first_category()
        print("add_first_category 데이터가 생성되었습니다.")
        
        add_second_category()
        print("add_second_category 데이터가 생성되었습니다.")
        
        add_third_category()
        print("add_third_category 데이터가 생성되었습니다.")
        
    except Exception as e:
        print('*' * 80)
        print('데이터 생성 중 오류가 발생하였습니다. 롤백합니다.')
        print(str(e))
        traceback.print_exc()
        transaction.rollback()

create_data()
