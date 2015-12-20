# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import SourceDocument, ObjectDocument, ExecuteDocument
from myproject.myapp.forms import SourceDocumentForm
from django.http import HttpResponse
from myproject.myapp.Compile_Execute import Run
from myproject.settings import MEDIA_ROOT
import os

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = SourceDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = SourceDocument(docfile=request.FILES['docfile'],  filename=str(request.FILES['docfile'])) 
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = SourceDocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = SourceDocument.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def compile(request):   
    # Handle file upload
    run_object = Run()

    if request.method == 'POST':
        if "_Compile" in request.POST:
            p_status = 10000
            stdout, stderr, p_status = run_object.compile(request.POST.get("_Compile"), os.path.basename(request.POST.get("_Compile")))
            if p_status == 0:
                objfile = request.POST.get("_Compile")[:-1]+'o'
                absPath = os.path.join(MEDIA_ROOT,objfile)
                if run_object.ifobjExists(absPath):
                    newdoc = ObjectDocument(objname=os.path.basename(objfile), stdout=stdout, stderr=stderr, p_status=p_status)
                    newdoc.save()
                    data = ObjectDocument.objects.filter(objname=os.path.basename(objfile))
                    return render_to_response(
                                              'compile.html',
                                              {'data': data },
                                              context_instance=RequestContext(request)
                                              )
            else:
                #flush old obj if exists with same name in uploaded folder and DB too
                run_object.flushObj(request.POST.get("_Compile"), os.path.basename(request.POST.get("_Compile")))
                objfile = request.POST.get("_Compile")[:-1]+'o'
                if ObjectDocument.objects.filter(objname=os.path.basename(objfile)).exists():
                    ObjectDocument.objects.filter(objname=os.path.basename(objfile)).delete()
                error_data = {}
                error_data["p_status"] = p_status
                error_data["stderr"] = stderr
                error_data["stdout"] = stdout
                print " hello "
                print error_data
                return render_to_response(
                                         'compile.html',
                                          {'error_data': error_data },
                                          context_instance=RequestContext(request)
                                          )

        elif "_Execute" in request.POST:
            executablefile = request.POST.get("_Execute")[:-1]+'o'
            absPath = os.path.join(MEDIA_ROOT,executablefile)
            if run_object.ifobjExists(absPath):
                stdout, stderr, p_status = run_object.execute(request.POST.get("_Execute"), os.path.basename(request.POST.get("_Execute")))
                if p_status >= 0:       
                    newdoc = ExecuteDocument(executablename=os.path.basename(executablefile),stdout=stdout, stderr=stderr, p_status=p_status)
                    newdoc.save()
                    exedata =ExecuteDocument.objects.filter(executablename=os.path.basename(executablefile))
                    return render_to_response(
                                              'compile.html',
                                              {'exedata': exedata },
                                              context_instance=RequestContext(request)
                                              )
            else:
                return  render_to_response(
                                            'compile.html',
                                            {'objfile_error': 'object file not found'},
                                            context_instance=RequestContext(request)
                                          )   