def solution(park, routes):
    direction = {"E" : (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    
    sy, sx = -1, -1
    
    def move(y, x):
        for route in routes:
            dir, length = map(str, route.split())
            length = int(length)
            
            dy, dx = direction[dir]
            
            passable = True
            for i in range(1, length + 1):
                ny = y + dy * i
                nx = x + dx * i
                if 0 <= ny < len(park) and 0 <= nx < len(park[0]):
                    if park[ny][nx] == "X":
                        passable = False
                        break
                else:
                    passable = False
                    break
            
            if not passable:
                continue
            else:
                y, x = ny, nx
    
        return [y, x]
    
    
    for y in range(len(park)):
        if sy != -1 and sx != -1:
            break
        for x in range(len(park[0])):
            if park[y][x] == "S":
                answer = move(y, x)
                break
                
    return answer