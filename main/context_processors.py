from .forms import NewsletterSub

def newsletterform(request):
        return('newsletterform': NewsletterSub())