import logging 
from django.http import HttpResponse 

logger = logging.getLogger(__name__)

# Create your views here.
 
def index(request): 
    logger.debug('Index page accessed')
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main page</title>
</head>
<body>
    <h1>It is main page</h1>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Non quisquam nam voluptas consequatur maiores consectetur. Aperiam, excepturi reprehenderit dolores quia, ut repellat amet fugiat perferendis quis hic fuga eos provident!</p>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptas, a tenetur impedit veniam illum ipsam repellat veritatis quod, doloremque earum laborum possimus inventore ea et, ex esse voluptate obcaecati quas!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut animi recusandae autem qui possimus porro aperiam facere. Perspiciatis et, modi ex velit exercitationem itaque laborum ipsum sunt? Ex, iste earum?</p>
    <a href="/about/">Go to about</a>
</body>
</html>
'''
    return HttpResponse(html) 
 
def about(request):
    logger.debug('About page accessed')
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>It is about page</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim eos, obcaecati totam harum error voluptas magni doloribus inventore corrupti in. Nesciunt, dignissimos non vero unde aliquid dolorum voluptatum. Eveniet, animi!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste quis architecto maxime exercitationem sint similique, delectus odit, quos quam porro provident nulla non, impedit magni? Voluptatum quibusdam amet similique veritatis.</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe laudantium dolorum sed tempora sunt eveniet! Nesciunt, velit reprehenderit quisquam nulla tempore ratione fuga dignissimos accusamus error deserunt, nam unde quidem.</p>
    <a href="/">Go to main</a>
</body>
</html>
'''
    return HttpResponse(html) 