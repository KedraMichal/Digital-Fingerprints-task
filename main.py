from snowflake import SnowflakeController

if __name__ == '__main__':
    input_ = [[3, 10, 9, 6, 4, 8], [4, 7, 8, 5, 6, 10], [4, 3, 2, 10, 2, 10], [8, 6, 7, 2, 8, 2],
              [5, 1, 8, 9, 4, 1], [9, 3, 5, 10, 2, 3], [2, 7, 4, 8, 9, 4], [3, 4, 7, 1, 3, 4],
              [6, 9, 10, 3, 8, 4], [4, 1, 3, 4, 8, 4], [1, 3, 3, 2, 7, 2], [8, 9, 4, 1, 5, 1]]
    result = SnowflakeController(input_).find_the_same_snowflakes()
    print(result)

