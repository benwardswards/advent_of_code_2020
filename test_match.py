def func(x, y):
    """Test match case"""
    match x, y:
        case 0, _:
            print(f"{x=},{y=} first case ")
        case 1, 2:
            print(f"{x=},{y=} second case ")
        case 1, 6 | 3 | 4 | 5:
            print(f"{x=},{y=} 3 case ")
        case 2, 2:
            print(f"{x=},{y=} 4 case ")


func(0, 1)
func(1, 2)
func(1, 5)

func(1, 1)

func(2, 2)
