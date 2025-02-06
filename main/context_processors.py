from .forms import NewsletterSub

def newsletterform(request):
    return {"Newsletterform": NewsletterSub()}  # ✅ Matches template variable name
