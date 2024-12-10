from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FormTemplates
from .serializers import UsersTemplateSerializer
from django.core.validators import validate_email
import re
from datetime import datetime


# Create your views here.

class CreateNewUsersTemplateAPIView(generics.CreateAPIView):
    queryset = FormTemplates.objects.all()
    serializer_class = UsersTemplateSerializer


class PostFormAPIView(APIView):
    def post(self, request, *args, **kwargs):
        params = request.query_params
        form_data = {}
        is_error_form_data = False
        for param_name, param_el in params.items():
            determine_field_data = self.determine_field(param_name, param_el)
            first_key = next(iter(determine_field_data))
            first_item = {first_key: determine_field_data[first_key]}
        #проверяем, есть ли ошибка в типе полученных данных, если да, то возвращаем ошибку
            if 'error_signal' in determine_field_data and determine_field_data['error_signal'] == True:
                is_error_form_data = True
            form_data.update(first_item)
        if is_error_form_data:
            return Response(form_data, status=status.HTTP_400_BAD_REQUEST)

        if not form_data:
            return Response(
                {"error": "Нет данных для поиска"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Составляем фильтры
        valid_filters = {}
        for key, value in form_data.items():
            # Проверяем, является ли поле ключом модели
            if hasattr(FormTemplates, key):
                valid_filters[key] = value
        # Если нет валидных фильтров
        if not valid_filters:
            return Response(
                {"error": "Некорректные параметры поиска"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Выполняем поиск в базе данных
        results = FormTemplates.objects.filter(**valid_filters)

        # Если записи не найдены
        if not results.exists():
            return Response(
                {"message": "Записи не найдены"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Формируем ответ с найденными данными
        result_data = [
            {
                "name": obj.name,
                "email": obj.email,
                "phone_number": obj.phone_number,
                "description": obj.description,
            }
            for obj in results
        ]
        return Response({"results": result_data}, status=status.HTTP_200_OK)
    @staticmethod
    def determine_field(param_name, param_el):
        """
        Проверяет, соответствует ли название параметра и его значение заданным требованиям.

        :param param_name: Название параметра (например, "email").
        :param param_el: Значение параметра (например, "example@mail.com").
        :return: Словарь с результатами проверки.
        """
        # Допустимые названия параметров
        allowed_params = {
            "name": str,
            "email": str,
            "phone_number": str,  # Номер телефона (формат: +7 xxx xxx xx xx)
            "date": str,  # Дата (формат: YYYY-MM-DD)
            "description": str,
            "user_template": int
        }
        # Проверка названия параметра
        if param_name not in allowed_params:
            return {
                param_name: "Недопустимое название параметра"
            }
        # Проверка значения параметра
        expected_type = allowed_params[param_name]
        try:
            if param_name == "email":
                validate_email(param_el)  # Django метод для валидации email

            elif param_name == "phone_number":
                # Убираем внешние кавычки (апострофы или двойные кавычки)
                phone = param_el.strip("'\"")
                # Убираем лишние пробелы
                phone = phone.strip()
                # Если номер начинается с пробела, заменяем на +
                if not phone[0] == "+":
                    phone = "+" + phone
                # Проверяем формат номера телефона
                if not re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', phone):
                    raise ValidationError("Некорректный формат номера телефона. Ожидается: +7 xxx xxx xx xx.")
                else:
                    param_el = phone

            elif param_name == "date":
                # Проверка формата даты
                datetime.strptime(param_el, '%Y-%m-%d')  # Пример: "2024-12-09"

            elif not isinstance(param_el, expected_type):
                # Проверка типа данных
                raise ValueError(f"Некорректный тип данных. Ожидается: {expected_type.__name__}")

            # Если все проверки пройдены
            return {
                param_name: param_el
            }

        except (ValueError, ValidationError) as e:
            return {
                param_name: str(e),
                'error_signal': True
            }
