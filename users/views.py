from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    """Registrar un nuevo usuario."""
    if request.method != 'POST':
        # Desplegar el formulario en blanco
        form = UserCreationForm()
    else:
        # Procesar los datos recibidos.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Autenticar el usuario y redirigir a la página principal.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
