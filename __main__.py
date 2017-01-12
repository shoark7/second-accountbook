from datetime import datetime
from .Accountbook import AccountBook, DailyAccountBook,\
                        MonthlyAccountBook, YearlyAccountBook

TODAY = datetime.today()


def app_start():

    book = AccountBook()
    today_book = DailyAccountBook(TODAY.year, TODAY.month, TODAY.day)
    book_this_year = YearlyAccountBook(TODAY.year)
    book_this_month = MonthlyAccountBook(TODAY.year, TODAY.month)

    print('\n', '-' * 80)
    print("   반갑습니다. 박성환의 출금내용을 입력하거나 내용을 확인할 수 있습니다.\n\
   간단하지만 연도별, 월별, 일별 통계도 지원하니 꼭 확인해보시길 바랍니다.\n")

    program_stop = False
    USER_CHOICE = ["1", "2", "3", "4", "5", "6", "7",]

    while not program_stop:
        print("-" * 50)
        print("\n가지고 있는 기능은 다음과 같습니다.\n")
        print("1. 오늘 지출 입력")
        print("2. 일별 통계")
        print("3. 월별 통계")
        print("4. 연도별 통계")
        print("5. 전체 통계")
        print("6. 데이터 수정")
        print("7. 종료")

        user_choice = input("\n원하시는 기능을 입력해주세요. : ")
        while user_choice not in USER_CHOICE:
            user_choice = input("잘못 입력하셨습니다. 다시 입력하세요 : ")

        """ Function 1. """
        if user_choice == "1":
            print()
            print('-' * 50)
            print("\n지출 데이터를 입력합니다.\n금액과 사유를 ','로 구분해서 입력하세요.\n")
            while True:
                money, reason = input("입력 : ").split(',')
                if ',' in reason or not money.isnumeric():
                    print("형식을 맞춰서, 다시 입력해주세요.")
                    continue
                money = int(money)
                reason = reason.strip()
                today_book.add_data(money, reason)

                re_entry = input("저장되었습니다. 더 입력하시려면 'y'를 누르세요 : ")
                if re_entry.lower() == 'y':
                    continue

                today_book.save_data()
                today_book.average_data()
                book_this_year = YearlyAccountBook(TODAY.year)
                book_this_month = MonthlyAccountBook(TODAY.year, TODAY.month)
                book = AccountBook()
                break

            print("감사합니다. 입력을 마칩니다.\n")
            book = AccountBook()

        elif user_choice == "2":
            print()
            print('-' * 50)
            print("\n일일 통계를 지원합니다.\n원하는 날짜를 입력해주세요. 기본은 오늘입니다.")
            wanted_date = input("입력(ex. 2016/03/01) : ").strip()

            if wanted_date == '':
                today_book.statistic_day()

            else:
                try:
                    year, month, day = [int(e) for e in wanted_date.split('/')]
                    wanted_book = DailyAccountBook(year, month, day)
                    wanted_book.statistic_day()
                except:
                    print("잘못 입력하셨습니다. 메인으로 돌아갑니다.\n\n")

        elif user_choice == "3":
            print()
            print('-' * 50)
            print("\n월별 통계를 지원합니다.")
            print("원하시는 연도, 월을 입력해주세요. 기본은 {}년 {}월입니다."\
                  .format(TODAY.year, TODAY.month))
            wanted_month = input("입력(ex. 2016/02) : \n")

            if wanted_month == '':
                year = TODAY.year
                month = TODAY.month
                wanted_book = book_this_month

            else:
                try:
                    year, month = [int(e) for e in wanted_month.split('/')]
                    wanted_book = MonthlyAccountBook(year, month)
                except:
                    print("잘못 입력하셨습니다. 메인으로 돌아갑니다.\n\n")
                    continue

            print("{}년 {}월의 통계를 출력합니다.".format(year, month))
            print("원하시는 통계 유형을 선택해주세요.(기본: 1)\n")
            print("1. 월 요약")
            print("2. 월내 모든 데이터")
            wanted_mode = input("\n입력 : ")

            if wanted_mode == '2':
                wanted_book.statistic_day_all()

            else:
                wanted_book.statistic_month()

        elif user_choice == "4":
            print()
            print('-' * 50)
            print("\n연도별 통계를 지원합니다.")
            print("원하시는 연도를 입력해주세요. 기본은 {}년입니다.".format(TODAY.year))

            wanted_year = input("입력(ex. 2016) : ")
            print()

            if wanted_year == '':
                year = TODAY.year
                wanted_book = book_this_year

            else:
                try:
                    year = int(wanted_year)
                    wanted_book = YearlyAccountBook(year)
                except:
                    print("잘못 입력하셨습니다. 메인으로 돌아갑니다.\n\n")
                    continue

            print("{}년의 통계를 출력합니다.".format(year))
            print("원하시는 통계 유형을 선택해주세요.(기본: 1)\n")

            print("1. 연도 요약")
            print("2. 모든 월 요약")
            print("3. 모든 월 출력")

            wanted_mode = input("\n입력 : ").strip()

            while True:
                if wanted_mode not in ["1", "2", "3"]:
                    wanted_mode = input("\n잘못된 입력입니다. 다시 입력하세요. : ").strip()
                    continue

                if wanted_mode == "1":
                    wanted_book.statistic_year()
                    break

                elif wanted_mode == "2":
                    wanted_book.statistic_month()
                    break

                else:
                    wanted_book.statistic_month_all()
                    break

        elif user_choice == "5":
            print()
            print('-' * 50)
            print("\n전체 통계를 출력합니다.")
            book.statistic_all()

        elif user_choice == '6':
            print()
            print('-' * 50)
            print("\n데이터를 수정하거나 삭제합니다.")
            print("원하시는 날짜를 입력해주세요. 기본은 '오늘'입니다.")
            date = input("입력(ex. 2016/12/31) : ").strip()

            if date == '':
                day_book = today_book
                year = TODAY.year
                month = TODAY.month
                day = TODAY.day

            else:
                while date.count('/') != 2:
                    print("\n잘못된 형식입니다. 다시 입력해주세요.")
                date = input("입력(ex. 2016/12/31) : ").strip()
                print()

                year, month, day = [e for e in date.split('/')]

                try:
                    day_book = book[int(year)][int(month)][int(day)]
                    assert day_book
                except:
                    continue

            print("\n{}년 {}월 {}일의 데이터가 존재합니다.".format(year, month, day))
            print("1. 삭제\n2. 수정")
            wanted_mode = input("입력 : ").strip()

            while wanted_mode not in ["1", "2"]:
                wanted_mode = input("원하시는 기능을 다시 선택해주세요. : ").strip()

            print()
            day_book.statistic_day()

            print('\n{}할 데이터의 번호를 선택해주세요 : '.\
                 format("삭제" if wanted_mode == '1' else "수정"))

            data = day_book.data['records']
            wanted_entry = input("입력 : ").strip()

            while wanted_entry not in [str(n) for n in range(1, len(data)+1)]:
                wanted_entry = input("번호를 올바르게 다시 입려해주세요. : ")

            wanted_data = data[int(wanted_entry) - 1]
            print('\n{}에 {:,}원을 사용하셨습니다.'.format(wanted_data['reason'], wanted_data['money']))

            if wanted_mode == "1":
                delete_or_not = input("정말 삭제하시겠습니까?(y/n) : ").strip()
                if delete_or_not.lower() == 'y':
                    data.pop(int(wanted_entry) - 1)
                    day_book.data['records'] = data
                    day_book.save_data()
                    day_book.average_data()
                    print("정상적으로 삭제되었습니다.")
                else:
                    print("취소합니다. 메인으로 돌아갑니다...")

            else:
                print("금액을 수정합니다.")
                print("\n정수 단위 금액을 입력하세요. 입력 안 하시면 수정하지 않습니다.")
                record = data[int(wanted_entry) - 1]

                new_money = input("입력 : ")

                if new_money.isnumeric():
                    new_money = int(new_money)

                elif not new_money:
                    pass
                else:
                    while not new_money.isnumeric():
                        new_money = input("금액을 제대로 입력하세요. : ")
                    new_money = int(new_money)

                print("\n사유를 수정합니다. 입력하지 않으면 수정하지 않습니다.")
                new_reason = input("입력 : ")

                if new_money:
                    record['money'] = new_money

                if new_reason:
                    record['reason'] = new_reason

                day_book.data['records'] = data
                day_book.save_data()
                day_book.average_data()
                print("정상적으로 수정되었습니다.")

        else:  # if user_choice = "7"
            print("프로그램을 종료합니다. 감사합니다.")
            program_stop = True


if __name__ == "__main__":
    app_start()
