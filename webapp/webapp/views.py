# import rssi
from django.shortcuts import render
from .utils import get_plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from .Locate import wknn
# from .Locate import dataCollectionInput
# from .Locate import dataCollectionRP
import io, base64

def home(request):
    return render(request,'landingpage.html')

def locate(request):
    # dataCollectionInput.get_input(rssi)
    wknn_output = wknn.apply_wknn()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(wknn_output[0], wknn_output[1], '--bo')
    fig.autofmt_xdate()
    ax.set_title('Library')
    ax.set_ylabel("y-coordinate")
    ax.set_xlabel("x-coordinate")
    ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
    flike = io.BytesIO()
    fig.savefig(flike)
    chart = base64.b64encode(flike.getvalue()).decode()

    return render(request,'locatePage.html', {'chart': chart})

def calibration(request):
    print("calibrateeee")
    if request.POST:
        print("postt")
        location = request.POST.get('location')
        x_coordinate = request.POST.get('x-coordinate')
        y_coordinate = request.POST.get('y-coordinate')
        # dataCollectionRP.calibrate_func(rssi,location,x_coordinate,y_coordinate)

        return render(request,'calibrate.html',{'status':'complete'})
    print("gett")
    return render(request,'calibrate.html')