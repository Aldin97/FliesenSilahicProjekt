from django.contrib import admin
from django.utils.html import format_html
from .models import BalkonTerasse, WC_Bad, Küche, Flur, Umbau

@admin.register(BalkonTerasse)
class BalkonTerasseAdmin(admin.ModelAdmin):
    list_display = ['image1_thumb', 'image2_thumb', 'image3_thumb', 'image4_thumb', 'image5_thumb', 'image6_thumb']

    def image1_thumb(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image1.url)
        return "No Image"
    image1_thumb.short_description = 'Image 1'

    def image2_thumb(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="100" />', obj.image2.url)
        return "No Image"
    image2_thumb.short_description = 'Image 2'

    def image3_thumb(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="100" />', obj.image3.url)
        return "No Image"
    image3_thumb.short_description = 'Image 3'

    def image4_thumb(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="100" height="100" />', obj.image4.url)
        return "No Image"
    image4_thumb.short_description = 'Image 4'

    def image5_thumb(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="100" height="100" />', obj.image5.url)
        return "No Image"
    image5_thumb.short_description = 'Image 5'

    def image6_thumb(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="100" height="100" />', obj.image6.url)
        return "No Image"
    image6_thumb.short_description = 'Image 6'

    def image7_thumb(self, obj):
        if obj.image7:
            return format_html('<img src="{}" width="100" height="100" />', obj.image7.url)
        return "No Image"
    image6_thumb.short_description = 'Image 7'

    def image8_thumb(self, obj):
        if obj.image8:
            return format_html('<img src="{}" width="100" height="100" />', obj.image8.url)
        return "No Image"
    image6_thumb.short_description = 'Image 8'



@admin.register(WC_Bad)
class WC_BadAdmin(admin.ModelAdmin):
    list_display = ['image1_thumb', 'image2_thumb', 'image3_thumb', 'image4_thumb', 'image5_thumb', 'image6_thumb']
    
    def image1_thumb(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image1.url)
        return "No Image"
    image1_thumb.short_description = 'Image 1'

    def image2_thumb(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="100" />', obj.image2.url)
        return "No Image"
    image2_thumb.short_description = 'Image 2'

    def image3_thumb(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="100" />', obj.image3.url)
        return "No Image"
    image3_thumb.short_description = 'Image 3'

    def image4_thumb(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="100" height="100" />', obj.image4.url)
        return "No Image"
    image4_thumb.short_description = 'Image 4'

    def image5_thumb(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="100" height="100" />', obj.image5.url)
        return "No Image"
    image5_thumb.short_description = 'Image 5'

    def image6_thumb(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="100" height="100" />', obj.image6.url)
        return "No Image"
    image6_thumb.short_description = 'Image 6'

    def image7_thumb(self, obj):
        if obj.image7:
            return format_html('<img src="{}" width="100" height="100" />', obj.image7.url)
        return "No Image"
    image6_thumb.short_description = 'Image 7'

    def image8_thumb(self, obj):
        if obj.image8:
            return format_html('<img src="{}" width="100" height="100" />', obj.image8.url)
        return "No Image"
    image6_thumb.short_description = 'Image 8'


@admin.register(Küche)
class KücheAdmin(admin.ModelAdmin):
    list_display = ['image1_thumb', 'image2_thumb', 'image3_thumb', 'image4_thumb', 'image5_thumb', 'image6_thumb']
    
    def image1_thumb(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image1.url)
        return "No Image"
    image1_thumb.short_description = 'Image 1'

    def image2_thumb(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="100" />', obj.image2.url)
        return "No Image"
    image2_thumb.short_description = 'Image 2'

    def image3_thumb(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="100" />', obj.image3.url)
        return "No Image"
    image3_thumb.short_description = 'Image 3'

    def image4_thumb(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="100" height="100" />', obj.image4.url)
        return "No Image"
    image4_thumb.short_description = 'Image 4'

    def image5_thumb(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="100" height="100" />', obj.image5.url)
        return "No Image"
    image5_thumb.short_description = 'Image 5'

    def image6_thumb(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="100" height="100" />', obj.image6.url)
        return "No Image"
    image6_thumb.short_description = 'Image 6'


@admin.register(Flur)
class FlurAdmin(admin.ModelAdmin):
    list_display = ['image1_thumb', 'image2_thumb', 'image3_thumb', 'image4_thumb', 'image5_thumb', 'image6_thumb']
    
    def image1_thumb(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image1.url)
        return "No Image"
    image1_thumb.short_description = 'Image 1'

    def image2_thumb(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="100" />', obj.image2.url)
        return "No Image"
    image2_thumb.short_description = 'Image 2'

    def image3_thumb(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="100" />', obj.image3.url)
        return "No Image"
    image3_thumb.short_description = 'Image 3'

    def image4_thumb(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="100" height="100" />', obj.image4.url)
        return "No Image"
    image4_thumb.short_description = 'Image 4'

    def image5_thumb(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="100" height="100" />', obj.image5.url)
        return "No Image"
    image5_thumb.short_description = 'Image 5'

    def image6_thumb(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="100" height="100" />', obj.image6.url)
        return "No Image"
    image6_thumb.short_description = 'Image 6'

@admin.register(Umbau)
class UmbauAdmin(admin.ModelAdmin):
    list_display = ['image1_thumb', 'image2_thumb', 'image3_thumb', 'image4_thumb', 'image5_thumb', 'image6_thumb']
    
    def image1_thumb(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image1.url)
        return "No Image"
    image1_thumb.short_description = 'Image 1'

    def image2_thumb(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="100" height="100" />', obj.image2.url)
        return "No Image"
    image2_thumb.short_description = 'Image 2'

    def image3_thumb(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="100" height="100" />', obj.image3.url)
        return "No Image"
    image3_thumb.short_description = 'Image 3'

    def image4_thumb(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="100" height="100" />', obj.image4.url)
        return "No Image"
    image4_thumb.short_description = 'Image 4'

    def image5_thumb(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="100" height="100" />', obj.image5.url)
        return "No Image"
    image5_thumb.short_description = 'Image 5'

    def image6_thumb(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="100" height="100" />', obj.image6.url)
        return "No Image"
    image6_thumb.short_description = 'Image 6'

    def image7_thumb(self, obj):
        if obj.image7:
            return format_html('<img src="{}" width="100" height="100" />', obj.image7.url)
        return "No Image"
    image6_thumb.short_description = 'Image 7'

    def image8_thumb(self, obj):
        if obj.image8:
            return format_html('<img src="{}" width="100" height="100" />', obj.image8.url)
        return "No Image"
    image6_thumb.short_description = 'Image 8'
