from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from pymongo import MongoClient
from .models import Product

client = MongoClient(settings.MONGO_URI)
db = client['ecommerce']
collection = db['products']

@receiver(post_save, sender=Product)
def save_to_mongo(sender, instance, **kwargs):
    print("✅ Product kaydedildi, Mongo'ya yazılıyor...")
    data = {
        "_id": instance.id,
        "uid": str(instance.uid),  # 👈 UUID stringe çevrildi
        "name": instance.name,
        "description": instance.description,
        "price": float(instance.price),
        "image": str(instance.image.url if instance.image else ""),
    }
    collection.replace_one({"_id": instance.id}, data, upsert=True)

@receiver(post_delete, sender=Product)
def delete_from_mongo(sender, instance, **kwargs):
    print("🗑️ Product MongoDB'den siliniyor...")
    collection.delete_one({"_id": instance.id})
