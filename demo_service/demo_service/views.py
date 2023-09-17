from rest_framework.response import Response

from demo_service.serializers import PetSerializer, PetCategorySerializer
from demo_service.models import PetCategory, Pet

from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema, OpenApiResponse


@extend_schema(tags=["Pet Categories"])
class PetCategoryViewSet(GenericViewSet):
    serializer_class = PetCategorySerializer
    queryset = PetCategory.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Создать категорию животного. Название должно быть уникальным.",
        responses={
            201: OpenApiResponse(response=PetCategorySerializer, description="Created (Возвращается созданный объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        description="Обновить категорию животного. Название должно быть уникальным.",
        responses={
            200: OpenApiResponse(response=PetCategorySerializer, description="Ok (Возвращается обновленный объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(instance=item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="Получить список всех категорий животных.",
        responses={
            200: OpenApiResponse(response=PetCategorySerializer, description="Ok (Возвращается список объектов)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    @extend_schema(
        description="Получить категорию животного по Id",
        responses={
            200: OpenApiResponse(response=PetCategorySerializer, description="Ok (Возвращается запрашиваемый объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            404: OpenApiResponse(description="Not found (Запрашиваемый объект не найден)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    @extend_schema(
        description="Удалить категорию животных.",
        responses={
            204: OpenApiResponse(response=PetCategorySerializer, description="No content. (Пустой ответ)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            404: OpenApiResponse(description="Not found (Запрашиваемый объект не найден)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=["Pets"])
class PetViewSet(GenericViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Создать животное. Название должно быть уникальным. Если категория не найдена приходит ответ 404.",
        responses={
            201: OpenApiResponse(response=PetSerializer, description="Created (Возвращается созданный объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        description="Получить список всех животных.",
        responses={
            200: OpenApiResponse(response=PetSerializer, description="Ok (Возвращается список объектов)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        # return Response(serializer.data)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    @extend_schema(
        description="Получить животное по Id.",
        responses={
            200: OpenApiResponse(response=PetSerializer, description="Ok (Возвращается запрашиваемый объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            404: OpenApiResponse(description="Not found (Запрашиваемый объект не найден)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    @extend_schema(
        description="Обновить животноe. Название должно быть уникальным.",
        responses={
            200: OpenApiResponse(response=PetSerializer, description="Ok (Возвращается обновленный объект)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(instance=item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="Удалить животное.",
        responses={
            204: OpenApiResponse(response=PetSerializer, description="No content. (Пустой ответ)"),
            400: OpenApiResponse(description="Bad request (Переданы не правильные данные в запросе)"),
            404: OpenApiResponse(description="Not found (Запрашиваемый объект не найден)"),
            500: OpenApiResponse(description="Internal server error (Ошибка внутри сервера)"),
        },
    )
    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
