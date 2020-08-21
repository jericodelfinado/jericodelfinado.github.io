import sys
from datetime import datetime

slug = sys.argv[1]
category = sys.argv[2]
now = datetime.now()

with open("./_posts/" + now.strftime("%Y-%m-%d") + "-" + slug + ".md", 'w') as f:
    f.write('---\n')
    f.write('layout: post\n')
    f.write('date: ' + now.strftime("%Y-%m-%d %H:%M") + '\n')
    f.write('title: "Placeholder Title"\n')
    f.write('category:\n')
    f.write('- ' + category + '\n')
    f.write('---\n\n')
