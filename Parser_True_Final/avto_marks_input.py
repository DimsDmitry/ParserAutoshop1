#Request all brands of all products to process them in the next stage

def mark_save():
    while True:
        url = input('Brand link:')
        with open('auto_list.txt') as fr:
            content = fr.read()
        if url in content:
            print('The brand is already there!')
            continue
        with open('auto_list.txt', 'a') as file:
            file.write(f'{url}\n')
            print('The link was recorded successfully!')


if __name__ == '__main__':
    mark_save()

