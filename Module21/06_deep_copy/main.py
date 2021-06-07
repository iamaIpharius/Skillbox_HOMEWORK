site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {product} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {product}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def get_new_sites(site, sites_ad):
    if sites_ad == 0:
        return
    name = input('Введите название продукта: ')
    site['html']['head']['title'] = site['html']['head']['title'].format(product=name)
    site['html']['body']['h2'] = site['html']['body']['h2'].format(product=name)
    print(site)
    sites_ad -= 1
    get_new_sites(site, sites_ad)


get_new_sites(site, 2)