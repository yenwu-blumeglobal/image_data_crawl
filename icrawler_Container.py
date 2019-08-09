from icrawler.builtin import GoogleImageCrawler

for keyword in ['shipping containers', '20 ft containers','40 ft containers', '45 ft containers', '53 ft containers']:
    google_crawler = GoogleImageCrawler(
            parser_threads=2, 
            downloader_threads=4,
            storage={'root_dir':'GoogleImageCrawler/{}'.format(keyword)})
    google_crawler.crawl(keyword=keyword, max_num=200, min_size=(200,200))
    
