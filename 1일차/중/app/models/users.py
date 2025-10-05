# app/models/users.py

import random


class UserModel:
    _data = []  # 전체 사용자 데이터를 저장하는 리스트
    _id_counter = 1  # ID 자동 증가를 위한 카운터

    def __init__(self, username, age, gender):
        self.id = UserModel._id_counter
        self.username = username
        self.age = age
        self.gender = gender

        # 클래스가 인스턴스화 될 때 _data에 추가하고 _id_counter를 증가시킴
        UserModel._data.append(self)
        UserModel._id_counter += 1

    @classmethod
    # 데코레이터를 사용함으로써 인스턴스 객체를 생성하지 않아도 됨
    # 함수가 실행될때마다 인스턴스가 생성됬다 판단, _data에 추가하고 _id_counter를 증가 실행
    def create(cls, username, age, gender):
        """새로운 유저 추가"""
        return cls(username, age, gender)

    @classmethod
    def get(cls, **kwargs):
        # 키워드 인자(= 이름을 지정한 인자)를 딕셔너리(dict)로 받는다
        """단일 객체를 반환 (없으면 None)"""
        for user in cls._data:
            if all(getattr(user, key) == value for key, value in kwargs.items()):
                # getattr(객체,문자열로 된 속성 이름)
                ## key라는 속석이름의 내용을 뽑아냄 즉, value값
                # kwargs.items() : 딕셔너리의 (키, 값) 쌍을 반환
                ## key="username" value="kihoon"
                ### 즉, value값 비교하는거임
                return user
        return None

    @classmethod
    def filter(cls, **kwargs):
        """조건에 맞는 객체 리스트 반환"""
        return [user for user in cls._data if all(getattr(user, key) == value for key, value in kwargs.items())]

    def update(self, **kwargs):
        """객체의 필드 업데이트"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                # hasattr(object, name) : 객체가 특정속성을 가지고 있는지 확인
                ## 있으면 True 없으면 False
                if value is not None:
                    setattr(self, key, value)

    def delete(self):
        """현재 인스턴스를 _data 리스트에서 삭제"""
        if self in UserModel._data:
            UserModel._data.remove(self)

    @classmethod
    def all(cls):
        """모든 사용자 반환"""
        return cls._data

    @classmethod
    def create_dummy(cls):
        for i in range(1, 11):
            cls(username=f"dummy{i}", age=15 + i, gender=random.choice(["male", "female"]))

    def __repr__(self):
        return f"UserModel(id={self.id}, username='{self.username}', age={self.age}, gender='{self.gender}')"

    def __str__(self):
        return self.username
