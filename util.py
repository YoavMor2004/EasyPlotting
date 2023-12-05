# noinspection SpellCheckingInspection
def get_equation(linregress_result, x_name: str = 'x', y_name: str = 'y') -> str:
    if 0 <= linregress_result.intercept:
        return f'{y_name} = {linregress_result.slope:.3g}{x_name} + {linregress_result.intercept:.3g}'
    return f'{y_name} = {linregress_result.slope:.3g}{x_name} - {abs(linregress_result.intercept):.3g}'
