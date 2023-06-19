from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import View
from .models import Compte
from .models import Prelevement
from .models import Virement

def SignupClient(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        ville = request.POST.get("ville")
        pays = request.POST.get("pays")
        email = request.POST.get("email")
        newclient = CustomUser(username = username, nom = nom, prenom = prenom, adresse = adresse, ville = ville, pays = pays, email= email)
        newclient.set_password(password)
        newclient.save()
        return redirect('/banque/login/client')
    else:
        return render(request, 'banque/creation_client.html')

def SignupPersonnel(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        ville = request.POST.get("ville")
        pays = request.POST.get("pays")
        email = request.POST.get("email")
        newclient = CustomUser(username = username, nom = nom, prenom = prenom, adresse = adresse, ville = ville, pays = pays, email= email, is_personnel=True)
        newclient.set_password(password)
        newclient.save()
        return redirect('/banque/login/personnel')
    else:
        return render(request, 'banque/creation_personnel.html')

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_personnel:
            return render(request, 'banque/dashboard.html')
        return render(request, 'banque/dashboard.html')
    else:
        return redirect('/banque/login/client')

def logoutUser(request):
    logout(request)
    return redirect('/banque/login/client')

def LoginClient(request):
    for i in list(CustomUser.objects.all()):
        print(i.password)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            print('ERREUR MDP')
            return redirect('/banque/login/client')
    else:
        return render(request, 'banque/login_client.html')

def LoginPersonnel(request):
    for i in list(CustomUser.objects.all()):
        print(i.password)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            print('ERREUR MDP')
            return redirect('/banque/login/personnel')
    else:
        return render(request, 'banque/login_personnel.html')

def depot(request):
    return render(request,'banque/depot.html')


def prelevement(request):
    return render(request,'banque/prelevement.html')

def virement(request):
    return render(request,'banque/virement.html')


def creation_compte(request):
    return render(request,'banque/creation_compte.html')


class DepotView(View):
    def post(self, request):
        montant = float(request.POST.get('montant'))

        # Effectuez les opérations pour mettre à jour la base de données et le montant du compte
        compte = Compte.objects.get(id=1)  # Supposons que le compte a l'ID 1
        compte.montant += montant
        compte.save()

        # Récupérez à nouveau le montant actuel pour l'afficher dans le contexte
        montant_actuel = compte.montant

        context = {
            'montant_actuel': montant_actuel,
            'depot_success': True  # Un indicateur pour afficher un message de succès dans le template
        }
        return render(request, 'depot.html', context)


class PrelevementView(View):
    def get(self, request):
        return render(request, 'prelevement.html')

    def post(self, request):
        compte_source_id = request.POST.get('compte_source')
        montant = request.POST.get('montant')

        # Effectuer les opérations nécessaires pour effectuer le prélèvement
        # ...

        # Rediriger vers la page de succès ou afficher un message de succès
        return redirect('prelevement_success')  # Remplacez 'prelevement_success' par le nom de votre vue de succès


class VirementView(View):
    def get(self, request):
        return render(request, 'virement.html')

    def post(self, request):
        compte_source_id = request.POST.get('compte_source')
        compte_destination_id = request.POST.get('compte_destination')
        montant = request.POST.get('montant')

        # Effectuer les opérations nécessaires pour effectuer le virement
        # ...

        # Enregistrer le virement dans la base de données
        virement = Virement.objects.create(
            compte_source_id=compte_source_id,
            compte_destination_id=compte_destination_id,
            montant=montant
        )

        # Rediriger vers la page de succès ou afficher un message de succès
        return redirect('virement_success')  # Remplacez 'virement_success' par le nom de votre vue de succès


