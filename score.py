from utils import score_file_path, bad_return_code


def add_score(difficulty):
    score = get_score()

    if score['error_code']:
        raise Exception("Something went wrong")

    points = difficulty * 3 + 5
    new_score = score['score'] + points

    file = open(score_file_path, 'w')
    file.write(str(new_score))
    file.close()

    return new_score


def get_score():
    try:
        file = open(score_file_path, 'r')
        score = int(file.read())
        file.close()

        return {
            "success": True,
            "score": score,
            "error_code": None,
        }
    except:
        return {
            'success': False,
            "score": None,
            'error_code': bad_return_code
        }
