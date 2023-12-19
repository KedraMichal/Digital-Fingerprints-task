class Snowflake:
    def __init__(self, arms: list):
        self.arms = arms
        self._validate_arms_type()

    def _validate_arms_type(self) -> None:
        if type(self.arms) != list:
            raise TypeError('Expected type list for arms')
        if len(self.arms) != 6:
            raise ValueError('Expected list of length = 6')
        for arm in self.arms:
            if type(arm) != int:
                raise TypeError('Expected type int for arm')
            elif not 0 < arm <= 10:
                raise ValueError('Expected arms values to be between (0,10]')

    def _move_right_arms_coordinate(self) -> None:
        last_arm = self.arms.pop()
        self.arms.insert(0, last_arm)

    def _reverse_snowflake_formula(self) -> list:
        return list(reversed(self.arms))

    def find_all_equal_snowflakes(self) -> list:
        equal_snowflakes = [self.arms.copy(), self._reverse_snowflake_formula()]
        for i in range(5):
            self._move_right_arms_coordinate()
            equal_snowflakes.extend([self.arms.copy(), self._reverse_snowflake_formula()])
        return equal_snowflakes

    def __eq__(self, other) -> bool:
        if self.arms in other.find_all_equal_snowflakes():
            return True
        return False


class SnowflakeController:
    def __init__(self, snowflakes_list: list):
        self._validate_snowflakes_type(snowflakes_list)
        self.snowflakes = [Snowflake(snowflake) for snowflake in snowflakes_list]

    def _validate_snowflakes_type(self, snowflakes_list: list):
        if type(snowflakes_list) != list:
            raise TypeError('Expected type list for snowflakes_list')
        return self

    def find_the_same_snowflakes(self) -> dict:
        results = {}
        for i in range(len(self.snowflakes)-1):
            for j in range(i+1, len(self.snowflakes)):
                if self.snowflakes[i] == self.snowflakes[j]:
                    key = tuple(self.snowflakes[i].arms)
                    for s in self.snowflakes[i].find_all_equal_snowflakes():
                        if tuple(s) in results.keys():
                            key = tuple(s)
                            break
                    if key in results:
                        results[key].extend([i, j])
                    else:
                        results[key] = [i, j]
        results = {str(list(k)): sorted(list(set(v))) for k, v in results.items()}

        return results
