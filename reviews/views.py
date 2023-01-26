from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)


from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Review
from .forms import ReviewForm


class Reviews(ListView):
    model = Review
    template_name = "reviews/reviews.html"
    context_object_name = 'reviews'


class CreateReview(LoginRequiredMixin, CreateView):
    """ View to create a review """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReview, self).form_valid(form)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to edit a review """
    template_name = "reviews/edit_review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a review """
    model = Review
    success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().user
