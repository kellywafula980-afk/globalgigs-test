# ============================================================
# FIXED DASHBOARD VIEW
# ============================================================

@login_required
def dashboard(request):
    """Employer dashboard showing all posted jobs and stats"""
    user = request.user
    
    # Fix: Handle UserProfile creation properly
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # Create a profile if it doesn't exist
        profile = UserProfile.objects.create(
            user=user,
            company_name=user.username + "'s Company"
        )
    
    # Get jobs posted by this employer
    jobs = EmployerJob.objects.filter(employer=user).order_by('-created_at')
    
    # Stats with safe defaults
    total_jobs = jobs.count()
    active_jobs = jobs.filter(status='active').count()
    paused_jobs = jobs.filter(status='paused').count()
    filled_jobs = jobs.filter(status='filled').count()
    expired_jobs = jobs.filter(status='expired').count()
    total_applications = sum(job.applications_count or 0 for job in jobs)
    
    # Recent applications with safe handling
    recent_applications = EmployerJobApplication.objects.filter(
        job__employer=user
    ).order_by('-applied_at')[:10] if EmployerJobApplication.objects.filter(job__employer=user).exists() else []
    
    context = {
        'profile': profile,
        'jobs': jobs,
        'total_jobs': total_jobs,
        'active_jobs': active_jobs,
        'paused_jobs': paused_jobs,
        'filled_jobs': filled_jobs,
        'expired_jobs': expired_jobs,
        'total_applications': total_applications,
        'recent_applications': recent_applications,
    }
    return render(request, 'jobs/dashboard.html', context)
