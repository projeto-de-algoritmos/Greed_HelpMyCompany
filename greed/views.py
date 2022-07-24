from django.shortcuts import render

from django.http import HttpRequest, HttpResponse,QueryDict
from django.shortcuts import render, redirect
from itertools import zip_longest
from greed.intervalscheduling import *
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def group_elements(n, iterable, padvalue='x'):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def home(request):
    return render(request,'formCadastroHorario.html')

def querydict_dict(start, end , weight):
    tupla = (start, end, weight)
    indices = []
    indices += [tupla]
    print(indices)
    

def getTime_table(request):

    postdata = []

    if request.method == 'POST':

        postdata = request.POST.dict()
        postdata.pop('csrfmiddlewaretoken')
        print(postdata)
        print(len(postdata))

        keysList = list(postdata.values()) ## CHAMAR FUNCAO REMOVE QUOTATION
        print(keysList)

        list_quatation = []
        list_quatation = removeQuotation(keysList)
        print('printando list quotation')
        print(list_quatation)


        print('printando new list quotation')
        print(list_quatation)    


        I = []
        try:
            for output in group_elements(4,list_quatation):
                I.append(output)

            print('printando I')
            print(I)

            ## CHAMA FUNCAO RESOLVE

            list_resolve = []
            list_resolve = resolve(I)
            print(list_resolve)
        except ValueError as erro:
            messages.info(request, 'Por favor certifique se todos os campos foram preenchidos')
            return HttpResponseRedirect('/home')


        try:
            weightedinterval = WeightedIntervalScheduling(list_resolve)
            max_weight, best_intervals = weightedinterval.weighted_interval()
        except RecursionError as erro:
            messages.info(request, 'O horário inicial deve ser menor que o horário final')
            return HttpResponseRedirect('/home')
            
        else:       
            current_date = datetime.now().date()

            best_intervals = replaceTime(best_intervals)

    return render(request,'scheduling.html', {'best_intervals': best_intervals, 'current_date': current_date})

def getFile(request):
    
    if request.method == 'POST':
        print('entrou')    
