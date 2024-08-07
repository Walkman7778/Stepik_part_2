#Students of 10 th class of school beegeek  got a task to read in vacantion 3 books:
#'what is maths'
#Mathimatical composal
#100 genial ideas in mathimatics
#Happeed that 
#𝑛 students red 1st book, 
#𝑚 second, 
#𝑘 third
#Also is known that
#𝑥 studets red 1st and 2nd, or both ones, 
#𝑦 studets red 2nd and 2d, or both ones,  
#𝑧 studets red 1nd and 3d, or at least 1 of them 
#𝑡 students managed all task
#a students is the number of all students
#a1 = numb. who red only 1 book
#b = red only 2 books
#c = red no one 

n, m, k, x, y, z, t, a =int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
a1 = (n + k -z - t) + (n + m + - x - t) + (k + m - y - t)
b = (x + z + t - n - m - k) + (x + y + t - n - m - k) + (y + z + t - n - m - k)
c = a - a1 - b - t
print(b, a1, c, sep="\n")