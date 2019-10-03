# Loop teste quantidade de palavras palindromos

if __name__ == "__main__":
    n = int(input())
    somaPalindromos = 0
    for i in range(n):
        entrada = input()
        if (entrada == entrada[::-1]):
            somaPalindromos += 1

    print(somaPalindromos)