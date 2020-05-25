from product_parser.models import CrawlingTask, Product, ProductImage
from product_parser.repos.amazon_finance_unit_of_word import AmazonFinanceUnitOfWork
from product_parser.services.detail_parser import AmazonParser
from product_parser.tools.headers_generator import HeadersGenerator


class TasksService:
    _headers_generator: HeadersGenerator
    _amazon_finance: AmazonFinanceUnitOfWork
    _parser: AmazonParser

    def __init__(self):
        self._headers_generator = HeadersGenerator()
        self._amazon_finance = AmazonFinanceUnitOfWork()
        self._parser = AmazonParser(self._headers_generator.generate())

    def parse_page(self) -> None:
        for task in CrawlingTask.objects.all():
            product, content, images = self._parser.get_detail_info(task.url)
            existing_product = Product.objects.filter(asin=product.asin).first()

            if existing_product:
                existing_product.product_title = product.product_title
                existing_product.url = product.url
                existing_product.price = product.price
                existing_product.rating_amount = product.rating_amount
                existing_product.shipping_weight = product.shipping_weight
                existing_product.weight = product.weight
                existing_product.dim_x, existing_product.dim_y, existing_product.dim_z = product.dim_x, product.dim_y, product.dim_z
                existing_product.model_number = product.model_number
                existing_product.bsr = product.bsr
                product = existing_product
                images_for_existing_product = ProductImage.objects.filter(product__id=existing_product.id)
                new_images = []
                for image in images:
                    if all(image.hash != existing_image for existing_image in images_for_existing_product):
                        new_images.append(image)
                images = new_images

            content.product = product
            product.save()
            content.save()
            ProductImage.objects.bulk_create(images)
            # url = 'https://www.amazon.com/nuLOOM-HJZOM1B-Tufted-Classie-Multi/dp/B00AW0TX10/ref=sr_1_6?dchild=1&pf_rd_i=684541011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=00b00417-8753-4d7d-a195-6b32e72824d6&pf_rd_r=841BSQVSD4HS6DVDYN9B&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1586618338&refinements=p_28%3Ashag&s=home-garden&sr=1-6'
