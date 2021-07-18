from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def deal_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 생성성공시 201
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)  # context 느낌
        print('----', serializer)
        return Response(serializer.data)
