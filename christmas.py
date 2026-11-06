inc=1
best_inc=1
dec=1
best_dec=1
["4","1,3,4,2"]
def christmas_trees(trees, height):
    for i in range(trees):
        if height[i]>height[i+1]:
            dec+=1
        if height[i]<height[i-1]:
            inc+=1
        if height[i]>height[i+1]:
            best_dec+=1
        if height[i]<height[i-1]:
            best_inc+=1
            print(best_inc)