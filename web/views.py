from django.shortcuts import render
from .models import BalkonTerasse, WC_Bad, Küche, Flur, Umbau
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html")

def gallery_view(request):
    balkon_terasa_images = BalkonTerasse.objects.all()
    wc_images = WC_Bad.objects.all()
    kuhinja_images = Küche.objects.all()
    hodnik_images = Flur.objects.all()
    umbau_images = Umbau.objects.all()
    
    context = {
        'balkon_terasa_images': balkon_terasa_images,
        'wc_images': wc_images,
        'kuhinja_images': kuhinja_images,
        'hodnik_images': hodnik_images,
        'umbau_images': umbau_images,
    }
    
    return render(request, "index.html", context)


def index_contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            ime = contact_form.cleaned_data['ime']
            telefon = contact_form.cleaned_data['telefon']
            email = contact_form.cleaned_data['email']
            poruka = contact_form.cleaned_data['poruka']

            # Slanje email-a
            subject = 'Novi upit sa kontakt forme'
            message = f'Ime: {ime}\nPrezime: {telefon}\nTelefon: {email}\nPoruka: {poruka}'
            recipients = ['fliesen.silahic@gmail.com']

            from_email = f'{ime} <{settings.EMAIL_HOST_USER}>'

            email_message = EmailMessage(
                subject,
                message,
                from_email=from_email,  # Kombinovani pošiljalac
                to=recipients,
                reply_to=[email]  # Reply-To zaglavlje
            )
            email_message.send()

            # Slanje automatskog odgovora korisniku
            auto_reply_subject = 'Empfangsbestätigung der Nachricht'
            auto_reply_message = render_to_string('auto_reply_email.html', {'ime': ime})

            auto_reply_email = EmailMessage(
                auto_reply_subject,
                auto_reply_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email]
            )
            auto_reply_email.content_subtype = 'html'
            auto_reply_email.send()


            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def datenschutz(request):
    return render(request, "datenschutzerklärung.html")

def impressum(request):
    return render(request, "impressum.html")



