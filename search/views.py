from django.shortcuts import render

from search.documents import FertilizersDocument


def search_fertilizer(request):
    q = request.GET.get('q')

    if q:
        fertilizers = FertilizersDocument.search().query('match', name=q)
    else:
        fertilizers = ''

    return render(request, 'search/search.html', {'fertilizers': fertilizers})
