import scrapy


class Ctf(scrapy.Spider):
    name = 'Ctftime'
    start_urls = [
        'https://ctftime.org/event/list/?year=2020&online=-1&format=0&restrictions=-1']

    def parse(self, response):
        name = response.css(".table-striped a::text").extract()
        date = response.css("td:nth-child(2)::text").extract()
        form = response.css("td:nth-child(3)::text").extract()
        location = response.css("td:nth-child(4)::text").extract()
        weight = response.css("td:nth-child(5)::text").extract()

        for i in range(len(name)):
            yield {
                "Name": name[i],
                "Date": date[i],
                "Form": form[i],
                "Location": location[i],
                "Weight": weight[i]

            }
