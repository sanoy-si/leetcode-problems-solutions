class node:
    def __init__(self,page):
        self.page=page
        self.next=None
        self.prev=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=node(homepage)
        self.curr_page=self.head
            

    def visit(self, url: str) -> None:
        new=node(url)
        self.curr_page.next=new
        new.prev=self.curr_page
        self.curr_page=self.curr_page.next

    def back(self, steps: int) -> str:
        while self.curr_page != self.head and steps>0:
            self.curr_page=self.curr_page.prev
            steps-=1
        return self.curr_page.page

    def forward(self, steps: int) -> str:
        while self.curr_page.next and steps>0:
            self.curr_page=self.curr_page.next
            steps-=1
        return self.curr_page.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)