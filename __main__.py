from datetime import datetime
from Accountbook import AccountBook, help_method, DailyAccountBook,\
                        MonthlyAccountBook, YearlyAccountBook

TODAY = datetime.today()




def app_start():

    book = AccountBook()
    today_book = DailyAccountBook(TODAY.year, TODAY.month, TODAY.day)
    book_this_year = book[TODAY.year]
    book_this_month = book[TODAY.year][TODAY.month]

    print('\n', '-' * 50)
    print("반갑습니다. 박성환의 출금내용을 입력하거나 내용을 확인할 수 있습니다.\n\
          간단하지만 연도별, 월별, 일별 통계도 지원하니 꼭 확인해보시길 바랍니다.\n")

    program_stop = False
    USER_CHOICE = ["1", "2", "3", "4", "5", "6", "7",]

    while not program_stop:
        print("-" * 50)
        print("가지고 있는 기능은 다음과 같습니다.\n")
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
            print("지출 데이터를 입력합니다.\n금액과 사유를 ','로 구분해서 입력하세요.\n")
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
                break

            print("감사합니다. 입력을 마칩니다.\n")
            book = AccountBook()

        elif user_choice == "2":
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

            print("연도 요약 : 1")
            print("모든 월 요약 : 2")
            print("모든 월 출력 : 3")

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
            print("전체 통계를 출력합니다.")
            book.statistic_all()

        elif user_choice == '6':
            pass

        else: # if user_choice = "7"
            print("프로그램을 종료합니다. 감사합니다.")
            program_stop = True


if __name__ == "__main__":
    app_start()
