# jobs/urls.py
# ============================================================
# JOB APP URLS - COMPLETE
# ============================================================

from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    # ============================================================
    # HOMEPAGE & JOB LISTINGS
    # ============================================================
    path('', views.job_list_view, name='home'),
    path('', views.homepage_job_board, name='homepage'),
    path('', views.content_batcher_dashboard, name='content_batcher'),
    
    # ============================================================
    # SCRAPED JOB DETAIL & APPLICATIONS
    # ============================================================
    path('jobs/<int:job_id>/', views.job_detail_view, name='job_detail'),
    
    # ============================================================
    # EMPLOYER JOB DETAIL (Public facing for employer-posted jobs)
    # ============================================================
    path('employer-jobs/<int:job_id>/', views.employer_job_detail, name='employer_job_detail'),
    
    # ============================================================
    # AUTHENTICATION
    # ============================================================
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # ============================================================
    # EMPLOYER DASHBOARD & JOB MANAGEMENT
    # ============================================================
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/post-job/', views.post_job, name='post_job_employer'),
    path('dashboard/edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('dashboard/delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('dashboard/toggle-status/<int:job_id>/', views.toggle_job_status, name='toggle_job_status'),
    
    # ============================================================
    # APPLICATION MANAGEMENT
    # ============================================================
    path('dashboard/job-applications/<int:job_id>/', views.job_applications, name='job_applications'),
    path('dashboard/update-application/<int:application_id>/', views.update_application_status, name='update_application_status'),
    path('dashboard/application/<int:application_id>/', views.view_application_detail, name='application_detail'),
    
    # ============================================================
    # EMPLOYER PROFILE
    # ============================================================
    path('profile/', views.profile, name='profile'),
    
    # ============================================================
    # SCRAPER & UTILITY (Keep these for admin use)
    # ============================================================
    path('run-production-sync/', views.secret_trigger_scraper, name='trigger_scraper'),
    path('enrich-jobs/', views.enrich_jobs_endpoint, name='enrich_jobs'),
    
    # ============================================================
    # DEBUG
    # ============================================================
    path('debug/', views.debug_jobs, name='debug'),
    path('category-debug/', views.category_debug, name='category_debug'),



    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    

]