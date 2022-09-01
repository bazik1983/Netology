import numpy as np

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)
next_user_stats = np.array([0, 1, 2, 0, 0, 0])


def cosine(users_stats, next_user_stats):
    # длины векторов
    users_stats_Length = np.linalg.norm(users_stats)
    next_user_stats_Length = np.linalg.norm(next_user_stats)

    return np.dot(users_stats, next_user_stats) / (users_stats_Length * next_user_stats_Length)


muls = np.apply_along_axis(cosine, 1, users_stats, next_user_stats)
best_user = np.argmax(muls)
print('Самый похожий пользователь: ', best_user)
