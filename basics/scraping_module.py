from dputils.scrape import Scraper, Tag

class MyScraper:
    def __init__(self,query,page=1):
        self.query=query
        self.page=page
        self.url=f'https://www.flipkart.com/search?q={query}&page={page}'
        self.dataset=[]

        def collect(self):
            #create object
            sc= Scraper(self.url)
            #page items
            target = Tag(cls='_1YokD2 _3Mn1Gg_')
            items=Tag(cls='_1AtVbE col-12-12')
            #product items
            title= Tag(cls='_4rR01T')
            price=Tag(cls='_30jeq3 _1_WHN1')
            rating=Tag('span', cls='_2_R_DZ')
            out=Scraper.get_all(target,items,name=title,price=price,rr=rating)
            return out
        
        def collect_all(self):
            while True:
                result=self.collect()
                if len(result)==0:
                    break
                self.dataset.extend(result)
                self.page+=1
                self.url=f'https://www.flipkart.com/search?q={self.query}&page={self.page}'
        
        def save(self,filename):
            df=pd.DataFrame(self.dataset)
