from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.category_name)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product_name)


class ProductDetails(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    warranty = models.CharField(max_length=20)
    weightAndDimension = models.TextField(max_length=220)
    display = models.TextField(max_length=220)
    chip = models.TextField(max_length=120)
    iSightCamera = models.TextField(max_length=220)
    vedioRecording = models.TextField(max_length=220)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productDetail")

    def __str__(self):
        return "{}".format(self.product.product_name)


class Specifications(models.Model):
    specification = models.TextField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product.product_name)


class Description(models.Model):
    FeatureName = models.CharField(max_length=50)
    Description = models.TextField(max_length=220)
    Image = models.FileField(max_length=100, upload_to='Images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product.product_name)


class Images(models.Model):
    Images = models.FileField(max_length=100, upload_to='Images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product.product_name)


class Capacity(models.Model):
    Capacity = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Capacity)


class Credentials(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.username)