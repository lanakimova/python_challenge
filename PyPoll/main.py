import csv
import os


# Function get dictionary with votes for each candidate and total number of votes and calculate percents
def get_votes_percent(votes_dict, total_votes):
    results_in_percent = {}
    for candidate in votes_dict:
        results_in_percent[candidate] = round((votes_dict[candidate] / total_votes) * 100, 3)

    return results_in_percent


# Function return winner
def get_winner(votes_dict):
    # found who get the most votes in dictionary
    winner = max(votes_dict, key=votes_dict.get)
    # return winner's name
    return winner


def main():
    # path to data file
    csv_path = os.path.join('Resources', 'election_data.csv')

    # declare dictionary to save votes for each candidate
    votes_summary = {}
    # read data from file and count votes for each candidate
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        for row in csv_reader:
            if row[2] not in votes_summary:
                votes_summary[row[2]] = 1
            elif row[2] in votes_summary:
                votes_summary[row[2]] += 1

    total_votes = 0
    for candidate in votes_summary:
        total_votes += votes_summary[candidate]

    percent_votes = get_votes_percent(votes_summary, total_votes)

    print("Election Results")
    print("-------------------------")
    print(f'Total votes: {total_votes}')
    print("-------------------------")

    for key in percent_votes:
        print(f'{key}: {percent_votes[key]}% {votes_summary[key]}')

    print("-------------------------")
    print(f'Winner: {get_winner(percent_votes)}')

    # Write result to a file
    with open('Analysis/vote_report.csv', 'w') as writer:
        # declare variable nxt_ln because F-String doesn't accept backslash.
        nxt_ln = '\n'
        writer.write(f"Election Results {nxt_ln}")
        writer.write(f"------------------------- {nxt_ln}")
        writer.write(f'Total votes: {total_votes} {nxt_ln}')
        writer.write(f"-------------------------{nxt_ln}")

        for key in percent_votes:
            writer.write(f'{key}: {percent_votes[key]}% {votes_summary[key]} {nxt_ln}')

        writer.write(f"-------------------------{nxt_ln}")
        writer.write(f'Winner: {get_winner(percent_votes)} {nxt_ln}')

    if __name__ == '__main__':
        main()


main()
