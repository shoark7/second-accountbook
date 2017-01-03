from datetime import datetime
from Accountbook import AccountBook, help_method, DailyAccountBook,\
                        MonthlyAccountBook, YearlyAccountBook


TODAY = datetime.today()


book = AccountBook()
today_book = DailyAccountBook(TODAY.year, TODAY.month, TODAY.day)
book_this_year = book[TODAY.year]
book_this_month = book[TODAY.year][TODAY.month]


def app_start():
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

        """ Function 2. """
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

        """ Function 3."""
        elif user_choice == "3":
            pass

        elif user_choice == "4":
            pass

        elif user_choice == "5":
            pass

        elif user_choice == '6':
            pass

        else: # if user_choice = "7"
            print("프로그램을 종료합니다. 감사합니다.")
            program_stop = True


if __name__ == "__main__":
    app_start()
