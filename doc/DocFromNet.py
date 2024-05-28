import datetime as dt
import sys

if __name__=="__main__":
    min_html_beg = "<!doctype html><html><head><link rel='stylesheet' href='../../bootstrap.css'></head><body>"
    min_html_end = "</body></html>"



class Doc:
    id=1
    def __init__(self,title="No Title",content="No Content",link=None,tags=[]):
        self.d_crea= dt.datetime.now()
        self.id_article = self.id
        Doc.id += 1  
        self.title = title
        self.content = content
        self.link = link
        #self.args = args
        #self.cmd = cmd
        self.tags = tags
        
    def bs_card(self):
        res = ' <div class="card">'
        
        res += f'<h3 class="card-title">{self.title}</h3>'
        res += f'<div class="card-body"><p>{self.content}\n{self.d_crea}</p>'
        res += f'<a href="{self.link}">lien vers site : {self.title}</a>' 
        res += "<p>"
        for t in self.tags:
            res += f"<a href={t}>{t}</a> "
        res += '</p></div></div>'

        return res
    
    def get_id(self,format="html"):
        return f"doc_{self.id_article}.{format}"
    
    def req_ins_doc(self):
        req = f"insert into doc (title,content,link,date) values ({self.title,self.link,self.d_crea})"
        return req
    #def doc_json(self):
    #    return self.args
        
def main(title="No Title",content="No content",link=None,tag=[]):
    # arg tuple ? **args
    #print(args)
    d0 = Doc(title,content,link,tag)
    return d0.bs_card

    
print(__name__)
if __name__ == "__main__" or len(sys.argv) < 2 :
    a1 = Doc("Trump est jugé!","il s'est pris 15 ans et ce n'est pas encore assez ! c'est que pense la quasi totalité des gens censé ...","http://trump_in_jail",["trump","prison","goodnews"])
    print(a1.bs_card())

    with open(f"{a1.get_id()}","w") as f:
        f.write(f"{min_html_beg}{a1.bs_card()}{min_html_end}")
        print(f"{a1.title} is writed !")
else :
    main(sys.argv)
    
