# from django.shortcuts import render
# from .models import Inventorius
# from django.db.models import Q
# #
# # def pradinis(request):
# #     inventoriai = Inventorius.objects.all()
# #     # return render(request, 'inventorius/pradinis.html', {'inventoriai': inventoriai})
# #     return render(request, 'pradinis.html', {'inventoriai': inventoriai})
#
#
# # def pradinis(request):
# #     kategorija = request.GET.get('kategorija')
# #     turto_tipas = request.GET.get('turto_tipas')
# #     pavadinimas = request.GET.get('pavadinimas')
# #     inventorinis_numeris = request.GET.get('inventorinis_numeris')
# #     vieta = request.GET.get('vieta')
# #     inventoriai = Inventorius.objects.all()
# #
# #     if kategorija:
# #         inventoriai = inventoriai.filter(kategorija__pavadinimas__icontains=kategorija)
# #     if turto_tipas:
# #         inventoriai = inventoriai.filter(turto_tipas__icontains=vieta)
# #     if pavadinimas:
# #         inventoriai = inventoriai.filter(pavadinimas__icontains=vieta)
# #     if inventorinis_numeris:
# #         inventoriai = inventoriai.filter(inventorinis_numeris__icontains=vieta)
# #     if vieta:
# #         inventoriai = inventoriai.filter(vieta__icontains=vieta)
#
# # def pradinis(request):
# #     query = request.GET.get('q')
# #     if query:
# #         inventoriai = Inventorius.objects.filter(pavadinimas__icontains=query)
# #     else:
# #         inventoriai = Inventorius.objects.all()
# #
# #     return render(request, 'pradinis.html', {'inventoriai': inventoriai})
#
# def pradinis(request):
#     query = request.GET.get('q', '')  # Gauti paieškos užklausą iš GET parametro
#     inventoriai = Inventorius.objects.all()  # Pirmiausia paimame visus įrašus
#
#     if query:
#         inventoriai = inventoriai.filter(
#             Q(pavadinimas__icontains=query) |Q(serijinis_numeris__icontains=query) | Q(inventorinis_numeris__icontains=query) | Q(kaina__icontains=query) | Q(vieta__pavadinimas__icontains=query) | Q(busena__icontains=query) | Q(kategorija__pavadinimas__icontains=query) | Q(ivedimo_data__icontains=query) | Q(turto_tipas__icontains=query)
#         )
#         if not inventoriai.exists():
#             no_results_message = "Pagal jūsų užklausą nieko nerasta."
#         # else:
#         #     no_results_message = None
#     else:
#         no_results_message = None
#
#
#     return render(request, 'pradinis.html', {'inventoriai': inventoriai, 'no_results_message': no_results_message})
#
#     # return render(request, 'pradinis.html', {'inventoriai': inventoriai})


from django.shortcuts import render
from django.db.models import Q
from .models import Inventorius

def pradinis(request):
    query = request.GET.get('q', '').strip()
    no_results_message = None

    if query:
        filtruoti = Inventorius.objects.filter(
            Q(pavadinimas__icontains=query) |
            Q(serijinis_numeris__icontains=query) |
            Q(inventorinis_numeris__icontains=query) |
            Q(vieta__pavadinimas__icontains=query) |
            Q(kategorija__pavadinimas__icontains=query)
        )

        if filtruoti.exists():
            inventoriai = filtruoti
        else:
            inventoriai = Inventorius.objects.all()
            no_results_message = "Pagal jūsų užklausą nieko nerasta."
    else:
        inventoriai = Inventorius.objects.all()

    return render(request, 'pradinis.html', {
        'inventoriai': inventoriai,
        'no_results_message': no_results_message
    })
