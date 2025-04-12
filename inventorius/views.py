from django.shortcuts import render
from .models import Inventorius
from .forms import InventoriusForm
from django.db.models import Q, Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse

def pradinis(request):
    query = request.GET.get('q', '')
    no_results_message = None

    if query:
        filtruoti = Inventorius.objects.filter(
             Q(pavadinimas__icontains=query) |
             Q(serijinis_numeris__icontains=query) |
             Q(inventorinis_numeris__icontains=query) |
             Q(kaina__icontains=query) |
             Q(vieta__pavadinimas__icontains=query) |
             Q(busena__icontains=query) |
             Q(kategorija__pavadinimas__icontains=query) |
             Q(ivedimo_data__icontains=query) |
             Q(turto_tipas__icontains=query)
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

class InventoriusCreateView(CreateView):
    model = Inventorius
    form_class = InventoriusForm
    template_name = 'inventorius_form.html'
    success_url = reverse_lazy('pradinis')

class InventoriusUpdateView(UpdateView):
    model = Inventorius
    fields = '__all__'
    template_name = 'inventorius_form.html'
    success_url = reverse_lazy('pradinis')

class InventoriusDeleteView(DeleteView):
    model = Inventorius
    template_name = 'inventorius_confirm_delete.html'
    success_url = reverse_lazy('pradinis')

# def statistika(request):
#     remontuojamu_kiekis = Inventorius.objects.filter(busena='Remontuojamas').count()
#     kiekvienos_busenos_kiekiai = Inventorius.objects.values('busena').annotate(kiekis=Count('id'))
#     kiekvienos_kategorijos_kiekis = Inventorius.objects.values('kategorija__pavadinimas').annotate(kiekis=Count('id'))
#     inventoriai_pagal_vieta = Inventorius.objects.values('vieta__pavadinimas').annotate(kiekis=Count('id'))
#
#     return render(request, 'statistika.html', {
#         'remontuojamu_kiekis': remontuojamu_kiekis,
#         'kiekvienos_busenos_kiekiai': kiekvienos_busenos_kiekiai,
#         'kiekvienos_kategorijos_kiekis': kiekvienos_kategorijos_kiekis,
#         'inventoriai_pagal_vieta': inventoriai_pagal_vieta,
#     })
from django.db.models import Count
from django.shortcuts import render
from .models import Inventorius

def statistika(request):
    bendras_kiekis = Inventorius.objects.count()
    pagal_turto_tipa = Inventorius.objects.values('turto_tipas').annotate(kiekis=Count('id'))
    kiekvienos_busenos_kiekiai = Inventorius.objects.values('busena').annotate(kiekis=Count('id'))
    kiekvienos_kategorijos_kiekis = Inventorius.objects.values('kategorija__pavadinimas').annotate(kiekis=Count('id'))

    return render(request, 'statistika.html', {
        'bendras_kiekis': bendras_kiekis,
        'pagal_turto_tipa': pagal_turto_tipa,
        'kiekvienos_busenos_kiekiai': kiekvienos_busenos_kiekiai,
        'kiekvienos_kategorijos_kiekiai': kiekvienos_kategorijos_kiekis
    })
def pasirinktas_veiksmas(request):
    if request.method == 'POST':
        pasirinktas_id = request.POST.get('pasirinktas_id')
        veiksmas = request.POST.get('veiksmas')

        if pasirinktas_id:
            if veiksmas == 'redaguoti':
                return redirect('redaguoti', pk=pasirinktas_id)
            elif veiksmas == 'istrinti':
                return redirect('istrinti', pk=pasirinktas_id)

    return redirect('pradinis')