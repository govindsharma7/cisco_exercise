from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import RouterDetails


# Create your views here.
class ListView(View):

    def get(self, request):
        router_data = RouterDetails.objects.filter(active=1)
        context = {'router_data': router_data}
        return render(request, 'list.html', context)


class AddView(View):

    def get(self, request):
        return render(request, 'add.html')

    def post(self, request):
        sapid = request.POST.get('sapid')
        hostname = request.POST.get('hostname')
        loopback = request.POST.get('loopback')
        mac_addr = request.POST.get('mac_addr')

        router_details = RouterDetails(
            sapid=sapid,
            hostname=hostname,
            loopback=loopback,
            mac_addr=mac_addr)

        router_details.save()
        return redirect('list_view')


class UpdateView(View):

    def get(self, request, *args, **kwargs):
        router_data = RouterDetails.objects.get(id=kwargs['pk'])
        context = {'router_data': router_data}
        return render(request, 'update.html', context)

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        sapid = request.POST.get('sapid')
        hostname = request.POST.get('hostname')
        loopback = request.POST.get('loopback')
        mac_addr = request.POST.get('mac_addr')

        RouterDetails.objects.filter(
            id=id).update(
            sapid=sapid,
            hostname=hostname,
            loopback=loopback,
            mac_addr=mac_addr)
        return redirect('list_view')


class DeleteView(View):

    def post(self, request):
        id = request.POST.get('id')

        RouterDetails.objects.filter(id=id).update(active=0)

        # json_data = json.dumps({"status": 1, "message": "Seccessfully deleted."})
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse({"status": 1, "message": "Seccessfully deleted."})


class SearchView(View):

    def post(self, request):
        search_text = request.POST.get('search_text')
        result = RouterDetails.objects.filter(
            sapid__icontains=search_text).values(
            'sapid', 'hostname', 'loopback', 'mac_addr', 'active', 'id')
        return JsonResponse({'result': list(result), 'status': 1})


# Exercise 2, point no. 6
def genRouterDetails(last_id):
    loopback_first = last_id
    loopback_second = last_id
    loopback_third = last_id
    loopback_fourth = last_id
    counter = last_id
    data = {}
    while True:
        if loopback_fourth > 255:
            loopback_fourth = 0
            loopback_third += 1

        if loopback_third > 255:
            loopback_third = 0
            loopback_second += 1

        if loopback_second > 255:
            loopback_second = 0
            loopback_first += 1

        if loopback_first > 255:
            loopback_first = 1

        loopback = str(loopback_first) + '.' + str(loopback_second) + '.' + str(loopback_third) + '.' + str(
            loopback_fourth)

        data = {'sapid': 'sap' + str(counter), 'hostname': 'hostname' + str(counter), 'loopback': loopback,
                'mac_addr': 'mac' + str(counter)}
        counter += 1
        loopback_fourth += 1
        yield data


def generateNewRecords(request):
    last_id = 0
    last_val = RouterDetails.objects.order_by('-created_at')
    if last_val:
        last_id = last_val[0].id
    print(last_id)
    generate_rec = genRouterDetails(last_id)
    router_list = []

    for i in range(10):
        record = next(generate_rec)
        router_list.append(
            RouterDetails(
                sapid=record['sapid'],
                hostname=record['hostname'],
                loopback=record['loopback'],
                mac_addr=record['mac_addr']))

    RouterDetails.objects.bulk_create(router_list)
    return redirect('list_view')
