# urls.py
# ============================================================
# COMPLETE URLS FOR GLOBALGIGS
# ============================================================

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from jobs import views

urlpatterns = [
    # ============================================================
    # CORE ROUTES
    # ============================================================
    path('robots.txt', views.robots_txt, name='robots'),
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),  # This includes your jobs/urls.py
    
    # ============================================================
    # VERIFICATION FILES
    # ============================================================
    path('ads.txt', TemplateView.as_view(template_name='jobs/ads.txt', content_type='text/plain')),
    path('google56bce93523ece129.html', TemplateView.as_view(template_name='jobs/google56bce93523ece129.html', content_type='text/html')),
    
    # ============================================================
    # DEBUG ENDPOINTS
    # ============================================================
    path('debug/', views.debug_jobs, name='debug'),
    path('category-debug/', views.category_debug, name='category_debug'),
    
    # ============================================================
    # JOB POSTING & PAYMENTS (Existing)
    # ============================================================
    path('post-job/', views.post_job_page, name='post_job'),
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment/callback/', views.payment_callback, name='payment_callback'),
    path('paystack-webhook/', views.paystack_webhook, name='paystack_webhook'),
    
    # ============================================================
    # SITEMAP
    # ============================================================
    path('sitemap.xml', views.generate_sitemap, name='sitemap'),
    
    # ============================================================
    # 🚀 SCRAPER & ENRICHMENT ENDPOINTS
    # ============================================================
    path('scraper/trigger/', views.secret_trigger_scraper, name='trigger_scraper'),
    path('enrich-jobs/', views.enrich_jobs_endpoint, name='enrich_jobs'),
    
    # ============================================================
    # MIGRATIONS & UTILITY
    # ============================================================
    path('migrate/', views.run_migrations, name='run_migrations'),
    
    # ============================================================
    # CATEGORY MANAGEMENT
    # ============================================================
    path('create-categories-prod/', views.create_categories_production, name='create_categories_prod'),
    path('categorize-jobs-prod/', views.categorize_jobs_production, name='categorize_jobs_prod'),
    path('force-assign-categories/', views.force_assign_categories, name='force_assign_categories'),
    path('simple-categorize/', views.simple_categorize, name='simple_categorize'),
    
    # ============================================================
    # 🆕 EMPLOYER AUTHENTICATION ROUTES
    # ============================================================
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # ============================================================
    # 🆕 EMPLOYER DASHBOARD & JOB MANAGEMENT
    # ============================================================
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/post-job/', views.post_job, name='post_job_employer'),
    path('dashboard/edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('dashboard/delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('dashboard/toggle-status/<int:job_id>/', views.toggle_job_status, name='toggle_job_status'),
    
    # ============================================================
    # 🆕 APPLICATION MANAGEMENT
    # ============================================================
    path('dashboard/job-applications/<int:job_id>/', views.job_applications, name='job_applications'),
    path('dashboard/update-application/<int:application_id>/', views.update_application_status, name='update_application_status'),
    path('dashboard/application/<int:application_id>/', views.view_application_detail, name='application_detail'),
    
    # ============================================================
    # 🆕 EMPLOYER PROFILE
    # ============================================================
    path('profile/', views.profile, name='profile'),
    
    # ============================================================
    # 🆕 EMPLOYER JOB DETAIL (Public facing)
    # ============================================================
    path('employer-jobs/<int:job_id>/', views.employer_job_detail, name='employer_job_detail'),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)