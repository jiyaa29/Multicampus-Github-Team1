# 노트(note)를 정리하는 프로그램이다.
# 사용자는 노트에 콘텐츠를 적을 수 있다.
# 노트는 노트북(notebook)에 삽입된다.
# 노트북은 타이틀(title)이 있다.
# 노트북은 노트가 삽입될 때 페이지를 생성하며, 최대 300 페이지까지 저장할 수 였다.
# 300페이지를 넘기면 노트를 더는 삽입하지 못한다.

class Note(object):
    def __init__(self, contenst= None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = contents

    def remove_all(self):
        self.contents = None

    def __str__(self):
        return self.contents


class Notebook(object):
    def __init__(self, title, page_number, notes):
        self.title = title
        self.page_number = 0
        self.notes = {}

    def add_note(self, note):
        if self.page_number < 300:
            self.notes.append(note)
            self.page_number += 1
        else:
            print("저장할 수 없습니다.")

    def remove_note(self, note):
        self.notes.remove(note)
        self.page_number -= 1

    def __str__(self):
        return self.title + " " + str(self.page_number) + " " + str(self.notes)

    def get_number_of_pages(self):
        return self.page_number