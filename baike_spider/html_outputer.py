class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        flout = open('output.html', 'w')

        flout.write("<html>")
        flout.write("<body>")
        flout.write("<table>")
        for data in self.datas:
            flout.write("<tr>")
            flout.write("<td>%s</td>" % data['url'])
            flout.write("<td>%s</td>" % data['title'])
            flout.write("<td>%s</td>" % data['summary'])
            flout.write("</tr>")
        flout.write("</table>")
        flout.write("</body>")
        flout.write("</html>")