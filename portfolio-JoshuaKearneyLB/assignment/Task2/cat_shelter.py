import sys


def cat_visit_calc(file):

    own_cat_visits = 0
    other_cat_visits = 0
    time_spent_list = []
    tuple_list = []

    with open(file, 'r') as f:
        for line in f:
            tuple_list.append(line.split(','))

        for item in tuple_list[:-1]:
            if item[0] == "OURS":
                own_cat_visits += 1
                time_spent_list.append(int(item[2]) - int(item[1]))
            else:
                other_cat_visits += 1

        print(f"Cat visits: {own_cat_visits}")
        print(f"Other cats: {other_cat_visits}\n")
        print(f"Total time in house: {sum(time_spent_list) // 60} hours, {sum(time_spent_list) % 60} minutes\n")

        print(f"Average visit length: {round(sum(time_spent_list) / own_cat_visits)} minutes")
        time_spent_list.sort()
        print(f"Longest visit:        {time_spent_list[len(time_spent_list) - 1]} minutes")
        print(f"Longest visit:        {time_spent_list[0]} minutes")


if __name__ == '__main__':

    cat_log_file = " "

    try:
        cat_log_file = sys.argv[1]
    except IndexError:
        print("Missing command line argument!")
        exit()

    try:
        open(cat_log_file, 'r')
        print("Log file analysis")
        print("=================")
        cat_visit_calc(cat_log_file)

    except FileNotFoundError:
        print(f"Cannot open \"{cat_log_file}\" .")
        exit()







