from django.contrib import admin
from at_research_visualiser import models, forms


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mapbox_id', 'parent_location')

    def render_change_form(self, request, context, *args, **kwargs):
        # here we define a custom template
        self.change_form_template = 'at_research_visualiser/admin/location_change_form.html'

        extra = {
            'search_form': forms.MapboxSearchForm()
        }
        context.update(extra)
        return super(LocationAdmin, self).render_change_form(request, context, *args, **kwargs)


####################################################################
########## STEP 3: Register here as well
####################################################################

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_id')

class ToolAdmin(admin.ModelAdmin):
    pass #list_display = ('name')#,'approach')

class ApproachAdmin(admin.ModelAdmin):
    pass

class AssistiveProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name') # This should just be one field

class OutcomeDefinitionAdmin(admin.ModelAdmin):
    pass

class StratifiedAdmin(admin.ModelAdmin):
    pass

# class ProportionAdmin(admin.ModelAdmin):
#     list_display = ('proportion', 'n', 'out_of', 'ci_low', 'ci_high')
#
#
# class ResultAdmin(admin.ModelAdmin):
#     pass #list_display = ('assistive_product')


class GeoResultAdmin(admin.ModelAdmin):
    pass


class StudyAdmin(admin.ModelAdmin):
    pass
    # list_display = ('study_ID', 'title', 'author', 'url', 'publication_date',
    #                 'data_collection_start', 'data_collection_end',
    #                 'age_range_low', 'age_range_high',
    #                 'tool', 'approach', 'survey_name', 'dataset_used', 'study_design',
    #                 'sampling_method', 'sampling_frame', 'enumerated_sample_size',
    #                 'quality', 'stratified', 'georesults'
    #                 )


# class GeoResult(models.Model):
#     location = models.ManyToManyField(Location)
#     ap_type = SortedManyToManyField(AssistiveProduct)
#     impairment_definition = models.CharField(max_length=500)
#     impairment_definition_other = models.CharField(max_length=500)
#     outcome_definition = SortedManyToManyField(OutcomeDefinition)
#     outcome_definition_other = models.CharField(max_length=500)
#     proportion = models.FloatField()
#     n = models.IntegerField()
#     out_of_n = models.IntegerField()
#     out_of_population = models.CharField(max_length=200)
#     95%_ci_high = models.IntegerField()
#     95%_ci_low = models.IntegerField()
####################################################################
########## STEP 4: Register here as well
####################################################################

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tool, ToolAdmin)
admin.site.register(models.Approach, ApproachAdmin)
admin.site.register(models.AssistiveProduct, AssistiveProductAdmin)
admin.site.register(models.OutcomeDefinition, OutcomeDefinitionAdmin)
admin.site.register(models.Stratified, StratifiedAdmin)
# admin.site.register(models.Proportion, ProportionAdmin)
# admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.GeoResult, GeoResultAdmin)
admin.site.register(models.Study, StudyAdmin)
